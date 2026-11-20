# 2026-10-08 — Interactive viewer

Per-well microscopy for the C wells of `nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782`,
behind [Result 3](./main.md#result-3-detecting-bacterially-produced-hsl-in-solution)
on the main page. Vizarr cannot open a plate filtered to a subset of wells, so each
well below is its own viewer.

| Condition | Plasmid | Supernatant used | Wells |
| --- | --- | --- | --- |
| HSL sensing GUVs | LuxR-mNeonGreen | NEB5α w/ LuxI | C3, C4, C5 |
| Negative control | LuxR-mNeonGreen | NEB5α ΔLuxI | C6, C7, C8 |
| Constitutive control | Constitutive mNeonGreen | NEB5α ΔLuxI | C9, C10, C11 |

Each viewer below opens at the store's own default contrast and timepoint. The
static figures on the main page use a different window instead, GFP 30000 to 60000
at T = 19. Use the sliders below to match that window.

<!-- review-notes.yml#c-viewer-01 -->

## C3 — HSL sensing GUVs

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/3/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C4 — HSL sensing GUVs

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/4/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C5 — HSL sensing GUVs

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/5/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C6 — negative control

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/6/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C7 — negative control

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/7/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C8 — negative control

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/8/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C9 — constitutive control

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/9/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C10 — constitutive control

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/10/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C11 — constitutive control

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/11/0",
    "height": "600px",
    "menuOpen": true
}
:::
