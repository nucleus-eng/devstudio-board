---
title: 'Co-Encapsulated Cell-Free PLA1 Expression in beta-Galactosidase GUVs'
thumbnail: ./figures/fig8-endpoint-abs-15h.png
---

<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

<!-- Drafted 2026-10-12 from the Google Doc "Single Vesicle Lysis System
Leveraging deGFP CFPE".
Source: https://docs.google.com/document/d/1DouMRrZWCUKdWzuMoH48izjj8-7_oyKGCQrU2xOm5GI
Prose, tables, step lists, captions and all nine figures are carried
verbatim from that Doc, including its own section order (two experiments,
each with its own Results and Conclusion). The Doc's own title/byline block
(title heading, then each author's name, role and email as body text) is
not repeated in the body: title, authors and their emails live in this
file's frontmatter and in curvenote.yml instead, and render as the page
byline — same fix as mk-mb-devnote-3. Figure captions drop the literal
"Figure N." prefix the Doc gives them, since MyST auto-numbers the
`:::{figure}` directive; same fix as mk-mb-devnote-3. A "Plasmid maps"
subsection is added after Plasmids and proteins (not in the source Doc),
following the same placement request applied to mk-mb-devnote-3's single
construct, and holds both plasmid maps as a two-item tab-set (on request,
2026-10-12), one tab per construct. A number of sentences gained {ref}
cross-links to the table, figure, or seqviz view they describe (on
request, 2026-10-12); two of those are new bridging sentences not in the
source Doc, added only to carry a cross-link to the follow-up's master
mix and plate layout tables. No value, unit, or claim changed. -->

<!-- :::{admonition} Open items from the draft
:class: warning dropdown
:name: flags-review

**The source skips Figure 5 entirely.** Results run Figure 1 through
Figure 4, then the Follow Up Experiment's Results run Figure 6 through
Figure 10 — no Figure 5 caption and no ninth image exists anywhere in the
source Doc (nine images for ten figure numbers). Carried as supplied; not
a gap introduced here.

**Because of that gap, this devnote's rendered figure numbers no longer
match the source Doc's own numbers from the second Results section on.**
Captions here carry no literal "Figure N." text (same fix as
mk-mb-devnote-3, so MyST's auto-numbering is the only number shown), and
MyST numbers the nine figures 1 through 9 with no gap. So what the source
Doc calls Figure 6 renders here as Figure 5, Figure 7 as Figure 6, and so
on through Figure 10 rendering as Figure 9. The page is internally
consistent — every caption and cross-reference agrees with the number
next to it — but a reader checking against the original Doc will see the
second Results section's numbers shifted down by one.

**The Materials table's beta-galactosidase row forward-references an item
the source never defines.** It lists stock concentration as "see open
items," but the source Doc has no open-items list of its own — the same
pattern as mk-mb-devnote-3's CPRG substrate line. Carried as written.

**The source Doc gives no date anywhere in its text.** `curvenote.yml` uses
the Drive file's own creation date, 2026-10-12, checked the same day. The
other three DevNotes on this board all state a date inside the Doc itself;
this one does not.

**Dr. Mary Kelly's email differs from her other DevNotes on this board.**
This source gives marydkelly1@gmail.com. `devnote-mk-20260925-20260928`,
`mk-mb-devnote2` and `mk-mb-devnote-3` all give marykelly2026@u.northwestern.edu.
Carried exactly as this Doc states it; confirm which address is current
before publishing.

**One sentence in the Follow Up Experiment's Design section reads as
garbled in the source.** "Expression of deGFP causes membrane permeability
and TetR turns down expression. We used detergent-removed purified TetR at
two doses, and an in-house CF TetR preparation and aTc turns it back up
across four levels: 0, 0.025, 0.1 and 0.5 µM." Carried exactly as written;
the clause structure does not fully parse.

**The Follow Up Experiment's Design table numbers conditions starting at
3**, with no conditions 1 or 2 shown anywhere in this Doc. Carried as
supplied — likely numbered against a larger pilot not included here.

**The Plasmids and proteins table carried Google Docs export artifacts
(`\#\#\#`, `\*\*`) around every cell in the source pull.** Removed here as
a formatting fix; no value, unit, or row changed.

**Both plasmid files are reused verbatim from this board's sibling
DevNotes, not built fresh here.** `dna/pOpen-TetO-PLA.gb` is taken from
`devnote/mk-mb-devnote2`'s `dna/pOpen-TetO-PLA.gb`; `dna/pOpen-TetO-deGFP.gb`
is taken from `devstudio/devnote-mk-20260925-20260928`'s
`dna/pOpen-TetO-deGFP.gb`. Both carry the open items already recorded in
those DevNotes — neither file is in the canonical `nucleus-eng/DNA` repo,
and neither sibling branch is merged to `main` yet. Drive this devnote's
own {ref}`seqviz-popen-teto-pla` and {ref}`seqviz-popen-teto-degfp`.
::: -->

# Abstract

This experiment moves PLA1 expression inside the vesicle. Rather than expressing phospholipase in bulk and delivering it to the outside of pre-formed GUVs, the complete cell-free reaction is co-encapsulated with β-galactosidase, so that transcription, translation and any resulting membrane damage all occur within the compartment. Lysis is read as CPRG conversion by β-galactosidase escaping into the external volume.

Sixteen reactions cover four axes at once. The first is the construct: no DNA, deGFP, and PLA1 at 0.5 nM and 1 nM. The second is repression: TetR supplied at 100 nM from the MedChemExpress preparation, from the same preparation after detergent removal, or from in-house cell-free expression run overnight or for 1 h. The third is the sham: cell-free expressed deGFP substituted volume-for-volume wherever a cell-free TetR preparation is used, so the effect of adding a finished cell-free reaction is controlled independently of the repressor it contains. The fourth is induction: every condition is split across 0 and 1 µM aTc.

Each reaction is encapsulated separately, the vesicle pellet is resuspended in 100 µL, mixed 1:1 with PEG-NB precursor, dispensed at 20 µL per well and crosslinked under blue light. CPRG and aTc are then delivered together in a single 2 µL addition to the well exterior, and absorbance at 575 nm is followed over time. Sixteen conditions in triplicate at two aTc levels fill 96 wells.

The detergent-removal and sham arms are direct responses to the preceding experiment, in which adding the MedChemExpress TetR preparation raised CPRG conversion in wells containing no phospholipase at all. The headline result here is separate from both: protein expression by itself appears to lyse vesicles, and a follow-up experiment addressing that finding is reported at the end of this document.

# Overview

**Why move expression inside.** Delivering a finished cell-free reaction to the outside of a vesicle brings everything in that reaction to the membrane at once — salts, unconsumed substrates, surfactant-active proteins and whatever buffer the added protein came in. Co-encapsulation removes that bolus entirely. The only thing crossing the membrane from outside is CPRG and aTc, both small molecules added in 2 µL. Anything that happens to the membrane now originates inside the compartment.

**The readout, inverted.** Because β-galactosidase and CPRG now start on opposite sides of the membrane, conversion requires the two to meet. An intact vesicle keeps them apart; a breached one lets β-galactosidase into the external volume where CPRG is waiting. Absorbance at 575 nm therefore rises only as vesicles fail, and the hydrogel holds each vesicle in place while that happens.

**Three sources of TetR.** The MedChemExpress preparation is used as supplied and after detergent removal, since Tween 80 in its storage buffer is the leading explanation for the repressor-associated conversion seen previously. Alongside both, TetR expressed in-house by cell-free reaction is supplied as 3 µL of an overnight or 1 h reaction. That route avoids the commercial buffer altogether, but introduces a different confound — a finished cell-free reaction is itself a complex addition — which is what the shams control for.

**The shams.** Wherever a cell-free TetR preparation is added, a matched condition receives 3 µL of a cell-free deGFP reaction instead. Both the overnight and the 1 h sham are deGFP. These pairs isolate the repressor from its vehicle: if a TetR condition and its deGFP sham behave identically, the signal belongs to the act of adding an expressed reaction, not to repression.

**Two PLA1 doses.** PLA1 is run at 0.5 nM and 1 nM plasmid. If lysis is driven by phospholipase, the higher dose should lyse faster or more completely; if the two doses are indistinguishable, the signal is more likely coming from expression itself than from the product.

**aTc added from outside.** Induction is delivered after crosslinking, in the same 2 µL as the CPRG. aTc is small and membrane-permeable, so it should reach TetR in the lumen, but the kinetics of that crossing are not characterised here and induction is necessarily slower than it would be in bulk.

**What a successful run looks like.** Conversion from the PLA1 conditions clearly above the deGFP conditions at matched expression level; a dose difference between 0.5 nM and 1 nM PLA1; TetR conditions held below their constitutive counterparts and restored by aTc; and each cell-free TetR condition separated from its deGFP sham. Detergent-removed TetR should sit below untreated TetR in the no-DNA and deGFP arms if Tween 80 was the earlier culprit.

# Materials

## Plasmids and proteins

:::{table} Plasmids and proteins.
:label: tbl-plasmids-proteins
:align: center

| Item | Working stock | Final in reaction | Role |
| --- | --- | --- | --- |
| pOpen-PLA | 12.5 nM / 25 nM / 50 nM | 0.5 or 1 nM | Phospholipase A1 |
| pOpen-deGFP | 25 nM | 1 nM | Non-lytic expression control |
| TetR-His (MedChemExpress) | 1 µM | 100 nM | Repressor, as supplied |
| TetR-His, detergent-removed | 1 µM | 100 nM | Same, after Tween-removal column |
| CF TetR, ON and 1 h | — | 3 µL per reaction | Repressor without commercial buffer |
| CF deGFP, ON and 1 h | — | 3 µL per reaction | Sham for the above |
| β-galactosidase (LacZ) | see open items | 0.5 µL per reaction | Lysis reporter, co-encapsulated |
:::

Three plasmid stocks are used so that a fixed small volume delivers the intended final concentration in each block of conditions. Plasmid maps for both constructs are in {ref}`Plasmid maps <plasmid-maps>`.

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

## Cell-free system

:::{table} Cell-free system, per 25 µL reaction.
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
| LacZ | 0.5 | 2.0% |
| **Master mix total** | **21.5** | **86%** |
:::

β-galactosidase is carried in the master mix here, since every condition is encapsulated and every vesicle needs the reporter.

## Reagents, consumables and equipment

- CPRG, 5 mM stock — chromogenic β-galactosidase substrate, read at 575 nm
- Anhydrotetracycline (aTc), 10 µM stock, delivered with the CPRG — light-sensitive, keep foiled
- Detergent-removal spin columns for the TetR-His preparation
- PEG-norbornene precursor with crosslinker and photoinitiator, blue-light curable
- Lipid films for GUV formation, 16 required — one per condition
- Outer solution and inner-solution components as in the preceding GUV protocols
- Mineral oil, BioUltra; BSA 2% w/v; nuclease-free water
- Blue light source for PEG-NB crosslinking
- Refrigerated microcentrifuge, 18,000 rcf at 4 °C; 37 °C incubation
- 384-well plate and plate reader capable of 575 nm absorbance kinetics

# Protocol

## Part 1 — Assemble the sixteen reactions

All sixteen share one master mix ({ref}`tbl-part1-mastermix`). The variable additions are plasmid, and either a purified TetR preparation or 3 µL of a finished cell-free reaction, listed in {ref}`tbl-part1-conditions` and {ref}`tbl-part1-additions`.

### Conditions

:::{table} Part 1 conditions.
:label: tbl-part1-conditions
:align: center

| # | Condition | DNA | Added protein |
| --- | --- | --- | --- |
| 1 | No DNA | — | — |
| 2 | No DNA + TetR | — | 100 nM MedChem TetR |
| 3 | No DNA + TetR, Tween-removed | — | 100 nM MedChem TetR, detergent-removed |
| 4 | deGFP constitutive | 1 nM deGFP | — |
| 5 | deGFP + TetR | 1 nM deGFP | 100 nM MedChem TetR |
| 6 | deGFP + TetR, Tween-removed | 1 nM deGFP | 100 nM MedChem TetR, detergent-removed |
| 7 | PLA constitutive, low | 0.5 nM PLA | — |
| 8 | PLA constitutive, high | 1 nM PLA | — |
| 9 | PLA low + TetR | 0.5 nM PLA | 100 nM MedChem TetR |
| 10 | PLA low + TetR, Tween-removed | 0.5 nM PLA | 100 nM MedChem TetR, detergent-removed |
| 11 | PLA high + TetR | 1 nM PLA | 100 nM MedChem TetR |
| 12 | PLA high + TetR, Tween-removed | 1 nM PLA | 100 nM MedChem TetR, detergent-removed |
| 13 | PLA + overnight cell-free TetR | 1 nM PLA | 3 µL overnight cell-free TetR |
| 14 | PLA + overnight sham | 1 nM PLA | 3 µL overnight cell-free deGFP |
| 15 | PLA + 1 h cell-free TetR | 1 nM PLA | 3 µL 1 h cell-free TetR |
| 16 | PLA + 1 h sham | 1 nM PLA | 3 µL 1 h cell-free deGFP |
:::

Conditions 14 and 16 are both deGFP shams, matched in volume and expression time to the TetR preparations in 13 and 15.

### Variable additions, µL per 25 µL reaction

:::{table} Part 1 variable additions.
:label: tbl-part1-additions
:align: center

| Conditions | DNA stock | DNA | TetR or sham | Water | Total with 21.5 MM |
| --- | --- | --- | --- | --- | --- |
| 1 | — | 0 | 0 | 3.5 | 25.0 |
| 2, 3 | — | 0 | 2.5 | 1.0 | 25.0 |
| 4–6 | 25 nM deGFP | 1.0 | 0 or 2.5 | 2.5 or 0 | 25.0 |
| 7, 9, 10 | 12.5 nM PLA | 1.0 | 0 or 2.5 | 2.5 or 0 | 25.0 |
| 8, 11, 12 | 25 nM PLA | 1.0 | 0 or 2.5 | 2.5 or 0 | 25.0 |
| 13–16 | 50 nM PLA | 0.5 | 3.0 | 0 | 25.0 |
:::

### Master mix batch

:::{table} Part 1 master mix batch.
:label: tbl-part1-mastermix
:align: center

| Component | 16 reactions (µL) | 18 reactions, with overage (µL) |
| --- | --- | --- |
| Smix | 120 | 135 |
| tRNA | 40 | 45 |
| Pmix | 48 | 54 |
| Ribosomes | 72 | 81 |
| RIM | 20.8 | 23.4 |
| Sucrose | 35.2 (54.4 mg) | 39.6 (61.2 mg) |
| LacZ | 8 | 9 |
| **Total** | **344** | **387** |
:::

Make the 18-reaction batch. Sixteen encapsulations plus pipetting loss will not come out of a 16-reaction mix.

### Steps

1. Prepare the cell-free TetR and deGFP reactions in advance — one pair run overnight, one pair run 1 h — so they are ready when the main reactions are assembled.
2. Pass an aliquot of the MedChemExpress TetR through a detergent-removal column. Keep the untreated stock alongside it.
3. Weigh out the solid sucrose for the batch and vortex it into the Smix until dissolved, then add tRNA, Pmix, ribosomes, RIM and LacZ in that order, at the fractions in {ref}`tbl-cellfree`.
4. Combine plasmid, protein addition and water for each condition in its own tube and pre-incubate 10 min at 37 °C so TetR can bind tetO before transcription starts.
5. Add 21.5 µL of master mix to each tube. Mix by gentle pipetting; do not vortex.
6. Hold on ice and encapsulate immediately — expression must start inside the vesicle, not in the tube.

:::{note}
Time from master mix to encapsulation is the critical variable here. Any expression that happens before the vesicles close is expression in bulk, and it is lost to the assay — or worse, it damages membranes during formation. Work cold, work in small batches, and record the elapsed time per condition so that a systematic drift across the sixteen can be spotted later.
:::

## Part 2 — Encapsulate each condition

1. Prepare 16 lipid films, one per condition, and dissolve each in mineral oil as in the preceding GUV protocols.
2. Add the assembled reaction to its cold lipid/oil mixture, vortex 30 s, and rest on ice 5 min.
3. Layer each emulsion over outer solution, rest on ice 5 min, then centrifuge 15 min at 18,000 rcf, 4 °C.
4. Remove the mineral oil and collect each vesicle pellet with a fresh tip.
5. Resuspend each pellet in 100 µL of outer solution. Keep the sixteen preparations separate from here on.

## Part 3 — Cast and crosslink the hydrogel

1. Add 100 µL of PEG-NB precursor to each 100 µL vesicle suspension, giving 200 µL per condition.
2. Dispense 20 µL per well. Each condition fills 6 wells — three without aTc and three with — consuming 120 µL and leaving 80 µL spare.
3. Crosslink under blue light for 60 seconds.
4. Confirm by eye or by microscopy that the gel has set and vesicles are still present before adding substrate.

## Part 4 — Add substrate and inducer, then read

CPRG and aTc are delivered together in one 2 µL addition, so that the clock starts at the same moment for substrate and induction.

:::{table} CPRG and aTc addition.
:label: tbl-part4-addition
:align: center

| Addition | Stock | Volume | Final in 22 µL well |
| --- | --- | --- | --- |
| CPRG | 5 mM | 2 µL | ≈0.45 mM |
| aTc (induced rows only) | 10 µM | 2 µL | ≈0.9 µM |
:::

1. Add 2 µL of 5 mM CPRG to the no-aTc wells, and 2 µL of 5 mM CPRG plus 10 µM aTc to the induced wells, per {ref}`tbl-part4-addition`.
2. Read absorbance at 575 nm kinetically. Seal the plate against evaporation before starting — an unsealed long read cost the in-solution arm of the preceding experiment.
3. Read long enough for the constitutive PLA conditions to separate from the deGFP conditions, and record the full kinetic trace rather than an endpoint.

### Plate layout, 384-well

Columns 3–18 carry conditions 1–16 in order, as in {ref}`tbl-part4-layout`. Rows C–E are the uninduced triplicate; rows F–H are the 1 µM aTc triplicate.

:::{table} Plate layout, 384-well.
:label: tbl-part4-layout
:align: center

| Rows | aTc | Columns 3–18 | Wells |
| --- | --- | --- | --- |
| C, D, E | none | Conditions 1–16, one per column | 48 |
| F, G, H | 1 µM | Conditions 1–16, one per column | 48 |
:::

96 wells total. 16 conditions × 3 replicates × 2 aTc states.

# Results

:::{figure} ./figures/fig1-lysis-no-dna.png
:label: fig-1-lysis-no-dna
:align: center
:width: 90%
CPRG conversion over time for no-DNA reactions co-encapsulated with β-galactosidase. n = 3 technical replicates. No DNA, No DNA + aTc and No DNA + 100 nM MedChemExpress TetR converted fastest and were indistinguishable from one another. The two conditions receiving TetR passed through a detergent-removal spin column converted slowest.
:::

:::{figure} ./figures/fig2-lysis-degfp.png
:label: fig-2-lysis-degfp
:align: center
:width: 90%
CPRG conversion at 575 nm over 5 h, 1 nM pOpen-TetO-deGFP encapsulated in all conditions. n = 3 technical replicates. Conversion was highest in the constitutive conditions, with and without aTc. Both TetR-containing conditions converted less, with untreated MedChemExpress TetR giving lower conversion than the detergent-removed preparation. Adding aTc to either repressed condition raised conversion, consistent with deGFP production itself driving vesicle leakage — maybe by protein adsorption to the inner leaflet, by osmotic change, or both.
:::

:::{figure} ./figures/fig3-degfp-vs-pla1.png
:label: fig-3-degfp-vs-pla1
:align: center
:width: 90%
CPRG conversion at 575 nm over 5 h, n = 3 technical replicates. Traces for 1 nM pOpen-TetO-deGFP and 1 nM pOpen-TetO-PLA are nearly superimposable, indicating that the signal reflects protein expression rather than PLA1 activity.
:::

:::{figure} ./figures/fig4-pla1-dose.png
:label: fig-4-pla1-dose
:align: center
:width: 90%
CPRG conversion at 575 nm over 5 h, n = 3 technical replicates. Raising pOpen-TetO-PLA from 0.5 nM to 1 nM increased conversion. Read alongside {ref}`fig-3-degfp-vs-pla1`, where a non-lytic protein at matched template concentration produced the same trace, the dose effect is attributable to expression load rather than to phospholipase activity.
:::

# Conclusion

Co-encapsulating the cell-free reaction changed what this assay measures. With the reaction inside the vesicle and only CPRG and aTc added from outside, the signal is no longer explicable by anything delivered to the membrane externally — and it is still there. The central finding is that protein expression by itself permeabilises these vesicles.

Three observations converge on it. deGFP and PLA1 at matched template concentration gave nearly identical traces ({ref}`fig-3-degfp-vs-pla1`), so the lytic readout does not distinguish a phospholipase from a fluorescent protein. Raising the PLA1 template from 0.5 nM to 1 nM raised conversion ({ref}`fig-4-pla1-dose`), and because the deGFP comparison rules out product identity, that dose effect tracks how much protein is being made rather than what it is. And within the deGFP series, repression lowered conversion while aTc induction restored it ({ref}`fig-2-lysis-degfp`) — the same ordering, driven by expression level alone.

This experiment therefore provides no evidence that PLA1 is lysing vesicles. Any lytic contribution it makes is below what expression alone produces, and the current design cannot resolve it. Candidate mechanisms for the expression effect are worth separating before anything else: the osmotic drop as nucleotides and amino acids are polymerised into macromolecules; nascent or misfolded protein associating with the inner leaflet; crowding and viscosity changes in the lumen; and depletion of a component contributing to membrane stability. The follow-up experiment is designed around that question.

One caveat on vocabulary: the readout is β-galactosidase reaching external CPRG, which reports loss of containment. Whether that is frank lysis or graded permeabilisation is not established here, and microscopy of the membrane channel would settle it.

# Follow Up Experiment

Designed in response to the finding above: if protein expression by itself permeabilises vesicles, then expression level should be the variable that controls it.

## Rationale

The preceding experiment could not separate phospholipase activity from expression, because deGFP and PLA1 produced the same traces at matched template concentration. This follow-up removes PLA1 from the question entirely and works only with deGFP, where no lytic product exists to confound the readout.

Expression of deGFP causes membrane permeability and TetR turns down expression. We used detergent-removed purified TetR at two doses, and an in-house CF TetR preparation and aTc turns it back up across four levels: 0, 0.025, 0.1 and 0.5 µM. If expression drives loss of containment, CPRG conversion should rise monotonically with aTc in every repressed condition and should be highest where repression is weakest.

## Design

Five conditions, all 1 nM pOpen-TetO-deGFP in SV vesicles, each split across four aTc levels in duplicate. 5 × 4 × 2 = 40 wells. See {ref}`tbl-followup-design`.

:::{table} Follow-up design.
:label: tbl-followup-design
:align: center

| # | Condition | Repression source | Dose | LacZ in IS | Films |
| --- | --- | --- | --- | --- | --- |
| 3 | SV 1 nM deGFP | none — constitutive reference | — | Yes | 1 |
| 4 | SV 1 nM deGFP + 100 nM TetR, spin column | MedChem TetR-His, detergent-removed | 100 nM | Yes | 1 |
| 5 | SV 1 nM deGFP + 500 nM TetR, spin column | MedChem TetR-His, detergent-removed | 500 nM | Yes | 1 |
| 6 | SV 1 nM deGFP + 2.5 µL overnight cell-free TetR | Overnight cell-free TetR | 2.5 µL | Yes | 1 |
| 7 | SV 1 nM deGFP + 2.5 µL overnight sham | Overnight cell-free deGFP | 2.5 µL | Yes | 1 |
:::

All five carry 1 nM pOpen-TetO-deGFP and one lipid film each. Conditions 4 and 5 are the same detergent-removed preparation at two doses, so the pair is a clean dose series rather than a treated-versus-untreated comparison. Condition 3 sets the unrepressed ceiling.

### Assembly, µL per 25 µL reaction

All five share one master mix, {ref}`tbl-followup-mastermix`.

:::{table} Follow-up assembly volumes.
:label: tbl-followup-assembly
:align: center

| Component | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- |
| Master mix (Smix, tRNA, Pmix, Rib, RIM, sucrose, LacZ) | 21.5 | 21.5 | 21.5 | 21.5 | 21.5 |
| DNA (25 nM pOpen-TetO-deGFP) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| TetR or sham | 0 | 2.5 | 1.25 | 2.5 | 2.5 |
| Water | 2.5 | 0 | 1.25 | 0 | 0 |
| **Total** | **25.0** | **25.0** | **25.0** | **25.0** | **25.0** |
:::

Purified TetR stocks differ by condition so that a convenient volume gives the intended dose: 1 µM for condition 4 (2.5 µL → 100 nM) and 10 µM for condition 5 (1.25 µL → 500 nM). LacZ is 250 U/mL stock, 0.5 µL per reaction, giving 5 U/mL in the lumen.

### Master mix, five reactions

:::{table} Follow-up master mix, five reactions.
:label: tbl-followup-mastermix
:align: center

| Component | Volume (µL) |
| --- | --- |
| Smix | 37.5 |
| tRNA | 12.5 |
| Pmix | 15 |
| Ribosomes | 22.5 |
| RIM | 6.5 |
| Sucrose | 11 (17 mg) |
| LacZ | 2.5 |
| **Total** | **107.5** |
:::

### Plate layout

Conditions 3–7 are plated across the four aTc levels in duplicate, per {ref}`tbl-followup-layout`.

:::{table} Follow-up plate layout.
:label: tbl-followup-layout
:align: center

| Rows | Condition | Cols 2–3 | Cols 4–5 | Cols 6–7 | Cols 8–9 |
| --- | --- | --- | --- | --- | --- |
| C | 3 — deGFP constitutive | 0 µM aTc | 0.25 µM | 1 µM | 5 µM |
| D | 4 — + 100 nM TetR | 0 µM aTc | 0.25 µM | 1 µM | 5 µM |
| E | 5 — + 500 nM TetR, spin column | 0 µM aTc | 0.25 µM | 1 µM | 5 µM |
| F | 6 — + 2.5 µL overnight cell-free TetR | 0 µM aTc | 0.25 µM | 1 µM | 5 µM |
| G | 7 — + 2.5 µL overnight sham | 0 µM aTc | 0.25 µM | 1 µM | 5 µM |
:::

Two wells per aTc level, so n = 2 technical replicates — one fewer than the preceding experiments.

# Results

:::{figure} ./figures/fig6-constitutive-degfp-atc-series.png
:label: fig-6-constitutive-degfp-atc-series
:align: center
:width: 90%
Kinetic absorbance at 575 nm over 14 h for constitutively expressed 1 nM pOpen-TetO-deGFP, with no TetR present, across the full aTc series. n = 2 technical replicates. Conversion was high in every well, and aTc concentration produced no systematic difference between traces.
:::

:::{figure} ./figures/fig7-repressed-degfp-atc-series.png
:label: fig-7-repressed-degfp-atc-series
:align: center
:width: 90%
Kinetic absorbance at 575 nm over 14 h for 1 nM pOpen-TetO-deGFP repressed with purified TetR: 100 nM (top panel) and 500 nM (bottom panel), both passed through the detergent-removal spin column before use. n = 2 technical replicates. Conversion rate rose with aTc concentration in both panels, giving a graded colorimetric response to inducer.
:::

:::{figure} ./figures/fig8-endpoint-abs-15h.png
:label: fig-8-endpoint-abs-15h
:align: center
:width: 90%
Endpoint absorbance at 575 nm after 15 h. n = 2 technical replicates. Constitutively expressed deGFP gave the highest conversion, and conversion rose with aTc concentration in both repressed conditions.
:::

:::{figure} ./figures/fig9-hydrogel-photos.png
:label: fig-9-hydrogel-photos
:align: center
:width: 90%
Hydrogels containing GUVs with 1 nM pOpen-TetO-deGFP repressed by 500 nM TetR, across increasing aTc. Color develops with aTc, consistent with aTc relieving repression, deGFP expression rising, the membrane permeabilising, and encapsulated β-galactosidase reaching external CPRG.
:::

:::{figure} ./figures/fig10-cf-tetr-sham-atc-series.png
:label: fig-10-cf-tetr-sham-atc-series
:align: center
:width: 90%
Kinetic absorbance at 575 nm over 14 h for cell-free expressed TetR (top panel) and the vehicle control (bottom panel). n = 2 technical replicates. Conversion rose with aTc concentration, with the largest change at 0.5 µM aTc.
:::

# Conclusion

This follow-up closes the loop on the preceding experiment, and {ref}`fig-6-constitutive-degfp-atc-series` is what makes the rest of it interpretable. In the constitutive condition, where no TetR is present and aTc has nothing to de-repress, conversion was uniformly high and unaffected by aTc concentration. aTc therefore does not drive CPRG conversion on its own — not by acting on the membrane, not by absorbing at 575 nm, not by any route independent of the repressor. Every aTc dose response elsewhere in this experiment is acting through TetR.

Against that baseline, the repressed conditions give a graded response. Conversion tracked aTc at both 100 nM and 500 nM purified TetR ({ref}`fig-7-repressed-degfp-atc-series`) and with cell-free expressed TetR ({ref}`fig-10-cf-tetr-sham-atc-series`), and the constitutive condition sat at the top of the range in the endpoint comparison ({ref}`fig-8-endpoint-abs-15h`). Because deGFP has no lytic activity of its own, the only thing aTc controls here is how much protein gets made. Expression level sets the rate of containment loss — inferred from template dose in the preceding experiment, demonstrated directly here.

That reframes the finding. Expression-driven permeabilisation is not only real but graded and controllable: a small molecule applied outside a crosslinked hydrogel produces a tunable colorimetric output from inside the vesicle. As a lysis assay for phospholipase that is a problem, since it sets a floor no PLA1 signal has yet cleared. As a reporter architecture it is a result in its own right — an inducible, dose-responsive release system needing no lytic enzyme at all.

The mechanism remains unresolved. Osmotic change as substrates are polymerised, nascent protein at the inner leaflet, lumenal crowding, and depletion of a stabilising component all remain live, and nothing here distinguishes them. Direct osmolarity measurement on expressed versus unexpressed reactions is still the cheapest discriminating experiment. Separately, any future attempt to measure PLA1 activity in this format will need to hold total protein synthesis constant between the PLA1 and control arms rather than matching template concentration.
