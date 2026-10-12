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

:::{danger} Two stores do not resolve, and two named wells have no store at all
:name: gap-zarr-stores-not-live

Checked directly on 2026-10-11. Both URLs below, and every sub-path
tried under them (`/`, `/.zattrs`, `/.zgroup`, `/0/.zattrs`,
`/E/12/0/.zarray`), return 404. Their `.parquet` companions, at the same
base filename, both return 200 and are reachable.

- `https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr`
- `https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr`

The two viewers below are wired to these URLs and will likely render
blank until the stores are uploaded. Ask whoever ran this microscopy
session whether the Zarr export is still pending. Also ask whether the
URL in `log-devnote-draft.docx` has a typo against the real location.

E14 (PEG4Nb pre-gel) and E16 (LGA) have no store named anywhere in the
source at all, not even an unreachable one. No viewer is written for
them below, so as not to imply a source exists.
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

## E15 — GFP-GUVs+LUVs in ULGA, z-stack

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr`, caption: (GFP-GUVs+LUVs in ULGA, well E15, z-stack.)]

This store's filename names E15 specifically, unlike the paired
solution store above. It is used at its root rather than addressed to a
well path. Whether it is in fact single-well is not confirmed, since
the store does not resolve to check.

## E14 — GFP-GUVs+LUVs in PEG4Nb pre-gel

No store is named for this well anywhere in the source.

## E16 — GFP-GUVs+LUVs in LGA

No store is named for this well anywhere in the source.
