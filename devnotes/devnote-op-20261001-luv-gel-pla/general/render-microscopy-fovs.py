#!/usr/bin/env python3
"""Render one field of view per well from the OME-Zarr store named in viewers.md.

Writes figures/fov-<well>.png. Run from the DevNote directory:

    python3 general/render-microscopy-fovs.py

Requires: zarr>=3, numpy, pillow.

Three things this script decides, because the data does not record them.

1. Crop. "One field of view" is taken as a centre crop covering 1/9 of the
   plane's area, that is 1/3 of its width and 1/3 of its height, at full
   (s0) resolution. The same crop position and size is used for all four
   wells, so no region was chosen per well.

2. Z-slice. Each store is a 12-plane z-stack. A single slice at the middle
   index (z=6 of 0-11) is rendered, not a projection, so the image is one
   real plane rather than a composite.

3. Contrast, per well rather than pooled. The pH-sensor DevNote's render
   script pools one stretch across its wells, because that figure compares
   signal level between conditions. This figure does not: its only claim is
   that GFP-expressing GUVs are present in each gel. Measured directly, the
   four wells' GFP medians span roughly 4100 to 12300, a 3-fold range,
   consistent with the main page's own report of higher autofluorescence in
   PEG4Nb than ULGA or LGA. A pooled stretch puts that whole range inside
   one window, so the dimmer wells render as a near-uniform wash rather
   than showing the GUVs in them. Each well is stretched from its own 50th
   to 99.9th percentile instead, which held no pixels at either 0 or 255 in
   every well checked. Brightfield is stretched from its own 1st to 99th
   percentile and blended in at 25% weight, for the gel matrix as context,
   not as a second measurement.

Channel note: each well's image carries three channels, Brightfield and
two both labelled "GFP" in the store's own omero metadata, with different
intensity ranges (one roughly 9000-14000, the other roughly 4000-7000).
Which one is the intended GFP read is not stated anywhere in the source.
This script renders the first GFP-labelled channel (index 1) and leaves
the second (index 2) out. See gap-second-gfp-channel in main.md.
"""
import json
import urllib.request

import numpy as np
import zarr
from PIL import Image, ImageDraw, ImageFont

STORE = (
    'https://data.nucleus.engineering/microscopy/nucleus-bnext-01/'
    'OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr'
)
WELLS = [
    ('E14', 'E/14/0'),
    ('E15', 'E/15/0'),
    ('E16', 'E/16/0'),
    ('E21', 'E/21/0'),
]
Z_INDEX = 6            # middle of 12 planes (0-11)
CROP_FRACTION = 1 / 3  # linear fraction per side; 1/3 x 1/3 = 1/9 area
OUT_PX = 650
GFP_PCT = (50.0, 99.9)
BRIGHTFIELD_PCT = (1.0, 99.0)
BRIGHTFIELD_WEIGHT = 0.25
GFP_COLOR = np.array([0.0, 1.0, 0.0])
OUTDIR = 'figures'


def load(well_path):
    """Return (um per pixel, brightfield crop, GFP crop) for one well."""
    meta = zarr.open(f'{STORE}/{well_path}/s0', mode='r')
    _, _, z, height, width = meta.shape
    assert z == 12, f'expected 12 z-planes, found {z}'

    crop_h = int(round(height * CROP_FRACTION))
    crop_w = int(round(width * CROP_FRACTION))
    y0 = (height - crop_h) // 2
    x0 = (width - crop_w) // 2
    crop = np.asarray(
        meta[0, :2, Z_INDEX, y0:y0 + crop_h, x0:x0 + crop_w]
    ).astype(np.float32)

    attrs_url = f'{STORE}/{well_path}/zarr.json'
    req = urllib.request.Request(attrs_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        ome = json.load(resp)['attributes']['ome']
    scale = ome['multiscales'][0]['datasets'][0]['coordinateTransformations'][0]['scale']
    um_per_px = scale[-1]
    print(f'  {well_path}: crop {crop_w}x{crop_h} px at ({x0},{y0}), '
          f'z={Z_INDEX}, {um_per_px} um/px')
    return um_per_px, crop[0], crop[1]


def stretch(channel, pct):
    lo, hi = np.percentile(channel, pct[0]), np.percentile(channel, pct[1])
    return np.clip((channel - lo) / max(hi - lo, 1), 0, 1), (float(lo), float(hi))


def draw(name, um_per_px, brightfield, gfp):
    bf_norm, bf_range = stretch(brightfield, BRIGHTFIELD_PCT)
    gfp_norm, gfp_range = stretch(gfp, GFP_PCT)

    rgb = np.zeros(gfp.shape + (3,), np.float32)
    rgb += bf_norm[..., None] * BRIGHTFIELD_WEIGHT
    rgb += gfp_norm[..., None] * GFP_COLOR
    img = Image.fromarray((np.clip(rgb, 0, 1) * 255).astype(np.uint8))
    if img.size != (OUT_PX, OUT_PX):
        img = img.resize((OUT_PX, OUT_PX), Image.LANCZOS)

    width, height = img.size
    draw_ctx = ImageDraw.Draw(img)
    bar_um = min([25, 50, 100, 200, 250, 500],
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
    text = f'{bar_um} um'
    box = draw_ctx.textbbox((0, 0), text, font=font)
    draw_ctx.text(
        (width - margin - (box[2] - box[0]),
         height - margin - bar_h - (box[3] - box[1]) - int(height * 0.018)),
        text, fill=(255, 255, 255), font=font)
    draw_ctx.text((margin, margin), name, fill=(255, 255, 255), font=font)

    path = f'{OUTDIR}/fov-{name}.png'
    img.save(path)
    return path, bar_um, bf_range, gfp_range


def main():
    params = {}
    for name, well_path in WELLS:
        print(f'loading {name} ...')
        um_per_px, brightfield, gfp = load(well_path)
        path, bar_um, bf_range, gfp_range = draw(name, um_per_px, brightfield, gfp)
        print(f'  {path}  {OUT_PX}x{OUT_PX} px  bar {bar_um} um  '
              f'brightfield {bf_range[0]:.0f}-{bf_range[1]:.0f}  '
              f'GFP {gfp_range[0]:.0f}-{gfp_range[1]:.0f}')
        params[name] = {'brightfield_stretch': bf_range, 'gfp_stretch': gfp_range}

    with open(f'{OUTDIR}/fov-render-params.json', 'w') as handle:
        json.dump({
            'store': STORE,
            'z_index': Z_INDEX,
            'crop_fraction': CROP_FRACTION,
            'out_px': OUT_PX,
            'gfp_percentiles': GFP_PCT,
            'brightfield_percentiles': BRIGHTFIELD_PCT,
            'brightfield_weight': BRIGHTFIELD_WEIGHT,
            'per_well_stretch': params,
        }, handle, indent=1)


if __name__ == '__main__':
    main()
