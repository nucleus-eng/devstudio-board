<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

# Overview

[PLEASE FILL IN]

<!-- No source log carries an overview or introduction section. The four logs
open directly on Notes, on "Day #1", or on their own first sentence.
Candidate framing, from the platemap
Experiment column, not adopted: "EsaO-mNG / [EsaO]2-mNG EsaR titration +/- AHSL"
and "EsaO-mNG / [EsaO]2-mNG DNA template titration +/- AHSL (EsaR fixed at
highest prior dose)". -->

:::{danger} Unresolved before publication
:name: flags-blocking

**Title and authors.** No source log carries a Specification table or an
Authors table. `curvenote.yml` holds `[PLEASE FILL IN]` for both, with
candidate text in comments. Three Log folders are prefixed `CN`. The fourth
is prefixed `MB`, and its notebook names `JM-MB`.

**Two figures have no surviving producing cell.** {numref}`fig-20260924-esao`
and {numref}`fig-20260924-esao2` were pasted into the 2026-09-24 log. The
`platereader.ipynb` in `CN-20260924_repressor_test` loads the right data file
and the right platemap. Its cell 15 plots the same 0, 1, 4 and 7 µL EsaR
series. No cell in it produces the two-panel `EsaR/EsaO` figure that the log
shows. The notebook was saved on 2026-09-26, after the figures were pasted.
Restore those cells before publication.

**No DNA sequences.** {numref}`tbl-constructs` names seven linear templates
and carries no sequence for any of them. A DevNote must be self-contained, so
every sequence has to be added inline. No `.gb` file for any of the seven was
located, so `devstudio-verify-dna-constructs` was not run and no
construct-to-file identity claim is made here.

**Agarose gel image missing.** The 2026-09-24 log states that the constructs
were run on an agarose gel and instructs "Ask Manuel for image". No gel image
exists in any of the four Log folders.

**No build file for 2026-10-01.** The file named `build` in that folder is a
platemap. It holds `Well`, `Date`, `Experiment`, `Name` and `Type` and nothing
else, so it carries no component, no concentration and no volume. No
composition table can be produced for that day and no sidecar exists.
{numref}`tbl-volumes-20261001` carries the log's own volume table instead, and
that table has no stock or final concentrations in it. Supply a build file in
the canonical format.
:::

:::{admonition} Open review items
:class: warning dropdown
:name: flags-review

**Date labels on two platemaps.** `CN-20260925-DNA_titration` holds
`20260924-dna-titration-esar-fixed.csv` and
`CN-20260926-DNA_titration_spent_EsaR` holds `20260924-esao2-dna-titration.csv`.
Both carry 20260924 inside a later folder. Each is the file that folder's own
notebook loads, so both read as naming slips rather than wrong data. The folder
date and the filename date still disagree, and that is a human call. The `Date`
column inside all three CN platemaps also reads `2026-09-24`.

**Template residue in every `test-data/` subfolder.** All four folders hold an
identical `20251111-122213-cytation5-pure-timecourse-gfp-MFG-98-tRNA-QC.txt`
plus `platemap-microscopy.csv` and `platemap-platereader.csv`. These look like
unedited copies from `00-template-LOG`, not run data. Nothing here links them.

**EsaR volume labels in {numref}`tbl-composition-20260924`.** The condition
names read 0, 1, 4 and 7 µL EsaR. The `Pre-expressed EsaR` row reads 0, 2, 8
and 14 µL. The reactions are 65 µL against a 32.5 µL standard reaction, so the
row is the per-65-µL volume and the name is the per-32.5-µL volume. Both are
carried as the build file writes them.

**DNA stock disagreements.** The 2026-09-24 build sheet states one 200 ng/µL
stock, yet EsaO takes 2.87 µL and \[EsaO\]2 takes 3.25 µL. The 2026-09-25 sheet
states 200 ng/µL in its standard-reaction block and 10 and 150 ng/µL in its own
comment. The comment values are the ones carried in
{numref}`tbl-composition-20260925`. The 2026-09-26 conditions all take 0.46 µL
because their stocks differ at 10, 50 and 100 ng/µL.

**Pre-expressed EsaR has no concentration.** No build sheet records a stock or
final concentration for it. All four concentration cells are `—`. The 2026-09-24
log states a final EsaR concentration of 576 nM from back-of-the-napkin maths,
which is narrative, not a build-file value.

**Stale sheets in the 2026-09-24 build file.** `build` in
`CN-20260924_repressor_test` also contains sheets named `20260926_DNA_titration`
and `Sheet6` whose contents duplicate the 2026-09-25 titration. Only
`20260924_Repression_test_rxns` was used here.

**AHL and AHSL.** The 2026-09-24 and 2026-09-25 logs write "AHL". Every
platemap writes "AHSL". The 2026-09-26 log writes "AHL" in its reaction
preparation and "AHSL" in its result. All are carried as written. Agree one
spelling.

**No reagents data.** No source log or build sheet carries a vendor,
catalog number, price or storage condition. `devstudio-build-to-materials` was
not run against the Materials Reference, so {numref}`tbl-reagents` carries
component names only.

**Two figures are still static PNGs.** The four 2026-09-25 and 2026-09-26
figures now carry `#| label:` tags and resolve against their notebook cells.
The two 2026-09-24 figures stay `static-png`, because their producing cell does
not exist to label. That is the blocking item above.

**One label carries the wrong year.** Cell 15 of the 2026-09-26 notebook is
tagged `cn-20250926-fig1`, which reads 2025. A `cell_label` is carried verbatim
and is never reformatted, so `main.md` and `manifest.json` both use the string
as written. Retag the cell and this DevNote follows.

**The 2026-10-01 platemap date disagrees with everything around it.** The
folder is `2026/10/01 - MB - MgSweepof preeincubation` and the data file is
`20261001-181311-...`. Every row of the platemap reads `2026-10-02`. Confirm
which date is the run date.

**An unused platemap copy sits in the 2026-10-01 folder.**
`build-platemap-csv.csv` holds the same sixteen wells as the `build` Sheet. Its
`Type` column is empty where the Sheet reads `Sample`. The notebook loads the
Sheet. Delete the copy, or say which one is authoritative.

**Authorship of the 2026-10-01 experiment.** The folder and the notebook name
MB and JM. The cell label reads `mbcn-20261001-fig1`. Name every author of that
day's work, and say where they sit in the author list.

**Uncertainty markers.** Every result paragraph in all three CN logs is prefixed
`*Prior to analysis` or `*Prior to data analysis`. Those statements are the
author's pre-analysis impressions, carried verbatim, and must be resolved or
confirmed before this reaches DevNote(M).
:::

# Reagents

:::{table} Reagents and equipment. Component names come from the three CN build sheets, from the 2026-10-01 log's own volume table, and from the 2026-09-23 construct preparation. No source carries vendor, catalog, price or storage data.
:label: tbl-reagents
:align: center

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| tRNA | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| Protein mix | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| Ribosomes | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| RNase inhibitor | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| Nuclease free water | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| AHSL | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| Fluorescein | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| Q5 polymerase | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| HF buffer | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| M15 Fwd primer | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| M15 Rev primer | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| Magnesium | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
| E.coli pol | [PLEASE FILL IN] | [PLEASE FILL IN] | N/A | N/A | N/A | |
:::

# Constructs

:::{table} Linear DNA templates prepared on 2026-09-23. No sequence and no sequence file was found for any of the seven.
:label: tbl-constructs
:align: center

| Name | Sequence | Purpose |
| --- | --- | --- |
| T7-mNG-t7term | [PLEASE FILL IN] | [PLEASE FILL IN] |
| T7-\[EsaO\]-mNG-T7term | [PLEASE FILL IN] | [PLEASE FILL IN] |
| T7-\[EsaO\]2-mNG-t7term | [PLEASE FILL IN] | [PLEASE FILL IN] |
| T7-PLA1-t7term | [PLEASE FILL IN] | [PLEASE FILL IN] |
| T7-\[EsaO\]-PLA1-T7term | [PLEASE FILL IN] | [PLEASE FILL IN] |
| T7-\[EsaO\]2-PLA1-t7term | [PLEASE FILL IN] | [PLEASE FILL IN] |
| T7-EsaR(D91G)-T7term | [PLEASE FILL IN] | [PLEASE FILL IN] |
:::

<!-- Four of these seven templates (T7-mNG, T7-PLA1, T7-[EsaO]-PLA1,
T7-[EsaO]2-PLA1) were prepared on 2026-09-23 but do not appear in any
composition table in this DevNote. T7-mNG is used as the unrepressed control
in the three CN experiments. The three PLA1 templates are not used here. -->

# Protocol

<!-- STYLE: the source heading was the underlined run-in label "Day #1
(20260923)". It is promoted to a subsection heading here. -->

## Linear DNA template preparation (2026-09-23)

Linear DNA templates prepared for following constructs

1.  T7-mNG-t7term
2.  T7-\[EsaO\]-mNG-T7term
3.  T7-\[EsaO\]2-mNG-t7term
4.  T7-PLA1-t7term
5.  T7-\[EsaO\]-PLA1-T7term
6.  T7-\[EsaO\]2-PLA1-t7term
7.  T7-EsaR(D91G)-T7term

Gblocks were amplified using Q5 polymerase (2x HF buffer) and M15 Fwd and Rev
primers (Ta = 64˚C) @ 250 µL Vf

All constructs yielded approximately 200 ng/µL at 30 µL final volume.

Constructs ran on agarose gel (**Ask Manuel for image**)

# Methods

<!-- STYLE: the source heading was the underlined run-in label "Day #2
(20260924)". It is promoted to a subsection heading here. -->

## 2026-09-24 — EsaR titration at fixed sensor DNA

T7-EsaR(D91G)-T7term expressed for 3 hrs at 37 ˚C and placed at 4 ˚C.

Cytosol reactions were prepared according to "20260924_Repressor_test" sheet.
Briefly, a large mastermix of cytosol was prepared (- DNA, - water). Whilst
this was being prepared, varying amounts of pre-expressed T7-EsaR(D91G)-T7term
were added to 320.5 ng T7-\[EsaO\]-mNG-T7term or T7-\[EsaO\]2-mNG-t7term
constructs before being placed at 37˚C for 15 mins. An appropriate amount of
H20 was then added to each mixture before adding the cytosol mastermix to a
total volume of 65 µL. Reactions were split in half before adding AHL to one
set of reactions to a final concentration of 5 µM. Reactions were distributed
in triplicate into a 384 well plate before incubation at 37˚C in a platereader
set to detect GFP.

<!-- Composition table sourced from build file: build (Google Sheet), sheet
20260924_Repression_test_rxns, in CN-20260924_repressor_test. Mastermix
component volumes are the standard-reaction volumes at the distribution factor
the sheet states. That factor is "Distribute into 1x 23.72 µL (mNG), and 8x
47.44 µL (EsaO & [EsaO]2)". -->

::::{admonition} Reaction composition, 2026-09-24
:class: dropdown

:::{table} Reaction composition, 2026-09-24. Full sidecar: [`experiments/build-composition-20260924.csv`](./experiments/build-composition-20260924.csv).
:label: tbl-composition-20260924
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | mNG [µL] | EsaO-mNG (0 µL EsaR) [µL] | EsaO-mNG (1 µL EsaR) [µL] | EsaO-mNG (4 µL EsaR) [µL] | EsaO-mNG (7 µL EsaR) [µL] | \[EsaO\]2-mNG (0 µL EsaR) [µL] | \[EsaO\]2-mNG (1 µL EsaR) [µL] | \[EsaO\]2-mNG (4 µL EsaR) [µL] | \[EsaO\]2-mNG (7 µL EsaR) [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 9.85 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 |
| tRNA | 10 | × | 1 | × | 3.25 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 |
| Protein mix | 8.33 | × | 1 | × | 3.90 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 |
| Ribosomes | 5.5 | × | 1 | × | 5.91 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.81 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 |
| DNA Template | 200 | ng/µL | 10 | ng/µL | 1.54 | 2.87 | 2.87 | 2.87 | 2.87 | 3.25 | 3.25 | 3.25 | 3.25 |
| Pre-expressed EsaR | — | — | — | — | 0 | 0 | 2 | 8 | 14 | 0 | 2 | 8 | 14 |
| Nuclease free water | — | — | — | — | 7.23 | 14.69 | 12.69 | 6.69 | 0.69 | 14.31 | 12.31 | 6.31 | 0.31 |
| Total [µL] |   |   |   |   | 32.5 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 |
:::
::::

## 2026-09-25 — Sensor DNA titration at fixed EsaR

T7-EsaR(D91G)-T7term expressed for 3 hrs at 37 ˚C and placed at 4 ˚C

Cytosol reactions were prepared according to "20260925_DNA _titration" sheet.
Briefly, a large mastermix of cytosol was prepared (- DNA, - water). Whilst
this was being prepared, 14 uL of pre-expressed EsaR was mixed with varying
amounts of T7-\[EsaO\]-mNG-T7term or T7-\[EsaO\]2-mNG-t7term constructs before
being placed at 37˚C for 15 mins. An appropriate amount of H20 was then added
to each mixture before adding the cytosol mastermix to a total volume of 65 µL.
Reactions were split in half before adding AHL to one set of reactions to a
final concentration of 5 µM. Reactions were distributed in triplicate into a
384 well plate before incubation at 37˚C in a platereader set to detect GFP. .

<!-- Composition table sourced from build file: build (Google Sheet), sheet
20260925_DNA_titration, in CN-20260925-DNA_titration. -->

::::{admonition} Reaction composition, 2026-09-25
:class: dropdown

:::{table} Reaction composition, 2026-09-25. Full sidecar: [`experiments/build-composition-20260925.csv`](./experiments/build-composition-20260925.csv).
:label: tbl-composition-20260925
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | mNG [µL] | EsaO-mNG (0.1 nM) [µL] | EsaO-mNG (0.5 nM) [µL] | EsaO-mNG (1 nM) [µL] | EsaO-mNG (3 nM) [µL] | EsaO-mNG (6 nM) [µL] | EsaO-mNG (9 nM) [µL] | \[EsaO\]2-mNG (0.1 nM) [µL] | \[EsaO\]2-mNG (0.5 nM) [µL] | \[EsaO\]2-mNG (1 nM) [µL] | \[EsaO\]2-mNG (3 nM) [µL] | \[EsaO\]2-mNG (6 nM) [µL] | \[EsaO\]2-mNG (9 nM) [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 9.85 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 |
| tRNA | 10 | × | 1 | × | 3.25 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 |
| Protein mix | 8.33 | × | 1 | × | 3.90 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 |
| Ribosomes | 5.5 | × | 1 | × | 5.91 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.81 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 |
| DNA Template | 10 / 10 / 150 / 150 / 150 / 150 | ng/µL | 0.1 / 0.5 / 1 / 3 / 6 / 9 | nM | 1.54 | 0.44 | 2.12 | 0.28 | 0.85 | 1.69 | 2.46 | 0.43 | 2.16 | 0.29 | 0.86 | 1.73 | 2.59 |
| Pre-expressed EsaR | — | — | — | — | 0 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 |
| Nuclease free water | — | — | — | — | 7.23 | 3.12 | 1.44 | 3.27 | 2.71 | 1.86 | 1.09 | 3.13 | 1.40 | 3.27 | 2.69 | 1.83 | 0.97 |
| Total [µL] |   |   |   |   | 32.5 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 |
:::
::::

## 2026-09-26 — Sensor DNA titration with overnight EsaR

T7-EsaR(D91G)-T7term expressed for 17 hrs at 30 ˚C and placed at 4 ˚C

Cytosol reactions were prepared according to "20260926_DNA
_titration_EsaR_spent" sheet. Briefly, a large mastermix of cytosol was
prepared (- DNA, - water). Whilst this was being prepared, 14 uL of
pre-expressed EsaR was mixed with varying amounts of T7-\[EsaO\]2-mNG-t7term
constructs before being placed at 37˚C for 15 mins. An appropriate amount of
H20 was then added to each mixture before adding the cytosol mastermix to a
total volume of 70 µL. Reactions were split in half before adding 0.35 µL AHL
(stock: 0.5 mM) to one set of reactions (final concentration: 5 µM). Reactions
were distributed in triplicate into a 384 well plate before incubation at 37˚C
in a platereader set to detect GFP.

<!-- Composition table sourced from build file: build (Google Sheet), sheet
20260926-DNA_titration_EsaR_spent, in CN-20260926-DNA_titration_spent_EsaR.
The sheet's own comment reads: "Reaction volume increased to 35, but 14 µL EsaR
volume maintained. Lowered the relative amount of EsaR in each reaction by 1.5%
compared to previous experiment". -->

::::{admonition} Reaction composition, 2026-09-26
:class: dropdown

:::{table} Reaction composition, 2026-09-26. Full sidecar: [`experiments/build-composition-20260926.csv`](./experiments/build-composition-20260926.csv).
:label: tbl-composition-20260926
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | mNG [µL] | \[EsaO\]2-mNG (0.1 nM) [µL] | \[EsaO\]2-mNG (0.5 nM) [µL] | \[EsaO\]2-mNG (1 nM) [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 10.61 | 21.22 | 21.22 | 21.22 |
| tRNA | 10 | × | 1 | × | 3.50 | 7.00 | 7.00 | 7.00 |
| Protein mix | 8.33 | × | 1 | × | 4.20 | 8.40 | 8.40 | 8.40 |
| Ribosomes | 5.5 | × | 1 | × | 6.36 | 12.72 | 12.72 | 12.72 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.88 | 1.76 | 1.76 | 1.76 |
| DNA Template | 10 / 50 / 100 | ng/µL | 0.1 / 0.5 / 1 | nM | 1.66 | 0.46 | 0.46 | 0.46 |
| Pre-expressed EsaR | — | — | — | — | 0 | 14 | 14 | 14 |
| Nuclease free water | — | — | — | — | 7.79 | 4.44 | 4.44 | 4.44 |
| Total [µL] |   |   |   |   | 35 | 70 | 70 | 70 |
:::
::::

## 2026-10-01 — Magnesium sweep with EsaR and DNA pre-incubation

Optimising EsaR repression by preeincubating EsaR with the DNA with a higher Mg
concentration

Preexpressing EsaR for 3-4h

And then add the DNA with the PURE reaction for 1h at 37 to ensure full
repression

::::{admonition} Reaction volumes, 2026-10-01
:class: dropdown

:::{table} Reaction volumes as the 2026-10-01 log writes them. This is not a composition table. It carries no stock or final concentrations, and no build file exists to source one from. The first column sums to the stated 10 µL and the second to the stated 33 µL, a 3.3-fold scale.
:label: tbl-volumes-20261001
:align: center

| Component | Volume (µL) | Scaled (µL) |
| --- | --- | --- |
| S-mix | 3 | 9.9 |
| Ribosomes | 1.8 | 5.94 |
| P-mix | 1.2 | 3.96 |
| T rna | 1 | 3.3 |
| E.coli pol | 0 | 0 |
| DNA | 0.15 | 0.495 |
| Rnase inhibitor | 0.25 | 0.825 |
| EsaR | 2.3 | 7.59 |
| AHL optional | 0.15 | 0.495 |
| Mg | 0.15 | 0.495 |
| Total | 10 | 33 |
:::
::::

The log continues:

Mix of DNA and EsaR pure reaction:
Final is 0.332
DNA stock at 22ng/µL
2.6 overall\* 3.5
Mg concentrations: 5, 10, 20 locally:
Stocks of Mg:
X20 = 346.7mM
X10 = 173.3mM
X5 = 86.6mM

# Results

## 2026-09-24 — EsaR titration at fixed sensor DNA

Results: \*Prior to analysis, it appeared that there was not any repression in
any constructs. We believe that the ratio of Sensor template:EsaR was too high.
There was not enough EsaR to fully repress the system. Back of the napkin maths
assuming a final concentration of EsaR in each reaction of 576 nM, and a sensor
DNA template final concentration of 15.35 nM, suggests a ratio of 37.5:1
EsaR:DNA. We think this should be higher aiming for at least 100:1. For
reference, b.next use a ratio of 1000:1 purified TetR:TetO DNA for their sensing
constructs. A DNA titration from 0.1 nM - 9 nM sensor DNA whilst maintaining the
highest amount of pre-expressed EsaR in each reaction will be performed on
20260925.

:::{figure} ./figures/20260924-esao-mng-esar-titration.png
:label: fig-20260924-esao
:align: center
:width: 75%
Single-operator EsaO-mNG with 0, 1, 4 and 7 µL pre-expressed EsaR, minus and plus AHSL. Reaction composition is in {numref}`tbl-composition-20260924`.
:::

[`fig-20260924-esao`, notebook:`CN-20260924_repressor_test/platereader.ipynb`, platemap:`build - 20260924_Platemap.csv`, data source:`20260924-151252-cytation5-pure-timecourse-gfp-repressor_test.txt`, caption: (Single-operator EsaO-mNG with 0, 1, 4 and 7 µL pre-expressed EsaR, minus and plus AHSL.)]

:::{figure} ./figures/20260924-esao2-mng-esar-titration.png
:label: fig-20260924-esao2
:align: center
:width: 75%
Dual-operator \[EsaO\]2-mNG with 0, 1, 4 and 7 µL pre-expressed EsaR, minus and plus AHSL. Reaction composition is in {numref}`tbl-composition-20260924`.
:::

[`fig-20260924-esao2`, notebook:`CN-20260924_repressor_test/platereader.ipynb`, platemap:`build - 20260924_Platemap.csv`, data source:`20260924-151252-cytation5-pure-timecourse-gfp-repressor_test.txt`, caption: (Dual-operator [EsaO]2-mNG with 0, 1, 4 and 7 µL pre-expressed EsaR, minus and plus AHSL.)]

## 2026-09-25 — Sensor DNA titration at fixed EsaR

\*Prior to data analysis: Appears that we have repression, and it is dependent
on \[EsaR\]:\[Sensor DNA\]. The \[EsaO\]2 constructs appear to repress more
strongly than the \[EsaO\]1 constructs.

:::{figure} #cn-20260925-fig1
:label: fig-20260925-0p1nm
:align: center
:width: 75%
0.1 nM sensor DNA at approximately 576 nM EsaR and 5 µM AHSL, single operator against dual operator. Reaction composition is in {numref}`tbl-composition-20260925`.
:::

[`fig-20260925-0p1nm`, notebook:`CN-20260925-DNA_titration/platereader.ipynb`, platemap:`20260924-dna-titration-esar-fixed.csv`, data source:`20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`, caption: (0.1 nM sensor DNA at approximately 576 nM EsaR and 5 µM AHSL, single operator against dual operator.)]

:::{figure} #cn-20260925-fig2
:label: fig-20260925-0p5nm
:align: center
:width: 75%
0.5 nM sensor DNA at approximately 576 nM EsaR and 5 µM AHSL, single operator against dual operator. Replicate wells are drawn individually rather than as a mean. Reaction composition is in {numref}`tbl-composition-20260925`.
:::

[`fig-20260925-0p5nm`, notebook:`CN-20260925-DNA_titration/platereader.ipynb`, platemap:`20260924-dna-titration-esar-fixed.csv`, data source:`20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`, caption: (0.5 nM sensor DNA at approximately 576 nM EsaR and 5 µM AHSL, single operator against dual operator.)]

:::{figure} #cn-20260925-fig3
:label: fig-20260925-1nm
:align: center
:width: 75%
1 nM sensor DNA at approximately 576 nM EsaR and 5 µM AHSL, single operator against dual operator. Reaction composition is in {numref}`tbl-composition-20260925`.
:::

[`fig-20260925-1nm`, notebook:`CN-20260925-DNA_titration/platereader.ipynb`, platemap:`20260924-dna-titration-esar-fixed.csv`, data source:`20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`, caption: (1 nM sensor DNA, single operator against dual operator.)]

:::{admonition} Three of six DNA concentrations are unreported
:class: warning
:name: review-20260925-missing-panels

{numref}`tbl-composition-20260925` and the platemap both carry 0.1, 0.5, 1, 3,
6 and 9 nM for each construct. The log shows panels for 0.1, 0.5 and 1 nM only.
The 3, 6 and 9 nM wells were run and are not reported here. The notebook also
holds a steady-state AHSL fold-induction bar plot that the log does not show.
:::

## 2026-09-26 — Sensor DNA titration with overnight EsaR

Results: \*Prior to analysis - The constructs are being repressed similarly to
the previous experiment. Adding "spent" EsaR reactions doesn't appear to be
improving the amount of repression noticeably.

:::{figure} #cn-20250926-fig1
:label: fig-20260926-esar-spent
:align: center
:width: 100%
Dual-operator \[EsaO\]2-mNG at 0.1, 0.5 and 1 nM sensor DNA with EsaR pre-expressed for 17 hrs at 30 ˚C, minus and plus AHSL. Reaction composition is in {numref}`tbl-composition-20260926`.
:::

[`fig-20260926-esar-spent`, notebook:`CN-20260926-DNA_titration_spent_EsaR/platereader.ipynb`, platemap:`20260924-esao2-dna-titration.csv`, data source:`20260926-115326-synergy2-pure-timecourse-gfp-DNA_titration_EsaR_spent.txt`, caption: (Dual-operator [EsaO]2-mNG at 0.1, 0.5 and 1 nM sensor DNA, minus and plus AHSL.)]

Repression is still observed in all cases when AHSL is not present; however, it
appears the total induced signal is lower than that of the previous experiment
in which the EsaR was pre-expressed for 3 hrs @ 37 ˚C, rather than 17 hrs @
30˚C. **Include fluorescein control in each graph, and also plot fold
change/steady state ratio of induced:uninduced to enable comparison between DNA
titration**.

## 2026-10-01 — Magnesium sweep with EsaR and DNA pre-incubation

[PLEASE FILL IN]

<!-- The 2026-10-01 log carries no results narrative. It ends on the magnesium
stock concentrations. The figure below is the only reported outcome. -->

:::{figure} #mbcn-20261001-fig1
:label: fig-20261001-mg-sweep
:align: center
:width: 100%
Added magnesium at 0, 5 and 10 mM, each minus and plus 5 µM AHSL, after pre-incubating EsaR with the DNA. Reaction volumes are in {numref}`tbl-volumes-20261001`.
:::

[`fig-20261001-mg-sweep`, notebook:`2026-10-01-MB-MgSweep/20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.ipynb`, platemap:`20261001-mg-sweep-platemap.csv`, data source:`20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.txt`, caption: (Added magnesium at 0, 5 and 10 mM, minus and plus 5 µM AHSL.)]

:::{admonition} The 20 mM magnesium arm is unreported
:class: warning
:name: review-20261001-missing-arm

The platemap carries four magnesium levels: 0, 5, 10 and 20, each minus and
plus AHSL, in two wells apiece. The log names "5, 10, 20 locally" and gives a
stock for each. Cell 8 plots 0, 5 and 10 only. The 20 mM wells were run and
have no reported panel.
:::

# Notes

[PLEASE FILL IN]

<!-- No source log carries a Notes section distinct from its narrative. The
2026-09-25 and 2026-09-26 logs open with an underlined "Notes" label. The text
under that label is the reaction preparation protocol. It is carried under
Methods. -->

# What's next

<!-- RENAMED: "Next steps" → "What's next" -->

From the 2026-09-25 log:

1.  Prepare DNA titration with 0.1 nM, 0.5 nM, 1 nM \[EsaO\]2-mNG adding EsaR
    from a reaction incubated overnight at 30 ˚C to assess whether adding
    "unspent" cytosol components from pre-expressed EsaR is affecting the state
    of repression. **Consider doing this with optiprep to see if affects the
    performance of the sensor.**
2.  0.1 nM, 0.5 nM, 1 nM, 15 nM const. PLA1 in GUVs to determine whether there
    is enough DNA to burst GUVs. Lipids: 99.15 % POPC, 0.85% DSPE-PEG2K. 20 µL
    inner solution. 37 ˚C incubation 3 hrs.
3.  Depending on which DNA concentration is capable of bursting GUVs, we then
    take those candidate concentrations forward to the two vesicle system.

From the 2026-09-26 log:

1.  Wait for purified EsaR to arrive.

# Resources

Reaction composition, one sidecar per day. No sidecar exists for 2026-10-01,
because that folder has no build file.

- [`experiments/build-composition-20260924.csv`](./experiments/build-composition-20260924.csv)
- [`experiments/build-composition-20260925.csv`](./experiments/build-composition-20260925.csv)
- [`experiments/build-composition-20260926.csv`](./experiments/build-composition-20260926.csv)

Analysis notebooks.

- [`experiments/20260924-repressor-test/platereader.ipynb`](./experiments/20260924-repressor-test/platereader.ipynb)
- [`experiments/20260925-dna-titration/platereader.ipynb`](./experiments/20260925-dna-titration/platereader.ipynb)
- [`experiments/20260926-dna-titration-esar-spent/platereader.ipynb`](./experiments/20260926-dna-titration-esar-spent/platereader.ipynb)
- [`experiments/20261001-mg-osmo-sweep/20261001-mg-osmo-sweep.ipynb`](./experiments/20261001-mg-osmo-sweep/20261001-mg-osmo-sweep.ipynb)

Platemaps.

- [`experiments/20260924-repressor-test/build - 20260924_Platemap.csv`](./experiments/20260924-repressor-test/build%20-%2020260924_Platemap.csv)
- [`experiments/20260925-dna-titration/20260924-dna-titration-esar-fixed.csv`](./experiments/20260925-dna-titration/20260924-dna-titration-esar-fixed.csv)
- [`experiments/20260926-dna-titration-esar-spent/20260924-esao2-dna-titration.csv`](./experiments/20260926-dna-titration-esar-spent/20260924-esao2-dna-titration.csv)
- [`experiments/20261001-mg-osmo-sweep/20261001-mg-sweep-platemap.csv`](./experiments/20261001-mg-osmo-sweep/20261001-mg-sweep-platemap.csv)

Raw instrument data.

- [`experiments/20260924-repressor-test/20260924-151252-cytation5-pure-timecourse-gfp-repressor_test.txt`](./experiments/20260924-repressor-test/20260924-151252-cytation5-pure-timecourse-gfp-repressor_test.txt)
- [`experiments/20260925-dna-titration/20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`](./experiments/20260925-dna-titration/20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt)
- [`experiments/20260926-dna-titration-esar-spent/20260926-115326-synergy2-pure-timecourse-gfp-DNA_titration_EsaR_spent.txt`](./experiments/20260926-dna-titration-esar-spent/20260926-115326-synergy2-pure-timecourse-gfp-DNA_titration_EsaR_spent.txt)
- [`experiments/20261001-mg-osmo-sweep/20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.txt`](./experiments/20261001-mg-osmo-sweep/20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.txt)
