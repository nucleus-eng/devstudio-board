#!/usr/bin/env python3
"""Render one field of view per well from the OME-Zarr stores named in main.md.

Writes figures/fov-<well>.png. Run from the DevNote directory:

    python3 general/render-microscopy-fovs.py

Requires: zarr>=3, numpy, pillow, requests.

Three things this script decides, because the data does not record them.

1. Channel colors. The stores' omero block says Rhodamine is FF0000 and
   Alexa Fluor 647 is 0000FF. The viewer the team reads these in shows
   Rhodamine yellow and Alexa Fluor 647 red. DISPLAY below follows the
   viewer, not the metadata.

2. Contrast. The stores' omero window is the full 0-65535 for every channel,
   which renders almost black. This script computes one low and one high per
   channel, pooled across all four wells, so the wells stay comparable: a
   well with less signal looks darker. Per-well stretching would hide exactly
   the differences the DevNote's Results claim.

3. Crop. The stores are stitched tile mosaics about 3.7 mm across. Seams sit
   near 1350, 2700, 2848 and 4048 px at s1. ORIGIN and FOV below pick a
   square strictly inside one tile, so no seam crosses the figure.

The scale bar is not hardcoded: it is read from each store's own
coordinateTransformations.

Exposure, gain and laser power are recorded nowhere in these stores. The
common stretch assumes they were matched across the four acquisitions. The
camera floor agrees across wells, p0.1 spreads of 16 and 77 counts, which is
consistent with that, but it is not proof.
"""
import json
import numpy as np
import requests
import zarr
from PIL import Image, ImageDraw, ImageFont

BASE = 'https://data.nucleus.engineering/microscopy/nucleus-bnext-01'
WELLS = [
    ('D4', 'SH-0925-D4_2026-09-25_11-27-49.059491.zarr', 'D/4/0'),
    ('D5', 'SH-0925-D5_2026-09-25_11-32-48.009691.zarr', 'D/5/0'),
    ('E4', 'SH-0925-E4_2026-09-25_12-03-09.447054.zarr', 'E/4/0'),
    ('E5', 'SH-0925-E5-2_2026-09-25_12-04-22.672843.zarr', 'E/5/0'),
]
LEVEL = 's1'          # 0.666 um/px
FOV = 1080            # px, a 719 um square
ORIGIN = (2910, 2760)  # (y, x), strictly inside one stitching tile
LO_PCT, HI_PCT = 1.0, 99.5
DISPLAY = {'Rhodamine': (255, 220, 60), 'Alexa Fluor 647': (255, 60, 40)}
OUTDIR = 'figures'

SESSION = requests.Session()
# The host answers 403 without a browser user agent.
SESSION.headers['User-Agent'] = 'Mozilla/5.0'


def load(store):
    """Return (channel labels, um per pixel, cropped array) for one well."""
    ome = SESSION.get(f'{store}/zarr.json').json()['attributes']['ome']
    labels = [c['label'] for c in ome['omero']['channels']]
    scales = {d['path']: d['coordinateTransformations'][0]['scale'][-1]
              for d in ome['multiscales'][0]['datasets']}
    y, x = ORIGIN
    arr = zarr.open(f'{store}/{LEVEL}', mode='r')
    return labels, scales[LEVEL], np.asarray(
        arr[0, :, 0, y:y + FOV, x:x + FOV]).astype(np.float32)


def common_stretch(crops, labels):
    """One low and one high per channel, pooled over every well."""
    out = {}
    for ci, label in enumerate(labels):
        pool = np.concatenate([c[2][ci].ravel() for c in crops.values()])
        out[label] = (float(np.percentile(pool, LO_PCT)),
                      float(np.percentile(pool, HI_PCT)))
    return out


def draw(name, labels, um_per_px, arr, stretch):
    rgb = np.zeros(arr.shape[1:] + (3,), np.float32)
    for ci, label in enumerate(labels):
        lo, hi = stretch[label]
        norm = np.clip((arr[ci] - lo) / max(hi - lo, 1), 0, 1)
        rgb += norm[..., None] * (np.array(DISPLAY[label], np.float32) / 255)
    img = Image.fromarray((np.clip(rgb, 0, 1) * 255).astype(np.uint8))

    width, height = img.size
    draw_ctx = ImageDraw.Draw(img)
    bar_um = min([50, 100, 200, 250, 500],
                 key=lambda v: abs(v - width * um_per_px / 5))
    bar_px = int(round(bar_um / um_per_px))
    margin = int(width * 0.04)
    bar_h = max(4, int(height * 0.009))
    try:
        font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',
                                  int(height * 0.045))
    except OSError:
        font = ImageFont.load_default()
    draw_ctx.rectangle(
        [width - margin - bar_px, height - margin - bar_h,
         width - margin, height - margin], fill=(255, 255, 255))
    text = f'{bar_um} µm'
    box = draw_ctx.textbbox((0, 0), text, font=font)
    draw_ctx.text(
        (width - margin - (box[2] - box[0]),
         height - margin - bar_h - (box[3] - box[1]) - int(height * 0.018)),
        text, fill=(255, 255, 255), font=font)
    draw_ctx.text((margin, margin), name, fill=(255, 255, 255), font=font)

    path = f'{OUTDIR}/fov-{name}.png'
    img.save(path)
    return path, bar_um


def main():
    crops = {}
    for name, store, well in WELLS:
        crops[name] = load(f'{BASE}/{store}/{well}')
        print(f'  loaded {name}  {crops[name][2].shape}  {crops[name][1]} um/px')

    labels = crops[WELLS[0][0]][0]
    stretch = common_stretch(crops, labels)
    print('\ncommon stretch, pooled over all wells:')
    for label, (lo, hi) in stretch.items():
        print(f'   {label:18s} {lo:8.0f} -> {hi:8.0f}')

    print()
    for name, _, _ in WELLS:
        chan_labels, um_per_px, arr = crops[name]
        path, bar_um = draw(name, chan_labels, um_per_px, arr, stretch)
        print(f'  {path}  {FOV}x{FOV} px  '
              f'{FOV * um_per_px:.0f} um field  bar {bar_um} um')

    with open(f'{OUTDIR}/fov-render-params.json', 'w') as handle:
        json.dump({'level': LEVEL, 'fov_px': FOV, 'origin_yx': list(ORIGIN),
                   'percentiles': [LO_PCT, HI_PCT], 'display_rgb': DISPLAY,
                   'stretch': stretch}, handle, indent=1)


if __name__ == '__main__':
    main()
