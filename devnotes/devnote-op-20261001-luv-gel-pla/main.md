<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

# Overview

We are trying to embed vesicle systems in hydrogels to study their yield,
stability, and structural integrity in different polymer environments.

<!-- Overview supplied by the reviewer in review cycle v1, prompt 5, and
carried verbatim. The source log carries no overview. Its entire body is the
heading "# Results", one pasted figure, and the line
"Analysis: https://colab.research.google.com/drive/1ebR3gcpx0j-HCuA4N5lDdILkSQ6BneoJ#scrollTo=5a08dde5". -->

:::{danger} Unresolved before publication
:name: flags-blocking

**Date mismatch across three sources.** The Log folder is named
`OP-20261001`. The three plate reader data files the notebook loads are named
`20260930-164151-synergy2-luv-gel-OJ.txt`,
`20260930-164151-synergy2-luv-gel-OJ-Day2.txt` and
`20260930-164151-synergy2-luv-gel-OJ-Day2-afterPLA.txt`, all carrying the date
`20260930`. The platemap rows carry the date `2/10/2026`. Confirm which date
belongs to this experiment before proceeding. A wrong date links the wrong
data to the wrong experiment. This DevNote adopts none of the three, and
`curvenote.yml` holds `[PLEASE FILL IN]` for `date`.

**Still open, review cycle v1, prompt 3.** The reviewer answered "Dates do
not matter". That is a deferral and not a date. The venue needs one date in
`curvenote.yml`, so the field stays `[PLEASE FILL IN]`. Name one of the
three, or say that any of the three is acceptable and the folder date is
adopted.

**The source log is a stub.** It has no overview, no protocol, no methods
narrative, no results prose and no notes. Every section below marked
`[PLEASE FILL IN]` is a gap for that reason, not an extraction failure. The
analysis notebook is the only substantial record of this experiment.

**No build file.** The Log folder holds no build spreadsheet, so
`devstudio-build-to-composition` has not run and no composition table can be
produced.

**Closed, review cycle v1, prompt 4.** The reviewer answered "Leave as is".
This DevNote carries no composition table.

**Title and authors.** The source log carries no Specification table and no
Authors table. The Log folder is prefixed `OP` and the data filenames are
suffixed `OJ`. Neither is a stated name.

**Answered, review cycle v1, prompts 1 and 2.** The title is
"Embedding Developer Cells in Gels". The author is Ojaswita Pant, with the
email `ojaswitapant2029@u.northwestern.edu`. Both are now in
`curvenote.yml`.

Two things the answer did not settle. The affiliation is read off the email
domain as Northwestern University, which is evidence and not a statement by
the author. No ORCID is recorded.
:::

# Reagents

:::{table} Reagents and equipment
:label: tbl-reagents

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
:::

:::{attention} Reagents not recorded
:name: gap-reagents

The source log has no reagents section and the folder holds no materials
file. The sample names in {numref}`tbl-platemap` identify seven conditions by
abbreviation: `LUV`, `PEG_gel`, `PEG_pregel`, `ULGA`, `LGA`, `Cytosol-PLA`
and `buffer-PLA`. Expand each abbreviation and supply the vendor, catalog
number, price and storage conditions for every reagent used.

**Deferred, review cycle v1, prompt 8.** The reviewer answered "skip for
now". The table stays blank and this flag stays live. The gel stocks in
{numref}`tbl-stock-peg4nb`, {numref}`tbl-stock-ulga` and
{numref}`tbl-stock-lga` name chemicals and amounts, and they are not a
reagents table.
:::

# Protocol

## Vesicles

[PLEASE FILL IN]

## Gels

Three gel formulations were used. Each stock table below is reproduced from
the `Gel formulations` sheet, one tab per formulation.

:::::{tab-set}

::::{tab-item} PEG4Nb
:sync: peg4nb

:::{table} PEG4Nb gel stock
:label: tbl-stock-peg4nb

| Chemical | Conc. | Mwt | Amount (g) |
| --- | --- | --- | --- |
| PEG4Nb | 80 mM | 5000 Da | 0.4 |
| PEG4SH | 20 mM | 2000 Da | 0.04 |
| LAP | 16.9 mM | 294.21 g/mol | 0.004972149 |
| Buffer | 1 ml | | |
:::

The sheet carries the formula `Mass (g) = Molarity (mol/L) × Volume (L) ×
Molar Mass (g/mol)` beside this table, and two notes. The first reads
"buffer used was PBS and Tris:HEPES. Component Tris1M-HEPES1.15M buffer
stock (~2520 mOsm)". The second reads "did not work with PBS in SWH's GUVs".

::::

::::{tab-item} ULGA
:sync: ulga

:::{table} ULGA gel stock, London
:label: tbl-stock-ulga

| Chemical | Conc. | Amount |
| --- | --- | --- |
| ULGA | 1 w/v% | 0.02 g |
| OS (glucose) | 1057 Osm | 2 mL |
:::

::::

::::{tab-item} LGA
:sync: lga

:::{table} LGA gel stock, SWH
:label: tbl-stock-lga

| Chemical | Conc. | Amount |
| --- | --- | --- |
| LGA | 2.70% | 40.5 mg |
| UPDI water (UltraPure DNase/RNase-Free Distilled Water) | | 1500 ul |
:::

The sheet carries one note beside this table: "dilute it down to 0.7%".

::::

:::::

:::{attention} Protocol still incomplete
:name: gap-protocol

The source log has no protocol section. The plate was read three times, on
day 1, on day 2 after overnight incubation, and on day 2 after PLA addition.
That read order is taken from the data filenames and from the column labels
in the `PLA-CPR/CPRG` sheet. No written protocol states it. Supply the
vesicle preparation, the gel conditions, the PLA addition step and the plate
reader settings.

**Answered in part, review cycle v1, prompt 6.** The reviewer asked for two
subsections, vesicles and gels. The reviewer also pointed at the
`Gel formulations` sheet for a tab-set of tables. The three stock tables
above come from that sheet. Their tabs are `PEG4Nb`, `ULGA-London` and
`LGA-SWH`.

Three things the answer did not supply. The vesicle preparation is still
blank. The gel stocks above are stocks, and not the embedding steps. The PLA
addition step and the plate reader settings are still missing.
:::

# Methods

## PEG-NB

:::{admonition}
Please add a protocol for embedding vesicles in PEG-NB
:::

## LGA

:::{admonition}
Please add a protocol for embedding vesicles in LGA
:::

## ULGA

:::{admonition}
Please add a protocol for embedding vesicles in ULGA
:::

## LUV-Gel

<!-- The heading carries no date. The folder date, the data filenames
and the platemap disagree. See the blocking date flag above. -->

This experiment has no composition table. The Log folder holds no build
spreadsheet, and the reviewer closed the question in review cycle v1, prompt
4, with "Leave as is".

<!-- Resolved, review cycle v1, prompt 4. Answer: "Leave as is".

:::{attention} Composition table cannot be produced
:name: gap-composition

No `build-composition.csv` was found for `OP-20261001`, and the Log folder
holds no build spreadsheet to generate one from. Run
`devstudio-build-to-composition` on the build file for this experiment, then
insert the table here. Do not reconstruct it from the platemap. The platemap
names the conditions and does not give volumes or concentrations.
:::
-->

The platemap below is reproduced from the source, and is not a composition
table. It assigns a condition to each well and nothing more.

:::{table} Plate reader platemap, wells D3 to D9
:label: tbl-platemap

| Date | Experiment Name | Well | Name | Type |
| --- | --- | --- | --- | --- |
| 2/10/2026 | LUV-Gel | D3 | LUV+buffer | Sample |
| 2/10/2026 | LUV-Gel | D4 | LUV+PEG_gel | Sample |
| 2/10/2026 | LUV-Gel | D5 | LUV+PEG_pregel | Sample |
| 2/10/2026 | LUV-Gel | D6 | LUV+ULGA | Sample |
| 2/10/2026 | LUV-Gel | D7 | LUV+LGA | Sample |
| 2/10/2026 | LUV-Gel | D8 | LUV+Cytosol-PLA | Control |
| 2/10/2026 | LUV-Gel | D9 | LUV+buffer-PLA | Control |
:::

Wells D8 and D9 carry the two controls. They were read only on day 2 after
PLA addition. The day 1 and day 2 overnight reads cover D3 to D7 only, as
recorded in the `PLA-CPR/CPRG` sheet. The reviewer confirmed this read
pattern in review cycle v1, prompt 9. The two controls have no baseline read
of their own.

# Results

1. LUVs show PLA expression in hydrogels.
2. The best expression is in ULGA.
3. LUVs are leaky overnight, which is bad.

<!-- Results supplied by the reviewer in review cycle v1, prompt 7, and
carried verbatim as the three numbered statements they wrote. The source log
states no result.

:::{attention} Results narrative not recorded
:name: gap-results-prose

The source log states no result. Its Results section holds the figure below
and nothing else. Supply what the ratio shows, and say which conditions are
being compared against which control.
:::
-->

:::{figure} #op-20261001-fig1
:label: fig-op-20261001-cpr-cprg-ratio
:align: center
:width: 75%
CPR (570) to CPRG (412) absorbance ratio by sample, one panel per plate
reader read: `luvgel01_data.txt`, `luvgel02_data.txt` and
`luvgel02PLA_data.txt`. Sample names are as given in {numref}`tbl-platemap`.
:::

[`fig-op-20261001-cpr-cprg-ratio`, notebook:`OP-20261001/Copy of Copy of platereader.ipynb`, platemap:`LUV-gelplatemap-platereader - platemap-platereader - LUV-gelplatemap-platereader - platemap-platereader.csv`, data source:`20260930-164151-synergy2-luv-gel-OJ.txt`, caption: (CPR 570 to CPRG 412 absorbance ratio by sample.)]

The absorbance values the ratio is calculated from are recorded in the
`PLA-CPR/CPRG` sheet:

:::{table} CPRG (412 nm) and CPR (570 nm) absorbance, as recorded in the `PLA-CPR/CPRG` sheet
:label: tbl-absorbance

| Read | Wavelength | D3 | D4 | D5 | D6 | D7 | D8 | D9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| day 1 | 412 | 0.154 | 0.186 | 0.19 | 0.941 | 0.157 | not read | not read |
| day 1 | 570 | 0.102 | 0.089 | 0.088 | 0.823 | 0.107 | not read | not read |
| day 2 overnight incubation | 412 | 0.292 | 0.31 | 0.293 | 1.031 | 0.272 | not read | not read |
| day 2 overnight incubation | 570 | 0.254 | 0.256 | 0.246 | 0.929 | 0.246 | not read | not read |
| day 2 after PLA addition | 412 | 0.372 | 0.285 | 0.476 | 0.4 | 0.248 | 0.356 | 0.305 |
| day 2 after PLA addition | 570 | 0.266 | 0.249 | 0.4 | 0.365 | 0.257 | 0.267 | 0.238 |
:::

<!-- tbl-absorbance is transposed from the PLA-CPR/CPRG sheet, which lays the
wells out across columns and the three reads down the rows. No value is
changed. The sheet gives no unit for either wavelength row. The notebook
reads the values as absorbance. -->

<!-- Resolved, review cycle v1, prompt 10. Answer: "we are just using the
labeled figure". The two unlabeled figures stay out.

:::{attention} Two further figures exist and were not carried forward
:name: gap-figures-not-selected

The notebook draws two figures besides the one above, and the reviewer
selected neither on 2026-10-05. Cell 18 draws raw CPRG (412) and CPR (570)
absorbance by sample, one panel per data file. Cell 21 draws the absorbance
change from `luvgel02_data.txt` to `luvgel02PLA_data.txt`, which is day 2
after PLA addition minus day 2 before PLA addition. Neither cell carries a
`#| label:` tag. Add one to either cell to carry it into a later revision.
:::
-->

# Notes

:::{admonition}
Please add any further notes that the reader needs to know
:::
[PLEASE FILL IN]

# What's next
:::{admonition}
Please add in any additional comments about what can be done next
:::
[PLEASE FILL IN]

# Resources

- `experiments/20261001-luv-gel-pla/platereader.ipynb`, the analysis
  notebook. Its source in Drive is named `Copy of Copy of platereader.ipynb`.
- `experiments/20261001-luv-gel-pla/LUV-gelplatemap-platereader - platemap-platereader - LUV-gelplatemap-platereader - platemap-platereader.csv`
  holds the platemap the notebook loads.
- `experiments/20261001-luv-gel-pla/20260930-164151-synergy2-luv-gel-OJ.txt`
  holds the day 1 read.
- `experiments/20261001-luv-gel-pla/20260930-164151-synergy2-luv-gel-OJ-Day2.txt`
  holds the day 2 read after overnight incubation.
- `experiments/20261001-luv-gel-pla/20260930-164151-synergy2-luv-gel-OJ-Day2-afterPLA.txt`
  holds the day 2 read after PLA addition.
- `experiments/20261001-luv-gel-pla/PLA-CPR-CPRG.csv` holds the recorded
  absorbance values, reproduced in {numref}`tbl-absorbance`.

The three data files are served from
`https://data.nucleus.engineering/platereader/devstudio/`. The notebook
downloads them from there, and downloads the platemap from Drive.

Review cycle v1 is the Doc "Review: LUV gel and PLA, CPR/CPRG absorbance
(op-20261001) v1", in the Drive folder
`02-devnotes/devnote-op-20261001-luv-gel-pla`. It carries twelve open
prompts. Each one names the admonition it belongs to.

The source log names its analysis as
`https://colab.research.google.com/drive/1ebR3gcpx0j-HCuA4N5lDdILkSQ6BneoJ#scrollTo=5a08dde5`.
It is recorded here as text rather than as a link, because a reader without
Drive access cannot open it.
