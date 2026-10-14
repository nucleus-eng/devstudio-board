---
title: Build a Base Cell
subtitle: Validation-01
---

# Overview

This DevNote pools the Build a Base Cell protocol validation from the
DevStudio Capstone event, 2026-10-13. It covers every guest who built a
Base Cell liposome that day.

  - Process protocol: <https://docs.nucleus.engineering/docs/processes/build-base-cell/main/>
  - Base cytosol specification: <https://docs.nucleus.engineering/docs/modules/base-cytosol/spec/>

:::{admonition} One plate, one devnote, not one devnote per guest
:name: scope-consolidated

Most guests left the Capstone before anyone processed their own well on
its own. A separate Validation-NN DevNote per guest stays mostly empty
under those conditions. This page instead presents the one plate-wide
dataset every guest's liposomes are part of. A pooled Discussion section
collects the protocol feedback guests wrote down.
:::

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

## Cell segmentation check

A spot check of four segmented objects across four wells and timepoints.
Each one matches its stored label at 100%.

:::{figure} ./figures/cell-grid-1.png
:label: fig-cell-grid
:align: center
:width: 90%

Four example objects: one from well MC 2 (t7), one from BP (t5), and two
from MB 1 (t7 and t2). Each one shows the Rhodamine and GFP channels
with its segmentation mask outlined.
:::

## Population summaries

:::{figure} ./figures/summary-0.png
:label: fig-summary
:align: center
:width: 90%

Cell count and median GFP intensity per well, by name, across all 9
timepoints.
:::

:::{figure} ./figures/size-0.png
:label: fig-size
:align: center
:width: 90%

Object size distribution per well over time.
:::

:::{figure} ./figures/size-expression-0.png
:label: fig-size-expression
:align: center
:width: 90%

Object size plotted against GFP expression.
:::

:::{figure} ./figures/density-over-time-0.png
:label: fig-density-over-time
:align: center
:width: 90%

Object density per well over time.
:::

:::{figure} ./figures/quantile-ribbon-0.png
:label: fig-quantile-ribbon
:align: center
:width: 90%

GFP intensity quantile ribbon per well over time.
:::

:::{figure} ./figures/ecdf-0.png
:label: fig-ecdf
:align: center
:width: 90%

Empirical cumulative distribution of GFP intensity per well: what
populations are present, and how long their tails run.
:::

:::{figure} ./figures/positive-fraction-0.png
:label: fig-positive-fraction
:align: center
:width: 90%

Fraction of cells scored GFP-positive per well over time, gated at the
99th percentile: how many cells turn on, and how bright they get.
:::

:::{admonition} Large figure: 4824x26369 px, 21.8 MB
:class: warning
:name: flags-fogplot-size

The two fogplot figures below are tall, one panel per well stacked
vertically. Loading both on one page adds a heavy page weight. Decide
whether these belong on their own page before this goes further.
:::

:::{figure} ./figures/fogplot-0.png
:label: fig-fogplot
:align: center
:width: 90%

Per-well GFP distribution ("fog plot"), one panel per well.
:::

:::{figure} ./figures/fogplot-compare-0.png
:label: fig-fogplot-compare
:align: center
:width: 90%

Per-well GFP distributions compared directly against each other.
:::

# Discussion

Pooled from the guests who left written feedback. Each entry is
attributed to the guest who wrote it, carried over verbatim.

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

## What changed how you're thinking about your own work?

No guest answered this question in writing.

# Contributors

Everyone who built a Base Cell liposome in this plate, per the platemap.

| Name | Affiliation | Well(s) |
| --- | --- | --- |
| Surendra Yadav | | D5 |
| Neha Kamat | | D6 |
| Andrew Ellington | | D7 |
| Becky Pferdehirt | | D8 |
| Richard Murray | | D9 |
| Leopold Green | | E5 |
| Michael Booth | University College London | E6, E7 |
| Michael Clear | Schmidt Sciences | E8, E9 |
| Claudia Contini | Imperial College London | E10 |

:::{admonition} Affiliations and roles still open for everyone
:name: gap-contributor-affiliations

No affiliation is on file for Surendra Yadav, Neha Kamat, Andrew
Ellington, Becky Pferdehirt, Richard Murray, or Leopold Green. Surendra
Yadav ran the session and is proposed as an author in curvenote.yml, not
only a contributor. Settle both before this goes further.
:::
