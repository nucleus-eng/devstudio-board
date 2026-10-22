#!/usr/bin/env python3
"""Render one representative field of view for three of the twelve gel
stores under Result 2's gels subsection, from z = 50 of each store's own
101-plane Z-stack.

Adapted from general/render-solution-fovs.py. Real differences:

1. Each of these twelve stores is a single-well store in its own right (one
   row, one column in its plate metadata), carrying a real z dimension (101
   planes) and a single timepoint, rather than z=1 with many timepoints.
   z = 50 is a fixed single slice, not an endpoint timepoint.

2. The contrast window is fixed (4526-12204 on the GFP channel) and gamma is
   1 (linear), both given by Anton rather than computed.

3. Rendered from s0 (full native resolution, 0.333 um/px): this store's own
   pyramid is finer relative to its frame size than the solution store's.

Condition-to-well mapping, resolved 2026-10-12. tbl-gel-conditions
originally named D3-D5 "HSL sensing gels" and D6-D8 "Negative control gels",
disagreeing with the store filenames (J_N_-100uM_AHL_D*_gels for D3-D5,
J_N_+100uM_AHL_D*_gels for D6-D8). Anton's correction matches the store
filenames and swaps the two labels; the well clusters themselves did not
change. WELLS below reflects the corrected mapping.

Two earlier attempts preceded this one, both superseded, for the record:
(1) wells D5, D7, D9 at a 3615-9372 window, single z = 50 slice: D5 and D7
were nearly black, which could not settle the label question on its own.
(2) wells D6, D5, D11 at this same 4526-12204 window, but a maximum-intensity
projection across all 101 z-planes rather than a single slice, matching a
script Niall uses: D5 and D11 looked right, but D6's projected maximum
(57623) was far past the window ceiling and rendered fully saturated.
Returning to a single z = 50 slice fixed it: D6's raw value there is 23460,
inside a displayable range.
"""
import os
import matplotlib
import numpy as np
import zarr
from PIL import Image, ImageDraw, ImageFont

BASE = 'https://data.nucleus.engineering/microscopy/nucleus-bnext-01'
WELLS = [
    ('HSL sensing gels', 'D6', 'J_N_+100uM_AHL_D6_gels_2026-10-07_14-36-46.345035', 'D/6/0'),
    ('Negative control gels', 'D5', 'J_N_-100uM_AHL_D5_gels_2026-10-07_14-44-55.273559', 'D/5/0'),
    ('Constitutive control gels', 'D11', 'J_N_Consitutive_AHL_D11_gels_2026-10-07_14-53-48.138799', 'D/11/0'),
]
Z = 50
T = 0
GFP_CHANNEL = 1
LO, HI = 4526, 12204
GAMMA = 1.0
UM_PER_PX = 0.333  # s0 scale, confirmed from each store's own multiscales metadata
BAR_UM = 100
CROP_FRACTION = 1 / 3  # linear fraction -> 1/9 area, "about one field of view"
OUTDIR = 'figures'


def center_crop(frame, fraction):
    n = frame.shape[0]
    crop_n = round(n * fraction)
    start = (n - crop_n) // 2
    return frame[start:start + crop_n, start:start + crop_n]


def render(img, lo, hi, gamma):
    v = np.clip((img.astype(np.float32) - lo) / (hi - lo), 0, 1)
    if gamma != 1.0:
        v = v ** (1.0 / gamma)
    rgb = np.zeros((*v.shape, 3), dtype=np.uint8)
    rgb[..., 1] = (v * 255).astype(np.uint8)
    return rgb


def main():
    font_path = os.path.join(matplotlib.get_data_path(), 'fonts', 'ttf', 'DejaVuSans.ttf')
    bar_px = round(BAR_UM / UM_PER_PX)

    for label, well, store, path in WELLS:
        arr = zarr.open_group(f'{BASE}/{store}.zarr/{path}', mode='r')['s0']
        full = np.asarray(arr[T, GFP_CHANNEL, Z, :, :]).astype(np.float32)
        frame = center_crop(full, CROP_FRACTION)
        print(f'  {well} ({label}): full {full.shape} -> crop {frame.shape}, '
              f'min {frame.min():.0f}, max {frame.max():.0f}')

        img = Image.fromarray(render(frame, LO, HI, GAMMA), mode='RGB')

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
