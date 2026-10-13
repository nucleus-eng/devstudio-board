# Base Cell Validation — Neha Kamat

## Overview

This DevNote validates the Build a Base Cell protocol (accessed on: 2026-10-13) at the DevStudio Capstone event.

:::{admonition}
:name: scope-demo-dataset

This run uses the EsaR-mNG AHSL dataset as a stand-in for a pipeline speed run on 2026-10-13, not a real Base Cell deGFP acquisition. The author says this is intentional for this demo.
:::

## Result

:::{admonition}
:name: gap-result-observations

Please fill in: describe what you see in your well. Do you see green fluorescence? How does it compare to the example image in the Base Cell protocol?
:::

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/201009o_EsaR_mNG_0.1_0.5_K_L_2026-10-09_19-47-50.861429.zarr/K/18/0",
    "height": "600px",
    "menuOpen": true
}
:::

<!-- missing notebook -->
<!-- REVIEW: no static archival figure. A viewer does not survive JATS conversion, and this run has no screenshot captured yet. Add one once the author records an observation. -->

Well ID: K18

:::{table} Platemap, 2026-10-09 EsaR-mNG AHSL run
:label: tbl-platemap-nk

| Well | Name | Type |
| --- | --- | --- |
| K18 | + AHSL | Sample |
:::

Full platemap: [20261013-validation-platemap-esaR-mNG-AHSL.csv](../../resources/20261013-validation-platemap-esaR-mNG-AHSL.csv)

## What's next

:::{admonition}
:name: gap-whats-next

Please fill in: what do you want to do with this cell next? What questions did this raise?
:::

## Credit

:::{admonition}
:name: gap-credit

Please fill in: did anyone in the community help you get this running?
:::
