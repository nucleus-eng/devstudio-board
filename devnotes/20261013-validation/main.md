---
title: Build a Base Cell
subtitle: Validation
---

# Overview

This DevNote validates the Build a Base Cell protocol at the DevStudio Capstone event. Documentation was accessed on 2026-10-13

  - Process protocol: <https://docs.nucleus.engineering/docs/processes/build-base-cell/main/>
  - Base cytosol specification: <https://docs.nucleus.engineering/docs/modules/base-cytosol/spec/>


# Results

The plate held 11 wells, one or two per guest, imaged over 9 timepoints
(t0-t8). Every well carries the same reporter construct, pOpen-T7-deGFP,
2812 bp, circular, from
[nucleus-eng/DNA](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-deGFP.gbk).

:::::{tab-set}

::::{tab-item} Construct
:sync: construct

:::{seqviz} ./dna/pOpen-deGFP.gbk
:height: 400px
:::

::::

::::{tab-item} Platemap
:sync: platemap

:::{platemap} ./experiments/20261013-devstudio-liposomes-platemap.csv
:height: 420px
:fields: Person, DNA, Membrane
:label: platemap-20261013-validation
:::

::::

:::::

Full notebook: [Liposome Timeseries Analysis (2026-10-13)](./20261013-devstudio-liposomes-timeseries_2026-10-13_12-07-24.011026.ipynb).

:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/20261013-devstudio-liposomes-timeseries_2026-10-13_12-07-24.011026.zarr/E/10/0",
    "height": "600px",
    "menuOpen": true
}
:::

Showing well E10 (Claudia Contini), not the plate root. The full-plate
grid failed to fetch on deployment, since it loads all 11 wells at
once instead of one. Name a different well to show here instead of E10.


## Population summaries

The population summary below comes from segmented liposome images taken
at the Capstone.

:::{figure} ./figures/fogplot-compare-0.png
:label: fig-fogplot-compare
:align: center
:width: 90%

Per-well GFP distributions compared directly against each other.
:::

# Discussion

## Did the protocol work as written?

- **Claudia Contini:** Everything worked as expected.
- **Michael Booth:** Instead of the 5 µL of water at the end, added 1 µL
  extra of ribosomes and 4 µL of water. Otherwise, the protocol worked
  very well and was clear, with Surendra Yadav also showing the steps.
- **Michael Clear:** Too much of the aqueous phase was still present
  before resuspending the pellet, roughly 100 µL of solution left at the
  time of resuspension.

## What was unclear or missing?

- **Claudia Contini:** Adding 20 µL of lipid-oil solution on top of
  glucose.
- **Michael Clear:** Some lack of clarity around the lipid removal step
  after centrifugation. The general approach was clear, but it was not
  optimized for concentration.

# Participants

Surendra Yadav (b.next, well D5), Neha Kamat (Northwestern University,
well D6), Andrew Ellington (University of Texas at Austin, well D7),
Becky Pferdehirt (Astera Institute, well D8), Richard Murray (Schmidt
Sciences, well D9), Leopold Green (Purdue University, well E5), Michael
Booth (University College London, wells E6 and E7), Michael Clear
(Schmidt Sciences, wells E8 and E9), and Claudia Contini (Imperial
College London, well E10).

# Acknowledgments

Thank you to Yen-Yu Hsu (b.next) and Surendra Yadav (b.next) for serving
as TAs at this session.

