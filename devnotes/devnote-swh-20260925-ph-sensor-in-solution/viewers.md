# Interactive viewers

Per-well microscopy for pH Sensor Validation in Solution, as interactive viewers. Each well is one OME-Zarr store.
The well descriptions are in the tab-set captions on [the main page](./main.md), under Results.

The viewers are stacked rather than tabbed. The Vizarr widget creates its viewer on a
detached element with no width and never re-measures, so any instance hidden when the page
mounts renders blank permanently.

Each viewer sets `"menuOpen": true`, because the widget starts its sidebar closed by
default and that sidebar holds the per-channel contrast sliders a reader needs.

Each viewer also sets `colors` and `contrast_limits`, one entry per channel in the store's
own order: Rhodamine first, then Alexa Fluor 647. The values are the ones
`figures/fov-render-params.json` records for the static figures on
[the main page](./main.md), the 1.0 and 99.5 percentiles they were stretched to, so a
viewer opens on the same yellow and red at the same stretch.

| Channel | Color | Window start | Window end |
| --- | --- | --- | --- |
| Rhodamine | `FFDC3C` | 2410 | 50690 |
| Alexa Fluor 647 | `FF3C28` | 1904 | 30863 |

Vizarr will not take these from its own image config. It reads a channel's color and
window from the store's `omero` metadata whenever that block exists, and ignores what it
is handed. The widget therefore applies them to that metadata on its way in. The stores
themselves still carry `FF0000` and `0000FF` with a window of 0 to 65535, the full 16-bit
range, which is why a viewer without these keys opens almost black. Writing the values
into each store's `omero` block would make the override unnecessary, and is the better
fix where a store can be rewritten.

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
    "menuOpen": true,
    "colors": ["FFDC3C", "FF3C28"],
    "contrast_limits": [[2410, 50690], [1904, 30863]]
}
:::

## D5 — pH 6.3, PLA1-GUV only
:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/SH-0925-D5_2026-09-25_11-32-48.009691.zarr/D/5/0",
    "height": "600px",
    "menuOpen": true,
    "colors": ["FFDC3C", "FF3C28"],
    "contrast_limits": [[2410, 50690], [1904, 30863]]
}
:::

## E4 — pH 7.6, PLA1-GUV + CPRG-LUV
:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/SH-0925-E4_2026-09-25_12-03-09.447054.zarr/E/4/0",
    "height": "600px",
    "menuOpen": true,
    "colors": ["FFDC3C", "FF3C28"],
    "contrast_limits": [[2410, 50690], [1904, 30863]]
}
:::

## E5 — pH 6.3, PLA1-GUV + CPRG-LUV
:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/SH-0925-E5-2_2026-09-25_12-04-22.672843.zarr/E/5/0",
    "height": "600px",
    "menuOpen": true,
    "colors": ["FFDC3C", "FF3C28"],
    "contrast_limits": [[2410, 50690], [1904, 30863]]
}
:::

