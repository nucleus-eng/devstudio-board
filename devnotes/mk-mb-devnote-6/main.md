---
title: 'Double Vesicle Lysis System Leveraging deGFP CFPE'
thumbnail: ./figures/fig1-two-vesicle-kinetics.png
---

<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

<!-- Drafted 2026-10-21 from the Google Doc "Double Vesicle Lysis System
Leveraging deGFP CFPE".
Source: https://docs.google.com/document/d/1_iOQShy9GgeXlZnNVNlVYgMxIKNLkmq3wFapNrh9Qh4
Prose, tables and step lists are carried verbatim from that Doc, including
its own section order. The Doc has no separate Results heading; its one
figure sits inside Part 4 of the Protocol, exactly where the source puts
it. Figure caption drops the literal "Figure." label the Doc gives it,
since MyST auto-numbers the `:::{figure}` directive. A "Plasmid maps"
subsection is added after Plasmids and proteins (not in the source Doc),
the same placement used for this construct pair in mk-mb-devnote-4. -->

<!-- :::{admonition} Open items from the draft
:class: warning dropdown
:name: flags-review

**Materials and the Part 4 Plate layout table give 0, 0.25, 1 and 5 µM;
the Abstract, Overview, the figure legend and the Conclusion all give 0,
0.025, 0.1 and 0.5 µM — roughly ten-fold lower at every level.** The
likely explanation (Anton Molina, 2026-10-22): the first set is the aTc
stock concentration, and the second is the final concentration after
dilution into the well. Part 3 dispenses 20 µL of the vesicle/gel mixture
per well, and Part 4 adds 2 µL of CPRG plus aTc on top, for a 22 µL well —
an 11-fold dilution, close enough that 0.25/1/5 µM stock rounds to the
reported 0.025/0.1/0.5 µM final (0.25 → 0.023, 1 → 0.091, 5 → 0.455). The
Doc never states this explicitly, so it is not carried as fact in the
body text, but it is consistent with the Conclusion's own statement that
the delivered series ran lower than the plate was designed around.

**Part 3 step 1's description of how the two populations were combined is
hard to follow unambiguously.** "The reporter populations pellet was
resuspended to 100 uL and 10 uL were added to 25 uL of GUVs per condition
(cell free GUV pellets were resuspended to 50 uL). Then the outer solution
was added to 50 uL total." Carried exactly as written; which volume is
final-per-well versus final-per-batch is not fully clear from the text
alone.
::: -->

# Abstract

This experiment splits the assay across two separately formed GUV populations. Expression vesicles carry the cell-free reaction and its plasmid but no β-galactosidase; reporter vesicles carry β-galactosidase and nothing else. The two are combined only after both are made, embedded together in PEG-NB hydrogel, and read by CPRG conversion at 575 nm.

The architecture is designed to answer a question the single-population format could not. In the co-encapsulated design, expression and reporting happened in the same compartment, so anything that permeabilised a vesicle released the reporter from the very compartment that was making protein — and expression alone proved sufficient to do that. Separating the two populations asks whether the damage travels. If an expression vesicle permeabilises and nothing crosses to the reporter vesicles, conversion stays low; if a diffusible product or condition reaches the reporter population, conversion rises. The reporter is no longer dependent on its own compartment's expression.

Eleven expression populations are reported here, all built on a single β-galactosidase-free master mix: seven carrying pOpen-TetO-PLA at 0.5 nM and four carrying pOpen-TetO-deGFP at 0.5 nM. Each is repressed with TetR from one of four sources — MedChemExpress protein at 100 nM or 1000 nM, the same protein after detergent removal at either dose, or an overnight cell-free preparation — with cell-free deGFP shams where the cell-free route is used. Two reporter populations supply β-galactosidase at a nominal 5 U/mL and 50 U/mL, so that reporter abundance is itself a variable rather than a fixed assumption.

Every combination is read across four aTc levels: 0, 0.025, 0.1 and 0.5 µM. The deGFP arms set what expression alone produces in this geometry; the PLA1 arms ask whether a phospholipase adds anything beyond it. The two reporter doses test whether the readout is limited by how much β-galactosidase is available or by how much reaches it.

# Overview

**What the split buys.** Co-encapsulation established that protein expression permeabilises the vesicle doing the expressing. That finding left the phospholipase question unanswerable in that format, because every lytic signal had a non-lytic explanation sitting in the same compartment. Here the reporter sits in a different compartment entirely. Expression vesicles can permeabilise freely without, by itself, producing any signal — conversion requires that something released from an expression vesicle reaches a reporter vesicle and breaches it, or that β-galactosidase released from a reporter vesicle meets external CPRG.

**What the deGFP arms measure now.** In the single-population format, deGFP set the floor for expression-driven release. Here it sets the floor for expression-driven damage at a distance. A deGFP expression vesicle that permeabilises releases its contents into the gel; whether those contents then harm a neighbouring reporter vesicle is exactly what conditions 15 through 18 measure. Any conversion they produce is the background against which PLA1 must be judged.

**What the PLA1 arms could show.** Phospholipase is an enzyme and acts catalytically on membranes it encounters. If PLA1 escapes a permeabilised expression vesicle, it should damage reporter vesicles in a way that a released fluorescent protein does not. That difference — PLA1 arms above deGFP arms at matched template and matched repression — is the signal this geometry is built to detect, and it is a cleaner claim than anything the co-encapsulated format could support.

**Why two reporter doses.** At 5 U/mL and 50 U/mL, the reporter populations differ tenfold in enzyme per vesicle. If conversion scales with that dose, the readout is reporting how much β-galactosidase was released and the assay is enzyme-limited. If it does not, conversion is limited by how many reporter vesicles were breached, which is the quantity of interest. The pair is a built-in test of what the colour is actually measuring.

**Four sources of TetR.** Purified MedChemExpress protein is used at 100 nM and 1000 nM, before and after detergent removal, giving a full two-by-two of dose against column treatment. That resolves the confound left open by earlier runs, where treated and untreated preparations were never compared at matched dose. Overnight cell-free TetR provides a route avoiding the commercial buffer altogether, with volume-matched cell-free deGFP shams.

**What a successful run looks like.** Conversion from PLA1 conditions clearly above the matched deGFP conditions; aTc raising conversion in repressed arms of both; a difference between the two reporter doses that identifies what limits the readout; and treated against untreated TetR separating at matched dose, or not, settling what the spin column does.

# Materials

## Plasmids and proteins

:::{table} Plasmids and proteins.
:label: tbl-plasmids-proteins
:align: center

| Item | Working stock | Final in reaction | Role |
| --- | --- | --- | --- |
| pOpen-TetO-PLA | 12.5 nM | 0.5 nM | Phospholipase A1 |
| pOpen-TetO-deGFP | 12.5 nM | 0.5 nM | Non-lytic expression control |
| TetR-His (MedChemExpress) | 1 µM and 10 µM | 100 or 1000 nM | Repressor, as supplied |
| TetR-His, detergent-removed | 1 µM and 10 µM | 100 or 1000 nM | Same, after Tween-removal column |
| Cell-free TetR, overnight | — | 2.5 µL per reaction | Repressor without commercial buffer |
| Cell-free deGFP, overnight | — | 2.5 µL per reaction | Sham for the above |
| β-galactosidase (LacZ) | 125 U/mL and 1000 U/mL | 5 or 50 U/mL | Reporter, separate population |
:::

## Plasmid maps

:::::{tab-set}

::::{tab-item} pOpen-TetO-PLA
:sync: pla

(seqviz-popen-teto-pla)=

:::{seqviz} ./dna/pOpen-TetO-PLA.gb
:::

::::

::::{tab-item} pOpen-TetO-deGFP
:sync: degfp

(seqviz-popen-teto-degfp)=

:::{seqviz} ./dna/pOpen-TetO-deGFP.gb
:::

::::

:::::

## Cell-free system, expression populations

β-galactosidase is absent from this master mix — that is the defining change from the co-encapsulated protocol.

:::{table} Cell-free system, expression populations, per 25 µL reaction.
:label: tbl-cellfree
:align: center

| Component | Per 25 µL reaction (µL) | Fraction of reaction |
| --- | --- | --- |
| Smix | 7.5 | 30% |
| tRNA | 2.5 | 10% |
| Pmix | 3.0 | 12% |
| Ribosomes | 4.5 | 18% |
| RIM | 1.3 | 5.2% |
| Sucrose (3.4 mg per 25 µL) | 2.2 | 8.8% |
| **Master mix total** | **21.0** | **84%** |
:::

## Reagents, consumables and equipment

- CPRG, 5 mM stock — chromogenic β-galactosidase substrate, read at 575 nm
- Anhydrotetracycline (aTc), delivered with the CPRG at four levels: 0, 0.25, 1 and 5 µM final
- HEPES, 1 M — the bulk of the reporter vesicle inner solution
- Detergent-removal spin columns for the TetR-His preparations
- PEG-norbornene precursor with crosslinker and photoinitiator, blue-light curable
- Lipid films: 11 for the expression populations, 1.5 each for the two reporter populations, 14 total
- Outer solution as in the preceding GUV protocols
- Mineral oil, BioUltra; BSA 2% w/v; nuclease-free water
- Blue light source; refrigerated microcentrifuge, 18,000 rcf at 4 °C; 37 °C incubation
- 384-well plate and plate reader capable of 575 nm absorbance kinetics

# Protocol

## Part 1 — Reporter vesicle populations

Two populations carrying β-galactosidase and no cell-free machinery. The inner solution is almost entirely 1 M HEPES, matching the osmolarity of the expression vesicles and of the hydrogel they will share.

:::{table} Reporter vesicle populations.
:label: tbl-part1-reporters
:align: center

| Component | Pop 1 — 5 U/mL | Pop 2 — 50 U/mL |
| --- | --- | --- |
| Sucrose | 2.2 µL | 2.2 µL |
| LacZ | 1.0 µL of 125 U/mL | 1.25 µL of 1000 U/mL |
| HEPES, 1 M | 21.8 µL | 21.55 µL |
| **Total** | **25.0 µL** | **25.0 µL** |
| Resulting LacZ | 5 U/mL | 50 U/mL |
| Films | 1.5 | 1.5 |
:::

Both populations are assembled to 25 µL — see the note below.

### Steps

1. Prepare 1 lipid film per reporter population and dissolve each in mineral oil as in the preceding GUV protocols.
2. Add the β-galactosidase inner solution to the cold lipid/oil mixture, vortex 30 s, rest on ice 5 min.
3. Layer over outer solution, rest on ice 5 min, centrifuge 15 min at 18,000 rcf, 4 °C.
4. Remove the mineral oil, collect each pellet with a fresh tip, and resuspend in outer solution.
5. Confirm before use that the external phase is free of β-galactosidase. A leaky reporter population converts CPRG in every well regardless of what the expression vesicles do, and would invalidate the entire plate.

## Part 2 — Expression vesicle populations

Eleven reactions on one master mix: seven PLA1 and four deGFP, all at 0.5 nM plasmid.

### Conditions

:::{table} Part 2 conditions.
:label: tbl-part2-conditions
:align: center

| # | Condition | Plasmid | Repression source | Dose |
| --- | --- | --- | --- | --- |
| 8 | DV 0.5 nM PLA | PLA | none — constitutive | — |
| 9 | DV 0.5 nM PLA + 100 nM TetR | PLA | MedChem TetR-His | 100 nM |
| 10 | DV 0.5 nM PLA + 1000 nM TetR | PLA | MedChem TetR-His | 1000 nM |
| 11 | DV 0.5 nM PLA + 100 nM TetR, spin column | PLA | MedChem, detergent-removed | 100 nM |
| 12 | DV 0.5 nM PLA + 1000 nM TetR, spin column | PLA | MedChem, detergent-removed | 1000 nM |
| 13 | DV 0.5 nM PLA + overnight cell-free TetR | PLA | Overnight cell-free TetR | 2.5 µL |
| 14 | DV 0.5 nM PLA + overnight sham | PLA | Overnight cell-free deGFP | 2.5 µL |
| 15 | DV 0.5 nM deGFP | deGFP | none — constitutive | — |
| 16 | DV 0.5 nM deGFP + 1000 nM TetR | deGFP | MedChem TetR-His | 1000 nM |
| 17 | DV 0.5 nM deGFP + 1000 nM TetR, spin column | deGFP | MedChem, detergent-removed | 1000 nM |
| 18 | DV 0.5 nM deGFP + overnight cell-free TetR | deGFP | Overnight cell-free TetR | 2.5 µL |
:::

Conditions 9 through 12 form a two-by-two of TetR dose against spin-column treatment — the comparison earlier experiments left unresolved.

### Assembly, µL per 25 µL reaction

:::{table} Part 2 assembly volumes.
:label: tbl-part2-assembly
:align: center

| Component | Condition 8 and 15 (no TetR) | All other conditions |
| --- | --- | --- |
| Master mix | 21.0 | 21.0 |
| DNA (12.5 nM stock) | 1.0 | 1.0 |
| TetR or sham | 0 | 2.5 |
| Water | 3.0 | 0.5 |
| **Total** | **25.0** | **25.0** |
:::

Purified TetR stocks are 1 µM for the 100 nM arms and 10 µM for the 1000 nM arms, so 2.5 µL gives the intended dose in both cases.

### Master mix, eleven reactions

:::{table} Part 2 master mix, eleven reactions.
:label: tbl-part2-mastermix
:align: center

| Component | Volume (µL) |
| --- | --- |
| Smix | 82.5 |
| tRNA | 27.5 |
| Pmix | 33 |
| Ribosomes | 49.5 |
| RIM | 14.3 |
| Sucrose | 24.2 (37.4 mg) |
| LacZ | 0 — none |
| **Total** | **231.0** |
:::

### Steps

1. Prepare the overnight cell-free TetR and deGFP reactions in advance.
2. Pass aliquots of both MedChemExpress TetR stocks through detergent-removal columns, keeping the untreated stocks alongside.
3. Weigh out the solid sucrose for the batch and vortex it into the Smix until dissolved, then add tRNA, Pmix, ribosomes and RIM.
4. Combine plasmid, protein addition and water for each condition in its own tube and pre-incubate 10 min at 37 °C so TetR can bind tetO before transcription starts.
5. Add 21 µL of master mix to each tube, mix by gentle pipetting, and encapsulate immediately — expression must start inside the vesicle.
6. Encapsulate each condition on its own lipid film, following the same emulsion, centrifugation and resuspension steps as the reporter populations.

## Part 3 — Combine the populations and cast the hydrogel

1. Pair each expression population with each reporter population, keeping the mixing ratio constant across every combination. The reporter populations pellet was resuspended to 100 uL and 10 uL were added to 25 uL of GUVs per condition (cell free GUV pellets were resuspended to 50 uL). Then the outer solution was added to 50 uL total.
2. 50 uL of the PEG-NB precursor was added to each mixture and 20 uL were dispensed per well.
3. Crosslink under blue light for 60 seconds and confirm the gel has set before adding substrate.

## Part 4 — Add substrate and inducer, then read

1. Add CPRG and aTc together to each well, at the aTc level that well's column calls for. 2 uL are added to each well.
2. Seal the plate against evaporation before starting.
3. Read absorbance at 575 nm kinetically, recording the full trace rather than an endpoint.

### Plate layout, 384-well

Rows J–M carry the four deGFP expression populations. Each row spans four aTc levels crossed with the two reporter doses, eight wells per condition.

:::{table} Plate layout, deGFP block, rows J-M.
:label: tbl-part4-layout-degfp
:align: center

| Row | Expression population | Cols 2–3: 0 µM aTc | Cols 4–5: 0.25 µM | Cols 6–7: 1 µM | Cols 8–9: 5 µM |
| --- | --- | --- | --- | --- | --- |
| J | 15 — deGFP constitutive | 5 / 50 U/mL | 5 / 50 | 5 / 50 | 5 / 50 |
| K | 16 — deGFP + 1000 nM TetR | 5 / 50 U/mL | 5 / 50 | 5 / 50 | 5 / 50 |
| L | 17 — deGFP + 1000 nM TetR, spin column | 5 / 50 U/mL | 5 / 50 | 5 / 50 | 5 / 50 |
| M | 18 — deGFP + overnight cell-free TetR | 5 / 50 U/mL | 5 / 50 | 5 / 50 | 5 / 50 |
:::

Within each aTc pair, the left column is the 5 U/mL reporter population and the right is 50 U/mL. 32 wells for the deGFP arms.

### PLA1 block, columns 16–23

Six PLA1 populations across the same four aTc levels and two reporter doses, 48 wells. Conditions 13 and 14 are split across three rows rather than occupying one each.

:::{table} PLA1 block, columns 16-23.
:label: tbl-part4-layout-pla1
:align: center

| Rows | Expression population | Wells | Reporter doses |
| --- | --- | --- | --- |
| H | 9 — PLA + 100 nM TetR | 8 | 5 and 50 U/mL, alternating |
| G | 10 — PLA + 1000 nM TetR | 8 | 5 and 50 U/mL, alternating |
| F | 11 — PLA + 100 nM TetR, spin column | 8 | 5 and 50 U/mL, alternating |
| E | 12 — PLA + 1000 nM TetR, spin column | 8 | 5 and 50 U/mL, alternating |
| C, D | 13 — PLA + overnight cell-free TetR | 8 | 5 U/mL in row C, 50 U/mL in row D |
| C, I | 14 — PLA + overnight sham | 8 | 5 U/mL in row C, 50 U/mL in row I |
:::

Rows E through H each hold one condition with the two reporter doses alternating across columns. Row C interleaves the 5 U/mL wells of conditions 13 and 14, with their 50 U/mL wells displaced to rows D and I; every condition still totals 8 wells. 80 wells in all across both blocks.

:::{figure} ./figures/fig1-two-vesicle-kinetics.png
:label: fig-1-two-vesicle-kinetics
:align: center
:width: 80%
Kinetic absorbance at 575 nm over 14 h for expression GUVs mixed with β-galactosidase reporter GUVs in PEG-NB hydrogel. (Top) deGFP background — conversion proceeded at a similar rate across all aTc concentrations. (Middle) PLA1 repressed with 100 nM TetR — no robust aTc response. (Bottom) PLA1 repressed with 1000 nM TetR — strong colorimetric response at 0.1 µM and 0.5 µM aTc, well above the deGFP background.
:::

# Conclusion

Splitting the reporter into its own vesicle population did what it was meant to do: it produced a PLA1 signal that cannot be explained by expression alone. In the co-encapsulated format, deGFP and PLA1 at matched template gave superimposable traces, and no lysis claim survived. Here the deGFP arms are flat with respect to aTc — expression level does not drive conversion in this geometry — while PLA1 under 1000 nM TetR responds to inducer at 0.1 and 0.5 µM ({ref}`fig-1-two-vesicle-kinetics`). The difference between those panels is the phospholipase.

That the deGFP background is aTc-insensitive is the result that makes the rest interpretable, and it is a direct consequence of the architecture. When reporter and expression shared a compartment, expression-driven permeabilisation released the reporter from the vesicle doing the expressing, and the readout tracked expression. With the reporter in a separate population, an expression vesicle can permeabilise without producing signal — whatever leaks out has to reach and breach a reporter vesicle. Expression alone evidently does not travel; PLA1 does.

Repression depth matters more than expected. At 100 nM TetR the aTc response was weak, at 1000 nM it was strong. Both carry the same template, so the likely explanation is that 100 nM is insufficient to hold PLA1 off — leaky expression in the uninduced state raises the baseline and compresses the window aTc can act in. That is consistent with the earlier deGFP work, where the 1000 nM arms repressed more tightly, and it argues for 1000 nM as the standard going forward.

The aTc series delivered here ran lower than the 0–5 µM range the plate was designed around, and the response at 0.1 and 0.5 µM is a useful finding in itself: the system is sensitive at doses well below those used previously. Whether it saturates or declines above 0.5 µM is now an open question rather than an answered one, and worth a dedicated titration.

Two limits on how far this can be pushed. Constitutive PLA1 was not plated, so the experiment has no unrepressed ceiling — the induced wells cannot be placed on a scale running from fully off to fully on, and the absolute efficiency of the system is unknown. And with one well per aTc level per reporter dose, the dose response rests on n = 1; the shape across the series carries the argument, not any single pair. Adding condition 8 and a replicate well is what would turn this from a promising result into a solid one.
