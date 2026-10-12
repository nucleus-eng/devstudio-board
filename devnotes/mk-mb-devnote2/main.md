<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

<!-- Drafted 2026-10-11 from the Google Doc "TetO-PLA For Triggered Lysis of
beta-Galactosidase-Loaded GUVs".
Source: https://docs.google.com/document/d/1vmAaYyH21pxErmB583Prsc-LUFs3JG34Y1ZjypEiRbI
Prose, tables, step lists, captions and the plasmid sequence are carried
verbatim from that Doc. The Doc's section order is kept, not the DevNote
template order. The Doc is a written protocol, and its steps refer to each
other by Part number. Reordering it breaks those references. -->

<!-- :::{admonition} Open items from the draft
:class: warning dropdown
:name: flags-review

**Authorship is carried from this author's sibling DevNote, not re-confirmed
here.** Name, email and affiliation (Mary Kelly, Northwestern University) are
copied from `devnotes/devnote-mk-20260925-20260928/curvenote.yml`, where Anton
Molina supplied them on 2026-10-04. The source Doc for this DevNote names no
author. Confirm this is the same Mary Kelly before publishing.

**The source numbers two different steps "5" in Part 3.** The blue-light
crosslinking step and the CPRG-addition step are both "5." in the Doc.
Renumbered here as steps 4 to 6, in the order the Doc lists them. Confirm this
is the intended sequence.

**One sentence in the Overview reads as garbled in the source.** "Why two
stages" opens: "a vesicle functions improperly may have, failed to lyse, or
lysed so early that nothing accumulated." Carried exactly as written; the
likely intended meaning is something like "a vesicle may have functioned
improperly, failed to lyse, or lysed so early that nothing accumulated."

**The Materials section's plasmids-and-proteins table carried Google Docs
export artifacts (`\#\#\#`, `\*\*`) around every cell in the source pull.**
Removed here as a formatting fix; no value, unit, or row changed.

**The source itself forward-references an item it never defines.** Materials
lists "beta-galactosidase substrate for the plate reader — see open items,"
but the source Doc has no open-items list of its own. Carried as written; the
substrate is CPRG per Part 3 step 5, but confirm that is what this line meant.

**Part 4 step 2 reads "Read kinetically at 37C," without the degree symbol or
space used everywhere else in the Doc (elsewhere: "37 °C").** Carried exactly
as written.

**`dna/pOpen-TetO-PLA.gb` was built here, not taken from a source of
record.** It carries this Doc's sequence byte for byte, with the five
features the Doc's own landmark column supports, and drives
{ref}`seqviz-popen-teto-pla`. `nucleus-eng/DNA`'s part-type directories
(`reporters`, `detectors`, `promoters`, `pores`, `emitters`, `control`,
`assembly`, `PURE`, `RBS`, `terminators`, `energy`) were listed on 2026-10-11;
none names a PLA1 or phospholipase construct, so no canonical match exists for
the full plasmid.

The PLA1 CDS (bases 104 to 1075 here) translates identical, byte for byte, to
the PLA1 CDS already in this board's
`devnotes/devnote-op-20261001-luv-gel-pla/dna/t7pro-esao-ls1-pla1.gbk`
(translation `MSMSLSFTSAIAPAAIQPP...ANA`, 323 aa) — same enzyme, under a
different promoter (EsaO/R quorum-sensing there, T7/tetO here). That file is
itself not yet in `nucleus-eng/DNA`. So the PLA1 part is shared with an
in-flight sibling DevNote on this board, but the full `pOpen-TetO-PLA`
plasmid has no file of record anywhere. `devstudio-verify-dna-constructs` was
run against the canonical repo only; no construct-to-file identity claim
beyond the CDS match above is made.

**This DevNote's directory name does not follow the board's
`devnote-<initials>-<daterange>` convention.** The source Doc gives no
experiment date distinct from its own 2026-10-11 drafting date, so there is no
date range to name it with. Named `mk-mb-devnote2` and branched as
`devnote/mk-mb-devnote2` on direct instruction; rename both if a dated slug is
preferred once the experiment date is confirmed.

**No notebook, platemap, or raw instrument file is referenced anywhere in the
source Doc**, unlike the sibling `devnote-mk-20260925-20260928`. There is
nothing to place in `experiments/`, and no Resources section is added here for
that reason.
::: -->

# Abstract

We ask whether phospholipase A1 (PLA1) produced in a cell-free reaction can lyse giant unilamellar vesicles (GUVs) when supplied from the outside, and whether that lytic activity can be placed under TetR/anhydrotetracycline (aTc) control. The assay is deliberately split into two stages so that expression and lysis are measured independently: PLA1 is expressed first, in bulk, and only then delivered to pre-formed vesicles.

In stage one, four plasmids — PJL-PLA, pOpen-PLA, pOpen-deGFP and a no-DNA control — are each run in three regulatory states: expressed (no TetR), repressed (1000 nM TetR), and induced (1000 nM TetR plus 1 µM aTc). The twelve 25 µL reactions proceed for 3 h at 37 °C.

In stage two, 4 µL of each finished reaction is added to the outside of GUVs loaded with β-galactosidase. Lysis is read as the appearance of β-galactosidase activity in the external volume, since the enzyme is released only when the membrane is breached. Each condition is tested in two environments in parallel — vesicles free in outer solution, and vesicles embedded in PEG-NB hydrogel cast in 1 M HEPES — to ask whether a surrounding matrix protects the membrane from an externally supplied lytic enzyme. All twelve conditions are run in triplicate in each environment, filling 72 wells of a 384-well plate.

The pOpen-deGFP arm reports on the cell-free reaction itself, confirming that expression occurred and that TetR repression and aTc induction behaved as expected in the same master mix that drove the PLA1 arms. A separate control supplies purified TetR protein directly to the vesicle exterior, testing whether the protein preparation perturbs membranes on its own.

# Overview

**Why two stages.** Expressing PLA1 inside the same compartment it is meant to lyse confounds the two events: a vesicle functions improperly may have, failed to lyse, or lysed so early that nothing accumulated. Running expression to completion in bulk first, then delivering a fixed 4 µL dose to intact vesicles, separates the question "was the enzyme made?" from the question "does the enzyme lyse the membrane?"

**The reporter.** GUVs are loaded with β-galactosidase (LacZ) in the inner solution. Intact vesicles keep the enzyme sequestered; a breached membrane releases it into the external volume where it meets its substrate. The readout is therefore a gain of signal on lysis, with the vesicle acting as its own negative control until the moment it fails.

**The genetic circuit.** Both PLA constructs place the coding sequence downstream of a tetO operator, so purified TetR blocks transcription and aTc relieves that block. Two backbones are compared: PJL-PLA and pOpen-PLA. The three states per plasmid give the full regulatory picture in one pass — the expressed arm sets the maximum lytic activity available, the repressed arm asks how tight the off state is, and the induced arm asks how much of the expressed activity aTc can recover.

**Solution versus hydrogel.** The same GUV preparation is assayed free in outer solution and embedded in PEG-NB hydrogel. The hydrogel is cast in 1 M HEPES, and the vesicle inner solution is built to match it osmotically (≈397 mM sucrose plus ≈892 mM HEPES). Comparing the two environments asks whether the matrix slows the arrival of enzyme at the membrane, mechanically supports vesicles that would otherwise burst, or has no effect at all.

**Controls.** pOpen-deGFP runs the circuit without a lytic product, so any signal it produces in the lysis readout is background rather than enzymatic membrane damage. The no-DNA arm reports what the cell-free mix alone does to vesicles — a 4 µL addition of a concentrated reaction brings salts, PEG, detergent-like components and surfactant-active proteins to the membrane, and some vesicle loss from that alone is expected. Externally supplied TetR tests the purified protein prep separately.

**What a successful run looks like.** β-galactosidase release from both PLA constructs in their expressed state, clearly above the deGFP and no-DNA arms; little or no release from the repressed arms; and release from the induced arms that recovers a substantial share of the expressed signal. The deGFP arm should show the expected repression and induction in its own fluorescence channel, confirming the circuit worked in the reactions that fed the assay.

# Materials

::::{admonition} Lipids (in chloroform)
:class: dropdown

:::{table} Lipids, as supplied in chloroform.
:label: tbl-lipids
:align: center

| Amphiphile | MW (g/mol) | Stock (mg/mL) | Stock (mM) | Role | Vendor / cat. |
| --- | --- | --- | --- | --- | --- |
| POPC | 760.09 | 25 | 32.9 | Bulk bilayer lipid | Avanti |
| Cholesterol (ovine) | 386.7 | 19.3 | 50 | Membrane stability | Avanti |
| 18:1 Liss Rhod PE | 1301.7 | 1 | 0.77 | Membrane fluorophore | Avanti |
:::
::::

::::{admonition} Cell-free expression system
:class: dropdown

Components are the OnePot PURE-style sub-mixes; each is dispensed as a fixed fraction of the reaction volume.

:::{table} Cell-free sub-mixes, as a fraction of reaction volume.
:label: tbl-cellfree
:align: center

| Component | Fraction of reaction | Notes |
| --- | --- | --- |
| Solution mix (Smix) | 30% | Energy, amino acids, salts, buffer |
| Ribosomes (Rib) | 18% | — |
| Protein mix (Pmix) | 12% | Translation factors, aaRS, T7 RNAP |
| tRNA | 10% | — |
| RNase inhibitor, murine (RIM) | 5.2% | — |
| **Total master mix** | **84%** | Remainder is DNA, TetR, and water |
:::
::::

::::{admonition} Plasmids and proteins
:class: dropdown

:::{table} Plasmids and proteins.
:label: tbl-plasmids-proteins
:align: center

| Item | Working stock | Final in reaction | Role |
| --- | --- | --- | --- |
| PJL-PLA | 25 nM | 1 nM | Phospholipase A1, backbone 1 |
| pOpen-PLA | 25 nM | 1 nM | Phospholipase A1, backbone 2 |
| pOpen-deGFP | 25 nM | 1 nM | Non-lytic expression control |
| TetR, His-tagged (MedChemExpress) | 10 µM | 1000 nM | Repressor |
| β-galactosidase (LacZ) | 250 U/mL | 5 U/mL | GUV cargo, lysis reporter |
:::
::::

:::{admonition} Lipids, buffers and small molecules
:class: dropdown

- Lipid film for GUV formation — as in the deGFP GUV protocol (9:1 POPC:cholesterol with fluorescent lipid), 8 films for this experiment
- Anhydrotetracycline (aTc), 1 µM final in the induced reactions — light-sensitive, keep foiled
- CPRG, 0.5 mM final in the final reactions — light-sensitive, keep foiled
- Sucrose, solid and as 400 mM stock
- HEPES, 1 M stock — both the GUV inner solution and the hydrogel are built on this
- PEG-norbornene (PEG-NB) with crosslinker and photoinitiator, cast in 1 M HEPES
- Outer solution — as in the deGFP GUV protocol (glucose/HEPES, osmotically matched to the inner solution)
- β-galactosidase substrate for the plate reader — see open items
- Bovine serum albumin (BSA), 2% w/v, for glass passivation
- BioUltra mineral oil; chloroform for lipid handling; nuclease-free water
:::

:::{admonition} Consumables and equipment
:class: dropdown

- Glass vials with PTFE-lined caps, Hamilton glass syringes, low-retention tips
- 384-well plate suited to the chosen β-galactosidase readout; glass-bottom plate if imaging in parallel
- Nitrogen line, vacuum oven, 80 °C hot plate, vortex, ice
- Refrigerated microcentrifuge capable of 18,000 rcf at 4 °C
- 37 °C incubator or thermocycler block for the 3 h expression step
- Blue light for PEG-NB crosslinking
- Plate reader with the 575 Abs
:::

# Stocks to prepare in advance

Prepare these before the day of the experiment; everything after the lipid film is time-sensitive.

:::{table} Stocks to prepare before the day of the experiment.
:label: tbl-stocks
:align: center

| Stock | Concentration | Storage | Notes |
| --- | --- | --- | --- |
| Glucose | 2 M | RT | Outer solution component |
| HEPES | 1 M, pH 7.6 | 4 °C | Outer solution buffer |
| Sucrose | 400 mM | 4 °C | Inner solution osmolyte |
| BSA | 2% w/v in water | 4 °C | Glass passivation, make fresh weekly |
| aTc | 5000 uM | −20 °C, dark | Light-sensitive; wrap in foil |
| Plasmid | 100 nM in nuclease-free water | −20 °C | — |
| TetR | ~10 µM | −80 °C, single-use aliquots | Avoid freeze-thaw |
| CPRG | 10 mM | −20 °C | Light-sensitive; wrap in foil |
:::

Lipid films can be dried the day before and left under vacuum overnight.

# Part 1 — Express or repress the plasmids, 3 h at 37 °C

Twelve 25 µL reactions: four plasmids × three regulatory states. All twelve take the same master mix, so it is batched once and split.

## Conditions

:::{table} Part 1 conditions.
:label: tbl-part1-conditions
:align: center

| # | Plasmid | State | TetR | aTc |
| --- | --- | --- | --- | --- |
| 1 | PJL-PLA | Expressed | 0 nM | — |
| 2 | PJL-PLA | Repressed | 1000 nM | — |
| 3 | PJL-PLA | Induced | 1000 nM | 1 µM |
| 4 | pOpen-PLA | Expressed | 0 nM | — |
| 5 | pOpen-PLA | Repressed | 1000 nM | — |
| 6 | pOpen-PLA | Induced | 1000 nM | 1 µM |
| 7 | pOpen-deGFP | Expressed | 0 nM | — |
| 8 | pOpen-deGFP | Repressed | 1000 nM | — |
| 9 | pOpen-deGFP | Induced | 1000 nM | 1 µM |
| 10 | No DNA | Expressed | 0 nM | — |
| 11 | No DNA | Repressed | 1000 nM | — |
| 12 | No DNA | Induced | 1000 nM | 1 µM |
:::

All reactions carry 1 nM plasmid except the no-DNA arms.

## Assembly, volumes in µL per reaction

:::{table} Part 1 assembly volumes.
:label: tbl-part1-assembly
:align: center

| Component | Expressed (0 TetR) | Repressed / Induced (1000 nM TetR) |
| --- | --- | --- |
| Smix | 7.5 | 7.5 |
| tRNA | 2.5 | 2.5 |
| Pmix | 3.0 | 3.0 |
| Ribosomes | 4.5 | 4.5 |
| RIM | 1.3 | 1.3 |
| Sucrose | 2.2 | 2.2 |
| *Master mix subtotal* | *21.0* | *21.0* |
| Plasmid DNA (25 nM) | 1.0 | 1.0 |
| TetR | 0 | 3.0 |
| Nuclease-free water | 3.0 | 0 |
| **Total** | **25.0** | **25.0** |
:::

aTc is added to the induced reactions only, to 1 µM final, within the water or TetR allowance.

:::{note}
Scale these reactions up before you run them. Each condition feeds 6 wells at 4 µL, which is 24 µL out of a 25 µL reaction — 1 µL of headroom, or 4%. One slow pipette and the last well is short. Making 30 µL instead gives 6 µL of headroom (20%) at the same component fractions: Smix 9.0, tRNA 3.0, Pmix 3.6, Rib 5.4, RIM 1.56, sucrose 2.64 (master mix 25.2), DNA 1.2, TetR 3.6, water 3.6 or 0. This matches the 30 µL figure already written at the head of your reaction sheet.
:::

## Steps

1. Thaw cell-free components on ice and keep them there throughout.
2. Weigh out the solid sucrose for the batch and vortex it into the Smix until fully dissolved, then add tRNA, Pmix, ribosomes and RIM in that order.
3. Combine plasmid DNA, TetR and water for each condition in its own tube and incubate 10 min at 37 °C, so TetR binds tetO before transcription can start. The expressed and no-DNA arms carry water only but go through the same incubation.
4. Add aTc to the induced tubes to 1 µM final.
5. Add 21 µL of master mix to each pre-incubated tube. Mix by gentle pipetting; do not vortex the assembled reaction.
6. Incubate 3 h at 37 °C. Hold on ice afterwards and use the same day.
7. Reserve an aliquot of each deGFP reaction to read GFP fluorescence directly, confirming expression and repression in this batch.

# Part 2 — Prepare β-galactosidase-loaded GUVs

The inner solution is built on 1 M HEPES so that it matches the hydrogel the vesicles will sit in. Eight lipid films supply the 720 µL of resuspended GUVs this plate consumes.

## Inner solution, 200 µL

:::{table} GUV inner solution, 200 µL.
:label: tbl-inner-solution
:align: center

| Component | Amount | Resulting concentration |
| --- | --- | --- |
| Sucrose (solid) | 27.2 mg, ≈17.6 µL | ≈397 mM |
| HEPES, 1 M | 178.4 µL | ≈892 mM |
| β-galactosidase (LacZ) | 4 µL | 5 U/mL |
| **Total** | **200 µL** | — |
:::

This pairs with the outer solution from the deGFP GUV protocol (400 mM glucose, 800 mM HEPES) and with PEG-NB cast in 1 M HEPES, so all three phases sit at comparable osmolarity.

## Steps

1. Prepare 8 lipid films and dissolve each in 200 µL mineral oil as in the deGFP GUV protocol.
2. Add 20 µL of the β-galactosidase inner solution to each cold lipid/oil mixture. Vortex 30 s, then rest on ice 5 min.
3. Layer each emulsion over 100 µL outer solution and rest on ice 5 min.
4. Centrifuge 15 min at 18,000 rcf, 4 °C.
5. Remove the mineral oil, collect each pellet with a fresh tip, and pool the eight preparations.
6. Resuspend to 720 µL total in outer solution. Keep on ice.
7. Before plating, confirm by microscopy that vesicles are intact and that the β-galactosidase is inside rather than free in the suspension — a leaky preparation will read as lysis in every well.

# Part 3 — Plate the vesicles in solution and in hydrogel

Each well receives 10 µL of GUV suspension plus 10 µL of either outer solution or PEG-NB precursor. Columns 3–5 are the hydrogel arm; columns 6–8 are the solution arm.

## Plate layout, 384-well

:::{table} Plate layout, 384-well.
:label: tbl-plate-layout
:align: center

| Row | Condition | Cols 3–5: PEG-NB in 1 M HEPES | Cols 6–8: Outer solution |
| --- | --- | --- | --- |
| C | 1 — PJL-PLA Expressed | ✓ ✓ ✓ | ✓ ✓ ✓ |
| D | 2 — PJL-PLA Repressed | ✓ ✓ ✓ | ✓ ✓ ✓ |
| E | 3 — PJL-PLA Induced | ✓ ✓ ✓ | ✓ ✓ ✓ |
| F | 4 — pOpen-PLA Expressed | ✓ ✓ ✓ | ✓ ✓ ✓ |
| G | 5 — pOpen-PLA Repressed | ✓ ✓ ✓ | ✓ ✓ ✓ |
| H | 6 — pOpen-PLA Induced | ✓ ✓ ✓ | ✓ ✓ ✓ |
| I | 7 — pOpen-deGFP Expressed | ✓ ✓ ✓ | ✓ ✓ ✓ |
| J | 8 — pOpen-deGFP Repressed | ✓ ✓ ✓ | ✓ ✓ ✓ |
| K | 9 — pOpen-deGFP Induced | ✓ ✓ ✓ | ✓ ✓ ✓ |
| L | 10 — No DNA Expressed | ✓ ✓ ✓ | ✓ ✓ ✓ |
| M | 11 — No DNA Repressed | ✓ ✓ ✓ | ✓ ✓ ✓ |
| N | 12 — No DNA Induced | ✓ ✓ ✓ | ✓ ✓ ✓ |
:::

12 conditions × 3 replicates × 2 environments = 72 wells, consuming 720 µL of GUV suspension.

## Steps

1. Block the wells with 2% w/v BSA for at least 20 min, then remove and rinse with outer solution.
2. Dispense 10 µL of GUV suspension per well, mixing the stock gently between rows so vesicles do not settle out of the pipette.
3. Add 10 µL of PEG-NB precursor to columns 3–5 and 10 µL of outer solution to columns 6–8.
4. Crosslink the hydrogel columns under blue light. Hold under blue light for 60 seconds to crosslink.
5. Add 2 µL of 5 mM CPRG per well for a final concentration of ~0.5 mM.
6. Let the plate equilibrate to the read temperature before adding enzyme.

# Part 4 — Deliver the cell-free reactions and read lysis

1. Add 4 µL of the matching 3 h cell-free reaction to the outside of each well, following the layout above.
2. Read kinetically at 37C and at absorbance 575 nm.
3. Read for long enough to separate the no-DNA background from genuine lysis — the background rises slowly as the cell-free addition perturbs membranes, while enzymatic lysis should appear as a faster, earlier rise.

# Plasmid reference — pOpen-TetO-PLA

The expression cassette places the *tetO* operator immediately downstream of the T7 promoter, so bound TetR occludes the polymerase at initiation rather than acting as a roadblock during elongation.

:::{table} Elements of pOpen-TetO-PLA.
:label: tbl-plasmid-reference
:align: center

| Element | Sequence landmark | Function |
| --- | --- | --- |
| T7 promoter | TAATACGACTCACTATAGGG | Transcription start, T7 RNAP |
| *tetO* operator | TCCCTATCAGTGATAGAGA | TetR binding site; aTc-releasable |
| T7 g10 leader + RBS | AAGGAGATATACAT | Ribosome binding |
| PLA CDS | atgtctatgtcactgtcttttacatcggctatc… | Lytic Enzyme |
| T7 terminator | …tagagaccgagataacagatacttcggtatctgttatctgtt | Transcription stop |
| AmpR (*bla*) | — | Selection marker |
| pUC origin | — | Plasmid replication |
:::

The terminator and backbone sequences are not transcribed in the cell-free reaction, but the full sequence is kept here so the construct is traceable from the protocol.

(seqviz-popen-teto-pla)=

:::{seqviz} ./dna/pOpen-TetO-PLA.gb
:::

<!-- The map above is built from this Doc's own sequence and its own landmark
column. Each feature is placed by searching the sequence for the landmark
string the table gives, so no coordinate is asserted by hand. The table also
names AmpR and the pUC origin, with a dash in place of a landmark, so neither
is annotated. -->

<!-- Positions measured against the sequence below on 2026-10-11: total
3140 bp; T7 promoter at base 5; tetO operator at base 26; g10 leader and RBS
at base 90; PLA1 CDS 104 to 1075, which is 972 nt and 323 codons plus stop;
T7 terminator at base 1076. The CDS translates identical to the PLA1 CDS in
devnotes/devnote-op-20261001-luv-gel-pla/dna/t7pro-esao-ls1-pla1.gbk; see
Open items. No file carrying the full pOpen-TetO-PLA plasmid was found in
nucleus-eng/DNA. -->

:::{admonition} Full sequence
:class: dropdown

```
ggagTAATACGACTCACTATAGGGATCCCTATCAGTGATAGAGAGACCACAACGGTTTCC
CTCTAGAAATAATTTTGTTTAACTTTAAGAAGGAGATATACATatgtctatgtcactgtc
ttttacatcggctatcgcgcccgctgctattcaaccgccaatggtccgtacacagccgga
accgttgtcctctagtcagcctgtggaagcgagcgctacaaaagcccctgtcgcaaccct
gagtcagaactccctcaatgcccaatcattgctcaataccctcgtctccgaaatctctgc
cgccgctccggcggcagctaatcaaggagtcacgcgcgggcagcagccacagaaaggaga
ctatactttggcgctgctcgctaaagatgtttattcaaccggttcacagggtgtcgaagg
gttcaaccgcctgtcagctgatgcgttgttaggagcaggtatagatccggcaagtctgca
ggacgccgcttccggctttcaagcagggatttatacggataaccagcagtacgttcttgc
ttttgctgggaccaatgatatgcgagattggttgagcaacgtccgtcaagcgaccggata
cgacgatgtacagtataatcaggctgtcagcttggcaaaatctgctaaagccgccttcgg
cgacgcgcttgttattgccggccatagcttagggggcggcctcgccgcaacggctgcatt
ggctacagggactgtggctgttacttttaacgcagctggggtgtcagattatacgcttaa
tcgtatgggaattgaccctgcggcagccaaacaggatgcccaggccggtgggatccgtcg
ctatagcgaacaatacgatatgcttactgggacacaagaatcaacaagcctcatcccaga
cgctattggtcataaaattaccttagcgaacaacgatacattgagtggcattgatgactg
gcgtccctcaaaacacctggatcgttcactgactgcacatggtatcgataaagttatctc
gagtatggcggaacagaagccgtgggaagcaatggccaacgcatgatgaagagcttagag
accgagataacagatacttcggtatctgttatctgttttttttctaagcatcacactgcc
gtccgctgaggtgtcaatcgtcggagccgctgagcaataactagcataaccccttggggc
ctctaaacgggtcttgaggggttttttgcatggtcatagctgtttcctgagagcttggca
ggtgatgacacacattaacaaatttcgtgaggagtctccagaagaatgccattaatttcc
ataggctccgcccccctgacgagcatcacaaaaatcgacgctcaagtcagaggtggcgaa
acccgacaggactataaagataccaggcgtttccccctggaagctccctcgtgcgctctc
ctgttccgaccctgccgcttaccggatacctgtccgcctttctcccttcgggaagcgtgg
cgctttctcatagctcacgctgtaggtatctcagttcggtgtaggtcgttcgctccaagc
tgggctgtgtgcacgaaccccccgttcagcccgaccgctgcgccttatccggtaactatc
gtcttgagtccaacccggtaagacacgacttatcgccactggcagcagccactggtaaca
ggattagcagagcgaggtatgtaggcggtgctacagagttcttgaagtggtggcctaact
acggctacactagaagaacagtatttggtatctgcgctctgctgaagccagttaccttcg
gaaaaagagttggtagctcttgatccggcaaacaaaccaccgctggtagcggtggttttt
ttgtttgcaagcagcagattacacgcagaaaaaaaggatctcaagaaggcctactattag
caacaacgatcctttgatcttttctacggggtctgacgctcagtggaacgaaaactcacg
ttaagggattttggtcatgagattatcaaaaaggatcttcacctagatccttttaaatta
aaaatgaagttttaaatcaatctaaagtatatatgagtaaacttggtctgacagttacca
atgcttaatcagtgaggcacctatctcagcgatctgtctatttcgttcatccatagttgc
ctgactccccgtcgtgtagataactacgatacgggagggcttaccatctggccccagtgc
tgcaatgataccgcgagaaccacgctcaccggctccagatttatcagcaataaaccagcc
agccggaagggccgagcgcagaagtggtcctgcaactttatccgcctccatccagtctat
taattgttgccgggaagctagagtaagtagttcgccagttaatagtttgcgcaacgttgt
tgccattgctacaggcatcgtggtgtcacgctcgtcgtttggtatggcttcattcagctc
cggttcccaacgatcaaggcgagttacatgatcccccatgttgtgcaaaaaagcggttag
ctccttcggtcctccgatcgttgtcagaagtaagttggccgcagtgttatcactcatggt
tatggcagcactgcataattctcttactgtcatgccatccgtaagatgcttttctgtgac
tggtgagtactcaaccaagtcattctgagaatagtgtatgcggcgaccgagttgctcttg
cccggcgtcaatacgggataataccgcgccacatagcagaactttaaaagtgctcatcat
tggaaaacgttcttcggggcgaaaactctcaaggatcttaccgctgttgagatccagttc
gatgtaacccactcgtgcacccaactgatcttcagcatcttttactttcaccagcgtttc
tgggtgagcaaaaacaggaaggcaaaatgccgcaaaaaagggaataagggcgacacggaa
atgttgaatactcatactcttcctttttcaatattattgaagcatttatcagggttattg
tctcatgagcggatacatatttgaatgtatttagaaaaataaacaaataggggttccgcg
cacctgcaccagtcagtaaaacgacggccagtagtcaaaagcctacgaccggaggctttt
gacttggttcaggtggagtg
```

<!-- Sequence as supplied, 5′→3′. Lowercase marks coding and backbone regions;
uppercase marks the promoter/operator/RBS region at the 5′ end. The Doc
gives it as one unbroken string. It is wrapped at 60 characters per line
here so it fits the page; no character is changed. -->
:::

# Results

Evaporation, most likely from inadequate plate sealing over the 10 h read, cost us the in-solution arm entirely. The results below are from the crosslinked PEG-NB arm only.

:::{figure} ./figures/fig1-pla1-guv-lysis-kinetics.png
:label: fig-1-pla1-guv-lysis-kinetics
:align: center
:width: 90%
*Figure 1.* Kinetic CPRG conversion over 10 h in GUVs embedded in PEG-NB hydrogel, following external addition of 4 µL cell-free reaction. n = 3 technical replicates. (Top left) No DNA — high conversion in all three states, with and without TetR or aTc. (Top right) pOpen-deGFP — low conversion in the constitutive state, rising with TetR and with TetR + aTc. (Bottom left) pOpen-PLA — constitutive conversion closely resembles constitutive deGFP; TetR alone produced no increase, while TetR + aTc gave substantially higher conversion. (Bottom right) PJL-PLA — weak conversion across all states.
:::

<!-- [`fig-1-pla1-guv-lysis-kinetics`, extraction_method: pasted image in source
Doc, extracted with pandoc --extract-media. No notebook, platemap or raw
instrument file is referenced anywhere in the source Doc for this figure.] -->

First, adding TetR-His raised CPRG conversion in conditions that contain no phospholipase at all. Both the no-DNA and deGFP arms show this. The most likely cause is Tween 80 in the MedChemExpress TetR storage buffer, which would permeabilize the membrane directly. Every TetR-containing well therefore receives a detergent dose alongside the repressor, and the induced wells receive it too.

Second, constitutive pOpen-PLA was indistinguishable from constitutive deGFP. If PLA1 were being expressed and were active, the constitutive arm should be the most lytic condition on the plate; instead it sits at the non-lytic baseline. The induced pOpen-PLA condition did give clearly higher conversion than either its constitutive or repressed counterpart, which is the one result consistent with functional PLA1 — but that same condition is the one carrying both TetR buffer and aTc, so the detergent confound cannot be separated from genuine lytic activity with the controls run here.

Third, we predict that the reason the no DNA lysis was so high was because without DNA, no protein was synthesized and that with protein synthesis comes a decrease in osmolarity. So the No DNA GUVs are undergoing high osomotic shock than the other GUVs that got spent cell free reaction.

PJL-PLA underperformed pOpen-PLA across the board.

# Conclusion

This run does not yet establish that cell-free expressed PLA1 lyses GUVs. The assay reported a strong, reproducible signal, but the signal tracks the presence of TetR-His rather than the presence of a phospholipase gene, and the constitutive PLA1 condition — which should have been the most lytic well on the plate — was no more lytic than the non-lytic deGFP control. The elevated conversion in induced pOpen-PLA is the only observation pointing toward working PLA1, and it is confounded by the detergent carried in with the repressor.

For the next attempt, remove Tween 80 from the TetR preparation with a detergent-removal spin column. pOpen-PLA will be carried forward over PJL-PLA.
