#!/usr/bin/env python3
"""Render one representative field of view for three of the twelve gel
stores under Result 2's gels subsection, from z = 50 of each store's own
101-plane Z-stack.

Adapted from general/render-solution-fovs.py, with real differences:

1. Each of these twelve stores is a single-well store in its own right (one
   row, one column in its plate metadata), not one plate with many wells, and
   each carries a real z dimension (101 planes) rather than z=1. A fixed
   z = 50, the requested slice, is used for all three, not an endpoint
   timepoint: each store has only one timepoint (a single end-point Z-stack),
   so there is no time axis to pick from here.

2. The contrast window is fixed (3615-9372 on the GFP channel), given by
   Anton rather than computed, unlike the pooled-percentile window the
   solution figures use.

3. Rendered from s0 (full native resolution, 0.333 um/px), not s2: this
   store's own pyramid is finer relative to its frame size (750x750 at s2
   against 3000x3000 at s0), so s0 keeps the crop sharp.

The condition labels (HSL sensing gels / Negative control gels / Constitutive
control gels) are the Doc's own tbl-gel-conditions labels for D5, D7 and D9.
They disagree with what the store filenames themselves claim for D5 and D7
(J_N_-100uM_AHL_D5_gels and J_N_+100uM_AHL_D7_gels say the opposite of what
the table says); flagged in main.md as flags-gel-well-hsl-mismatch, not
resolved here.
"""
import os
import matplotlib
import numpy as np
import zarr
from PIL import Image, ImageDraw, ImageFont

BASE = 'https://data.nucleus.engineering/microscopy/nucleus-bnext-01'
WELLS = [
    ('HSL sensing gels', 'D5', 'J_N_-100uM_AHL_D5_gels_2026-10-07_14-44-55.273559', 'D/5/0'),
    ('Negative control gels', 'D7', 'J_N_+100uM_AHL_D7_gels_2026-10-07_14-42-23.412204', 'D/7/0'),
    ('Constitutive control gels', 'D9', 'J_N_Consitutive_AHL_D9_gels_2026-10-07_14-52-02.837332', 'D/9/0'),
]
Z = 50
T = 0
GFP_CHANNEL = 1
LO, HI = 3615, 9372
UM_PER_PX = 0.333  # s0 scale, confirmed from each store's own multiscales metadata
BAR_UM = 100
CROP_FRACTION = 1 / 3  # linear fraction -> 1/9 area, "about one field of view"
OUTDIR = 'figures'


def center_crop(frame, fraction):
    n = frame.shape[0]
    crop_n = round(n * fraction)
    start = (n - crop_n) // 2
    return frame[start:start + crop_n, start:start + crop_n]


def main():
    font_path = os.path.join(matplotlib.get_data_path(), 'fonts', 'ttf', 'DejaVuSans.ttf')
    bar_px = round(BAR_UM / UM_PER_PX)

    for label, well, store, path in WELLS:
        arr = zarr.open_group(f'{BASE}/{store}.zarr/{path}', mode='r')['s0']
        full = np.asarray(arr[T, GFP_CHANNEL, Z, :, :]).astype(np.float32)
        frame = center_crop(full, CROP_FRACTION)
        print(f'  {well} ({label}): full {full.shape} -> crop {frame.shape}, '
              f'min {frame.min():.0f}, max {frame.max():.0f}')

        norm = np.clip((frame - LO) / (HI - LO), 0, 1)
        rgb = np.zeros((*norm.shape, 3), dtype=np.uint8)
        rgb[..., 1] = (norm * 255).astype(np.uint8)
        img = Image.fromarray(rgb, mode='RGB')

        draw = ImageDraw.Draw(img)
        margin = max(15, int(img.width * 0.03))
        font = ImageFont.truetype(font_path, max(16, int(img.width * 0.045)))
        x0, y0 = margin, img.height - margin
        draw.rectangle([x0, y0, x0 + bar_px, y0 + max(3, int(img.height * 0.01))],
                       fill=(255, 255, 255))
        text = f'{BAR_UM} µm'
        box = draw.textbbox((0, 0), text, font=font)
        draw.text((x0 + (bar_px - (box[2] - box[0])) / 2,
                   y0 - (box[3] - box[1]) - int(img.height * 0.02)),
                  text, fill=(255, 255, 255), font=font)
        draw.text((margin, margin), well, fill=(255, 255, 255), font=font)

        path_out = f'{OUTDIR}/gel-{well.lower()}.png'
        img.save(path_out)
        print(f'  -> {path_out} {img.size}')


if __name__ == '__main__':
    main()
