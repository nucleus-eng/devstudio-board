#!/usr/bin/env python3
"""Render one representative field of view per condition for the solution
subsection of Result 2, from the Lysate_LuxR_Cytosol_EsaR store.

Adapted from general/render-microscopy-fovs.py (Result 3), with two real
differences, both forced by the data rather than chosen:

1. No Anton-supplied Vizarr view state exists for this store, so these are
   whole-well renders at resolution level s2, not a cropped and zoomed field.
2. This store's dynamic range is far lower than the Result 3 store: raw GFP
   maxima were 17179 (J4), 26639 (J7), 35357 (J10), against that store's
   signal reaching the full 16-bit range. A fixed 30000-60000 window would
   render J4 and J7 almost entirely black here. Instead, one window is
   computed by pooling all three wells' pixels and taking the 1st and 99.5th
   percentile, the same pooled-percentile convention
   devnote-swh-20260925-ph-sensor-in-solution/general/render-microscopy-fovs.py
   uses, so the three panels stay directly comparable.
"""
import json
import os
import matplotlib
import numpy as np
import zarr
from PIL import Image, ImageDraw, ImageFont

STORE = 'https://data.nucleus.engineering/microscopy/nucleus-bnext-01/Lysate_LuxR_Cytosol_EsaR_2026-10-05_18-59-02.423661.zarr'
WELLS = [
    ('HSL sensing GUVs', 'J4', 'J/4/0'),
    ('Negative control', 'J7', 'J/7/0'),
    ('Constitutive control', 'J10', 'J/10/0'),
]
T = 17  # last of 18 frames (indices 0-17), the endpoint the Doc's narrative discusses
GFP_CHANNEL = 1
LO_PCT, HI_PCT = 1.0, 99.5
UM_PER_PX = 1.332  # s2 scale, confirmed from this store's own multiscales metadata
BAR_UM = 500
OUTDIR = 'figures'


def main():
    frames = {}
    for name, well, path in WELLS:
        arr = zarr.open_group(f'{STORE}/{path}', mode='r')['s2']
        frame = np.asarray(arr[T, GFP_CHANNEL, 0, :, :]).astype(np.float32)
        frames[well] = frame
        print(f'  {well}: min {frame.min():.0f}, max {frame.max():.0f}')

    pool = np.concatenate([f.ravel() for f in frames.values()])
    lo, hi = float(np.percentile(pool, LO_PCT)), float(np.percentile(pool, HI_PCT))
    print(f'pooled window ({LO_PCT}-{HI_PCT} pct): {lo:.0f} to {hi:.0f}')

    font_path = os.path.join(matplotlib.get_data_path(), 'fonts', 'ttf', 'DejaVuSans.ttf')
    font = ImageFont.truetype(font_path, 40)
    bar_px = round(BAR_UM / UM_PER_PX)

    for name, well, path in WELLS:
        frame = frames[well]
        norm = np.clip((frame - lo) / (hi - lo), 0, 1)
        rgb = np.zeros((*norm.shape, 3), dtype=np.uint8)
        rgb[..., 1] = (norm * 255).astype(np.uint8)
        img = Image.fromarray(rgb, mode='RGB')

        draw = ImageDraw.Draw(img)
        margin = 80
        x0, y0 = margin, img.height - margin
        draw.rectangle([x0, y0, x0 + bar_px, y0 + 10], fill=(255, 255, 255))
        label = f'{BAR_UM} µm'
        box = draw.textbbox((0, 0), label, font=font)
        draw.text((x0 + (bar_px - (box[2] - box[0])) / 2, y0 - 55), label,
                   fill=(255, 255, 255), font=font)
        draw.text((margin, margin), well, fill=(255, 255, 255), font=font)

        path_out = f'{OUTDIR}/solution-{well.lower()}.png'
        img.save(path_out)
        print(f'  -> {path_out}')

    with open(f'{OUTDIR}/solution-fov-params.json', 'w') as handle:
        json.dump({'t': T, 'gfp_channel': GFP_CHANNEL,
                   'window_pooled_percentiles': [LO_PCT, HI_PCT],
                   'window_values': [lo, hi], 'um_per_px': UM_PER_PX,
                   'wells': {well: name for name, well, _ in WELLS}},
                  handle, indent=1)


if __name__ == '__main__':
    main()
