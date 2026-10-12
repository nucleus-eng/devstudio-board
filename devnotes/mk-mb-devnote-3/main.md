---
title: 'Expressing Cell-Free TetO-GFP in Solution with aTc Titration'
thumbnail: ./figures/fig2-endpoint-gfp-atc-titration.png
---

<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

<!-- Drafted 2026-10-11 from the Google Doc "TetO-plamGFP in Solution".
Source: https://docs.google.com/document/d/1F3oW_PK6oKyVTA1JaVtpX5BvqwYHdBwEvA59MDBIMes
Prose, tables, step lists, captions and both figures are carried verbatim
from that Doc, including its own section order. The Doc's own title/authors
block ("Title: ..." / "Authors:" / each name and email) is not repeated in
the body: title, authors and their emails live in this file's frontmatter
and in curvenote.yml instead, and render as the page byline. -->

<!-- :::{admonition} Open items from the draft
:class: warning dropdown
:name: flags-review

**The Reagents and stocks, Master mix, Reaction conditions, and Results
tables carried Google Docs export artifacts (`\#\#\#`, `\*\*`) around every
cell in the source pull.** Removed here as a formatting fix; no value, unit,
or row changed.

**The Results section carries two empty placeholder lines in the source
itself.** "dataset link:" and "Platemap link:" appear with nothing after the
colon. Carried as written; there is no dataset or platemap link to add.

**The fluorescein-standards description does not match the plate image.**
The text says "S1 to S4 ... in row G, columns 2 to 9, in duplicate." The
extracted image (`figures/fig1-plate-layout.png`) shows S1, S1, S2, S2, S3,
S3, S4 across columns 2 to 8 — S4 appears once, not in duplicate, and column
9 is blank. Both are carried as supplied; this is a discrepancy in the source,
not something introduced here.

**`dna/pOpen-pT7-tetO.gb` is the real file of record, not built here.** The
source Doc gives no inline sequence for this construct, only a name
(pT7-tetO-plamGFP) and a link to the Nucleus tetR-aTc Detector module spec.
`nucleus-eng/DNA`'s `detectors/pOpen-pT7-tetO.gb` was checked directly on
2026-10-11: 2954 bp, `DEFINITION` reads "PlamGFP green fluorescent protein
with repressed by the tet repressor tetR," and its features carry a T7
promoter, a `tetO` operator, a plamGFP CDS, and an AmpR marker — matching the
Doc's own description of the genetic circuit (tetO operator between the T7
promoter and the plamGFP coding sequence). This is the strongest identity
match found across this board's three DevNotes so far: the file's own
`DEFINITION` line names the construct, not just a filename resemblance. Taken
and used as-is, unmodified, and drives {ref}`seqviz-pt7-teto-plamgfp`.

**No sequence file was located, or was needed, for TetR or beta-galactosidase
reference material** — neither applies here; TetR is a purchased protein
(MedChemExpress HY-P71520A), same as in the sibling DevNotes on this board.
::: -->

# Abstract

TetR-based repression is a common building block for cell-free genetic circuits, but its dynamic range and its sensitivity to inducer depend on the extract and on the repressor concentration used. We measured repression of the pT7-tetO-plamGFP reporter by purified TetR in bulk cell-free reactions, and the relief of that repression across a seven-point anhydrotetracycline (aTc) titration. Reporter plasmid at 1 nM was expressed with 0, 500 or 1000 nM TetR at aTc concentrations from 0 to 10 µM, in triplicate, with GFP fluorescence followed for 6 h at 37 °C. Both repressor concentrations held expression near background in the absence of inducer and recovered to the unrepressed level by 5 µM aTc, but the 1000 nM condition needed roughly twice as much aTc as the 500 nM condition to reach the same point, so the amount of TetR sets where the switch threshold sits rather than whether the switch works.

# Overview

We tested TetR repression of the pT7-tetO-plamGFP reporter in bulk cell-free reactions, and the relief of that repression across a seven-point anhydrotetracycline (aTc) titration.

Four bulk reactions were assembled: a no-DNA control, an unrepressed reaction with reporter plasmid but no TetR, and two repressed reactions containing 500 nM or 1000 nM purified TetR. Each bulk reaction was aliquoted into a 384-well plate and supplemented with aTc to a final concentration of 0, 0.25, 0.35, 0.5, 1, 5 or 10 µM, in triplicate, giving 28 conditions and 84 reaction wells.

# Protocol

## Genetic circuit

The reporter plasmid pT7-tetO-plamGFP ([b.next, Nucleus tetR-aTc Detector module](https://docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec/)) places a tetO operator between the T7 promoter and the plamGFP coding sequence. Purified His-tagged TetR ([MedChemExpress, HY-P71520A](https://www.medchemexpress.com/us/en/recombinant-proteins/tetr-protein-e-coli-his.html?srsltid=AU7gw4XeoLAU4C1NcJKmfsKthnNGFGwvbKLvPkvOY3NtBwW2pcWP1Ys9)) binds tetO and blocks transcription; aTc binds TetR and releases it from the operator, restoring plamGFP expression. The output is therefore a graded GFP signal set by the aTc concentration.

## Reagents and stocks

Reactions were run in b.next Nucleus Base Cytosol, a PURE-type reconstituted system supplied as a premade reagent kit, and assembled following the Nucleus [Assemble Base Cytosol](https://docs.nucleus.engineering/docs/processes/assemble-base-cytosol/main) process. Per 10 µL of reaction the component ratios match that reference composition: 3.0 µL SMix, 1.0 µL tRNA, 1.2 µL PMix, 1.8 µL ribosomes and 0.5 µL RNase inhibitor. The reporter and repressor are the Nucleus [tetR-aTc Detector](https://docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec) module.

:::{table} Reagents and stocks.
:label: tbl-reagents
:align: center

| Component | Stock | Notes |
| --- | --- | --- |
| Small Molecule Mix (SMix) | working stock | Nucleus Base Cytosol component |
| tRNA | working stock | — |
| Protein Mix (PMix) | working stock | — |
| Ribosomes | working stock | — |
| RNase Inhibitor, Murine (RIM) | working stock | [NEB #M0314L](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| Sucrose | solid | 203 mg weighed directly into the master mix tube |
| [pT7-tetO-plamGFP reporter plasmid](https://docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec/) | 129.6 nM | Final concentration: 0 or 1 nM depending on sample |
| TetR protein | 10,000 nM (10 µM) | [MedChemExpress, HY-P71520A](https://www.medchemexpress.com/us/en/recombinant-proteins/tetr-protein-e-coli-his.html?srsltid=AU7gw4XeoLAU4C1NcJKmfsKthnNGFGwvbKLvPkvOY3NtBwW2pcWP1Ys9) |
| Anhydrotetracycline (aTc) | 11× working dilutions, 2.75–110 µM | added as 1 µL per 10 µL reaction |
| Nuclease-free H₂O | — | to volume |
:::

## Master mix

Components common to all four conditions (SMix, tRNA, PMix, Ribosomes, RIM, Sucrose) were combined into a single master mix in a 1.5 mL Eppendorf tube, sufficient for four 380 µL reactions. Amounts were obtained by summing the per-reaction requirements in the table below. Sucrose was weighed directly into the tube as 203 mg of solid, the remaining components were added on top, and the sucrose was dissolved by pipette mixing.

:::{table} Master mix, sufficient for four 380 µL reactions.
:label: tbl-mastermix
:align: center

| Component | Volume (µL) |
| --- | --- |
| SMix | 456 |
| tRNA | 152 |
| PMix | 182.4 |
| Ribosomes | 273.6 |
| RNase Inhibitor | 76 |
| Sucrose | 133.76 (203 mg solid) |
| **Total** | **1273.76** |
:::

The master mix was mixed gently by pipette and set aside while the DNA, TetR and water tubes were prepared, then split between them as described below. Apart from the 10 min pre-incubation, everything was kept on ice from assembly until the plate went into the reader.

## Reaction conditions

Each bulk reaction was brought to a final volume of 380 µL. Volumes below are per tube; the first six rows (SMix, tRNA, PMix, Ribosomes, RIM, Sucrose) make up the master mix volume added to each tube, as 318.44 µL to the pre-incubated plasmid, TetR, and water mixes.

Specifically, plasmid, TetR, and water were combined in their own tube per condition (61.56 µL in every case) and incubated at 37 °C for 10 min to allow TetR to bind the operator. The same volume of master mix, 318.44 µL, was then added to every tube and mixed gently.

:::{table} Reaction conditions, volumes in µL.
:label: tbl-conditions
:align: center

| Component | 1. No DNA | 2. Unrepressed (no TetR) | 3. 500 nM TetR | 4. 1000 nM TetR |
| --- | --- | --- | --- | --- |
| SMix (µL) | 114 | 114 | 114 | 114 |
| tRNA (µL) | 38 | 38 | 38 | 38 |
| PMix (µL) | 45.6 | 45.6 | 45.6 | 45.6 |
| Ribosomes (µL) | 68.4 | 68.4 | 68.4 | 68.4 |
| RNase Inhibitor (RIM) (µL) | 19 | 19 | 19 | 19 |
| Sucrose (µL) | 33.44 | 33.44 | 33.44 | 33.44 |
| pT7-tetO-plamGFP, 129.6 nM (µL) | 0 | 3 | 3 | 3 |
| TetR, 10,000 nM (µL) | 0 | 0 | 19 | 38 |
| H₂O (µL) | 61.56 | 58.56 | 39.56 | 20.56 |
| **Total (µL)** | **380** | **380** | **380** | **380** |
| Final DNA conc. | 0 nM | 1 nM | 1 nM | 1 nM |
| Final TetR conc. | 0 nM | 0 nM | 500 nM | 1000 nM |
:::

## aTc titration and plate layout

Each bulk reaction was dispensed at 10 µL per well into a 384-well plate, followed by 1 µL of aTc prepared at 11×, for an 11 µL final volume at the stated final aTc concentration. Each of the four conditions was plated across all seven aTc levels in triplicate.

Rows B–E carry the four conditions in order (B = no DNA, C = unrepressed, D = 500 nM TetR, E = 1000 nM TetR). Columns are grouped in threes by aTc level:

:::{table} aTc stock and final concentration by plate column.
:label: tbl-atc-columns
:align: center

| Columns | aTc stock added (µM) | Final aTc (µM) |
| --- | --- | --- |
| 2–4 | 0 | 0 |
| 5–7 | 2.75 | 0.25 |
| 8–10 | 3.85 | 0.35 |
| 11–13 | 5.5 | 0.5 |
| 14–16 | 11 | 1 |
| 17–19 | 55 | 5 |
| 20–22 | 110 | 10 |
:::

:::{figure} ./figures/fig1-plate-layout.png
:label: fig-1-plate-layout
:align: center
:width: 90%
*Figure 1.* Plate layout. Conditions 1–28 occupy rows B–E, columns 2–22, in triplicate and grouped in threes by aTc concentration. Rows run no DNA (B), no TetR (C), 500 nM TetR (D) and 1000 nM TetR (E). Fluorescein standards S1–S4 sit in row G, columns 2–9, in duplicate. Shaded wells around the perimeter hold water only.
:::

Four fluorescein standards (S1–S4, at 0, 0.5, 1 and 2 µM) were plated in duplicate in row G, columns 2–9, for conversion of arbitrary fluorescence units to molar equivalents of fluorescein (MEF).

Row A and columns 1 and 23 carried no samples and were filled with water, to buffer the outermost wells against evaporation and edge effects over the 6 h read.

# Data acquisition and analysis

Reactions were plated in a Greiner 384-well small-volume NoBind plate and read on a BioTek Cytation 3 plate reader (serial 130723A) held at 37 °C (gradient 0 °C). GFP fluorescence was recorded as a kinetic run over 6 h at 5 min intervals, with excitation at 485 nm and emission at 528 nm, top optics, gain 75. The light source was xenon flash at high lamp energy, normal read speed, 100 ms delay, 10 measurements per data point, read height 10.75 mm. The incubator was switched off at the end of the kinetic run.

Endpoint values are the final timepoint of the 6 h kinetic run, reported as raw fluorescence and plotted as the mean ± standard deviation of three wells per condition. No-DNA reactions are plotted alongside the samples at each aTc concentration rather than subtracted from them, so that any aTc-dependent change in background is visible directly; across the whole titration this background stayed between 40 and 90 RFU. Fluorescein standards at 0, 0.5, 1 and 2 µM were read on the same plate and give 31,805 RFU per µM for converting these values to molar equivalents of fluorescein. Where fold repression is quoted it is the unrepressed endpoint mean divided by the repressed endpoint mean at the same aTc concentration.

# Results

TetR represses the reporter tightly at both concentrations, and aTc relieves that repression fully, but the inducer concentration needed scales with the amount of repressor.

Without inducer, endpoint fluorescence fell from 21,662 RFU in the unrepressed reaction to 541 RFU at 500 nM TetR and 399 RFU at 1000 nM. Adding aTc restored expression in both cases, and by 5 µM neither repressed condition was distinguishable from the unrepressed one.

The two repressor concentrations separate across the middle of the titration. At 0.25 µM aTc the 500 nM reaction had already recovered to 6,587 RFU, about 30% of full expression, while the 1000 nM reaction was still almost fully repressed at 876 RFU. The 1000 nM curve reaches the same point near 0.5 µM aTc, so doubling the repressor shifts the induction curve roughly two-fold to the right in aTc.

:::{table} Endpoint RFU at 6 h, mean of three wells.
:label: tbl-results
:align: center

| aTc (µM) | −DNA | 0 nM TetR | 500 nM TetR | 1000 nM TetR |
| --- | --- | --- | --- | --- |
| 0 | 47 | 21,662 | 541 | 399 |
| 0.25 | 49 | 21,713 | 6,587 | 876 |
| 0.35 | 49 | 22,370 | 9,470 | 1,078 |
| 0.5 | 43 | 22,498 | 16,241 | 4,969 |
| 1 | 47 | 22,871 | 19,609 | 14,457 |
| 5 | 69 | 22,710 | 20,618 | 20,045 |
| 10 | 87 | 22,488 | 19,457 | 20,822 |
:::

The no-DNA control stayed between 43 and 87 RFU across the titration, so aTc contributes no meaningful fluorescence of its own at these concentrations and does not inhibit expression: the unrepressed reaction held at 21,662–22,871 RFU from 0 to 10 µM aTc.

dataset link:

Platemap link:

:::{figure} ./figures/fig2-endpoint-gfp-atc-titration.png
:label: fig-2-endpoint-gfp-atc-titration
:align: center
:width: 90%
*Figure 2.* Endpoint GFP expression across an aTc titration at three TetR concentrations. Bulk cell-free reactions containing 1 nM pT7-tetO-plamGFP and 0, 500 or 1000 nM purified TetR were induced with anhydrotetracycline at 0–10 µM final and read for 6 h at 37 °C. Points are fluorescence at the 6 h endpoint (ex 485 nm, em 528 nm, gain 75), mean ± SD of three wells per condition, with error bars smaller than the symbols in most cases. The −DNA control is a no-template reaction at the matching aTc concentration.
:::

# Conclusion

The tetR-aTc module works as specified in Nucleus Base Cytosol, repressing expression to near background at both 500 and 1000 nM TetR and recovering cleanly to the unrepressed level on induction. Both repressor concentrations are usable, so the choice between them is a choice about where the switch should sit: 500 nM gives a more sensitive detector that responds at 0.25 µM aTc, while 1000 nM gives a tighter OFF state and a threshold closer to 0.5–1 µM.

For circuits that need a sharp, late-triggering switch, 1000 nM is the better setting. For a detector meant to report low aTc, 500 nM is. The useful inducer range for either is 0.25–1 µM, which sits below the 2.5–5 µM the module specification recommends and well below the concentrations where aTc's own color interferes with the GFP channel.

Two things are worth noting about scope. The titration is coarse between 0.5 and 5 µM, so the thresholds quoted here are read off the measured points rather than interpolated; a finer spacing across 0.1–1 µM would pin down where each curve turns over. And this write-up looks only at the 6 h endpoint, though the run recorded fluorescence every 5 min throughout. Those kinetic traces are available from the same plate and would show whether the repressed conditions differ in onset time as well as in final level.

# Plasmid reference — pT7-tetO-plamGFP

(seqviz-pt7-teto-plamgfp)=

:::{seqviz} ./dna/pOpen-pT7-tetO.gb
:::

<!-- Not a section of the source Doc. Added because the source names the
construct and links to its Nucleus module spec, but supplies no sequence of
its own; the map above renders the real nucleus-eng/DNA file identified in
Open items, taken as-is and unmodified. -->

# Sources

- [Assemble Base Cytosol](https://docs.nucleus.engineering/docs/processes/assemble-base-cytosol/main) — Nucleus process, component names and reference composition
- [Detector: tetR-aTc](https://docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec) — Nucleus module specification for pT7-tetO-plamGFP and TetR
- [Make Ribosomes](https://docs.nucleus.engineering/docs/processes/make-ribosomes/main), [Make Small Molecule Mix](https://docs.nucleus.engineering/docs/processes/make-small-molecule-mix/main), [Make tRNAs](https://docs.nucleus.engineering/docs/processes/make-trna/main), [Protein Mix](https://docs.nucleus.engineering/docs/processes/make-36pot/main) — Nucleus component processes
- Yadav, S. (2025). First Nucleus Cytosol Testing: Evaluation of Nucleus Cytosol v0.5 Through deGFP Expression. [10.63765/fppr8928](https://doi.org/10.63765/fppr8928)
- RNase Inhibitor, Murine — New England Biolabs [#M0314L](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine)
- TetR repressor protein — MedChemExpress HY-P71520A
