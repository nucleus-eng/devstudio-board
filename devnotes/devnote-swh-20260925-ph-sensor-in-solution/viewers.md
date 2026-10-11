# Interactive viewers

Per-well microscopy for pH Sensor Validation in Solution, as interactive viewers. Each well is one OME-Zarr store.
The well descriptions are in the tab-set captions on [the main page](./main.md), under Results.

The viewers are stacked rather than tabbed. The Vizarr widget creates its viewer on a
detached element with no width and never re-measures, so any instance hidden when the page
mounts renders blank permanently.

Each viewer sets `"menuOpen": true`, because the widget starts its sidebar closed by
default and that sidebar holds the per-channel contrast sliders a reader needs.

The viewers do not open on the colors and stretch the static figures use, and they cannot
be made to from here. Vizarr takes a channel's color and window from the store's own
`omero` metadata whenever that metadata exists, and ignores the `colors` and
`contrast_limits` it is handed. Measured on 2026-10-11, outside any shadow root, against
`SH-0925-D4`: passing both keys, with and without `channel_axis`, left every contrast
slider at 0 to 65535.

So the fix belongs in the stores. These four carry `FF0000` and `0000FF` with a window of
0 to 65535, the full 16-bit range, which is why a viewer opens almost black. The values
that would match the static figures, from `figures/fov-render-params.json`, are:

| Channel | Color | Window start | Window end |
| --- | --- | --- | --- |
| Rhodamine | `FFDC3C` | 2410 | 50690 |
| Alexa Fluor 647 | `FF3C28` | 1904 | 30863 |

Those are the 1.0 and 99.5 percentiles the figures were stretched to. Writing them into
each store's `omero` block makes the viewers and the figures agree.

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

