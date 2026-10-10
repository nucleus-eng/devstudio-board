<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

# Supplement: source record and open gaps

This page is the full technical record `main.md` was drafted from. It
carries the asset chain for `OP-20261001`, every disagreement found
between sources, and the full history of review cycle v1. `main.md`
carries the document-facing draft, close to `log-devnote-draft.docx`. Both
pages build as one project. An ordinary `{ref}` or `{numref}` resolves a
label defined on the other page.

## Overview

We are trying to embed vesicle systems in hydrogels to study their yield,
stability, and structural integrity in different polymer environments.

<!-- Overview supplied by the reviewer in review cycle v1, prompt 5, and
carried verbatim. The source log carries no overview. Its entire body is the
heading "# Results", one pasted figure, and the line
"Analysis: https://colab.research.google.com/drive/1ebR3gcpx0j-HCuA4N5lDdILkSQ6BneoJ#scrollTo=5a08dde5". -->

The intro schematic from `log-devnote-draft.docx`, "Figure 1: Hydrogel
containing unilamellar vesicles", is in `main.md`'s own Overview rather
than copied here. A figure's `:label:` must be unique across this whole
project, not only within one page. A second copy here would collide with
that one rather than merely restate it. Measured directly on 2026-10-09:
`curvenote check` reports a duplicate identifier when the same `:label:`
is used on two pages of one project.

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

**A second source document names a second author and a different title.**
`log-devnote-draft.docx` was uploaded to the review folder on 2026-10-08.
It names Ojaswita Pant at Northwestern University and Manuel Bibrowski at
Imperial College London as its two authors. Manuel Bibrowski was not in
`curvenote.yml`. He is now added, with the affiliation the document itself
states. The document's own title is "Study of liposome behaviour in gels",
which disagrees with the title review cycle v1 already answered. The
answered title stays. Confirm which title is correct.

**The document names a build file that does not match this DevNote's
platemap.** It links a sheet named `build`, at
`1BI0gXBY33WXuJZO19aqzrlLL2ofd9EROV2j-iSKzwsE`. That sheet lays out wells
I4 to M13. Its rows cover five sample types: `GFP-GUVs+LUVs`,
`PLA-GUVs+LUVs`, `GFP GUVs`, `LUV only`, and a control row. Its columns
cover five gel conditions: PEG gel, pre-PEG, ULGA, LGA, and outer solution
only. Each condition sits in duplicate columns.

This DevNote's platemap, in {numref}`tbl-platemap`, covers wells D3 to D9
only, names no GUV condition, and carries no duplicate columns. Confirm
whether this `build` sheet describes the same run as this DevNote's data,
before using it as a composition table. See {ref}`gap-build-plate-mismatch`.
:::

## Reagents

:::{table} Reagents and equipment
:label: tbl-reagents

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| PEG4Nb | 4-Arm-PEG-Norbornene | Creative Pegworks | N/A | N/A | freezer at -20°C in the dark | |
| PEG-4SH crosslinker | 4-Arm PEG-Thiol | Creative Pegworks | N/A | N/A | freezer at -20°C in the dark | |
| LAP photoinitiator | Lithium phenyl-2,4,6-trimethylbenzoylphosphinate | Sigma-Aldrich | N/A | N/A | 2-8°C, in the dark, photosensitive | |
| Glucose and 50 mM HEPES buffer | N/A | N/A | N/A | N/A | 4°C | |
| DLP projector | N/A | Zwants Supplies Engineering | PRO4500-92-405 | N/A | N/A | |
| [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
:::

The five rows above come from `log-devnote-draft.docx`. That document also gives a concentration and a molecular weight for the
first three. PEG4Nb is 80 mM and 5000 Da. PEG-4SH is 20 mM and 2000 Da.
LAP is 16.9 mM and 294.21 g/mol. Neither column fits this table's schema, so both values are kept
here rather than dropped. These three concentrations agree with
{numref}`tbl-stock-peg4nb`.

:::{attention} Reagents still incomplete
:name: gap-reagents

The source log has no reagents section and the folder holds no materials
file. The sample names in {numref}`tbl-platemap` identify seven conditions by
abbreviation: `LUV`, `PEG_gel`, `PEG_pregel`, `ULGA`, `LGA`, `Cytosol-PLA`
and `buffer-PLA`. Expand each abbreviation and supply the vendor, catalog
number, price and storage conditions for every reagent used.

**Deferred, review cycle v1, prompt 8.** The reviewer answered "skip for
now".

**Answered in part, from `log-devnote-draft.docx`.** The document supplies
vendor and storage information for the five reagents used to make the
PEG4Nb gel, and for the one piece of equipment. It also supplies a catalog
number for the equipment. It names no vendor, catalog number, price or storage
condition for the lipid, the dye, the Optiprep, the ULGA, or the LGA. The ULGA and LGA chemicals are
named in {numref}`tbl-stock-ulga` and {numref}`tbl-stock-lga`, and carry no
vendor information there either.
:::

## Protocol

## Vesicles

The following is reproduced from `log-devnote-draft.docx`.

### LUVs

**Hydration**

1. Hydrate a dry POPC lipid film (~2 mg) in buffer containing glucose, 50 mM
   HEPES and 15 v/v% Optiprep, at a final osmolarity of 1200 mOsm. The
   buffer contains 15 mg/mL CPRG.
2. Vortex, then sonicate for 15 min.
3. Apply 5 freeze-thaw cycles, liquid nitrogen, then thaw in a
   room-temperature water bath.

**Clean-up by centrifugation**

1. Split the mixture into 5 tubes, each with 200 µL vesicles and 1 mL outer
   solution, glucose and 50 mM HEPES, 1200 mOsm.
2. Spin at 15,000 g for 15 min.
3. Resuspend the pellet in outer solution and wash again by pelleting at the
   same settings.
4. Repeat until the outer solution of the pellet looks clear, 2 to 4 washes.

### GUVs

**Lipid-in-oil mixture**

1. Resuspend a dried POPC film (~2 mg) in 500 µL mineral oil.
2. Sonicate for ~30 min.

**Inner solution**

Nucleus cytosol with 5 v/v% Optiprep and DNA at either T7-mNG or T7-PLA1.

**Outer solution**

Glucose and 50 mM HEPES, 1200 mOsm.

**Emulsion and transfer**

1. Pipette 20 µL cytosol reaction into 200 µL lipid-in-oil mixture.
2. Pipette up and down 9 times to form a water-in-oil emulsion.
3. Layer the emulsion onto ~250 µL outer solution, glucose and 50 mM HEPES,
   1200 mOsm.
4. Centrifuge for 20 min at 9,000 g.
5. Gently remove the oil and most of the outer solution.
6. Resuspend the GUV pellet in outer solution or in a solution of
   dye-loaded LUVs.

:::{attention} Substrate confirmed
:name: gap-substrate-confirmed

The LUV hydration buffer carries 15 mg/mL CPRG, the substrate the plate
reader reads at 412 nm and 570 nm in {numref}`tbl-absorbance`. The source
log and the notebook name the readout and never name the substrate. This
step is the only place in any source that states it.
:::

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

`log-devnote-draft.docx` names the same three concentrations and gives the
buffer as glucose and 50 mM HEPES rather than PBS or Tris:HEPES. The two
sources agree on PEG4Nb, PEG4SH and LAP, and disagree on the buffer.

Mix 15 µL vesicle solution with 15 µL PEG4Nb gel stock, then plate 30 µL per
well. This halves the stock concentration to a final 40 mM PEG4Nb.

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

From `log-devnote-draft.docx`:

1. Prepare ULGA at 1 w/v% in 1.2 M glucose solution.
2. Microwave in 10 s bursts, 5 to 7 times, until fully dissolved.
3. Keep on the 55 °C bead bath until use.

Mix 15 µL vesicle solution with 15 µL ULGA gel stock, then plate 30 µL per
well. This halves the stock concentration to a final 0.5 w/v% ULGA.

:::{attention} Solvent and osmolarity disagree between two sources
:name: gap-ulga-solvent

{numref}`tbl-stock-ulga` gives the outer solution as 1057 Osm glucose.
`log-devnote-draft.docx` gives the ULGA solvent as 1.2 M glucose, and states
elsewhere that the buffer osmolarity for the whole experiment is 1200 mOsm.
Neither value is changed here. Confirm which value, or whether both apply
at different steps, before this goes further.
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

From `log-devnote-draft.docx`:

1. Prepare LGA at 2.8 w/v% in 1.2 M glucose solution.
2. Heat in the 95 °C heat block until fully dissolved, vortexing
   occasionally.
3. Keep an aliquot in an Eppendorf tube at 45 °C.
4. Prepare vesicles in the sonicator bath and do the transfer there.

The document gives a final concentration of 0.7 w/v% LGA, from 7.5 µL
stock plus 7.5 µL outer solution. This agrees with the sheet's own note.

:::{attention} Stock concentration and solvent disagree between two sources
:name: gap-lga-solvent

{numref}`tbl-stock-lga` gives the stock as 2.70% in UPDI water.
`log-devnote-draft.docx` gives 2.8 w/v% in 1.2 M glucose solution. The two
concentrations round to the same figure, but the solvent disagrees, UPDI
water against glucose solution. Neither value is changed here. Confirm
which solvent was used.
:::

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

**Answered in full, `log-devnote-draft.docx`.** The vesicle preparation for
LUVs and GUVs is now in `## Vesicles`. The gel preparation steps and the
stock-to-final-concentration figures are now in each tab of `## Gels`,
alongside the stock tables already there. Two gels carry a flagged
disagreement between the document and the `Gel formulations` sheet, in
{ref}`gap-ulga-solvent` and {ref}`gap-lga-solvent`.

One thing the document does not supply. It describes gel preparation and
vesicle embedding, not the PLA addition step itself or the plate reader
settings. Both are still missing.
:::

## Methods

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

:::{attention} A build file exists, for a plate that does not match this DevNote
:name: gap-build-plate-mismatch

`log-devnote-draft.docx` links a sheet named `build`, at
`1BI0gXBY33WXuJZO19aqzrlLL2ofd9EROV2j-iSKzwsE`. It lays out wells I4 to M13.
Its five sample rows are `GFP-GUVs+LUVs`, `PLA-GUVs+LUVs`, `GFP GUVs`,
`LUV only` and a control row. Its five gel conditions are PEG gel, pre-PEG
gel, ULGA, LGA and outer solution only. Each condition sits in two
adjacent columns.

{numref}`tbl-platemap` covers wells D3 to D9 only, names no GUV condition,
and carries no duplicate columns. The two plates do not match on well
range, on row letter, or on condition set. Do not treat the `build` sheet as this DevNote's composition table. First
confirm it describes the same plate read on `OP-20261001`.
:::

The wider experimental design that `log-devnote-draft.docx` describes, which
the `build` sheet above belongs to, is reproduced here for reference.
Whether it describes a larger run than the one this DevNote's platemap and
data cover is not yet confirmed.

Conditions tested: GFP GUVs and LUVs, across four gel conditions, pre-PEG4Nb
gel solution, PEG4Nb gel, ULGA gel and LGA gel. One gel-only control per gel
condition, plus vesicles in outer solution as the reference control.

:::{table} Experimental design, from `log-devnote-draft.docx`
:label: tbl-experimental-design-doc

| | Outer solution | PEG4Nb pre-gel | PEG4Nb gel | ULGA | LGA |
| --- | --- | --- | --- | --- | --- |
| GFP-GUVs | | | | | |
| GFP-GUVs + LUVs | | | | | |
| PLA-GUVs + LUVs | | | | | |
| LUVs only | | | | | |
| Control | Outer solution only | Pre-gel only | Gel only | Gel only | Gel only |
:::

Vesicles in outer solution only, with no gel, serve as the reference
control. Each sample is 15 µL vesicle solution mixed with 15 µL gel stock,
plated at 30 µL per well, in duplicate.

Open questions, as the document states them: are LUVs leaky, can PLA lyse,
and do only the gels lyse.

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

## Results

1. LUVs show PLA expression in hydrogels.
2. The best expression is in ULGA.
3. LUVs are leaky overnight, which is bad.

:::{attention} A second source gives a Discussion, not yet reconciled
:name: gap-discussion-reconcile

`log-devnote-draft.docx` carries its own Discussion, two statements: "GFP
expression in all 3 gels" and "PLA lyses the vesicles in all gels". Neither
is changed here, and neither replaces the three numbered statements above,
which are the reviewer's own answer to review cycle v1, prompt 7. The
document's "GFP expression" does not obviously match this DevNote's figure,
which reads a CPR/CPRG colorimetric ratio rather than a fluorescence signal.
Confirm whether the two describe the same result, or two different results
from the same experiment.
:::

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

## A second graph, from a run not yet identified

`log-devnote-draft.docx` carries a graph under its own Results heading,
captioned "LUVs are most stable in PEG gels". The graph itself is titled
"LUV behaviour in hydrogels Read 2 (3:09 PM, 16 U/mL LacZ)". It is in
`main.md`'s own Results, not copied here. One `:label:` cannot serve two
pages of the same project, the same reason given under Overview above.

:::{attention} This graph's run is not confirmed, and it carries a new number
:name: gap-luv-only-read2

`log-devnote-draft.docx` names no notebook, no platemap and no data file for
this graph. Two placeholders sit near it in the source, `[Paste the graph
here]` and `[link to dataset URL here; .txt of matlab code in directory;
caption]`, both still unfilled. Neither this DevNote's data nor its
platemap names a LacZ concentration anywhere. This graph states one: 16
U/mL.

Its condition set is pre-PEG solution, PEG gel, ULGA, LGA, and in
solution. {numref}`tbl-platemap` is close but not the same. It also
carries `Cytosol-PLA` and `buffer-PLA`, and it carries no `in solution`
row. The two sets are possibly the same arm of work, read at two different
stages on two different dates. Confirm which run this graph comes from before
treating it as part of the data already in this DevNote's
{numref}`tbl-absorbance` and {numref}`fig-op-20261001-cpr-cprg-ratio`.
:::

## Notes

:::{admonition}
Please add any further notes that the reader needs to know
:::
[PLEASE FILL IN]

## What's next
:::{admonition}
Please add in any additional comments about what can be done next
:::
[PLEASE FILL IN]

## Resources

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

`log-devnote-draft.docx`, in the review folder, supplied three things. The
vesicle and gel preparation protocol is folded into `# Protocol` above. The
reagents are folded into {numref}`tbl-reagents`. A build sheet, at
`1BI0gXBY33WXuJZO19aqzrlLL2ofd9EROV2j-iSKzwsE`, is flagged in
{ref}`gap-build-plate-mismatch` as describing a plate that does not match
this DevNote's own data. Drive URLs are not written as links here, per the
rule above.

Review cycle v1 is the Doc "Review: LUV gel and PLA, CPR/CPRG absorbance
(op-20261001) v1", in the Drive folder
`02-devnotes/devnote-op-20261001-luv-gel-pla`. It carries twelve open
prompts. Each one names the admonition it belongs to.

The source log names its analysis as
`https://colab.research.google.com/drive/1ebR3gcpx0j-HCuA4N5lDdILkSQ6BneoJ#scrollTo=5a08dde5`.
It is recorded here as text rather than as a link, because a reader without
Drive access cannot open it.
