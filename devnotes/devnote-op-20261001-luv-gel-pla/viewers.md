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

These viewers do not survive JATS conversion. The archived record of
this result, once one exists, is a static figure and the prose on
[the main page](./main.md), not an image here. See
`gap-microscopy-no-static` on the main page for the full flag.

:::{danger} Neither store resolves yet, though both are confirmed multi-well
:name: gap-zarr-stores-not-live

Checked directly on 2026-10-11. Both URLs below, and every sub-path
tried under them (`/`, `/.zattrs`, `/.zgroup`, `/0/.zattrs`,
`/E/12/0/.zarray`), return 404. Their `.parquet` companions, at the same
base filename, both return 200 and are reachable.

- `https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr`
- `https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr`

The viewers below are wired to these URLs and will likely render blank
until the stores are uploaded. Ask whoever ran this microscopy session
whether the Zarr export is still pending. Also ask whether the URL in
`log-devnote-draft.docx` has a typo against the real location.

Each `.parquet` is a per-object feature table, not image data, and each
carries a `Well` column. Read directly, they show each store is
multi-well, despite each being named in the source for one well only.
The "E12" store's table lists wells `D12`, `E12` and `F12`. The "E15"
store's table lists fifteen wells, across rows D, E, F and G and
columns 14, 15, 16 and 21. That includes all four GFP-GUV gel
conditions named on the main page: `E14`, `E15`, `E16` and `E21`.

The well paths below, `<row>/<column>/0`, follow that table and the
convention already used for `E12`. They are not confirmed against the
Zarr group structure itself, since that structure is not reachable to
check. Confirm them once the store is live.
:::

## E12 — GFP-GUVs+LUVs in solution

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/E/12/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/E/12/0`, caption: (GFP-GUVs+LUVs in solution, well E12.)]

## G12 — outer-solution-only control

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/G/12/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/G/12/0`, caption: (Outer-solution-only control, well G12.)]

:::{attention} G12 carries no segmented objects in the parquet table
:name: gap-g12-no-objects

The "E12" store's `.parquet` lists wells `D12`, `E12` and `F12` only.
`G12` does not appear. `G12` is the outer-solution-only control. One
explanation is that it holds nothing for the segmentation step to find.
Another is that the well is missing from the store. Neither is
confirmed.
:::

## E14 — GFP-GUVs+LUVs in PEG4Nb pre-gel

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/14/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/14/0`, caption: (GFP-GUVs+LUVs in PEG4Nb pre-gel, well E14.)]

## E15 — GFP-GUVs+LUVs in ULGA, z-stack

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/15/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/15/0`, caption: (GFP-GUVs+LUVs in ULGA, well E15, z-stack.)]

## E16 — GFP-GUVs+LUVs in LGA

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/16/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/16/0`, caption: (GFP-GUVs+LUVs in LGA, well E16.)]

## E21 — GFP-GUVs+LUVs in PEG4Nb gel

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/21/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr/E/21/0`, caption: (GFP-GUVs+LUVs in PEG4Nb gel, well E21.)]
