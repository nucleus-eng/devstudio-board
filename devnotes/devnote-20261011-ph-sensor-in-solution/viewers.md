# Interactive viewers

Per-well microscopy for pH Sensor Validation in Solution, as interactive viewers. Each well is one OME-Zarr store.
The well descriptions are in the tab-set captions on [the main page](./main.md), under Results.

Each viewer opens with the same color and contrast stretch as the static figures on
[the main page](./main.md).

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

