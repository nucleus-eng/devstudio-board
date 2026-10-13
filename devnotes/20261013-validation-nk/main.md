# Build a Base Cell: Validation-01

## Overview

This DevNote validates the Build a Base Cell protocol (accessed on: 2026-10-13) at the DevStudio Capstone event.

## Result

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

:::{figure} ./figures/thumbnail-k18.png
:label: fig-thumbnail-k18
:align: center
:width: 75%

Well K18, final timepoint (t=19 of 20). Field of view: 2000x2000 px
(0.333 um/px) at x=3050, y=3200, full resolution. GFP in green, Alexa
Fluor 647 in blue, per the omero channel colors in the dataset metadata.
Contrast: a measured 1st-99.5th percentile stretch per channel. Scale
bar: 100 um. Source:
`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/201009o_EsaR_mNG_0.1_0.5_K_L_2026-10-09_19-47-50.861429.zarr/K/18/0`
:::

Well ID: K18
