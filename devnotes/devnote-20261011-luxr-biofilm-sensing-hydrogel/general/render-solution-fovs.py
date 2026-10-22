#!/usr/bin/env python3
"""Render one representative field of view per condition for the solution
subsection of Result 2, from the Lysate_LuxR_Cytosol_EsaR store.

Adapted from general/render-microscopy-fovs.py (Result 3), with real
differences forced by the data and by Anton's instruction rather than chosen
freely:

1. No Vizarr view state was supplied for this store, so there is no target
   pixel to crop around. Anton instead asked for the well's own center,
   cropped to about one field of view: the whole-well render at s2 is
   2775x2775 px and visibly a tiled grid of camera fields, so a crop to 1/9
   of that area (1/3 the linear extent, 925x925 px) centered on the well
   approximates one field, confirmed by eye against the visible tile seams.

2. This store's dynamic range is far lower than the Result 3 store: raw GFP
   maxima in the full well were 17179 (J4), 26639 (J7), 35357 (J10), against
   that store's signal reaching the full 16-bit range. A fixed 30000-60000
   window would render two of the three wells almost entirely black.
   Instead, one window is computed by pooling the three CROPPED wells'
   pixels (not the whole-well pixels) and taking the 1st and 99.5th
   percentile, the same pooled-percentile convention
   devnote-20261011-ph-sensor-in-solution/general/render-microscopy-fovs.py
   uses, so the three panels stay directly comparable to each other at this
   crop, which is not the same window as a whole-well version would need.
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
BAR_UM = 100
CROP_FRACTION = 1 / 3  # linear fraction -> 1/9 area, "about one field of view"
OUTDIR = 'figures'


def center_crop(frame, fraction):
    n = frame.shape[0]
    crop_n = round(n * fraction)
    start = (n - crop_n) // 2
    return frame[start:start + crop_n, start:start + crop_n]


def main():
    frames = {}
    for name, well, path in WELLS:
        arr = zarr.open_group(f'{STORE}/{path}', mode='r')['s2']
        full = np.asarray(arr[T, GFP_CHANNEL, 0, :, :]).astype(np.float32)
        frames[well] = center_crop(full, CROP_FRACTION)
        print(f'  {well}: full {full.shape} -> crop {frames[well].shape}, '
              f'min {frames[well].min():.0f}, max {frames[well].max():.0f}')

    pool = np.concatenate([f.ravel() for f in frames.values()])
    lo, hi = float(np.percentile(pool, LO_PCT)), float(np.percentile(pool, HI_PCT))
    print(f'pooled window on crops ({LO_PCT}-{HI_PCT} pct): {lo:.0f} to {hi:.0f}')

    font_path = os.path.join(matplotlib.get_data_path(), 'fonts', 'ttf', 'DejaVuSans.ttf')
    bar_px = round(BAR_UM / UM_PER_PX)

    for name, well, path in WELLS:
        frame = frames[well]
        norm = np.clip((frame - lo) / (hi - lo), 0, 1)
        rgb = np.zeros((*norm.shape, 3), dtype=np.uint8)
        rgb[..., 1] = (norm * 255).astype(np.uint8)
        img = Image.fromarray(rgb, mode='RGB')

        draw = ImageDraw.Draw(img)
        margin = max(15, int(img.width * 0.03))
        font = ImageFont.truetype(font_path, max(16, int(img.width * 0.045)))
        x0, y0 = margin, img.height - margin
        draw.rectangle([x0, y0, x0 + bar_px, y0 + max(3, int(img.height * 0.01))],
                       fill=(255, 255, 255))
        label = f'{BAR_UM} µm'
        box = draw.textbbox((0, 0), label, font=font)
        draw.text((x0 + (bar_px - (box[2] - box[0])) / 2,
                   y0 - (box[3] - box[1]) - int(img.height * 0.02)),
                  label, fill=(255, 255, 255), font=font)
        draw.text((margin, margin), well, fill=(255, 255, 255), font=font)

        path_out = f'{OUTDIR}/solution-{well.lower()}.png'
        img.save(path_out)
        print(f'  -> {path_out} {img.size}')

    with open(f'{OUTDIR}/solution-fov-params.json', 'w') as handle:
        json.dump({'t': T, 'gfp_channel': GFP_CHANNEL,
                   'window_pooled_percentiles': [LO_PCT, HI_PCT],
                   'window_values': [lo, hi], 'um_per_px': UM_PER_PX,
                   'crop_fraction_linear': CROP_FRACTION,
                   'bar_um': BAR_UM,
                   'wells': {well: name for name, well, _ in WELLS}},
                  handle, indent=1)


if __name__ == '__main__':
    main()
