#!/usr/bin/env python3
"""Render one representative field of view per condition, cropped and zoomed
to the view state Anton supplied from the bnext-bio Vizarr app.

Adapted from devnote-swh-20260925-ph-sensor-in-solution/general/render-microscopy-fovs.py,
same crop math: `target` is the centre in s0 pixels, `zoom` is log2 scale, so
the visible width in s0 pixels is OUT_PX / 2**ZOOM. One store here, not four,
so WELLS all point at the same zarr. One target and one zoom for every well,
same as that script, so all three panels sit at the same pixel offset and
scale; only the well (and therefore the real content) differs.

GFP only, fixed window 30000-60000 per Anton's instruction, not the pooled
percentile stretch the source script used for multiple channels.
"""
import json
import numpy as np
import requests
import zarr
from PIL import Image, ImageDraw, ImageFont

STORE = 'https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr'
WELLS = [
    ('HSL sensing GUVs', 'C4', 'C/4/0'),
    ('Negative control', 'C7', 'C/7/0'),
    ('Positive control', 'C10', 'C/10/0'),
]
T = 19
GFP_CHANNEL = 1
WINDOW = (30000, 60000)
# Copied verbatim from the bnext-bio Vizarr URL Anton gave, for well C4.
ZOOM = -0.873947580175899
TARGET = [6706.657784297582, 4480.135606141096]
OUT_PX = 1080
OUTDIR = 'figures'

SESSION = requests.Session()
SESSION.headers['User-Agent'] = 'Mozilla/5.0'


def load(store, well, target):
    ome = SESSION.get(f'{store}/{well}/zarr.json').json()['attributes']['ome']
    scales = {d['path']: d['coordinateTransformations'][0]['scale'][-1]
              for d in ome['multiscales'][0]['datasets']}
    base = scales['s0']

    extent = OUT_PX / (2 ** ZOOM)
    usable = [p for p in sorted(scales, key=lambda p: scales[p])
              if extent / (scales[p] / base) >= OUT_PX]
    level = usable[-1] if usable else 's0'
    factor = scales[level] / base

    half = extent / factor / 2
    x = int(round(target[0] / factor - half))
    y = int(round(target[1] / factor - half))
    n = int(round(2 * half))
    arr = zarr.open(f'{store}/{well}/{level}', mode='r')
    crop = np.asarray(arr[T, GFP_CHANNEL, 0, y:y + n, x:x + n]).astype(np.float32)
    um_per_out_px = extent * base / OUT_PX
    print(f'  {well}: level {level} ({scales[level]} um/px), crop {n}x{n} at '
          f'({x},{y}), field {extent * base:.0f} um, raw min/max '
          f'{crop.min():.0f}/{crop.max():.0f}')
    return um_per_out_px, crop


def draw(name, well, um_per_px, arr):
    lo, hi = WINDOW
    norm = np.clip((arr - lo) / (hi - lo), 0, 1)
    rgb = np.zeros(arr.shape + (3,), np.float32)
    rgb[..., 1] = norm
    img = Image.fromarray((rgb * 255).astype(np.uint8))
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
    text = f'{bar_um} µm'
    box = draw_ctx.textbbox((0, 0), text, font=font)
    draw_ctx.text(
        (width - margin - (box[2] - box[0]),
         height - margin - bar_h - (box[3] - box[1]) - int(height * 0.018)),
        text, fill=(255, 255, 255), font=font)
    draw_ctx.text((margin, margin), f'{name} ({well})', fill=(255, 255, 255), font=font)

    path = f'{OUTDIR}/fov-{well.lower()}.png'
    img.save(path)
    return path, bar_um


def main():
    params = {'zoom': ZOOM, 'target': TARGET, 't': T, 'gfp_channel': GFP_CHANNEL,
              'window': WINDOW, 'out_px': OUT_PX, 'wells': {}}
    for name, well, path_in_store in WELLS:
        um_per_px, arr = load(STORE, path_in_store, TARGET)
        out_path, bar_um = draw(name, well, um_per_px, arr)
        print(f'  -> {out_path}  {OUT_PX}x{OUT_PX} px  bar {bar_um} um')
        params['wells'][well] = {'condition': name, 'um_per_px': um_per_px,
                                  'bar_um': bar_um}
    with open(f'{OUTDIR}/fov-render-params.json', 'w') as handle:
        json.dump(params, handle, indent=1)


if __name__ == '__main__':
    main()
