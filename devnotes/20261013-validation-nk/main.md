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

:::{figure} ./figures/thumbnail-k18.png
:label: fig-thumbnail-k18
:align: center
:width: 75%

Archival record of the Vizarr viewer above, since a viewer does not
survive JATS conversion. Well K18, final timepoint (t=19 of 20), a centre
crop covering 1/9 of the plane. GFP shows in green and Alexa Fluor 647 in
blue, the store's own omero channel colors. Contrast comes from a
measured 1st-99.5th percentile stretch per channel, since the store's own
window metadata is the full 0-65535 range, not a real calibration. Scale
bar: 100 um.
:::

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
