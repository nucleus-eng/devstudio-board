# Interactive viewers

Per-well microscopy for pH Sensor Validation in Solution, as interactive viewers. Each well is one OME-Zarr store.
The well descriptions are in the tab-set captions on [the main page](./main.md), under Results.

The viewers are stacked rather than tabbed. The Vizarr widget creates its viewer on a
detached element with no width and never re-measures, so any instance hidden when the page
mounts renders blank permanently.

Each viewer sets `"menuOpen": true`, because the widget starts its sidebar closed by
default and that sidebar holds the per-channel contrast sliders a reader needs.

The viewers point at `../../plugins/vizarr/vizarr-viewer.mjs` rather than at the widget on
curvenote.github.io. myst-theme mounts an anywidget inside a shadow root, which the style
tags Material-UI and vizarr inject into `document.head` do not cross, so with the upstream
widget the panel renders with labels, zero-sized sliders and no stacking of its own. The
local copy mirrors those styles into the shadow root.

These viewers do not survive JATS conversion, and neither does the tab set of the same
four wells on [the main page](./main.md). The archived record of this result is the prose
description under each well, not an image.

## D4 — pH 7.6, PLA1-GUV only
:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/SH-0925-D4_2026-09-25_11-27-49.059491.zarr/D/4/0",
    "height": "600px",
    "menuOpen": true
}
:::

## D5 — pH 6.3, PLA1-GUV only
:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/SH-0925-D5_2026-09-25_11-32-48.009691.zarr/D/5/0",
    "height": "600px",
    "menuOpen": true
}
:::

## E4 — pH 7.6, PLA1-GUV + CPRG-LUV
:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/SH-0925-E4_2026-09-25_12-03-09.447054.zarr/E/4/0",
    "height": "600px",
    "menuOpen": true
}
:::

## E5 — pH 6.3, PLA1-GUV + CPRG-LUV
:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/SH-0925-E5-2_2026-09-25_12-04-22.672843.zarr/E/5/0",
    "height": "600px",
    "menuOpen": true
}
:::

