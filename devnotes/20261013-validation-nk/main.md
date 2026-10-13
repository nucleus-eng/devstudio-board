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

:::{admonition} Well ID and dataset link disagree
:class: warning
:name: flags-well-mismatch

The source doc's "Well ID" field reads K18, matching the well this guest
was originally assigned. The "Dataset" link pasted into the same doc
points at well K/20/0 instead. Rendered below using K18, the explicitly
labeled field. Say which well is correct before this goes further.
:::

Reporter: pOpen-T7-deGFP, 2812 bp, circular, from
[nucleus-eng/DNA](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-deGFP.gbk).

:::{seqviz} ./dna/pOpen-deGFP.gbk
:height: 400px
:::

:::{platemap} ./experiments/20261013-validation-platemap-esaR-mNG-AHSL.csv
:height: 480px
:fields: Guest
:wells: 384
:label: platemap-20261013-nk
:::

:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
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
