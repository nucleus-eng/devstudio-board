#!/usr/bin/env python3
"""Render a static thumbnail for well K18 of the 2026-10-09 EsaR-mNG AHSL
store: the final timepoint, a centre crop covering 1/9 of the plane's area,
an empirically measured per-channel contrast stretch, and a burned-in 100 um
scale bar.

Writes figures/thumbnail-k18.png and figures/thumbnail-render-params.json.
Run from the DevNote directory:

    python3 general/render-thumbnail.py

Requires: zarr>=3, numpy, pillow.

Four things this script decides, because the spec does not fully pin them
down.

1. Timepoint. "Final time point" is the last index along this store's `t`
   axis. The store has 20 timepoints (shape[0] == 20), so t=19. Read from
   the array's own shape rather than hardcoded, so a re-run against a
   store with a different timepoint count stays correct.

2. Crop. A centre crop covering 1/9 of the plane's area, i.e. 1/3 of its
   width and 1/3 of its height, at full (s0) resolution, matching the same
   convention devnote-op-20261001-luv-gel-pla/general/render-microscopy-fovs.py
   already uses for "one field of view."

3. Contrast. The store's own omero metadata gives a window of 0-65535 for
   both channels, the full bit depth, not a real calibration (the same
   degenerate-window pattern noted elsewhere in this project). "Optimal"
   is therefore a percentile stretch measured directly from this crop's
   actual pixel values, not read from metadata or guessed. Channel colors
   do come from metadata: the omero record names GFP green (00FF00) and
   Alexa Fluor 647 blue (0000FF), so this script uses those rather than
   inventing a different color assignment.

4. Scale bar correctness. The precedent script computes its bar length in
   original (pre-resize) pixel units but draws it on an image already
   resized to a fixed output size, without correcting for that resize
   ratio. Measured: this means two different output sizes may draw a
   100 um bar with different true lengths relative to the image, for the
   same um_per_px. This script computes the bar in the *output* image's
   own pixel scale instead: um_per_px is rescaled by (OUT_PX / crop_px)
   before the bar length is derived, so the drawn bar is correct for
   whatever OUT_PX this script is run with.
"""
import json
import urllib.request

import numpy as np
import zarr
from PIL import Image, ImageDraw, ImageFont

STORE = (
    'https://data.nucleus.engineering/microscopy/nucleus-bnext-01/'
    '201009o_EsaR_mNG_0.1_0.5_K_L_2026-10-09_19-47-50.861429.zarr'
)
WELL_PATH = 'K/18/0'
CROP_FRACTION = 1 / 3  # linear fraction per side; 1/3 x 1/3 = 1/9 area
OUT_PX = 650
BAR_UM = 100
CONTRAST_PCT = (1.0, 99.5)
CHANNEL_COLORS = {
    'GFP': np.array([0.0, 1.0, 0.0]),
    'Alexa Fluor 647': np.array([0.0, 0.0, 1.0]),
}
OUTDIR = 'figures'


def load():
    """Return (um_per_px at s0, t_index used, {channel label: crop array})."""
    meta = zarr.open(f'{STORE}/{WELL_PATH}/s0', mode='r')
    t, c, z, height, width = meta.shape
    t_index = t - 1  # final timepoint
    assert z == 1, f'expected a single z-plane, found {z}'

    crop_h = int(round(height * CROP_FRACTION))
    crop_w = int(round(width * CROP_FRACTION))
    y0 = (height - crop_h) // 2
    x0 = (width - crop_w) // 2
    crop = np.asarray(
        meta[t_index, :, 0, y0:y0 + crop_h, x0:x0 + crop_w]
    ).astype(np.float32)

    attrs_url = f'{STORE}/{WELL_PATH}/zarr.json'
    req = urllib.request.Request(attrs_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        ome = json.load(resp)['attributes']['ome']
    scale = ome['multiscales'][0]['datasets'][0]['coordinateTransformations'][0]['scale']
    um_per_px = scale[-1]
    channel_labels = [ch['label'] for ch in ome['omero']['channels']]

    print(f'  {WELL_PATH}: t={t_index} of {t}, crop {crop_w}x{crop_h} px '
          f'at ({x0},{y0}), {um_per_px} um/px')
    return um_per_px, t_index, dict(zip(channel_labels, crop)), (crop_h, crop_w)


def stretch(channel, lo, hi):
    return np.clip((channel - lo) / max(hi - lo, 1), 0, 1)


def font(height, scale=0.045):
    try:
        return ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',
                                   int(height * scale))
    except OSError:
        return ImageFont.load_default()


def render(um_per_px, channels, crop_shape):
    crop_h, crop_w = crop_shape
    measured = {}
    rgb = np.zeros(next(iter(channels.values())).shape + (3,), np.float32)
    for label, data in channels.items():
        color = CHANNEL_COLORS.get(label)
        if color is None:
            print(f'  skipping unrecognized channel {label!r}, no color assigned')
            continue
        lo, hi = np.percentile(data, CONTRAST_PCT[0]), np.percentile(data, CONTRAST_PCT[1])
        measured[label] = (float(lo), float(hi))
        rgb += stretch(data, lo, hi)[..., None] * color
        print(f'  {label}: measured {CONTRAST_PCT[0]}-{CONTRAST_PCT[1]} percentile '
              f'stretch {lo:.0f} -> {hi:.0f}')

    img = Image.fromarray((np.clip(rgb, 0, 1) * 255).astype(np.uint8))
    if img.size != (OUT_PX, OUT_PX):
        img = img.resize((OUT_PX, OUT_PX), Image.LANCZOS)

    # Rescale um_per_px to the *output* image's pixel size before deriving
    # the bar length, so the bar is correct for OUT_PX, not for the
    # pre-resize crop. See the module docstring, point 4.
    resize_ratio = OUT_PX / crop_w
    um_per_px_out = um_per_px / resize_ratio
    bar_px = int(round(BAR_UM / um_per_px_out))

    width, height = img.size
    draw_ctx = ImageDraw.Draw(img)
    margin = int(width * 0.04)
    bar_h = max(4, int(height * 0.009))
    f = font(height)
    draw_ctx.rectangle(
        [width - margin - bar_px, height - margin - bar_h,
         width - margin, height - margin], fill=(255, 255, 255))
    text = f'{BAR_UM} um'
    box = draw_ctx.textbbox((0, 0), text, font=f)
    draw_ctx.text(
        (width - margin - (box[2] - box[0]),
         height - margin - bar_h - (box[3] - box[1]) - int(height * 0.018)),
        text, fill=(255, 255, 255), font=f)
    return img, measured, bar_px, um_per_px_out


def main():
    um_per_px, t_index, channels, crop_shape = load()
    img, measured, bar_px, um_per_px_out = render(um_per_px, channels, crop_shape)

    img.save(f'{OUTDIR}/thumbnail-k18.png')
    print(f'\n  {OUTDIR}/thumbnail-k18.png  {img.size[0]}x{img.size[1]} px, '
          f'{BAR_UM} um bar = {bar_px} px')

    with open(f'{OUTDIR}/thumbnail-render-params.json', 'w') as handle:
        json.dump({
            'store': STORE,
            'well_path': WELL_PATH,
            't_index': t_index,
            'crop_fraction': CROP_FRACTION,
            'out_px': OUT_PX,
            'bar_um': BAR_UM,
            'bar_px': bar_px,
            'um_per_px_s0': um_per_px,
            'um_per_px_output': um_per_px_out,
            'contrast_percentiles': CONTRAST_PCT,
            'measured_channel_stretch': measured,
        }, handle, indent=1)


if __name__ == '__main__':
    main()
