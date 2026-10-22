# Interactive viewers

Per-well microscopy for GFP expression in hydrogels, as interactive
viewers. The well descriptions are on [the main page](./main.md), under
Results.

The viewers are stacked rather than tabbed. The Vizarr widget creates
its viewer on a detached element with no width. It never re-measures.
Any instance hidden when the page mounts renders blank permanently.

Each viewer sets `"menuOpen": true`, because the widget starts its
sidebar closed by default and that sidebar holds the per-channel
contrast sliders a reader needs.

**Changed on 2026-10-12: the viewers now point at
`../../plugins/vizarr/vizarr-viewer.mjs`, not at the widget on
`curvenote.github.io`.** myst-theme mounts an anywidget inside a shadow
root. The style tags Material-UI and vizarr inject into `document.head`
do not cross that boundary. With the upstream widget, the sidebar
renders with its labels but zero-sized sliders. An earlier screenshot
of this page showed thin vertical bars where the Z and channel sliders
belong, for that reason. The local copy mirrors those styles
into the shadow root, the same fix already in place for the pH-sensor
DevNote's viewers. This page's two prior reconciliations settled on the
upstream widget instead, because the local copy then on hand failed
`curvenote check`. That copy is not this one: `plugins/vizarr/` is a
later, shared fix, and it passes.

These viewers do not survive JATS conversion. The archived record of
this result, once one exists, is a static figure and the prose on
[the main page](./main.md), not an image here.

:::{note} Both stores are live, and the 2026-10-11 404s were a v2 check against a v3 store
:name: gap-zarr-stores-not-live

**RESOLVED on 2026-10-12.** Both stores answer at `zarr.json`, with
`200`. The 2026-10-11 check tested `.zattrs`, `.zgroup` and `.zarray`,
the Zarr v2 marker names. Both stores are Zarr v3. A Zarr v3 store uses
`zarr.json` for its group and array markers instead. Every path tried
on 2026-10-11 answered 404 for that reason, even though the data was
already there. A pixel
chunk fetched directly from `E/12/0/s0/c/0/0/0/0/0` also returns `200`.
The image data itself, not only the metadata, is reachable.

- `https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr`
- `https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr`

Each store's `zarr.json` carries an OME-NGFF plate record. That record
states the well lists read earlier from the `.parquet` companions. The
"E12" store is a 4-row (D, E, F, G), 1-column (12) plate. All four
wells, including `G12`, exist as groups in the store. The "E15" store is
a 4-row, 4-column (14, 15, 16, 21) plate. All sixteen wells exist. The
well paths below, `<row>/<column>/0`, are checked against this record,
not inferred from the `.parquet` alone as they were on 2026-10-11.

Each well's image group carries two channels, Brightfield and GFP, and
a multiscale pyramid with levels `s0` through `s4`. The viewers below
render against that data directly.
:::

## E12 — GFP-GUVs+LUVs in solution

:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/E/12/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/E/12/0`, caption: (GFP-GUVs+LUVs in solution, well E12.)]

## G12 — outer-solution-only control

:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/G/12/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/G/12/0`, caption: (Outer-solution-only control, well G12.)]

:::{note} G12 exists in the store, and carries no segmented objects in the parquet table
:name: gap-g12-no-objects

**Narrowed on 2026-10-12.** The store's own `zarr.json` lists `G12` as a
well group, alongside `D12`, `E12` and `F12`. The well is not missing
from the store. Its absence is only from the `.parquet`, the per-object
segmentation table. `G12` is the outer-solution-only control, so an
empty segmentation table for it is the expected result, not a gap in the
data.
:::

## E14 — GFP-GUVs+LUVs in PEG4Nb pre-gel

:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/14/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/14/0`, caption: (GFP-GUVs+LUVs in PEG4Nb pre-gel, well E14.)]

## E15 — GFP-GUVs+LUVs in ULGA, z-stack

:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/15/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/15/0`, caption: (GFP-GUVs+LUVs in ULGA, well E15, z-stack.)]

## E16 — GFP-GUVs+LUVs in LGA

:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/16/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/16/0`, caption: (GFP-GUVs+LUVs in LGA, well E16.)]

## E21 — GFP-GUVs+LUVs in PEG4Nb gel

:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/21/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/21/0`, caption: (GFP-GUVs+LUVs in PEG4Nb gel, well E21.)]
