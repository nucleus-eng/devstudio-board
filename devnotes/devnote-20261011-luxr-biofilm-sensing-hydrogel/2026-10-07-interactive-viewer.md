# 2026-10-07 — Interactive viewer

Per-well microscopy for six of the gel wells behind
[Detecting purified HSL using lysate-based synthetic cells in gels](./main.md),
as interactive viewers: D7 (HSL sensing gels), D4 (negative control gels), D10
(constitutive control gels), and D15, D16, D17 (empty ULGA gels).

D7, D4 and D10 were chosen to complement the static figures on the main page, which
show D6, D5 and D11. Together the two pages cover two of the three replicate wells for
the HSL sensing, negative control and constitutive control conditions. The empty ULGA
gels condition has no figure on the main page, so all three of its replicate wells are
viewers here instead.

Each viewer below opens at whatever contrast window and Z plane the store's own
`omero` metadata carries. The static figures on the main page use a fixed GFP
window instead, 4526 to 12204 at z = 50.

## D7 — HSL sensing gels

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_%2B100uM_AHL_D7_gels_2026-10-07_14-42-23.412204.zarr/D/7/0",
    "height": "600px",
    "menuOpen": true
}
:::

## D4 — negative control gels

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_-100uM_AHL_D4_gels_2026-10-07_14-46-52.618937.zarr/D/4/0",
    "height": "600px",
    "menuOpen": true
}
:::

## D10 — constitutive control gels

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_Consitutive_AHL_D10_gel_bigger_areas_2026-10-07_14-55-47.101109.zarr/D/10/0",
    "height": "600px",
    "menuOpen": true
}
:::

D10's store covers a bigger area than the other two, measured that way because of a
large air bubble. This viewer opens the well exactly as the store has it, with no
crop or re-measurement.

## D15 — empty ULGA gel

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_just_gel_1_2026-10-07_15-04-39.160520.zarr/D/15/0",
    "height": "600px",
    "menuOpen": true
}
:::

## D16 — empty ULGA gel

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_just_gel_2_2026-10-07_15-06-06.512744.zarr/D/16/0",
    "height": "600px",
    "menuOpen": true
}
:::

## D17 — empty ULGA gel

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_just_gel_3_2026-10-07_15-07-38.879378.zarr/D/17/0",
    "height": "600px",
    "menuOpen": true
}
:::
