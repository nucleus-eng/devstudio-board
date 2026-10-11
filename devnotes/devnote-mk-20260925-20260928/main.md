<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

<!-- Redrafted 2026-10-11 from the Google Doc "TetO-deGFP Encapsulated".
Source: https://docs.google.com/document/d/1oWYWO6-2OJEOMaWc-6dxgFCW8nUEhhw0ddNB8TZ9AXE
Prose, tables, step lists, captions and the plasmid sequence are carried
verbatim from that Doc. The Doc's section order is kept, not the DevNote
template order. The Doc is a written protocol, and its steps refer to each
other by Part number. Reordering it breaks those references.
STYLE: non-standard section headings preserved per participant intent. -->

:::{admonition} Open items from the redraft
:class: warning dropdown
:name: flags-review

**The 2026-09-25 experiment is no longer in this DevNote.** Earlier drafts
carried the 28-condition aTc titration from
`MK-20260925-tetO-plamGFP-titrate-atc` alongside the 2026-09-28 work. The
source Doc covers only 2026-09-28: the encapsulation run and its matched bulk
control. Carrying the Doc faithfully therefore drops the 2026-09-25 material.
The directory is still named `devnote-mk-20260925-20260928`. Rename it to
match, or say where the 2026-09-25 titration belongs.

**The outer solution buffer concentration is flagged in the source.** The Doc
states 800 µL of 1 M HEPES into 1000 µL total. It then says this gives 800 mM
HEPES, far above a normal buffer concentration. The Doc raises the problem
itself and does not resolve it. Both the table and the warning are carried
verbatim. Resolve this before anyone runs the protocol.

**Figure 3's caption and the Materials section disagree about the membrane
dye.** The caption reads "Membrane labeled with Cy5.5-PE". Every other mention
in the Doc, including the abstract, the overview and the lipid tables, reads
18:1 Liss Rhod PE at 0.1 mol%. Both are carried as written.

**The plasmid file was built here, not taken from a source of record.**
`dna/pOpen-TetO-deGFP.gb` carries this Doc's sequence byte for byte. It has the
five features the Doc's own landmark column supports, and it drives
{ref}`seqviz-popen-teto-degfp`. It is not an authoritative file.
`devstudio-verify-dna-constructs` was not run against it, so no
construct-to-file identity claim is made. Two candidate files in
`nucleus-eng/DNA` were compared against the sequence on 2026-10-11.

`detectors/pOpen-pT7-tetO.gb` is not this construct. It is 2954 bp against the
Doc's 2855, and its coding sequence is plamGFP: 693 nt, 230 amino acids,
beginning MEIEDVIKRDMK. The Doc's coding sequence is deGFP: 678 nt, 225 amino
acids, beginning MELFTGVVPILV. The two proteins share 7.6 percent of their
residues, which is the background two GFP-family proteins share. That file also
uses the UTR1 ribosome binding site and a T7hyb6 terminator, where the Doc uses
the T7 g10 leader and a different terminator.

`reporters/pOpen-deGFP.gbk` is the closest match. It is 2812 bp, exactly 43 bp
shorter than the Doc's sequence. Of 23 sampled 120-nucleotide windows of the
Doc, 22 appear in it verbatim. The one window that does not is bases 1 to 120,
which holds the promoter, the operator and the ribosome binding site. That file
carries the T7 promoter and the deGFP coding sequence but no `tetO` operator.
The Doc's plasmid reads as that file with the 43 bp operator region inserted
between the promoter and the ribosome binding site.

When a file of record exists, replace `dna/pOpen-TetO-deGFP.gb`. One built from
`reporters/pOpen-deGFP.gbk` plus that 43 bp insertion also carries its AmpR and
origin annotations, which the Doc's table cannot supply. Do not use
`detectors/pOpen-pT7-tetO.gb`.

**`figures/mk-20261005.jpeg` is not referenced.** It is a photograph of a
384-well plate with purple wells, dated 2026-10-05, after both experiments in
this DevNote. The Doc does not mention it and nothing here links it. Say where
it belongs or remove it.

**Three composition sidecars are now unreferenced.** `experiments/` holds
`composition-20260925.csv`, `composition-20260928.csv` and
`composition-20260928-microscopy.csv`, written before this redraft. The Doc
carries its own composition tables, so nothing points at them any more.
:::

# Abstract

We encapsulate a TetR-repressed, anhydrotetracycline (aTc)-inducible deGFP
cell-free expression reaction inside giant unilamellar vesicles and test
whether the sensor retains its dose-response behind a lipid bilayer. Vesicles
are formed by inverted emulsion transfer from POPC:cholesterol (9:1) doped with
0.1 mol% Liss Rhod PE, using a sucrose-in/glucose-out density mismatch to drive
droplets across the oil-water interface during centrifugation.

Three inner solutions are compared: a no-DNA autofluorescence floor, a 1 nM
pOpen-TetO-deGFP unrepressed ceiling, and a 1 nM DNA plus 1000 nM purified
His-TetR repressed sensor. Each is titrated across four aTc levels and imaged
in a BSA-blocked 384-well glass-bottom plate, scoring lumen GFP only in objects
with a continuous rhodamine rim. Reserved inner solution is run unencapsulated
on a plate reader in parallel, so a failure of the circuit can be distinguished
from a failure of encapsulation.

# Overview

This protocol encapsulates a TetR-repressed, aTc-inducible deGFP
transcription-translation reaction inside giant unilamellar vesicles (GUVs) and
asks whether the sensor still responds to inducer once it is behind a membrane.
GUVs are formed by inverted emulsion transfer, and the dose-response to
anhydrotetracycline (aTc) is read by fluorescence microscopy.

**The genetic circuit.** The pOpen-TetO-deGFP plasmid places a *tetO* operator
between the T7 promoter and the deGFP coding sequence. Purified His-tagged TetR
(MedChemExpress) binds *tetO* and blocks transcription; aTc binds TetR and
releases it, restoring deGFP expression. Output is therefore a graded GFP
signal set by the aTc concentration.

**Why GUVs.** The inverted emulsion (emulsion transfer) method builds the
bilayer in two steps. A water-in-oil droplet of inner solution acquires a lipid
monolayer in the lipid/mineral-oil phase; centrifugation drives the droplet
through a second monolayer at an oil/water interface, completing the bilayer. A
sucrose/glucose density mismatch between inner and outer solutions provides the
driving force and lets vesicles pellet.

**What the three inner solutions test.** Condition 1 (no DNA) sets the
autofluorescence floor of the cell-free mix. Condition 2 (1 nM DNA, no TetR)
gives the unrepressed expression ceiling. Condition 3 (1 nM DNA + 1000 nM TetR)
is the repressed sensor, titrated across four aTc levels.

**Readouts.** Rhodamine-PE at 0.1 mol% labels the membrane, so vesicle lumen
GFP can be scored only in objects with a continuous rhodamine rim. Extra inner
solution is run unencapsulated on a plate reader in parallel, so bulk and
encapsulated behavior can be compared directly.

**A run is successful if** unilamellar, rhodamine-rimmed vesicles are
recovered; the unrepressed condition is clearly brighter than the no-DNA
condition; and the TetR condition climbs with increasing aTc rather than
sitting flat at either extreme.

# Materials

Vendor and catalog columns are left for you to fill from what is actually on
the shelf; the concentrations below are the ones this run used.

## Lipids (in chloroform)

:::{table} Lipids, as supplied in chloroform.
:label: tbl-lipids
:align: center

| Amphiphile | MW (g/mol) | Stock (mg/mL) | Stock (mM) | Role | Vendor / cat. |
| --- | --- | --- | --- | --- | --- |
| POPC | 760.09 | 25 | 32.9 | Bulk bilayer lipid | Avanti |
| Cholesterol (ovine) | 386.7 | 19.3 | 50 | Membrane stability | Avanti |
| 18:1 Liss Rhod PE | 1301.7 | 1 | 0.77 | Membrane fluorophore | Avanti |
:::

## Cell-free expression system

Components are the OnePot PURE-style sub-mixes; each is dispensed as a fixed
fraction of the reaction volume.

:::{table} Cell-free sub-mixes, as a fraction of reaction volume.
:label: tbl-cellfree
:align: center

| Component | Fraction of reaction | Notes |
| --- | --- | --- |
| Solution mix (Smix) | 30% | Energy, amino acids, salts, buffer |
| Ribosomes (Rib) | 18% |   |
| Protein mix (Pmix) | 12% | Translation factors, aaRS, T7 RNAP |
| tRNA | 10% |   |
| Sucrose (inner osmolyte/density) | 8.8% |   |
| RNase inhibitor, murine (RIM) | 5.2% |   |
| **Total master mix** | **84%** | Remainder is DNA, TetR, and water |
:::

## Nucleic acids and proteins

:::{table} Nucleic acids and proteins.
:label: tbl-constructs
:align: center

| Item | Working stock | Final in reaction |
| --- | --- | --- |
| pOpen-TetO-deGFP plasmid | 100 nM | 1 nM |
| TetR, His-tagged (MedChemExpress) | ~10 µM | 1000 nM |
:::

## Small molecules and buffers

- Anhydrotetracycline (aTc) — inducer, added at four levels (0, 0.25, 0.5, 1)
- Sucrose — inner solution osmolyte and density agent
- D-glucose, 2 M stock — outer solution
- HEPES, 1 M stock — outer solution buffer
- Bovine serum albumin (BSA), 2% w/v — glass passivation
- Nuclease-free water
- Mineral oil, BioUltra grade
- Chloroform — lipid handling only, glass syringes and glass vials

## Consumables

- Glass vials with PTFE-lined caps, one per lipid film condition
- Hamilton glass syringes for chloroform transfers
- 1.5 mL microcentrifuge tubes, nuclease-free
- 384-well glass-bottom plate (microscopy)
- 384-well black plate (bulk plate-reader control)
- Glass slides and coverslips
- Low-retention pipette tips

## Equipment

- Nitrogen gas line for film drying
- Vacuum oven or desiccator (overnight lipid film drying)
- Hot plate capable of 80 °C
- Vortex mixer
- Refrigerated microcentrifuge, 18,000 rcf at 4 °C
- Ice bucket
- Confocal or widefield fluorescence microscope with GFP and rhodamine channels
- Plate reader with GFP excitation/emission

# Stocks to prepare in advance

Prepare these before the day of the experiment; everything after the lipid film
is time-sensitive.

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
| Plasmid | 100 nM in nuclease-free water | −20 °C |   |
| TetR | ~10 µM | −80 °C, single-use aliquots | Avoid freeze-thaw |
:::

Lipid films can be dried the day before and left under vacuum overnight.

# Part 1 — Lipid-in-oil preparation

Target composition is 9:1 POPC:cholesterol with 0.1 mol% Rhod-PE, delivered as
4.0 µmol total lipid in 200 µL mineral oil (20 mM).

## Film composition, per vial

:::{table} Lipid film composition, one vial per reaction condition.
:label: tbl-film
:align: center

| Lipid | Mole % | Stock (mM) | Volume (µL) | Amount (µmol) |
| --- | --- | --- | --- | --- |
| POPC | 89.9 | 32.9 | 109.3 | 3.596 |
| Cholesterol | 10.0 | 50 | 8.0 | 0.400 |
| 18:1 Liss Rhod PE | 0.1 | 0.77 | 5.2 | 0.004 |
| **Total** | **100** | — | **122.5** | **4.000** |
:::

Prepare one vial per reaction condition. Final lipid in oil: 4.0 µmol / 200 µL
= 20 mM.

## Steps

1. Combine the chloroform lipid stocks at the volumes above in the bottom of a
   glass vial. Use glass syringes; chloroform will leach plasticizer from
   plastic tips.
2. Dry under a gentle nitrogen stream, rotating the vial, until a uniform thin
   film has formed across the bottom.
3. Place in a vacuum oven (or desiccator) overnight, or at minimum a few hours,
   to remove residual chloroform.
4. Add 200 µL BioUltra mineral oil directly on top of the film.
5. Vortex briefly, then heat 30 min at 80 °C on a hot plate.
6. Vortex 5–10 s. If film is still visible on the glass, return to the hot
   plate for another 10 min and repeat until no film remains.
7. Cool the lipid/oil mixture on ice before use. Use the same day.

# Part 2 — Inner solution

Three conditions: no-DNA floor, unrepressed ceiling, and the repressed TetR
sensor. Condition 3 is made at a larger volume because it feeds four aTc
levels.

## Condition definitions

:::{table} The three inner solutions.
:label: tbl-conditions
:align: center

|   | 1 — No DNA | 2 — Unrepressed | 3 — TetR sensor |
| --- | --- | --- | --- |
| TetR (final) | 0 nM | 0 nM | 1000 nM |
| Plasmid (final) | 0 nM | 1 nM | 1 nM |
| Purpose | Autofluorescence floor | Expression ceiling | aTc dose-response |
:::

## Shared master mix

All three conditions take the same master mix, so it is batched once and split.
The three conditions need 310 µL of reaction (90 + 90 + 130); this batch is
made to 335 µL to carry 25 µL of overage for pipetting loss and dead volume.

:::{table} Shared master mix, batched to 335 µL of reaction.
:label: tbl-mastermix
:align: center

| Component | Volume (µL) | Fraction of reaction |
| --- | --- | --- |
| Smix | 100.5 | 30% |
| tRNA | 33.5 | 10% |
| Pmix | 40.2 | 12% |
| Ribosomes | 60.3 | 18% |
| RIM | 17.42 | 5.2% |
| Sucrose (45.6 mg solid) | 29.48 | 8.8% |
| **Total master mix** | **281.4** | **84%** |
:::

Sucrose is dosed at 3.4 mg per 25 µL of reaction, so 335 µL of reaction needs
45.6 mg. The 29.48 µL in the table is the volume the dissolved solid
contributes, not a volume pipetted from a stock. After dispensing 75.6, 75.6,
and 109.2 µL to the three conditions, roughly 21 µL of master mix is left over.

**Order of addition.** Weigh out the 45.6 mg of solid sucrose first and vortex
it into the Smix until fully dissolved. Only then add the remaining components
in the order listed — tRNA, Pmix, ribosomes, RIM. Dissolving sucrose into the
full mix instead risks prolonged vortexing against the ribosomes and
translation factors.

## Assembly, volumes in µL

:::{table} Inner solution assembly, volumes in µL.
:label: tbl-assembly
:align: center

| Component | 1 | 2 | 3 |
| --- | --- | --- | --- |
| Smix | 27.0 | 27.0 | 39.0 |
| tRNA | 9.0 | 9.0 | 13.0 |
| Pmix | 10.8 | 10.8 | 15.6 |
| Ribosomes | 16.2 | 16.2 | 23.4 |
| RIM | 4.68 | 4.68 | 6.76 |
| Sucrose | 7.92 | 7.92 | 11.44 |
| *Master mix subtotal* | *75.6* | *75.6* | *109.2* |
| Plasmid DNA | 0 | 0.9 | 1.3 |
| TetR | 0 | 0 | 13.0 |
| Nuclease-free water | 14.4 | 13.5 | 6.5 |
| **Total** | **90.0** | **90.0** | **130.0** |
:::

## Steps

1. Thaw all cell-free components on ice. Keep them on ice throughout; do not
   let the assembled mix warm before encapsulation.
2. Combine the plasmid DNA, TetR, and nuclease-free water for each condition in
   its own tube, at the volumes in the table above. Incubate 10 min at 37 °C so
   TetR binds the tetO operator before transcription can begin. Condition 1 is
   water only, but carry it through the same incubation.
3. Prepare the shared master mix as above and add it to each pre-incubated
   tube: 75.6, 75.6, and 109.2 µL for conditions 1, 2, and 3. Mix by gentle
   pipetting — do not vortex the assembled reaction.
4. Hold on ice and proceed immediately to Part 4. Reserve 10 µL per bulk
   control well (Part 6) before encapsulating.

# Part 3 — Outer solution

The outer solution is glucose-based so that the sucrose-loaded inner droplets
are denser than the surrounding phase and pellet through the interface during
centrifugation.

:::{table} Outer solution, per 1000 µL.
:label: tbl-outer
:align: center

| Component | Stock | Volume (µL) | Resulting concentration |
| --- | --- | --- | --- |
| Glucose | 2 M | 200 | 400 mM |
| HEPES | 1 M | 800 | 800 mM |
| Water | — | 0 | — |
| **Total** |   | **1000** |   |
:::

**Check this before running.** As written, 800 µL of 1 M HEPES gives 800 mM
HEPES, which is far above a normal buffer concentration and would badly
overshoot the inner solution osmolarity. The likely intent is a lower HEPES
stock or a much smaller HEPES volume with water to 1000 µL. See open items.

Prepare ~200 µL outer solution per condition: 100 µL as the receiving layer and
100 µL for resuspension. Match the outer osmolarity to the inner solution; a
mismatch will shrink or burst the vesicles.

# Part 4 — Emulsion transfer and vesicle recovery

Work cold and quickly. Everything from here until imaging should be kept on
ice.

1. Add 20 µL inner solution to the cold lipid/oil mixture.
2. Vortex 30 s to generate the water-in-oil emulsion. Incubate on ice 5 min so
   the lipid monolayer stabilizes around the droplets.
3. Carefully layer the emulsion on top of 100 µL outer solution. Pipette down
   the tube wall — do not let the emulsion punch through the interface.
4. Incubate on ice 5 min to let the oil/water interface equilibrate and acquire
   its monolayer.
5. In parallel, block glass slides or wells with 2% w/v BSA for at least
   20 min.
6. Centrifuge 15 min at 18,000 rcf, 4 °C. Droplets cross the interface and
   complete the outer leaflet.
7. Remove as much mineral oil from the top as possible without disturbing the
   interface.
8. With a fresh tip, collect the vesicle pellet from the bottom of the tube.
9. Resuspend each pellet in 200 µL outer solution.
10. Remove BSA from the wells, rinse, and load 20 µL the vesicles for imaging.

# Part 5 — Plate setup and imaging

Vesicles are imaged in a 384-well glass-bottom plate, BSA-blocked. Each well
receives 20 µL final reaction plus 2 µL aTc, and each condition is run in
duplicate (columns 5 and 6).

## Layout, 384-well glass-bottom plate

:::{table} Microscopy plate layout. Twelve conditions in duplicate.
:label: tbl-layout
:align: center

| Row | Condition | aTc level | Col 5 | Col 6 |
| --- | --- | --- | --- | --- |
| C | No DNA | 0 | ✓ | ✓ |
| D | No DNA | 0.25 | ✓ | ✓ |
| E | No DNA | 0.5 | ✓ | ✓ |
| F | No DNA | 1 | ✓ | ✓ |
| G | Unrepressed | 0 | ✓ | ✓ |
| H | Unrepressed | 0.25 | ✓ | ✓ |
| I | Unrepressed | 0.5 | ✓ | ✓ |
| J | Unrepressed | 1 | ✓ | ✓ |
| K | 1000 nM TetR | 0 | ✓ | ✓ |
| L | 1000 nM TetR | 0.25 | ✓ | ✓ |
| M | 1000 nM TetR | 0.5 | ✓ | ✓ |
| N | 1000 nM TetR | 1 | ✓ | ✓ |
:::

Twelve conditions × 2 replicates = 24 wells. Row B of the original layout
carried an unrelated in-gel PEG-NB entry and is not part of this experiment.

## Steps

1. Block the glass-bottom wells with 2% w/v BSA for ≥20 min, then remove and
   rinse with outer solution.
2. Dispense 20 µL of resuspended vesicles per well.
3. Add 2 µL aTc at the level for that row. Mix by gentle pipetting only.
4. Let vesicles settle to the glass before imaging.
5. Acquire rhodamine and GFP channels at each timepoint, with identical
   settings across all wells. Set exposure on the brightest expected well
   (unrepressed, high aTc) so nothing saturates.
6. Score GFP only inside objects with a continuous rhodamine rim.

# Part 6 — Bulk unencapsulated control

Run the same three inner solutions unencapsulated, so that a failure to express
can be told apart from a failure to encapsulate.

1. Before emulsification, reserve inner solution from each condition.
2. Plate 10 µL per well in a 384-well black plate, matching the same 12
   condition × aTc combinations.
3. Add aTc to match the microscopy plate, scaled to the 10 µL volume.
4. Read GFP fluorescence kinetically on the plate reader at 30 °C or 37 °C,
   with reads every 5–10 min for 3–6 h.

If the bulk reaction shows aTc-dependent GFP but the vesicles do not, the
problem is in encapsulation or vesicle integrity, not in the circuit.

# Plasmid reference — pOpen-TetO-deGFP

The expression cassette places the *tetO* operator immediately downstream of
the T7 promoter, so bound TetR occludes the polymerase at initiation rather
than acting as a roadblock during elongation.

:::{table} Elements of pOpen-TetO-deGFP.
:label: tbl-plasmid
:align: center

| Element | Sequence landmark | Function |
| --- | --- | --- |
| T7 promoter | TAATACGACTCACTATAGGG | Transcription start, T7 RNAP |
| *tetO* operator | TCCCTATCAGTGATAGAGA | TetR binding site; aTc-releasable |
| T7 g10 leader + RBS | AAGGAGATATACAT | Ribosome binding |
| deGFP CDS | atggagcttttcactggc… | Reporter, ~700 bp |
| T7 terminator | …tagagaccgagataacagatacttcggtatctgttatctgtt | Transcription stop |
| AmpR (*bla*) | — | Selection marker |
| pUC origin | — | Plasmid replication |
:::

The terminator and backbone sequences are not transcribed in the cell-free
reaction, but the full sequence is kept here so the construct is traceable from
the protocol.

(seqviz-popen-teto-degfp)=

:::{seqviz} ./dna/pOpen-TetO-deGFP.gb
:::

The map above is built from this Doc's own sequence and its own landmark
column. Each feature is placed by searching the sequence for the landmark
string the table gives, so no coordinate is asserted by hand. The table also
names AmpR and the pUC origin, with a dash in place of a landmark, so neither
is annotated.

<!-- Positions measured against the sequence below on 2026-10-11: total
2855 bp; T7 promoter at base 5; tetO operator at base 26; g10 leader and RBS at
base 90; deGFP CDS 104 to 781, which is 678 nt and 225 codons, consistent with
the "~700 bp" the table states; T7 terminator at base 791. No sequence file was
compared against, because none carrying this construct exists in the
repository. -->

:::{admonition} Full sequence
:class: dropdown

```
ggagTAATACGACTCACTATAGGGATCCCTATCAGTGATAGAGAGACCACAACGGTTTCC
CTCTAGAAATAATTTTGTTTAACTTTAAGAAGGAGATATACATatggagcttttcactgg
cgttgttcccatcctggtcgagctggacggcgacgtaaacggccacaagttcagcgtgtc
cggcgagggcgagggcgacgccacctacggcaagctgaccctgaagttcatctgcaccac
cggcaagctgcccgtgccctggcccaccctcgtgaccaccctgacctacggcgtgcagtg
cttcagccgctaccccgaccacatgaagcagcacgacttcttcaagtccgccatgcccga
aggctacgtccaggagcgcaccatcttcttcaaggacgacggcaactacaagacccgcgc
cgaggtgaagttcgagggcgacaccctggtgaaccgcatcgagctgaagggcatcgactt
caaggaggacggcaacatcctggggcacaagctggagtacaactacaacagccacaacgt
ctatatcatggccgacaagcagaagaacggcatcaaggtgaacttcaagatccgccacaa
catcgaggacggcagcgtgcagctcgccgaccactaccagcagaacacccccatcggcga
cggccccgtgctgctgcccgacaaccactacctgagcacccagtccgccctgagcaaaga
ccccaacgagaagcgcgatcacatggtcctgctggagttcgtgaccgccgccgggatctg
atgaagagcttagagaccgagataacagatacttcggtatctgttatctgttttttttct
aagcatcacactgccgtccgctgaggtgtcaatcgtcggagccgctgagcaataactagc
ataaccccttggggcctctaaacgggtcttgaggggttttttgcatggtcatagctgttt
cctgagagcttggcaggtgatgacacacattaacaaatttcgtgaggagtctccagaaga
atgccattaatttccataggctccgcccccctgacgagcatcacaaaaatcgacgctcaa
gtcagaggtggcgaaacccgacaggactataaagataccaggcgtttccccctggaagct
ccctcgtgcgctctcctgttccgaccctgccgcttaccggatacctgtccgcctttctcc
cttcgggaagcgtggcgctttctcatagctcacgctgtaggtatctcagttcggtgtagg
tcgttcgctccaagctgggctgtgtgcacgaaccccccgttcagcccgaccgctgcgcct
tatccggtaactatcgtcttgagtccaacccggtaagacacgacttatcgccactggcag
cagccactggtaacaggattagcagagcgaggtatgtaggcggtgctacagagttcttga
agtggtggcctaactacggctacactagaagaacagtatttggtatctgcgctctgctga
agccagttaccttcggaaaaagagttggtagctcttgatccggcaaacaaaccaccgctg
gtagcggtggtttttttgtttgcaagcagcagattacacgcagaaaaaaaggatctcaag
aaggcctactattagcaacaacgatcctttgatcttttctacggggtctgacgctcagtg
gaacgaaaactcacgttaagggattttggtcatgagattatcaaaaaggatcttcaccta
gatccttttaaattaaaaatgaagttttaaatcaatctaaagtatatatgagtaaacttg
gtctgacagttaccaatgcttaatcagtgaggcacctatctcagcgatctgtctatttcg
ttcatccatagttgcctgactccccgtcgtgtagataactacgatacgggagggcttacc
atctggccccagtgctgcaatgataccgcgagaaccacgctcaccggctccagatttatc
agcaataaaccagccagccggaagggccgagcgcagaagtggtcctgcaactttatccgc
ctccatccagtctattaattgttgccgggaagctagagtaagtagttcgccagttaatag
tttgcgcaacgttgttgccattgctacaggcatcgtggtgtcacgctcgtcgtttggtat
ggcttcattcagctccggttcccaacgatcaaggcgagttacatgatcccccatgttgtg
caaaaaagcggttagctccttcggtcctccgatcgttgtcagaagtaagttggccgcagt
gttatcactcatggttatggcagcactgcataattctcttactgtcatgccatccgtaag
atgcttttctgtgactggtgagtactcaaccaagtcattctgagaatagtgtatgcggcg
accgagttgctcttgcccggcgtcaatacgggataataccgcgccacatagcagaacttt
aaaagtgctcatcattggaaaacgttcttcggggcgaaaactctcaaggatcttaccgct
gttgagatccagttcgatgtaacccactcgtgcacccaactgatcttcagcatcttttac
tttcaccagcgtttctgggtgagcaaaaacaggaaggcaaaatgccgcaaaaaagggaat
aagggcgacacggaaatgttgaatactcatactcttcctttttcaatattattgaagcat
ttatcagggttattgtctcatgagcggatacatatttgaatgtatttagaaaaataaaca
aataggggttccgcgcacctgcaccagtcagtaaaacgacggccagtagtcaaaagccta
cgaccggaggcttttgacttggttcaggtggagtg
```

Sequence as supplied, 5′→3′. Lowercase marks coding and backbone regions;
uppercase marks the promoter/operator/RBS region at the 5′ end. The Doc
gives it as one unbroken string. It is wrapped at 60 characters per line
here so it fits the page; no character is changed.
:::

# Results

**Bulk.** The aTc titration was not clean above 0.25 µM, but the circuit itself
behaved as designed: TetR gave strong repression, and aTc relieved it. In the
unrepressed reaction deGFP reached 41,800 RFU by 6 h, against a no-DNA floor of
296 RFU. Adding 1000 nM TetR dropped expression to 4,100 RFU, a 9.8-fold
repression ratio. aTc restored expression dose-dependently from 0 to 0.25 µM
(3.3-fold), after which the titration became non-monotonic — the 0.5 µM
replicates disagreed 2.3-fold (21,306 vs 9,423 RFU, 55% CV, where every other
pair was under 12%), and 1 µM fell below 0.25 µM. aTc toxicity does not account
for this: the unrepressed wells at 1 µM aTc matched those at 0 µM, so aTc is
not inhibiting the reaction. All conditions plateaued by ~3 h.

:::{figure} ./figures/fig1-bulk-kinetics.png
:label: fig-1-bulk-kinetics
:align: center
:width: 100%
*Figure 1.* Kinetics of deGFP expression from pOpen-TetO-deGFP in bulk PURE reactions. Fluorescence (485/20 ex, 528/20 em, gain 50) read every 5 min for 6 h at 37 °C. Conditions: no-DNA control, unrepressed (1 nM plasmid), and 1 nM plasmid + 1000 nM TetR across 0–1 µM aTc. n = 2 wells per condition.
:::

[`fig-1-bulk-kinetics`, notebook:`MK- 20260928-tetO-R-deGFP-CellsAndWells/MK-20260928-platereader.ipynb`, platemap:`MK-20260928-platemap-nucleus-bulk.csv`, data source:`20260928-175538-synergy2-pure-timecourse-gfp-mk-teto-degfp-bulk-atc.txt`, caption: (Kinetics of deGFP expression from pOpen-TetO-deGFP in bulk PURE reactions.)]

:::{figure} ./figures/fig2-bulk-endpoint.png
:label: fig-2-bulk-endpoint
:align: center
:width: 75%
*Figure 2.* Endpoint deGFP fluorescence at 6 h, from the kinetic run in Figure 1. Individual replicates shown; n = 2 wells per condition.
:::

[`fig-2-bulk-endpoint`, notebook:`MK- 20260928-tetO-R-deGFP-CellsAndWells/MK-20260928-platereader.ipynb`, platemap:`MK-20260928-platemap-nucleus-bulk.csv`, data source:`20260928-175538-synergy2-pure-timecourse-gfp-mk-teto-degfp-bulk-atc.txt`, caption: (Endpoint deGFP fluorescence at 6 h, from the kinetic run in Figure 1.)]

<!-- Figures 1 and 2 are pasted images in the source Doc, extracted with pandoc
--extract-media. Neither carries a #| label: in the plate reader notebook. The
notebook's only label, mk-20260928, is on its final cell, kinetics.plot_summary.
REVIEW: add #| label: to the producing cells to switch both to the
quarto-label pattern. -->

**Encapsulated.** GUVs were imaged over 4 h in two formats: embedded in PEG-NB
hydrogel (left two columns) and free in solution (right two columns,
duplicate). The in-gel images are dominated by scattering background and are
not interpretable for expression. The in-solution samples show the expected
behavior — no-DNA vesicles stayed dark throughout, unrepressed vesicles became
strongly fluorescent, the 0 µM aTc condition remained repressed, and lumen
deGFP increased with aTc concentration.

:::{anywidget} ../../plugins/vizarr/vizarr-viewer.mjs
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/deGFP-GUV-PegNB-Soln_2026-09-28_17-44-06.899443.zarr",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/deGFP-GUV-PegNB-Soln_2026-09-28_17-44-06.899443.zarr`, caption: (Images of GUVs over 4 h. Membrane labeled with Cy5.5-PE; deGFP in the GFP channel. Left two columns, GUVs in PEG-NB hydrogel; right two columns, duplicate samples in solution.)]

*Figure 3.* Images of GUVs over 4 h. Membrane labeled with Cy5.5-PE; deGFP in
the GFP channel. Left two columns, GUVs in PEG-NB hydrogel; right two columns,
duplicate samples in solution.

<!-- The source Doc carries a link to
https://bnext-bio.github.io/vizarr/?source=<this store>&viewState={...} with the
instruction "Import microscope data for a figure here". The viewer above takes
the store URL from that link. The viewState is not carried, because the widget
does not forward it.

The viewer points at the plate root rather than deep-linking one well, by
decision on 2026-10-11. Figure 3's caption describes the whole montage, left
two columns in gel and right two in solution, so the full plate is what the
caption is written against.

The widget can also set channel colors and contrast limits per viewer, which
this one does not use. This store carries GFP 00FF00 and Alexa Fluor 647
0000FF, both windowed across the full 16-bit range. Values chosen to show the
result would go in the block above as colors and contrast_limits.

A viewer does not survive JATS conversion, so an archival static figure is
still needed for this panel. -->

:::{figure} #mk-20260928-uscope
:label: fig-4-lumen-degfp
:align: center
:width: 100%
*Figure 4.* Lumen deGFP fluorescence in solution-phase GUVs over 4 h. Each point is mean per-vesicle intensity. 2 technical replicates per condition.
:::

[`fig-4-lumen-degfp`, notebook:`MK- 20260928-tetO-R-deGFP-CellsAndWells/MK-20260928- microscopy`, platemap:`20260928-MK-full-sensor-microscopy.csv`, data source:`deGFP-GUV-PegNB-Soln_2026-09-28_17-44-06.899443.parquet`, caption: (Lumen deGFP fluorescence in solution-phase GUVs over 4 h.)]

:::{figure} #mk-20260928-uscope-subtract-bkg
:label: fig-5-background-subtracted
:align: center
:width: 100%
*Figure 5.* Background-subtracted quantification of Figure 4. aTc is autofluorescent in the GFP channel and raises background in proportion to dose, so the matched no-DNA control at each aTc concentration was subtracted from every condition.
:::

[`fig-5-background-subtracted`, notebook:`MK- 20260928-tetO-R-deGFP-CellsAndWells/MK-20260928- microscopy`, platemap:`20260928-MK-full-sensor-microscopy.csv`, data source:`deGFP-GUV-PegNB-Soln_2026-09-28_17-44-06.899443.parquet`, caption: (Background-subtracted quantification of Figure 4.)]

# Conclusion

deGFP expressed robustly in bulk PURE and after encapsulation in GUVs. TetR
repressed the sensor effectively in both formats — 9.8-fold in bulk — and aTc
relieved repression in both. In GUVs, induction increased with aTc up to 1 µM,
the highest dose tested.

# Resources

<!-- Not a section of the source Doc. Added so the assets the figures resolve
through are linked from the DevNote. -->

- Plate map, bulk: [`experiments/MK-20260928-platemap-nucleus-bulk.csv`](./experiments/MK-20260928-platemap-nucleus-bulk.csv)
- Plate map, microscopy: [`experiments/20260928-MK-full-sensor-microscopy.csv`](./experiments/20260928-MK-full-sensor-microscopy.csv)
- Analysis notebook, plate reader: [`experiments/MK-20260928-platereader.ipynb`](./experiments/MK-20260928-platereader.ipynb)
- Analysis notebook, microscopy: [`experiments/MK-20260928-microscopy.ipynb`](./experiments/MK-20260928-microscopy.ipynb)
- Microscopy image store: [the OME-Zarr plate on data.nucleus.engineering](https://data.nucleus.engineering/microscopy/nucleus-bnext-01/deGFP-GUV-PegNB-Soln_2026-09-28_17-44-06.899443.zarr)
- Microscopy per-object measurements: [the parquet beside that plate](https://data.nucleus.engineering/microscopy/nucleus-bnext-01/deGFP-GUV-PegNB-Soln_2026-09-28_17-44-06.899443.parquet)

The raw plate reader file lands in `experiments/` during asset assembly, as
`20260928-175538-synergy2-pure-timecourse-gfp-mk-teto-degfp-bulk-atc.txt`.

<!-- The microscopy notebook lands in experiments/ as
MK-20260928-microscopy.ipynb. Its Drive title is "MK-20260928- microscopy",
with a space and no extension. Rename it on the way in, and keep the toc entry
in curvenote.yml pointing at the renamed file. -->
