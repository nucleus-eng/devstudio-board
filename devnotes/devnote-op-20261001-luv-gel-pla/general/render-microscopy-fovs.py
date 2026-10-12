#!/usr/bin/env python3
"""Render one field of view per well from the OME-Zarr store named in viewers.md,
and stitch the four into one composite figure.

Writes figures/fov-<well>.png and figures/fov-composite.png. Run from the
DevNote directory:

    python3 general/render-microscopy-fovs.py

Requires: zarr>=3, numpy, pillow.

Four things this script decides, because the data does not record them.

1. Crop. "One field of view" is taken as a centre crop covering 1/9 of the
   plane's area, that is 1/3 of its width and 1/3 of its height, at full
   (s0) resolution. The same crop position and size is used for all four
   wells, so no region was chosen per well.

2. Z-slice. Each store is a 12-plane z-stack. A single slice at the middle
   index (z=6 of 0-11) is rendered, not a projection, so the image is one
   real plane rather than a composite of several.

3. Contrast, grouped only where that holds up. Measured directly, the four
   wells' GFP medians are E14 11130, E21 12320, E15 8405, E16 4158,
   consistent with the main page's own report of higher autofluorescence
   in PEG4Nb than ULGA or LGA. A single stretch pooled across all four
   puts that whole range in one window and washes the dimmer wells into a
   near-uniform green. The two PEG4Nb wells (E14, E21) pool cleanly, since
   their medians are close. E15 and E16 do not: pooling them, even with
   the high percentile raised to 99.99, left E15 a near-uniform wash and
   E16 almost dark, because E15's whole distribution sits close to E16's
   ceiling rather than merely having a brighter tail. E15 and E16 each
   keep their own one-well stretch. Brightfield stays per-well throughout,
   since it is shown only as gel-matrix context, not as a second
   measurement.

4. GROUP_PCT picks the 50th to 99.9th percentile within each group (or
   each well, for E15 and E16). Checked directly: this holds no pixels at
   0 or 255 in any of the four.

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
# name -> (well path, display label, group)
#
# PEG4Nb's two wells (E14, E21) pool into one stretch; their GFP medians,
# 11130 and 12320, are close enough that one window shows both. ULGA and
# LGA do not: tried pooled at the 50th-99.9th and 50th-99.99th percentile,
# and both left E15 (median 8405) a near-uniform wash and E16 (median
# 4158) almost dark, because E15's whole distribution sits close to E16's
# ceiling rather than merely having a brighter tail. E15 and E16 each keep
# their own one-well stretch instead.
WELLS = {
    'E14': ('E/14/0', 'E14 - PEG4Nb pre-gel', 'PEG4Nb'),
    'E21': ('E/21/0', 'E21 - PEG4Nb gel', 'PEG4Nb'),
    'E15': ('E/15/0', 'E15 - ULGA', 'E15'),
    'E16': ('E/16/0', 'E16 - LGA', 'E16'),
}
GRID = [['E14', 'E21'], ['E15', 'E16']]  # composite layout, one row per gel family

Z_INDEX = 6            # middle of 12 planes (0-11)
CROP_FRACTION = 1 / 3  # linear fraction per side; 1/3 x 1/3 = 1/9 area
OUT_PX = 650
GROUP_PCT = (50.0, 99.9)
BRIGHTFIELD_PCT = (1.0, 99.0)
BRIGHTFIELD_WEIGHT = 0.25
GFP_COLOR = np.array([0.0, 1.0, 0.0])
HEADER_PX = 48
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


def stretch(channel, lo, hi):
    return np.clip((channel - lo) / max(hi - lo, 1), 0, 1)


def group_stretch(crops, names, pct):
    pool = np.concatenate([crops[n][2].ravel() for n in names])
    lo, hi = np.percentile(pool, pct[0]), np.percentile(pool, pct[1])
    return float(lo), float(hi)


def font(height, scale=0.045):
    try:
        return ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',
                                   int(height * scale))
    except OSError:
        return ImageFont.load_default()


def render_panel(label, um_per_px, brightfield, gfp, gfp_lo, gfp_hi):
    bf_lo, bf_hi = np.percentile(brightfield, BRIGHTFIELD_PCT[0]), \
        np.percentile(brightfield, BRIGHTFIELD_PCT[1])
    bf_norm = stretch(brightfield, bf_lo, bf_hi)
    gfp_norm = stretch(gfp, gfp_lo, gfp_hi)

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
    f = font(height)
    draw_ctx.rectangle(
        [width - margin - bar_px, height - margin - bar_h,
         width - margin, height - margin], fill=(255, 255, 255))
    text = f'{bar_um} um'
    box = draw_ctx.textbbox((0, 0), text, font=f)
    draw_ctx.text(
        (width - margin - (box[2] - box[0]),
         height - margin - bar_h - (box[3] - box[1]) - int(height * 0.018)),
        text, fill=(255, 255, 255), font=f)

    # panel header bar with the well's label
    panel = Image.new('RGB', (width, height + HEADER_PX), (20, 20, 20))
    header_font = font(HEADER_PX, scale=0.6)
    header_draw = ImageDraw.Draw(panel)
    box = header_draw.textbbox((0, 0), label, font=header_font)
    header_draw.text(
        ((width - (box[2] - box[0])) / 2, (HEADER_PX - (box[3] - box[1])) / 2 - box[1]),
        label, fill=(255, 255, 255), font=header_font)
    panel.paste(img, (0, HEADER_PX))
    return panel, bar_um


def stitch(panels, grid, gap=6, background=(20, 20, 20)):
    rows = len(grid)
    cols = len(grid[0])
    cell_w = max(panels[n].width for row in grid for n in row)
    cell_h = max(panels[n].height for row in grid for n in row)
    out = Image.new('RGB',
                     (cols * cell_w + (cols - 1) * gap,
                      rows * cell_h + (rows - 1) * gap),
                     background)
    for r, row in enumerate(grid):
        for c, name in enumerate(row):
            out.paste(panels[name], (c * (cell_w + gap), r * (cell_h + gap)))
    return out


def main():
    crops = {name: load(path) for name, (path, _, _) in WELLS.items()}

    group_names = {}
    for name, (_, _, group) in WELLS.items():
        group_names.setdefault(group, []).append(name)
    group_ranges = {g: group_stretch(crops, names, GROUP_PCT)
                     for g, names in group_names.items()}
    print('\ngroup GFP stretch:')
    for g, (lo, hi) in group_ranges.items():
        print(f'   {g:10s} {lo:8.0f} -> {hi:8.0f}  (wells: {group_names[g]})')

    panels = {}
    bar_ums = {}
    for name, (_, label, group) in WELLS.items():
        um_per_px, brightfield, gfp = crops[name]
        lo, hi = group_ranges[group]
        panels[name], bar_ums[name] = render_panel(label, um_per_px, brightfield, gfp, lo, hi)
        panels[name].save(f'{OUTDIR}/fov-{name}.png')
        print(f'  {OUTDIR}/fov-{name}.png  bar {bar_ums[name]} um')

    composite = stitch(panels, GRID)
    composite.save(f'{OUTDIR}/fov-composite.png')
    print(f'\n  {OUTDIR}/fov-composite.png  {composite.size[0]}x{composite.size[1]} px')

    with open(f'{OUTDIR}/fov-render-params.json', 'w') as handle:
        json.dump({
            'store': STORE,
            'z_index': Z_INDEX,
            'crop_fraction': CROP_FRACTION,
            'out_px': OUT_PX,
            'group_percentiles': GROUP_PCT,
            'brightfield_percentiles': BRIGHTFIELD_PCT,
            'brightfield_weight': BRIGHTFIELD_WEIGHT,
            'groups': group_names,
            'group_gfp_stretch': group_ranges,
        }, handle, indent=1)


if __name__ == '__main__':
    main()
