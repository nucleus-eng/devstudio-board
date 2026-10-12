# 2026-10-07 — Interactive viewer

Per-well microscopy for three of the gel wells behind
[Detecting purified HSL using lysate-based synthetic cells in gels](./main.md),
as interactive viewers: D7 (HSL sensing gels), D4 (negative control gels), and D10
(constitutive control gels). Unlike the C-well page, each gel well is its own separate
store. It is not one well inside a shared plate store, so each viewer below points at a
different source.

These wells were chosen to complement the static figures on the main page, which show
D6, D5 and D11. Together the two pages cover two of the three replicate wells for each
condition.

:::{admonition} Custom contrast is not live in these viewers
:name: flags-gel-viewer-metadata

Vizarr reads the initial channel contrast and the initial Z plane from the store's own
`omero` metadata. The static figures on the main page use a fixed GFP window of 4526 to
12204 at z = 50, chosen on 2026-10-12. Neither value is written into these stores. Each viewer below opens at whatever window
and Z plane the store's own metadata carries, not that fixed window.
:::

Each viewer sets `"menuOpen": true`, so the contrast sliders are visible without a
click. Each viewer also loads
[`general/vizarr-viewer-patched.js`](./general/vizarr-viewer-patched.js), the same
patched widget copy used on [the C-well page](./2026-10-08-interactive-viewer.md). That
copy exists because Vizarr's own sliders render collapsed to 0x0 pixels under the
unpatched widget inside a shadow root.

These viewers do not survive JATS conversion. A static figure carrying the same result
belongs on [the main page](./main.md), under Results, as the archival record.

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

:::{admonition} D10's store covers a bigger area than the other two
:name: flags-gel-viewer-d10-area

The Doc's own note on `J_N_Consitutive_AHL_D10_gel_bigger_areas` says a bigger area was
measured because of a large air bubble. This viewer opens the well exactly as the store
has it. No crop or re-measurement was applied here.
:::
