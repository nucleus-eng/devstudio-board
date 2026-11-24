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

<!-- Implementation notes, not for the reader. These viewers do not survive JATS
conversion. The static figure on main.md is the archival record. Each viewer is its
own widget, stacked rather than tabbed. The Vizarr widget creates its viewer on a
detached element with no width and never re-measures it. A hidden instance at page
mount renders blank for good. Each viewer sets "menuOpen": true, so the contrast
sliders are visible without a click. Each viewer loads
general/vizarr-viewer-patched.js, a patched copy of
curvenote.github.io/widgets/widgets/vizarr-viewer.js. The unpatched widget's sliders
render collapsed to 0x0 pixels. This happens under Material-UI's JSS runtime inside
the myst-anywidget wrapper's shadow root, confirmed directly in the browser.
`adoptedStyleSheets` does not fix it. It throws on a parsed style tag's own sheet, even
though the sheet is same-origin. The patched copy mirrors each document stylesheet
into one constructed `CSSStyleSheet` per source, and adopts those. When JSS inserts a
rule, it fires no event. The patched copy polls rule count every 400 ms instead, to
keep the stylesheets in sync.

Open question, not yet answered. Writing the GFP window (30000-60000) and T = 19
start into this store's own omero metadata makes every viewer open pre-set. This store
is live and shared, so other viewers of the same data see the same write. Confirm
before this write happens. State whether it goes on this store or on a separate copy
made for this DevNote.

Why the D wells are not on this page: Vizarr has no option to open a plate filtered to
a subset of wells. Opening a plate source renders every well in the store's own
metadata, with no way to select a subset. -->

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
