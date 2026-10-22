<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

# Abstract

Over an intense 3-week collaboration at DevStudio, we set out to build developer cells that sense a bacterial-derived acyl-homoserine lactone signal. We leveraged EsaR/EsaO transcriptional regulation, an established quorum-sensing system {cite}`shong2013,minogue2002` in which the EsaR repressor blocks transcription until its signal is present. Previous implementations of this system in PURE co-expressed EsaR alongside the sensor construct, allowing early unrepressed transcription before EsaR accumulated {cite}`tang2018,chizzolini2017`. We improved this by pre-expressing EsaR separately before use and by adding a second EsaO operator to deepen repression. EsaR is first expressed in Nucleus cytosol, then added to the sensor reaction afterward, keeping the EsaO operator sites occupied from the start. We optimised repression by exploring several reaction conditions such as EsaR template competition and lower reaction temperatures, with the best condition reaching a 5.8-fold change between 'on' and 'off' states. We then encapsulated the sensor inside GUVs, producing developer cells that successfully detected exogenously added AHSL. We present these developer cells as a starting point for the construction of a synthetic cell device capable of sensing contaminated surfaces.

# Overview

Nucleus cytosol is a cell-free system of defined composition that can be encapsulated inside giant-unilamellar vesicles (GUVs) to produce developer cells; a platform that new synthetic cell modules can be designed, tested, and built from. In addition, synthetic biology has leveraged natural modes of communication to produce DNA sensors for a range of signalling molecules. As such, developer cells encapsulating these sensors can be programmed to communicate with and sense their external environment. An example of detectable signalling molecules are the acyl-homoserine lactones (AHSLs), small molecules secreted by bacteria that regulate gene expression in response to population density. A developer cell programmed to sense AHSL and produce a detectable output could enable sensitive detection of bacteria in specific environments. We envision these developer cells detecting food spoilage or contamination in medical settings.

Towards this goal, we programme developer cells to sense AHSL using the *Pantoea stewartii* repressor protein, EsaR. In the absence of its cognate ligand, 3-oxo-C6-HSL, EsaR natively binds the EsaO operator where it is thought to occlude RNA polymerase and prevent transcription {cite}`minogue2002`. In our case, we insert one or two EsaO operators downstream of the T7 promoter, blocking transcription in Nucleus cytosol until AHSL is added ({numref}`fig-esar-sensing`). EsaR has previously been co-expressed with an EsaO-controlled reporter both in bulk PURE reactions, and inside synthetic cells; however, the lag in EsaR expression was thought to result in early unrepressed transcription producing variable outputs {cite}`tang2018,chizzolini2017`. An alternative system supplied EsaR to lysate-encapsulated synthetic cells by pre-expressing EsaR in *E. coli* prior to lysate harvesting {cite}`ding2018`. This ensured that EsaR was present throughout the entire reaction; however, lysate-based systems often pose a challenge to further engineering due to their undefined composition.

To benefit from a defined chemical composition, and to limit early unrepressed transcription, we instead pre-express EsaR in [Nucleus cytosol](xref:nucleus-docs/docs/modules/base-cytosol/spec#overview) and pre-incubate it with the sensor DNA so that operator sites are occupied before the template enters the final reaction. We test single and dual operator sensor DNA constructs, the latter inspired by {cite}`shong2013`, in bulk cytosol reactions, optimising reaction conditions for increased sensor dynamic range before constructing developer cells that can sense exogenously added AHSL. We hope to build upon this work by embedding the developer cells in a hydrogel matrix, increasing their stability and progressing towards a deployable device ([DevStudio: London Node LuxR demo](https://devnotes.nucleus.engineering/articles/01a1121a-7513-7ec7-8378-0326c6b3630b)).

:::{figure} figures/EsaR-sensing.png
:label: fig-esar-sensing

EsaO/EsaR-dependent transcriptional regulation. EsaR binds the EsaO box preventing T7 polymerase from transcribing an mNeonGreen reporter protein. Upon binding of a AHSL signal, EsaR leaves the DNA re-enabling transcription.
:::
---

# Objectives

- Establish the pre-expressed EsaR : sensor DNA molar ratio needed to produce a defined 'on'/'off' state.
- Optimise sensor dynamic range by varying reaction conditions.
- Validate the optimised sensor in GUVs, as a step toward a deployable developer cell sensor.


<!-- Overview supplied by the reviewer in review cycle v2, prompt 21, and
carried verbatim. No source log carries an overview section. The five logs
open directly on Notes, on "Day #1", or on their own first sentence. The
2026-10-07 addition is not reflected here, because the overview text predates
it and was supplied verbatim by the reviewer; it is not rewritten here per
the review-cycle convention.
Candidate framing, from the platemap
Experiment column, not adopted: "EsaO-mNG / [EsaO]2-mNG EsaR titration +/- AHSL"
and "EsaO-mNG / [EsaO]2-mNG DNA template titration +/- AHSL (EsaR fixed at
highest prior dose)". -->

<!--
:::{danger} Unresolved before publication
:name: flags-blocking

**Answered, review cycle v2, prompt 2, and deferred.** These figures will be
rerun later against a subset of conditions that shows the DNA concentration is
in excess relative to the repressor. Both stay `static-png` until then. 

**No DNA sequences.** {numref}`tbl-constructs` names seven linear templates
and carries no sequence for any of them. A DevNote must be self-contained, so
every sequence has to be added inline. No `.gb` file for any of the seven was
located, so `devstudio-verify-dna-constructs` was not run and no
construct-to-file identity claim is made here.

**Every construct used in this DevNote is supplied and verified.** All four
are in the tree: `T7-EsaR(D91G)-T7term` in {ref}`seq-esar-d91g`,
`T7-\[EsaO\]-mNG-T7term` in {ref}`seq-esao-mng`, `T7-\[EsaO\]2-mNG-t7term` in
{ref}`seq-esao2-mng` and `T7-mNG-t7term`, the unrepressed control, in
{ref}`seq-mng`. The three mNG-bearing constructs agree with each other: they
share one mNeonGreen coding sequence byte for byte, and both reporters'
operator boxes are the same 19 bp.

None of the four is in `nucleus-eng/DNA`, on `main` or on
`devcells/devstudio-constructs`. The repo carries the neighbouring
quorum-sensing family but nothing for EsaR or EsaO. These belong in that repo,
and once they are there the DevNote can reference them by GitHub URL and carry
no local copy.

**No build file for 2026-10-01.** The file named `build` in that folder is a
platemap. It holds `Well`, `Date`, `Experiment`, `Name` and `Type` and nothing
else, so it carries no component, no concentration and no volume. No sidecar
exists for this day.

**Answered, review cycle v2, prompt 5, and deferred.** This will be addressed
later. The volume table stands in the meantime.
:::
-->

<!--
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

**Resolved, review cycle v2, prompt 6.** Each file holds the correct
information. The filenames are the slip, not the folders.

**Superseded, 2026-10-18.** For the 2026-09-26 file specifically, this call
was wrong on one field. A retrospective, provenance-documented platemap
(`20260926-nucleus-platemap-esao2-dna-titration-esar-spent.csv`, cross-checked
against the instrument file and log) shows `Date` and `Experiment` were
harmless copy-paste leftovers as this note says, but `EsaR Vol (uL)` also
carried a stale 2026-09-24 value (2.275, that day's top EsaR dose) instead of
the 2026-09-26 run's actual 2.0 µL (1.9802 in `+AHSL` wells). The stale file
has been replaced with the corrected one in
`experiments/20260926-dna-titration-esar-spent/` and in {numref}`platemap-20260926`.
The 2026-09-25 file (`20260924-dna-titration-esar-fixed.csv`) has not been
re-checked against a similar retrospective record and this resolution still
stands for it.

 **Template residue in every `test-data/` subfolder.** All four folders hold an
identical `20251111-122213-cytation5-pure-timecourse-gfp-MFG-98-tRNA-QC.txt`
plus `platemap-microscopy.csv` and `platemap-platereader.csv`. These look like
unedited copies from `00-template-LOG`, not run data. Nothing here links them.

**Resolved, review cycle v2, prompt 7.** They can be ignored if unedited. All
three files report identical byte counts in all four folders, which is the
evidence that none was edited. 

 **EsaR volume labels in {numref}`tbl-composition-20260924`.** The condition
names read 0, 1, 4 and 7 µL EsaR. The `Pre-expressed EsaR` row reads 0, 2, 8
and 14 µL. The reactions are 65 µL against a 32.5 µL standard reaction, so the
row is the per-65-µL volume and the name is the per-32.5-µL volume. Both are
carried as the build file writes them.

**Resolved, review cycle v2, prompt 8.** That reading is correct. 

**DNA stock disagreements.** The 2026-09-24 build sheet states one 200 ng/µL
stock, yet EsaO takes 2.87 µL and \[EsaO\]2 takes 3.25 µL. The 2026-09-25 sheet
states 200 ng/µL in its standard-reaction block and 10 and 150 ng/µL in its own
comment. The comment values are the ones carried in
{numref}`tbl-composition-20260925`. The 2026-09-26 conditions all take 0.46 µL
because their stocks differ at 10, 50 and 100 ng/µL. The 2026-10-01 log states
22 ng/µL.

**Deferred, review cycle v2, prompt 9.** The reviewer passed on this question.
Every stock value above is still carried as its own source writes it.

 **Pre-expressed EsaR has no concentration.** No build sheet records a stock or
final concentration for it. All four concentration cells are `—`. The 2026-09-24
log states a final EsaR concentration of 576 nM from back-of-the-napkin maths,
which is narrative, not a build-file value.

**Resolved, review cycle v2, prompt 10.** The concentration of pre-expressed
EsaR is not known. The dash stands, and the 576 nM figure stays narrative
only. 

**Stale sheets in the 2026-09-24 build file.** `build` in
`CN-20260924_repressor_test` also contains sheets named `20260926_DNA_titration`
and `Sheet6` whose contents duplicate the 2026-09-25 titration. Only
`20260924_Repression_test_rxns` was used here.

**Answered, review cycle v2, prompt 11, and hedged.** The reviewer says those
sheets are "probably stale". That is not a confirmation, so this stays open.

 **AHL and AHSL.** Before this cycle, the 2026-09-24 and 2026-09-25 logs
wrote "AHL", every platemap wrote "AHSL", the 2026-09-26 log wrote "AHL" in its
reaction preparation and "AHSL" in its result, and the 2026-10-01 volume table
wrote "AHL optional".

**Resolved and applied, review cycle v2, prompt 12.** Everything is written as
AHSL. Seven occurrences of "AHL" were replaced across Protocol, Methods,
Results and the 2026-10-01 volume table. This is the one place where verbatim
source wording was changed, and it was changed on the author's explicit
instruction. 

 RESOLVED 2026-10-12: {numref}`tbl-reagents` is now fully populated — in-house
components link to their b.next preparation processes in `nucleus-docs`, and
purchased reagents carry vendor product, catalog number, and link, sourced
across `DevCell_Materials_Tracker.xlsx`, the distribution-wide Materials
Reference, and vendor catalogs directly.

Original flagged text, kept for provenance:

**The reagents table cannot be filled from the Materials Reference.**
`devstudio-build-to-materials` has now run, and matched 0 of 14 components. The
detail, the two near misses and what to do about them are in
`review-materials-unmatched`. 
Construct purposes are still deferred to a
second pass, per review cycle v2, prompt 24.

**Two figures are still static PNGs.** The four 2026-09-25 and 2026-09-26
figures now carry `#| label:` tags and resolve against their notebook cells.
The two 2026-09-24 figures stay `static-png`, because their producing cell does
not exist to label. That is the blocking item above.

**One label carried the wrong year, and the Drive notebook still does.**
Cell 15 of the 2026-09-26 notebook was tagged `cn-20260926-fig1`, which reads
2025.

**Answered and applied here, review cycle v2, prompt 14.** It should be 2026.
This DevNote's copy of the notebook, `main.md` and `manifest.json` now all read
`cn-20260926-fig1`. The Drive original was last modified at 21:20 on
2026-10-04, before this change, so it still carries the 2025 spelling. Retag it
there so the two do not drift.

 **The 2026-10-01 platemap date disagrees with everything around it.** The
folder is `2026/10/01 - MB - MgSweepof preeincubation` and the data file is
`20261001-181311-...`. Every row of the platemap reads `2026-10-02`.

**Resolved, review cycle v2, prompt 15.** The run date is 2026-10-01. The
platemap was written the day after, which is why it reads 2026-10-02. 

**An unused platemap copy sits in the 2026-10-01 folder.**
`build-platemap-csv.csv` holds the same sixteen wells as the `build` Sheet. Its
`Type` column is empty where the Sheet reads `Sample`. The notebook loads the
Sheet. Delete the copy, or say which one is authoritative.

**Answered, review cycle v2, prompt 16, and deferred.** That platemap will be
rebuilt. The Sheet export is the copy vendored into this DevNote.

 **Authorship of the 2026-10-01 experiment.** The folder and the notebook
name MB and JM. The cell label reads `mbcn-20261001-fig1`.

**Resolved, review cycle v2, prompt 17.** MB is Manuel Bibrowski. Several sets
of initials appear because multiple experiments share one plate. The author
list itself is still open, under the blocking title-and-authors item. 

**All three sequence files say circular, and the constructs are linear.** The
`LOCUS` line of every file in `dna/` reads `circular`. The 2026-09-23
protocol amplifies these from gBlocks, which gives a linear product.
{numref}`tbl-constructs` calls all three linear templates. Correct the topology
in all three files.

Each sequence now renders through `{seqviz}` with `:viewer: linear` set
explicitly. The three maps display correctly as linear, regardless of what
each file's own `LOCUS` line claims. `seqviz` never reads that field. Only the
`:viewer:` option controls it. That fixes how the sequence looks here. It does
not fix the file, which is still worth correcting at the source.

**The log names M15 primers, and all three sequence files name M13.** The
2026-09-23 protocol reads "amplified using Q5 polymerase (2x HF buffer) and M15
Fwd and Rev primers". The feature labels in all three files read `M13_Fwd` and
`M13_Rev`. Say which is right.

**Two more experiments belong in this DevNote.** Review cycle v2, prompt 22,
closes with two lines naming work that is not drafted here: "Missing 2026-09-30
- Manuel initial Mg titration" and "Missing 2026-10-03 - Overnight EsaR 37 ˚C
pre-incubation". Neither Log folder was in the set selected for this DevNote.
Point me at the two folders and say whether they join this DevNote as a fifth
and sixth day, which would move the slug again.

**The 2026-09-24 sensor DNA concentration has two values.** The 2026-09-24 log
states "a sensor DNA template final concentration of 15.35 nM" in its own
pre-analysis note. The narrative supplied in review cycle v2 states "The
reporter construct concentration was held at 12.2 nM in each reaction". Both
are carried above, in their own paragraphs. Say which is correct.

**Uncertainty markers.** Every result paragraph in all three CN logs is prefixed
`*Prior to analysis` or `*Prior to data analysis`. Those statements are the
author's pre-analysis impressions, carried verbatim.

**Answered, review cycle v2, prompt 18, and in progress.** The analysis is
being done now. Each Results subsection already carries the reviewer's
post-analysis narrative above the log's pre-analysis note, so both are present
and labelled. This stays open until each pre-analysis note is confirmed or
replaced.
:::
-->

---

# Sensor Design

To quantify sensor output we chose mNeonGreen, a bright fluorescent protein commonly used to report on cell-free protein synthesis {cite}`copeland2022`. This would enable us to rapidly optimise the sensor using plate reader assays. To pre-express EsaR, we used the directed-evolution variant EsaR(D91G) ({cite}`shong2013-chembio`). This variant shows substantially increased 3-oxo-C6-HSL sensitivity relative to wild-type EsaR. For the sensor DNA constructs, we followed the design used by {cite}`chizzolini2017` in which the EsaO operator is placed directly adjacent to the T7 promoter for maximal repression. The EsaO is flanked by a leader sequence containing the epsilon enhancer sequence and a strong ribosomal binding site. To further deepen repression, a second EsaO operator was inserted upstream of the native operator in the dual-operator construct. The two operators are separated by a single thymine. This follows the P{sub}`esa`R-C design described by {cite}`shong2013`. P{sub}`esa`R-C showed tighter repression and greater derepression than the native promoter when tested in *E. coli*. We were interested to see whether this same behaviour would translate to Nucleus cytosol reactions.

---

# DNA Constructs

Four linear DNA templates were used throughout this work: the EsaR(D91G) template DNA used to pre-express EsaR, two EsaO-mNG sensor DNA constructs carrying either single or dual EsaO operator boxes, and an unrepressed mNG control. Linear templates were amplified from g-blocks using PCR and cleaned-up prior to their addition into cytosol reactions.

:::{table}  DNA constructs used throughout this work. Sequences with annotations are listed in the below viewers. All constructs contain mNeonGreen, a bright fluorescent protein commonly used to report on cell-free protein expression {cite}`copeland2022`.
:label: tbl-constructs
:align: center

| Name | Sequence | Purpose |
| --- | --- | --- |
| T7-\[EsaO\]-mNG-T7term | [`dna/t7pro-esao-ls1-mneongreen.gbk`](./dna/t7pro-esao-ls1-mneongreen.gbk) | EsaR-dependent expression of mNG in cytosol |
| T7-\[EsaO\]2-mNG-t7term | [`dna/t7pro-esao2-ls1-mneongreen.gbk`](./dna/t7pro-esao2-ls1-mneongreen.gbk) | EsaR-dependent expression of mNG in cytosol |
| T7-EsaR(D91G)-T7term | [`dna/t7pro-ls1-esard91g.gbk`](./dna/t7pro-ls1-esard91g.gbk) | Expression of EsaR in cytosol |
| T7-mNG-t7term | [`dna/t7pro-ls1-mneongreen.gbk`](./dna/t7pro-ls1-mneongreen.gbk) | Unrepressed mNG control, independent of AHSL (5 µM) |
:::

:::::{tab-set}

::::{tab-item} [EsaO]2-mNG (dual operator)

(seq-esao2-mng)=
**Name:** T7-\[EsaO\]2-mNG-t7term  
**Source file:** [`dna/t7pro-esao2-ls1-mneongreen.gbk`](./dna/t7pro-esao2-ls1-mneongreen.gbk)  
**Length:** 1118 bp  
**Annotations:** 5' spacer, M13_Fwd, T7pro, +1, EsaO, EsaO, LS1, mNeonGreen, T7 terminator, M13_Rev, 3' spacer  
**References:** {cite}`shong2013`, {cite}`chizzolini2017`, {cite}`copeland2022`

<!--Its mNeonGreen coding sequence is byte-identical to the one in
{ref}`seq-esao-mng`, so the two reporters differ only in the operator region.-->

The file carries two `EsaO` features, 19 bp each, at 62..80 and 82..100. Both
read `CCTGTACTATAGTGCAGGT`. One `T` separates them, at position 81.

:::{seqviz} ./dna/t7pro-esao2-ls1-mneongreen.gbk
:viewer: linear
:::
::::

::::{tab-item} EsaO-mNG (single operator)

(seq-esao-mng)=
**Name:** T7-\[EsaO\]-mNG-T7term  
**Source file:** [`dna/t7pro-esao-ls1-mneongreen.gbk`](./dna/t7pro-esao-ls1-mneongreen.gbk)  
**Length:** 1098 bp  
**Annotations:** 5' spacer, M13_Fwd, T7pro, +1, EsaO, Leader sequence 1, mNeonGreen, T7 terminator, M13_Rev, 3' spacer  
**References:** {cite}`chizzolini2017`, {cite}`copeland2022`

The file carries exactly one `EsaO` feature, 19 bp at 62..80, which is what
makes this the single-operator construct. It sits between the +1 transcription
start and the leader sequence.

:::{seqviz} ./dna/t7pro-esao-ls1-mneongreen.gbk
:viewer: linear
:::
::::

::::{tab-item} EsaR(D91G)

(seq-esar-d91g)=
**Name:** T7-EsaR(D91G)-T7term  
**Source file:** [`dna/t7pro-ls1-esard91g.gbk`](./dna/t7pro-ls1-esard91g.gbk)  
**Length:** 1118 bp  
**Annotations:** 5' spacer, M13_Fwd, T7pro, +1, LS1, EsaR, T7 terminator, M13_Rev, 3' spacer  
**References:** {cite}`shong2013-chembio`

The file encodes `EsaR(D91G)` an EsaR variant evolved by {cite}`shong2013-chembio` that exhibits higher sensitivity and derepression than the native EsaR protein. 

:::{seqviz} ./dna/t7pro-ls1-esard91g.gbk
:viewer: linear
:::
::::

::::{tab-item} mNG (constitutive control)

(seq-mng)=
**Name:** T7-mNG-t7term  
**Source file:** [`dna/t7pro-ls1-mneongreen.gbk`](./dna/t7pro-ls1-mneongreen.gbk)  
**Length:** 1079 bp  
**Annotations:** 5' spacer, M13_Fwd, T7pro, +1, LS1, mNeonGreen, T7 terminator, M13_Rev, 3' spacer  
**References:** {cite}`copeland2022`

:::{seqviz} ./dna/t7pro-ls1-mneongreen.gbk
:viewer: linear
:::
::::

:::::

<!-- RESOLVED 2026-10-12: the three PLA1 templates were dropped from
tbl-constructs, since they were prepared on 2026-09-23 but never used in any
experiment in this DevNote. T7-mNG-t7term, the unrepressed control used across
the CN experiments, was added to tbl-constructs on 2026-10-18 once its source
file (`dna/t7pro-ls1-mneongreen.gbk`) was supplied. -->

---

# Methods

## Materials

::::{admonition} List of consumables
:class: dropdown

:::{table} Reagents and equipment used throughout this work. In-house components (Small molecule mix, tRNA, Protein mix, Ribosomes) link to their b.next preparation processes in `nucleus-docs`; other components were purchased from vendors, with their product links provided.
:label: tbl-reagents
:align: center

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | Small Molecule Mix (SMix) | b.next (in-house) | N/A | N/A | -80 °C | [link](xref:nucleus-docs/docs/processes/make-small-molecule-mix/main#overview) |
| tRNA | Nucleus Total tRNA (35 µg/µL, 10×) | b.next (in-house) | N/A | N/A | -80 °C | [link](xref:nucleus-docs/docs/processes/make-trna/main#overview) |
| Protein mix | Protein Mix (PMix), 36 PURE proteins, 15 µg/µL | b.next (in-house) | N/A | N/A | -80 °C | [link](xref:nucleus-docs/docs/processes/make-36pot/main#overview) |
| Ribosomes | Ribosomes, 10 µM (5.55×) | b.next (in-house) | N/A | N/A | -80 °C | [link](xref:nucleus-docs/docs/processes/make-ribosomes/main#overview) |
| RNase inhibitor | RNase Inhibitor, Murine | NEB | M0314S | $87.00 | -25 °C to -15 °C | [link](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| Nuclease free water | Water, Nuclease-Free, for Molecular Biology | Sigma-Aldrich | W4502-1L | $88.40 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/w4502) |
| AHSL | N-(3-Oxohexanoyl)-L-homoserine lactone | Sigma-Aldrich (Aldrich) | K3007 | $40.70 | -20 °C | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/k3007) |
| Fluorescein | Fluorescein, NIST-Traceable Standard (50 µM nominal) | Invitrogen (Thermo Fisher Scientific) | F36915 | $554.00 | 2 °C to 8 °C, protect from light | [link](https://www.thermofisher.com/order/catalog/product/F36915) |
| Q5 polymerase | Q5® High-Fidelity 2X Master Mix | NEB | M0492S | $226.00 | -20 °C | [link](https://www.neb.com/en-us/products/m0492-q5-high-fidelity-2x-master-mix) |
| HF buffer | Included in Q5® High-Fidelity 2X Master Mix | NEB | M0492S | N/A (included) | -20 °C | [link](https://www.neb.com/en-us/products/m0492-q5-high-fidelity-2x-master-mix) |
| M13 Fwd primer | Custom DNA oligo: 5'-GTAAAACGACGGCCAGTG-3' | IDT | N/A (custom) | N/A | -20 °C | N/A |
| M13 Rev primer | Custom DNA oligo: 5'-CAGGAAACAGCTATGACCATG-3' | IDT | N/A (custom) | N/A | -20 °C | N/A |
| Magnesium | Magnesium acetate tetrahydrate | Sigma-Aldrich | M0631-100G | $34.80 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/m0631) |
| POPC | 16:0-18:1 PC (POPC), 25 mg/mL | Avanti Research | A80557 (formerly 850457) | $435.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Mineral oil | Mineral oil, light, BioReagent, for molecular biology | Sigma-Aldrich | M5904 | $80.90 | Room temperature | [link](https://www.sigmaaldrich.com/US/en/product/sigma/m5904) |
| Glucose | D-(+)-Glucose, ≥99.5% (GC) | Sigma-Aldrich | G8270-100G | $40.20 | Room temperature | [link](https://www.sigmaaldrich.com/US/en/product/sigma/g8270) |
| Optiprep | OptiPrep Density Gradient Medium, 60% (w/v) iodixanol | Sigma-Aldrich | D1556-250ML | $380.00 | Room temperature | [link](https://www.sigmaaldrich.com/US/en/product/sigma/d1556) |
| DMSO | Dimethyl sulfoxide, Hybri-Max, sterile-filtered, BioReagent, ≥99.7% | Sigma-Aldrich | D2650-100ML | $287.00 | Room temperature | [link](https://www.sigmaaldrich.com/US/en/product/sigma/d2650) |
:::
::::

<!-- STYLE: the source heading was the underlined run-in label "Day #2
(20260924)". It is promoted to a subsection heading here. -->
---

## Protocols

### Preparing linear DNA templates

Linear DNA templates were amplified from gBlocks by PCR using universal M13 forward/reverse primers, then cleaned up before use in cytosol reactions.

1. Resuspend each 1000 ng gBlock in 100 µL nuclease-free water (10 ng/µL stock). Resuspend primers to 100 µM.
2. Prepare a 7.5× master mix (250 µL reactions) of Q5 High-Fidelity 2X Master Mix, M13 forward and reverse primers, and nuclease-free water, omitting template.
3. Distribute 249 µL of the master mix per tube, then add 1 µL of the appropriate 10 ng/µL gBlock template to each (final reaction 250 µL). Composition in {numref}`tbl-composition-pcr`.
4. Run PCR (30 cycles): 30 s initial denaturation, then cycle through 10 s denaturation, 30 s annealing at 64 °C, and 45 s extension; finish with a 120 s final extension.
5. Clean up PCR products (NEB Monarch, T1130L). All samples were eluted in 30 µL across two 15 µL cleanups, each yielding ~200 ng/µL.

::::{admonition} Reaction composition
:class: dropdown

:::{table} PCR reaction composition. <!-- From the build file: "Standard reaction" and "Standard reaction (-template, -Fwd primer)" tables. The latter table labels its forward primer stock "10 µM," which doesn't reconcile with its own stated 0.5 µM final at 1.25 µL into 250 µL (that requires a 100 µM stock, matching the "Standard reaction" table and the Reagents table's M13 Fwd primer entry) — carried here as 100 µM, treating "10 µM" as a transcription slip. EsaO-PLA1, [EsaO]2-PLA1 and PLA1 were prepared in the same PCR batch for a parallel project; they are not used in this DevNote. -->
:label: tbl-composition-pcr
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | EsaO-mNG [µL] | [EsaO]2-mNG [µL] | EsaO-PLA1 [µL] | [EsaO]2-PLA1 [µL] | EsaR [µL] | mNG [µL] | PLA1 [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q5 High-Fidelity Master Mix | 2 | × | 1 | × | 125 | 125 | 125 | 125 | 125 | 125 | 125 |
| M13 Fwd primer | 100 | µM | 0.5 | µM | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 |
| M13 Rev primer | 100 | µM | 0.5 | µM | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 |
| Template (gBlock) | 10 | ng/µL | 0.04 | ng/µL | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Nuclease-free water | — | — | — | — | 121.5 | 121.5 | 121.5 | 121.5 | 121.5 | 121.5 | 121.5 |
| Total | | | | | 250 | 250 | 250 | 250 | 250 | 250 | 250 |
:::
::::
:::{div .dashed-hr}
:::

### Pre-expressing EsaR(D91G)

EsaR(D91G) is pre-expressed in a cell-free reaction containing the standard cytosol mastermix and EsaR(D91G) template DNA at a final concentration of 10 ng/µL (≈12 nM). The composition below is given per 10 µL; reactions were scaled up as needed for the day's total reaction volume and number of conditions.

::::{admonition} Reaction composition
:class: dropdown

:::{table} EsaR(D91G) pre-expression reaction, per 10 µL. <!-- The EsaR(D91G) template's stock concentration is not independently restated for this reaction, so its volume and the water volume it leaves are given as X — their actual values depend on whichever template stock is in hand, but the reaction's total volume stays consistent at 10 µL per unit. Scaling to other total volumes or batch sizes keeps these ratios fixed. -->
:label: tbl-composition-esar-preexpression
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume [µL] |
| --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 3 |
| tRNA | 10 | × | 1 | × | 1 |
| Protein mix | 8.33 | × | 1 | × | 1.2 |
| Ribosomes | 5.5 | × | 1 | × | 1.8 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.25 |
| EsaR(D91G) Template DNA | X | ng/µL | 10 | ng/µL | X |
| Nuclease-free water | — | — | — | — | X |
| Total | | | | | 10 |
:::
::::
:::{div .dashed-hr}
:::


### Base Nucleus cytosol protocol for sensor optimisation

Sensor optimisation reactions across all experiments in this DevNote shared a common base assembly:

1. Pre-express EsaR(D91G) in Nucleus cytosol as described above. Composition in {numref}`tbl-composition-esar-preexpression`.
2. Mix the pre-expressed EsaR with the sensor DNA and incubate for 15 min or 1 hr at 37 °C.

   :::{note}
   Volumes for pre-incubation can be calculated from each reaction composition as the sum of pre-expressed EsaR and sensor DNA. Typically, excess was prepared for each condition to ensure there was sufficient volume remaining post-incubation.
   :::
3. While the EsaR–DNA mixture incubates, prepare a mastermix of Nucleus cytosol, without DNA or water.
4. Add the premix to the Nucleus cytosol mastermix. Note: some conditions may require the premix to be topped-up with water prior to its addition.
5. Add AHSL (final 5 µM), either:
   - as a dedicated component pipetted directly into the mastermix at assembly (water in its place for the −AHSL condition), or
   - by splitting the fully assembled reaction in half and adding AHSL to one half.
6. Distribute in triplicate 10 µL volumes into a 384-well plate.
7. Read on a platereader (GFP, 37 °C, 6 hr timecourse).
:::{div .dashed-hr}
:::

*The following sections state how each experiment deviates from the above base protocol and include a reaction composition and platemap*

### EsaR titration into Nucleus cytosol reactions containing EsaO-mNG and [EsaO]2-mNG DNA

Deviates from the base protocol:
- Step 2: EsaR titrated across 0, 1, 4 or 7 µL per reaction, against a fixed 320.5 ng (12 nM) of either T7-\[EsaO\]-mNG-T7term or T7-\[EsaO\]2-mNG-t7term.
- Reaction scaled to 65 µL total.
- Step 5: AHSL added by splitting.

Reaction composition is in {numref}`tbl-composition-20260924`.

<!-- Composition table sourced from build file: build (Google Sheet), sheet
20260924_Repression_test_rxns, in CN-20260924_repressor_test. Mastermix
component volumes are the standard-reaction volumes at the distribution factor
the sheet states. That factor is "Distribute into 1x 23.72 µL (mNG), and 8x
47.44 µL (EsaO & [EsaO]2)". -->

::::{admonition} Reaction composition
:class: dropdown

:::{table} Reaction composition. Full sidecar: [`experiments/build-composition-20260924.csv`](./experiments/build-composition-20260924.csv).
:label: tbl-composition-20260924
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | mNG [µL] | EsaO-mNG (0 µL EsaR) [µL] | EsaO-mNG (1 µL EsaR) [µL] | EsaO-mNG (4 µL EsaR) [µL] | EsaO-mNG (7 µL EsaR) [µL] | \[EsaO\]2-mNG (0 µL EsaR) [µL] | \[EsaO\]2-mNG (1 µL EsaR) [µL] | \[EsaO\]2-mNG (4 µL EsaR) [µL] | \[EsaO\]2-mNG (7 µL EsaR) [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 9.85 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 |
| tRNA | 10 | × | 1 | × | 3.25 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 |
| Protein mix | 8.33 | × | 1 | × | 3.90 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 |
| Ribosomes | 5.5 | × | 1 | × | 5.91 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.81 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 |
| Sensor DNA Template | 200 | ng/µL | 10 | ng/µL | 1.54 | 2.87 | 2.87 | 2.87 | 2.87 | 3.25 | 3.25 | 3.25 | 3.25 |
| Pre-expressed EsaR | — | — | — | — | 0 | 0 | 2 | 8 | 14 | 0 | 2 | 8 | 14 |
| Nuclease free water | — | — | — | — | 7.23 | 14.69 | 12.69 | 6.69 | 0.69 | 14.31 | 12.31 | 6.31 | 0.31 |
| Total [µL] |   |   |   |   | 32.5 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 |
:::
::::

::::{admonition} Platemap
:class: dropdown

:::{platemap} ./experiments/20260924-repressor-test/build - 20260924_Platemap.csv
:height: 480px
:fields: EsaR Vol (uL), [AHSL] (uM), [Fluorescein] (uM)
:label: platemap-20260924
:::
::::

<!-- The platemap viewer reads the CSV directly. It does not replace the
build-composition table above, which carries per-component concentrations the
platemap itself does not record. -->
:::{div .dashed-hr}
:::

### Titrating EsaO-mNG and [EsaO]2-mNG DNA against fixed pre-expressed EsaR

Deviates from the base protocol:
- Step 2: pre-expressed EsaR fixed at 14 µL; sensor DNA titrated across 0.1–9 nM for each of T7-\[EsaO\]-mNG-T7term and T7-\[EsaO\]2-mNG-t7term.
- Reaction scaled to 65 µL total.
- Step 5: AHSL added by splitting.

Full reaction composition is in {numref}`tbl-composition-20260925`.

<!-- Composition table sourced from build file: build (Google Sheet), sheet
20260925_DNA_titration, in CN-20260925-DNA_titration. -->

::::{admonition} Reaction composition
:class: dropdown

:::{table} Reaction composition. Full sidecar: [`experiments/build-composition-20260925.csv`](./experiments/build-composition-20260925.csv).
:label: tbl-composition-20260925
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | mNG [µL] | EsaO-mNG (0.1 nM) [µL] | EsaO-mNG (0.5 nM) [µL] | EsaO-mNG (1 nM) [µL] | EsaO-mNG (3 nM) [µL] | EsaO-mNG (6 nM) [µL] | EsaO-mNG (9 nM) [µL] | \[EsaO\]2-mNG (0.1 nM) [µL] | \[EsaO\]2-mNG (0.5 nM) [µL] | \[EsaO\]2-mNG (1 nM) [µL] | \[EsaO\]2-mNG (3 nM) [µL] | \[EsaO\]2-mNG (6 nM) [µL] | \[EsaO\]2-mNG (9 nM) [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 9.85 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 | 19.70 |
| tRNA | 10 | × | 1 | × | 3.25 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 | 6.50 |
| Protein mix | 8.33 | × | 1 | × | 3.90 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 | 7.80 |
| Ribosomes | 5.5 | × | 1 | × | 5.91 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 | 11.82 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.81 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 | 1.62 |
| Sensor DNA Template | 10 / 10 / 150 / 150 / 150 / 150 | ng/µL | 0.1 / 0.5 / 1 / 3 / 6 / 9 | nM | 1.54 | 0.44 | 2.12 | 0.28 | 0.85 | 1.69 | 2.46 | 0.43 | 2.16 | 0.29 | 0.86 | 1.73 | 2.59 |
| Pre-expressed EsaR | — | — | — | — | 0 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 |
| Nuclease free water | — | — | — | — | 7.23 | 3.12 | 1.44 | 3.27 | 2.71 | 1.86 | 1.09 | 3.13 | 1.40 | 3.27 | 2.69 | 1.83 | 0.97 |
| Total [µL] |   |   |   |   | 32.5 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 |
:::
::::

::::{admonition} Platemap
:class: dropdown

:::{platemap} ./experiments/20260925-dna-titration/20260924-dna-titration-esar-fixed.csv
:height: 480px
:fields: EsaR Vol (uL), DNA Template (nM), [AHSL] (uM)
:wells: 384
:label: platemap-20260925
:::
::::
:::{div .dashed-hr}
:::

### Comparing unspent and spent pre-expressed EsaR added to [EsaO]2-mNG DNA reactions

Deviates from the base protocol:
- Step 1: EsaR instead pre-expressed for 17 hrs at 30 °C and held at 4 °C (rather than the standard 3 hrs at 37 °C).
- Step 2: pre-expressed EsaR fixed at 14 µL; sensor DNA titrated across 0.1, 0.5 and 1 nM of T7-\[EsaO\]2-mNG-t7term only.
- Reaction scaled to 70 µL total.
- Step 5: AHSL added by splitting.

Full reaction composition is in {numref}`tbl-composition-20260926`.

<!-- Composition table sourced from build file: build (Google Sheet), sheet
20260926-DNA_titration_EsaR_spent, in CN-20260926-DNA_titration_spent_EsaR.
The sheet's own comment reads: "Reaction volume increased to 35, but 14 µL EsaR
volume maintained. Lowered the relative amount of EsaR in each reaction by 1.5%
compared to previous experiment". -->

::::{admonition} Reaction composition
:class: dropdown

:::{table} Reaction composition. Full sidecar: [`experiments/build-composition-20260926.csv`](./experiments/build-composition-20260926.csv).
:label: tbl-composition-20260926
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | mNG [µL] | \[EsaO\]2-mNG (0.1 nM) [µL] | \[EsaO\]2-mNG (0.5 nM) [µL] | \[EsaO\]2-mNG (1 nM) [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 10.61 | 21.22 | 21.22 | 21.22 |
| tRNA | 10 | × | 1 | × | 3.50 | 7.00 | 7.00 | 7.00 |
| Protein mix | 8.33 | × | 1 | × | 4.20 | 8.40 | 8.40 | 8.40 |
| Ribosomes | 5.5 | × | 1 | × | 6.36 | 12.72 | 12.72 | 12.72 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.88 | 1.76 | 1.76 | 1.76 |
| Sensor DNA Template | 10 / 50 / 100 | ng/µL | 0.1 / 0.5 / 1 | nM | 1.66 | 0.46 | 0.46 | 0.46 |
| Pre-expressed EsaR | — | — | — | — | 0 | 14 | 14 | 14 |
| Nuclease free water | — | — | — | — | 7.79 | 4.44 | 4.44 | 4.44 |
| Total [µL] |   |   |   |   | 35 | 70 | 70 | 70 |
:::
::::

::::{admonition} Platemap
:class: dropdown

:::{platemap} ./experiments/20260926-dna-titration-esar-spent/20260926-nucleus-platemap-esao2-dna-titration-esar-spent.csv
:height: 480px
:fields: EsaR Vol (uL), DNA Template (nM), [AHSL] (uM)
:wells: 384
:label: platemap-20260926
:::
::::
:::{div .dashed-hr}
:::

### Effect of additional Mg on EsaR-dependent repression of [EsaO]2-mNG DNA

Deviates from the base protocol:
- Step 2: incubated for 1 hr instead of 15 min, with 0, 5, 10 or 20 mM Mg²⁺ added during this step.
- Step 5: AHSL pipetted directly into the mastermix as a dedicated component, not via splitting.
- Step 6: distributed in duplicate instead of triplicate.

Sensor DNA was provided so that the concentration in the final reaction was 0.5 nM. Composition in {numref}`tbl-composition-20261001`.

::::{admonition} Reaction composition
:class: dropdown

:::{table} Reaction composition. <!-- No build file exists for this day; final concentrations are calculated from the stock concentrations and volumes the log records. Magnesium concentrations are those reached in the EsaR–DNA–Mg pre-incubation (2.3 + 0.15 + 0.15 = 2.6 µL), not the diluted 10 µL final reaction — each Mg stock (346.7/173.3/86.6 mM) is diluted 0.15/2.6 to land on 20/10/5 mM. In the 0 mM Mg column, that 0.15 µL slot is water instead of Mg stock (see "Water" row). Reactions were scaled 3.3× (to 33 µL) for bulk pipetting before being distributed in triplicate 10 µL vols per well — see prose above. -->
:label: tbl-composition-20261001
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | 0 mM Mg [µL] | 5 mM Mg [µL] | 10 mM Mg [µL] | 20 mM Mg [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 3 | 3 | 3 | 3 |
| tRNA | 10 | × | 1 | × | 1 | 1 | 1 | 1 |
| Protein mix | 8.33 | × | 1 | × | 1.2 | 1.2 | 1.2 | 1.2 |
| Ribosomes | 5.5 | × | 1 | × | 1.8 | 1.8 | 1.8 | 1.8 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.25 | 0.25 | 0.25 | 0.25 |
| Sensor DNA Template | 22 | ng/µL | 0.5 | nM | 0.15 | 0.15 | 0.15 | 0.15 |
| Pre-expressed EsaR | — | — | — | — | 2.3 | 2.3 | 2.3 | 2.3 |
| Magnesium | — / 86.6 / 173.3 / 346.7 | mM | — / 5 / 10 / 20 | mM | 0 | 0.15 | 0.15 | 0.15 |
| Water (replacing Mg stock) | — | — | — | — | 0.15 | 0 | 0 | 0 |
| AHSL | — | — | 0 / 5 | µM | 0.15 | 0.15 | 0.15 | 0.15 |
| Total | | | | | 10 | 10 | 10 | 10 |
:::
::::

<!-- The log also reads: "Mix of DNA and EsaR pure reaction: Final is 0.332,
DNA stock at 22ng/µL, 2.6 overall* 3.5." The 22 ng/µL DNA stock is carried into
the table above, confirmed by calculation to give 0.5 nM (not the previously
stated 0.1 nM, a transcription slip) in the final 33 µL reaction: stock
molarity 22 ng/µL / 663,974.37 g/mol = 33.13 nM, diluted 0.495/33 into the
final reaction = 0.497 nM. "Final is 0.332" and "2.6 overall* 3.5" do not
reconcile against any other number in this log and are not inferred into the
table. The Mg stocks (X20/X10/X5) do reconcile: each diluted 0.15/2.6 into the
pre-incubation premix lands within rounding of the stated 20/10/5 mM. -->

::::{admonition} Platemap
:class: dropdown

:::{platemap} ./experiments/20261001-mg-osmo-sweep/20261001-mg-sweep-platemap.csv
:height: 480px
:label: platemap-20261001
:::
::::
:::{div .dashed-hr}
:::

### Effect of increasing EsaR DNA concentration on [EsaO]2-mNG DNA repression

Deviates from the base protocol:
- Step 2: the DNA added to the reaction is sensor DNA (4 ng/µL) diluted 1:1, either with water (−EsaR DNA) or with a 213 ng/µL EsaR template DNA stock (+EsaR DNA). This keeps the final sensor DNA concentration at 0.1 nM while increasing the EsaR template DNA concentration from 3.4 nM to 8.7 nM. This increases the EsaR template excess from 34× to 87×.
- Step 5: AHSL pipetted directly into the mastermix as a dedicated component, not via splitting.

<!-- The previous version of this paragraph also stated "Final reaction
volumes were 33 µL," matching the 2026-10-01 Mg sweep's scaled-batch volume.
This day's own composition table totals 10 µL with no scaled-batch column,
and nothing else in this day's log mentions a 33 µL batch, so that detail
looks like it was carried over from the Mg sweep day in error. Dropped here
rather than repeated; flagged for the author to confirm. -->

Reaction composition is in {numref}`tbl-composition-20261007`.

::::{admonition} Reaction composition
:class: dropdown

:::{table} Reaction composition. <!-- No build file exists for this day (the `build` Sheet in `CN-MB-20261007-EsaR_template_competition` is empty). Final concentrations are calculated from the stock concentrations and volumes the log records; mastermix stocks match the standard cytosol mastermix used throughout this work. "Pre-expressed EsaR (template DNA carryover)" is the residual, unreacted EsaR template DNA carried over from the pre-expression step, not EsaR protein — its concentration is reported here in nM DNA, present regardless of condition. The 0.33 µL DNA aliquot is a 1:1 (50:50) mix, split here into its two 0.165 µL halves: Reporter DNA (present in every condition) and either Added EsaR template (+EsaR DNA condition) or Water (−EsaR DNA condition). The reporter's 4 ng/µL stock (the "2×" stock the log refers to) was supplied by the author, not stated in the log excerpt itself; at 663,974.37 g/mol for [EsaO]2-mNG, 4 ng/µL diluted 0.165/10 into the full reaction gives 0.099 nM — matching the stated 0.1 nM final concentration. The 320 nM raw-PCR EsaR template stock, diluted 0.165/10, gives 5.28 nM ≈ 5.3 nM. -->
:label: tbl-composition-20261007
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | − EsaR DNA [µL] | + EsaR DNA (8.7 nM) [µL] |
| --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 3 | 3 |
| tRNA | 10 | × | 1 | × | 1 | 1 |
| Protein mix | 8.33 | × | 1 | × | 1.2 | 1.2 |
| Ribosomes | 5.5 | × | 1 | × | 1.8 | 1.8 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.25 | 0.25 |
| Pre-expressed EsaR (template DNA carryover) | 15 | nM DNA | 3.4 | nM DNA | 2.27 | 2.27 |
| Sensor DNA ([EsaO]2-mNG) | 4 | ng/µL | 0.1 | nM | 0.165 | 0.165 |
| Added EsaR template | — / 320 | nM DNA | — / 5.3 | nM DNA | 0 | 0.165 |
| Water (replacing EsaR template) | — | — | — | — | 0.165 | 0 |
| AHSL | — | — | 0 / 5 | µM | 0.15 | 0.15 |
| Total | | | | | 10 | 10 |
:::
::::

<!-- No build file exists for this day either. `build` in
`CN-MB-20261007-EsaR_template_competition` is an empty default Sheet, same
shape as the 2026-10-01 gap. 2.27 + 0.33 = 2.6, which matches the "2.6µL"
the log states, so that part of the arithmetic checks out. Whether the 0.15µL
AHSL/water volume sits inside the stated 7.4µL or on top of it is not stated,
and is not inferred here. The table above resolves it: 2.6 (EsaR-DNA premix)
+ 7.4 (rest) = 10 exactly, and the rest (7.4) matches the standard mastermix
(7.25) + AHSL/water (0.15), so the AHSL/water volume sits inside the stated
7.4 µL, not on top of it.

Separately, the log's own arithmetic reads "enhancing the 34x excess of DNA
template up to 77x." 8.7 nM / 0.1 nM = 87, not 77, matching the Results text
above and the 320 nM / 50:50 dilution math below — "77x" is carried here as
a probable transcription slip for "87x," not corrected in the log excerpt
itself. -->

::::{admonition} Platemap
:class: dropdown

:::{platemap} ./experiments/20261007-esar-template-competition/20261008-esao-mng-esar-ahsl.csv
:height: 480px
:fields: [EsaO-mNG] (nM), [EsaR] (nM), [AHSL] (uM)
:label: platemap-20261007
:::
::::
:::{div .dashed-hr}
:::

### Effect of lower reaction temperature on EsaR-dependent repression of [EsaO]2-mNG DNA

Deviates from the base protocol:
- Step 2: incubated for 1 hr instead of 15 min at 37 °C.
- Step 7: rather than the standard 3 hr incubation at 37 °C, reactions were instead incubated overnight at 25 °C and read the following day.
- Step 5: AHSL pipetted directly into the mastermix as a dedicated component, not via splitting.

<!-- As with the 2026-10-07 section above, this paragraph previously also
stated "Final reaction volumes were 33 µL," which doesn't match this day's
own composition table (10 µL total, no scaled-batch column) and isn't
mentioned anywhere else in this day's log. Dropped here rather than
repeated; flagged for the author to confirm. -->

Sensor DNA was provided so that the concentration in the final reaction was 0.1 nM. Reaction composition is in {numref}`tbl-composition-20261008`.

<!-- No build file exists for this day either, same gap as 2026-10-01 and
2026-10-07. Both tables are carried verbatim from the log. -->

::::{admonition} Reaction composition
:class: dropdown

:::{table} Reaction composition. <!--   No build file exists for this day. Final concentrations are calculated from the stock concentrations and volumes the log records. The DNA stock (4 ng/µL) is not restated in this day's own log excerpt — it is carried over from {numref}`tbl-composition-20261007`'s reporter DNA stock, since this experiment shares that day's plate, platemap, and raw data file; at 663,974.37 g/mol for [EsaO]2-mNG, 4 ng/µL diluted 0.15/10 gives 0.090 nM, close to the stated 0.1 nM. "Pre-expressed EsaR" has no stated stock or final concentration for this specific condition, unlike 2026-10-07's carryover value, and is not inferred here. -->
:label: tbl-composition-20261008
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | − EsaR [µL] | + EsaR [µL] |
| --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 3 | 3 |
| tRNA | 10 | × | 1 | × | 1 | 1 |
| Protein mix | 8.33 | × | 1 | × | 1.2 | 1.2 |
| Ribosomes | 5.5 | × | 1 | × | 1.8 | 1.8 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.25 | 0.25 |
| Sensor DNA Template ([EsaO]2-mNG) | 4 | ng/µL | 0.1 | nM | 0.15 | 0.15 |
| Pre-expressed EsaR | — | — | — | — | 0 | 2.45 |
| Water (replacing EsaR) | — | — | — | — | 2.45 | 0 |
| AHSL | — | — | 0 / 5 | µM | 0.15 | 0.15 |
| Total | | | | | 10 | 10 |
:::
::::

<!--::::{admonition} Platemap
:class: dropdown

:::{platemap} ./experiments/20261007-esar-template-competition/20261008-esao-mng-esar-ahsl.csv
:height: 480px
:fields: [EsaO-mNG] (nM), [EsaR] (nM), [AHSL] (uM)
:label: platemap-20261008
:::
::::-->
:::{div .dashed-hr}
:::

### Testing EsaR-dependent repression of [EsaO]2-mNG DNA in GUVs
:::{note}
 GUV synthesis follows the base protocol's early steps: pre-express EsaR, then incubate it with sensor DNA, before following its own procedure from there.
:::

**Stock preparation**

**Outer solution** is prepared by diluting a 2 M glucose stock with water to 1050 mM. *Ideally, this concentration would instead be matched to the osmolarity of the inner solution using an osmometer.* Dilution in {numref}`tbl-composition-outer`.

**AHSL** is dissolved directly in DMSO in the stock bottle to 50 mM. This is diluted to a 500 µM working solution using outer solution as the diluent and stored at −20 °C. Fresh working solutions are prepared every week.Dilution in {numref}`tbl-composition-ahsl`.

::::{admonition} Dilution tables
:class: dropdown

:::{table} Outer solution, per 10 mL prepared.
:label: tbl-composition-outer
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume per 10 mL [mL] |
| --- | --- | --- | --- | --- | --- |
| Glucose | 2 | M | 1050 | mM | 5.25 |
| Water | — | — | — | — | 4.75 |
| Total | | | | | 10 |
:::

:::{table} AHSL working solution, per 1 mL prepared, using the outer solution above as diluent.
:label: tbl-composition-ahsl
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume per 1 mL [µL] |
| --- | --- | --- | --- | --- | --- |
| AHSL | 50 | mM | 500 | µM | 10 |
| Outer solution (diluent) | 1050 | mM | 1039.5 | mM | 990 |
| Total | | | | | 1000 |
:::
::::

**EsaR-DNA mixture**

1. Pre-express EsaR(D91G) in a cell-free reaction at 24 nM template DNA, double the standard 12 nM, giving a final concentration of 5 nM in the GUV reaction. Composition in {numref}`tbl-volumes-20261009-esar`.
2. Incubate the pre-expressed EsaR with sensor DNA ([EsaO]2-mNG) for 1 hr at 37 °C to form the EsaR-DNA mixture.

**Emulsion phase transfer**

1. Dry 2 mg POPC under nitrogen, then under vacuum for at least 2 hours.
2. Resuspend the dried lipid film in 500 µL mineral oil (4 mg / mL).
3. Sonicate the lipid-in-oil mixture at room temperature for ~20 min.
4. Prepare the GUV inner solution in duplicate (2 × 20 µL), identical in both, including the EsaR-DNA mixture (above) in each. AHSL is not part of either inner solution — it is added at step 9. Composition per 20 µL prep in {numref}`tbl-volumes-20261009-guv`.
5. Add 200 µL of the lipid-in-oil mixture onto each inner solution and pipette up and down 9 times to form a water-in-oil emulsion.
6. Add each emulsion onto 250 µL outer solution (1050 mM glucose — ideally osmotically matched to the inner solution).
7. Centrifuge at 15 °C, 9,000 g, for 20 min to form GUVs.
8. Resuspend the resulting pellet in 100 µL outer solution.
9. For each condition:
   - **−AHSL**: add 1 µL outer solution to 99 µL GUV solution.
   - **+AHSL**: add 1 µL AHSL (500 µM) to 99 µL GUV solution.
10. Distribute in triplicate 30 µL vols in 384-well glass-bottom plate.
11. Image for 6 hrs at 37 °C.

<!-- No build file exists for this day either, same gap as 2026-10-01,
2026-10-07 and 2026-10-08. Both tables are carried verbatim from the log.

Step 10, "100 mL outer solution," is carried verbatim from the log. Every
other volume in this protocol is µL-scale; given the tiny (20 µL) inner
solution batch, 100 mL looks like a likely typo for 100 µL, but this is not
corrected here — flagged for the author to confirm. -->

::::{admonition} Reaction composition
:class: dropdown

:::{table} EsaR pre-expression reaction. <!-- No build file exists for this day; final concentrations are calculated from the stock concentrations and volumes the log records. The EsaR DNA Template stock (320 nM) is the same raw-PCR stock used in {numref}`tbl-composition-20261007`; its concentration cannot have changed, so "double the 12 nM used previously" is achieved by doubling the pipetted volume (0.375 µL for 12 nM, 0.75 µL for 24 nM here), not by a more concentrated stock. The log's own "EsaR DNA 0.15" row does not reflect this — 0.15 µL is the same boilerplate DNA volume used throughout this work's other protocols, so it looks like a copy-paste error rather than this day's actual pipetted volume. Water is adjusted here to keep the 10 µL total, but the exact total this day used is not independently confirmed. The log also lists an AHSL row in this pre-expression-only reaction — no reporter construct is present yet, so it has no obvious function here; carried verbatim from the log, not corrected or explained further. -->
:label: tbl-volumes-20261009-esar
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume [µL] |
| --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 3 |
| tRNA | 10 | × | 1 | × | 1 |
| Protein mix | 8.33 | × | 1 | × | 1.2 |
| Ribosomes | 5.5 | × | 1 | × | 1.8 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.25 |
| EsaR DNA Template | 320 | nM DNA | 24 | nM DNA | 0.75 |
| Water | — | — | — | — | 1.85 |
| AHSL | — | — | — | — | 0.15 |
| Total | | | | | 10 |
:::

:::{table} GUV inner solution <!--, scaled to the 20 µL actually prepared (the log's own component ratios total 10 µL; doubled here per the prose above). This 20 µL recipe is prepared twice, identically — AHSL is not part of either inner solution and is instead added to the outer solution of one of the two preps afterward (see the GUV synthesis steps above). The 4.5 µL "DNA-EsaR mixture" the log records (2.25 µL at the 10 µL basis) is split here into its two components, worked back from the stated final concentrations. The pre-expressed EsaR reaction (24 nM, {numref}`tbl-volumes-20261009-esar`) must contribute 5 × 20/24 = 4.17 µL to reach the stated 5 nM final, leaving 4.5 − 4.17 = 0.33 µL for the reporter DNA. At that volume, hitting the stated 0.1 nM final requires a reporter stock of 0.1 × 20/0.33 = 6.0 nM — 4.0 ng/µL at 663,974.37 g/mol for [EsaO]2-mNG — matching the same reporter DNA stock established in {numref}`tbl-composition-20261007`, independent confirmation that this day reused it.-->
:label: tbl-volumes-20261009-guv
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume [µL] |
| --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 6 |
| tRNA | 10 | × | 1 | × | 2 |
| Protein mix | 8.33 | × | 1 | × | 2.4 |
| Ribosomes | 5.5 | × | 1 | × | 3.6 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.5 |
| Pre-expressed EsaR reaction | 24 | nM DNA | 5 | nM DNA | 4.17 |
| Sensor DNA ([EsaO]2-mNG) | 4 | ng/µL | 0.1 | nM | 0.33 |
| Optiprep | — | — | — | — | 1 |
| Total | | | | | 20 |
:::
::::

---

# Results

:::{note}
The following data were collected by the authors during an intense 3-week collaboration at DevStudio held at Nucleus labs at b.next, San Francisco. To learn more about this collaboration see [here](https://devnotes.nucleus.engineering/articles/devstudio/week2). Whilst many experiments contain n=3 technical replicates, there was insufficient time to perform biological replicates across different days. Further work is planned to support the reproducibility of these results. 
:::

## EsaR titration fails to repress EsaO-mNG at 12 nM DNA

To determine the ratio of pre-expressed EsaR repressor to sensor DNA constructs that gives a well-defined ‘on’/’off’ state, we titrated increasing amounts of pre-expressed EsaR protein into Nucleus cytosol reactions containing single-operator EsaO-mNG or dual-operator [EsaO]2-mNG constructs. The sensor DNA was held at 12.2 nM (10 ng/µL) in all reactions. Each reaction was split, with AHSL added to one half to a final concentration of 5 µM.

No difference between the ‘on’ and ‘off’ states was observed at any EsaR volume tested ({numref}`fig-20260924-esao-titration`). Note that 7 µL is the highest achievable amount of EsaR that could be added without affecting the stoichiometry of Nucleus cytosol. This suggests either that the pre-expressed EsaR was non-functional, or that the sensor DNA remained in excess even at the highest EsaR-to-DNA ratio tested.

:::{figure} #fig-20260924-esao
:label: fig-20260924-esao-titration
:align: center
:width: 75%
Single-operator EsaO-mNG and dual-operator [EsaO]2-mNG with 0 and 7 µL pre-expressed EsaR, minus and plus 5 µM AHSL (n = 3 replicate wells; shaded region shows standard deviation). Reaction composition is in {numref}`tbl-composition-20260924`.
:::

<!-- [`fig-20260924-esao-titration`, notebook:`CN-20260924_repressor_test/platereader.ipynb`, platemap:`build - 20260924_Platemap.csv`, data source:`20260924-151252-cytation5-pure-timecourse-gfp-repressor_test.txt`, caption: (Single-operator EsaO-mNG and dual-operator [EsaO]2-mNG with 0 and 7 µL pre-expressed EsaR, minus and plus 5 µM AHSL.)] -->

## Repression scales with the EsaR : sensor DNA ratio

To test whether the sensor DNA templates had previously been in excess, we titrated the sensor DNA concentration while holding pre-expressed EsaR at the highest achievable concentration in each reaction. Repression was observed at concentrations lower than 1 nM DNA. At 0.1 nM and 0.5 nM, the single-operator construct gave fold-changes of approximately 1.5 and 1 respectively, while the dual-operator construct gave approximately 2 and 1.6 (Figure {numref}`%s <fig-20260925-0p1nm>`–{numref}`%s <fig-20260925-fold>`). At both concentrations, the dual-operator [EsaO]2-mNG construct showed higher fold-induction than the single-operator EsaO-mNG, consistent with the tighter repression expected from the additional EsaO operator. This suggests that the repressor behaviour exhibited *in vivo* may translate to PURE systems such as Nucleus cytosol.

Additionally, we noticed that the mNG control present at 15.6 nM was matched or exceeded in fluorescence signal by sensor DNA at 0.5 nM and upwards ({numref}`%s <fig-20260925-0p5nm>`–{numref}`%s <fig-20260925-3nm>`). This was surprising as the sensor DNA was 5- to 30-fold lower in concentration. We hypothesise this may be due to the pre-expressed EsaR preparation carrying over unspent energy components as well as transcription and translation factors that may supply additional capacity to the reaction. 


:::::{tab-set}

::::{tab-item} 0.1 nM DNA
:::{figure} #cn-20260925-fig1
:label: fig-20260925-0p1nm
:align: center
:width: 75%
0.1 nM sensor DNA at 7 µL pre-expressed EsaR and 5 µM AHSL, single operator against dual operator, alongside the mNG control (15.63 nM) (n = 3; shaded region shows standard deviation). Reaction composition is in {numref}`tbl-composition-20260925`.
:::

<!-- [`fig-20260925-0p1nm`, notebook:`CN-20260925-DNA_titration/platereader.ipynb`, platemap:`20260924-dna-titration-esar-fixed.csv`, data source:`20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`, caption: (0.1 nM sensor DNA at 7 µL pre-expressed EsaR and 5 µM AHSL, single operator against dual operator, alongside the mNG control (15.63 nM), n = 3, shaded region shows standard deviation.)] -->
::::

::::{tab-item} 0.5 nM DNA
:::{figure} #cn-20260925-fig2
:label: fig-20260925-0p5nm
:align: center
:width: 75%
0.5 nM sensor DNA at 7 µL pre-expressed EsaR and 5 µM AHSL, single operator against dual operator, alongside the mNG control (15.63 nM). Replicate wells are drawn individually rather than as a mean. Reaction composition is in {numref}`tbl-composition-20260925`.
:::

<!-- [`fig-20260925-0p5nm`, notebook:`CN-20260925-DNA_titration/platereader.ipynb`, platemap:`20260924-dna-titration-esar-fixed.csv`, data source:`20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`, caption: (0.5 nM sensor DNA at 7 µL pre-expressed EsaR and 5 µM AHSL, single operator against dual operator, alongside the mNG control (15.63 nM). Replicate wells are drawn individually rather than as a mean.)] -->
::::

::::{tab-item} 1 nM DNA
:::{figure} #cn-20260925-fig3
:label: fig-20260925-1nm
:align: center
:width: 75%
1 nM sensor DNA at 7 µL pre-expressed EsaR and 5 µM AHSL, single operator against dual operator, alongside the mNG control (15.63 nM) (n = 3; shaded region shows standard deviation). Reaction composition is in {numref}`tbl-composition-20260925`.
:::

<!-- [`fig-20260925-1nm`, notebook:`CN-20260925-DNA_titration/platereader.ipynb`, platemap:`20260924-dna-titration-esar-fixed.csv`, data source:`20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`, caption: (1 nM sensor DNA, single operator against dual operator, alongside the mNG control (15.63 nM), n = 3, shaded region shows standard deviation.)] -->
::::

::::{tab-item} 3 nM DNA
:::{figure} #cn-20260925-fig4
:label: fig-20260925-3nm
:align: center
:width: 75%
3 nM sensor DNA at 7 µL pre-expressed EsaR and 5 µM AHSL, single operator against dual operator, alongside the mNG control (15.63 nM) (n = 3; shaded region shows standard deviation). Reaction composition is in {numref}`tbl-composition-20260925`.
:::

<!-- [`fig-20260925-3nm`, notebook:`CN-20260925-DNA_titration/platereader.ipynb`, platemap:`20260924-dna-titration-esar-fixed.csv`, data source:`20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`, caption: (3 nM sensor DNA, single operator against dual operator, alongside the mNG control (15.63 nM), n = 3, shaded region shows standard deviation.)] -->
::::

::::{tab-item} Fold induction
:::{figure} #cn-20260925-fig5
:label: fig-20260925-fold
:align: center
:width: 75%
Steady-state AHSL fold induction (+AHSL / −AHSL) for EsaO-mNG and [EsaO]2-mNG at 0.1, 0.5, 1 and 3 nM sensor DNA (n = 3; n = 2 at 0.5 nM after excluding one low-outlier +AHSL well per construct; error bars show standard deviation).
:::

<!-- [`fig-20260925-fold`, notebook:`CN-20260925-DNA_titration/platereader.ipynb`, platemap:`20260924-dna-titration-esar-fixed.csv`, data source:`20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`, caption: (Steady-state AHSL fold induction (+AHSL / −AHSL) for EsaO-mNG and [EsaO]2-mNG at 0.1, 0.5, 1 and 3 nM sensor DNA, n = 3, n = 2 at 0.5 nM after excluding one low-outlier +AHSL well per construct, error bars show standard deviation.)] -->
::::

:::::

<!-- RESOLVED 2026-10-11 (partial): the author labelled a fourth producing
cell (`#| label: cn-20260925-fig4`, 3 nM DNA) and relabelled the fold-change
cell (`#| label: cn-20260925-fig5`), which now computes fold change through
3 nM rather than stopping at 1 nM. Both switched to the `quarto-label`
pattern, folded into the tab-set above alongside 0.1/0.5/1 nM. 6 nM and 9 nM
still have no producing cell in this notebook.

Original flagged text, kept for provenance:

**Three of six DNA concentrations are unreported.**
{numref}`tbl-composition-20260925` and the platemap both carry 0.1, 0.5, 1, 3,
6 and 9 nM for each construct. The log showed panels for 0.1, 0.5 and 1 nM
only.

**Answered and applied in part, review cycle v2, prompt 19.** These panels
should become figures, and three were added: {numref}`fig-20260925-all-conc`,
{numref}`fig-20260925-fold` and {numref}`fig-20260926-fold`.

Two gaps remain. No notebook cell plots the dual-operator construct across all
six concentrations, so {numref}`fig-20260925-all-conc` covers the single
operator only. And the fold-induction plots cover 0.1, 0.5 and 1 nM only,
because that is the range their own cell selects, so no fold change is reported
at 3, 6 or 9 nM. All three new figures are `static-png`, extracted from saved
cell outputs, because none of those cells carries a `#| label:` tag. -->

<!--
:::{admonition} 6 nM and 9 nM remain unreported for fold change
:class: warning
:name: review-20260925-missing-panels

{numref}`fig-20260925-fold` now reports fold change at 0.1, 0.5, 1 and 3 nM;
6 nM and 9 nM still have no producing cell for the fold calculation.
:::
-->

## Prolonged EsaR pre-expression doesn't improve repression but reduces yield

To test whether pre-expressing EsaR for longer increases the amount of repressor available and improves repression, we pre-expressed EsaR at 30 °C for 17 hrs instead of 37 °C for 3 hrs. EsaR volumes added to Nucleus cytosol reactions containing sensor DNA matched the previous experiment, and sensor DNA was limited to 0.1 nM, 0.5 nM and 1 nM. Data was compared to previous experiments in which EsaR was pre-expressed at 37 ˚C for 3 hrs. To ensure an accurate comparison, all data was first normalized to an internal 0.5 µM fluorescein control, before a second normalization step to a constitutive [EsaO]2-mNG without EsaR. This accounted for any batch-to-batch variations in Nucleus cytosol yields.

The fold-change between ‘on’ and ‘off’ states remained consistent at each DNA concentration ({numref}`fig-20260926-fold`), so extending pre-expression didn't improve repression. We did notice, however, that overall fluorescent yield decreased across all conditions when EsaR was pre-expressed at 30 ˚C for 17 hrs ({numref}`fig-20260926-endpoint`). We hypothesise that byproducts accumulating during the extended pre-expression, such as inorganic phosphate, may lower the yield of the subsequent reaction. Subsequent experiments maintained the pre-expression at 37 ˚C for 3 hrs; however, it is possible that a pre-expression period between 3–17 hrs is more optimal. Despite this, we don't expect the gains to be substantial as Nucleus cytosol reactions typically reach their steady-state by 3 hrs.

<!-- RESOLVED 2026-10-11: the author added fluorescein-normalized panels and a
fold-change plot, answering both asks below. {numref}`fig-20260926-normalized`
and {numref}`fig-20260926-fold` now source directly from labelled notebook
cells (`cn-20260926-fig1`, `cn-20260926-fig2`) via the `quarto-label` pattern.

Original flagged text, kept for provenance:

**Include fluorescein control in each graph, and also plot fold
change/steady state ratio of induced:uninduced to enable comparison between DNA
titration**. -->

:::::{tab-set}

::::{tab-item} Timecourse
:::{figure} #cn-20260926-fig1
:label: fig-20260926-normalized
:align: center
:width: 100%
Time-course fluorescence for dual-operator [EsaO]2-mNG, comparing EsaR pre-expressed for 3 hours at 37 °C against 17 hours at 30 °C. Fluorescence is calibrated to fluorescein and batch-corrected to the mNG control. Sensor DNA was tested at 0.1, 0.5 and 1 nM, with and without 5 µM AHSL. The mNG control is used only for the batch correction and is not plotted. Shaded regions show standard deviation across three replicate wells. Reaction composition is in {numref}`tbl-composition-20260926`.
:::

<!-- [`fig-20260926-normalized`, notebook:`CN-20260926-DNA_titration_spent_EsaR/platereader.ipynb`, platemap:`20260926-nucleus-platemap-esao2-dna-titration-esar-spent.csv`, data source:`20260926-115326-synergy2-pure-timecourse-gfp-DNA_titration_EsaR_spent.txt`, caption: (Time-course fluorescence for dual-operator [EsaO]2-mNG, EsaR pre-expressed 3 hours at 37C versus 17 hours at 30C, calibrated to fluorescein and batch-corrected to the mNG control, sensor DNA at 0.1, 0.5 and 1 nM with and without 5 µM AHSL, shaded regions show standard deviation across three replicate wells.)] -->
::::

::::{tab-item} Fold change (- AHSL / + AHSL)
:::{figure} #cn-20260926-fig2
:label: fig-20260926-fold
:align: center
:width: 55%
Fold-induction for [EsaO]2-mNG, comparing EsaR pre-expressed for 17 hours at 30 °C against 3 hours at 37 °C. Fluorescence is calibrated to 0.5 µM fluorescein. Sensor DNA was tested at 0.1, 0.5 and 1 nM. Error bars show standard deviation across three replicate wells, except at 1 nM for the 30 °C preparation and 0.5 nM for the 37 °C preparation. At each of these two conditions, one low-outlier +AHSL well was excluded, leaving two replicates.
:::

<!-- [`fig-20260926-fold`, notebook:`CN-20260926-DNA_titration_spent_EsaR/platereader.ipynb`, platemap:`20260926-nucleus-platemap-esao2-dna-titration-esar-spent.csv`, data source:`20260926-115326-synergy2-pure-timecourse-gfp-DNA_titration_EsaR_spent.txt`, caption: (Fold-induction for [EsaO]2-mNG, EsaR pre-expressed 17 hours at 30C versus 3 hours at 37C, calibrated to 0.5 µM fluorescein, sensor DNA at 0.1, 0.5 and 1 nM, n = 3 except n = 2 at 1 nM (30C) and 0.5 nM (37C) after excluding one low-outlier +AHSL well at each, error bars show standard deviation.)] -->
::::

::::{tab-item} End-point
:::{figure} #cn-20260926-fig3
:label: fig-20260926-endpoint
:align: center
:width: 55%
End-point fluorescence for [EsaO]2-mNG, comparing EsaR pre-expressed for 17 hours at 30 °C against 3 hours at 37 °C. Fluorescence is calibrated to fluorescein and batch-corrected to the mNG control. Sensor DNA was tested at 0.1, 0.5 and 1 nM. Error bars show standard deviation across three replicate wells, except at 1 nM for the 30 °C preparation and 0.5 nM for the 37 °C preparation. At each of these two conditions, the same low-outlier +AHSL well excluded in {numref}`fig-20260926-fold` was excluded here too, leaving two replicates.
:::

<!-- [`fig-20260926-endpoint`, notebook:`CN-20260926-DNA_titration_spent_EsaR/platereader.ipynb`, platemap:`20260926-nucleus-platemap-esao2-dna-titration-esar-spent.csv`, data source:`20260926-115326-synergy2-pure-timecourse-gfp-DNA_titration_EsaR_spent.txt`, caption: (End-point fluorescence for [EsaO]2-mNG, EsaR pre-expressed 17 hours at 30C versus 3 hours at 37C, calibrated to fluorescein and batch-corrected to mNG control, sensor DNA at 0.1, 0.5 and 1 nM, n = 3 except n = 2 at 1 nM (30C) and 0.5 nM (37C) after excluding the same low-outlier +AHSL well as the fold-induction figure, error bars show standard deviation.)] -->
::::

:::::

## Magnesium doesn't improve dynamic range but longer pre-incubation does

With the assumption that additional Mg²⁺ could improve EsaR–DNA binding, we next tested whether supplementing the EsaR–DNA pre-incubation with magnesium could strengthen repression. Sensor DNA and EsaR were pre-incubated together with 0, 5, 10 or 20 mM additional Mg²⁺. Contrary to previous experiments, incubation time was increased from 15 minutes to 1 hour at 37 °C. Pre-incubations were then added to the final cytosol reaction.

Magnesium did not alter the dynamic range at any concentration tested ({numref}`fig-20261001-mg-sweep`), and 20 mM markedly reduced overall yield. The longer pre-incubation, however, improved the switch from two-fold induction with the standard 15-minute pre-incubation to approximately three-fold across all conditions tested, with individual replicates reaching as high as four-fold ({numref}`fig-20261001-mg-sweep-fold`).
<!-- Results narrative supplied by the reviewer in review cycle v2, prompt 22,
and carried verbatim. The source log carries no results narrative. -->

:::::{tab-set}

::::{tab-item} Timecourse
:::{figure} #mbcn-20261001-fig1
:label: fig-20261001-mg-sweep
:align: center
:width: 100%
Time-course fluorescence for [EsaO]2-mNG, with 0, 5 or 10 mM additional magnesium added during the EsaR–DNA pre-incubation. Reactions were prepared with and without 5 µM AHSL (n = 2). Reaction composition is in {numref}`tbl-composition-20261001`.
:::

<!-- [`fig-20261001-mg-sweep`, notebook:`2026-10-01-MB-MgSweep/20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.ipynb`, platemap:`20261001-mg-sweep-platemap.csv`, data source:`20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.txt`, caption: (Time-course fluorescence for [EsaO]2-mNG, 0, 5 or 10 mM additional magnesium during the EsaR-DNA pre-incubation, with and without 5 µM AHSL, n = 2.)] -->
::::

::::{tab-item} Fold change
:::{figure} #mbcn-20261001-fig2
:label: fig-20261001-mg-sweep-fold
:align: center
:width: 55%
Fold-induction for [EsaO]2-mNG at 0, 5 and 10 mM magnesium, after pre-incubating EsaR with the DNA for 1 hour at 37 °C. Error bars show standard deviation across two replicate wells.
:::

<!-- [`fig-20261001-mg-sweep-fold`, notebook:`2026-10-01-MB-MgSweep/20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.ipynb`, platemap:`20261001-mg-sweep-platemap.csv`, data source:`20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.txt`, caption: (Fold-induction for [EsaO]2-mNG at 0, 5 and 10 mM magnesium, EsaR pre-incubated with DNA for 1 hour at 37C, error bars show standard deviation across two replicate wells.)] -->
::::

:::::



<!-- :::{admonition} The 20 mM magnesium arm is unreported
:class: warning
:name: review-20261001-missing-arm

The platemap carries four magnesium levels: 0, 5, 10 and 20, each minus and
plus AHSL, in two wells apiece. The log names "5, 10, 20 locally" and gives a
stock for each. Cell 8 plots 0, 5 and 10 only. The 20 mM wells were run and
have no reported panel.

**Answered, review cycle v2, prompt 20.** It is unreported because adding that
much Mg in Nucleus cytosol poisons the reaction. Carried into the Results
narrative above.
::: -->

## EsaR DNA template competition improves sensor dynamic range but reduces yield

Thus far, any EsaR template present in the final cytosol reaction was carryover from the initial EsaR pre-expression. This gave a final concentration of ~3.4 nM, a 34-fold excess over the 0.1 nM sensor DNA. To further deepen the 'off' state, 5.3 nM EsaR template was added by diluting the sensor DNA stock in EsaR template rather than water. This brought the total EsaR template in the final reaction to 8.7 nM, an 87-fold excess over the sensor DNA. This served two purposes. It increased the overall amount of EsaR available to repress the sensor DNA, and it continuously diverted Nucleus cytosol resources away from sensor DNA expression.

As expected, expressing additional EsaR reduced overall fluorescence yield roughly four-fold ({numref}`fig-20261007-normalized`). This came with an improved dynamic range, rising from 2.8 without added EsaR template to a reliable 4-fold change with it ({numref}`fig-20261007-fold`).

:::::{tab-set}

::::{tab-item} Timecourse
:::{figure} #mbcn-20261007-fig1
:label: fig-20261007-normalized
:align: center
:width: 100%
Time-course fluorescence for EsaO-mNG at 0.1 nM, with and without 8.7 nM added EsaR DNA template, each with and without AHSL (n = 3). Fluorescence is raw RFU. Reaction composition is in {numref}`tbl-composition-20261007`.
:::
::::

::::{tab-item} Fold change
:::{figure} #mbcn-20261007-fig2
:label: fig-20261007-fold
:align: center
:width: 65%
Fold-induction for EsaO-mNG at 0.1 nM, with and without 8.7 nM added EsaR DNA template (n = 3). Error bars show standard deviation.
:::
::::

:::::

<!-- [`fig-20261007-normalized`, notebook:`CN-MB-20261007-EsaR_template_competition/platereader.ipynb`, platemap:`20261008-esao-mng-esar-ahsl.csv`, data source:`20261007-170653-YH Cytosol comparison_CH.txt`, caption: (Time-course fluorescence for EsaO-mNG at 0.1 nM, with and without 8.7 nM added EsaR DNA template, with and without AHSL, n = 3, raw RFU.)] -->

<!-- [`fig-20261007-fold`, notebook:`CN-MB-20261007-EsaR_template_competition/platereader.ipynb`, platemap:`20261008-esao-mng-esar-ahsl.csv`, data source:`20261007-170653-YH Cytosol comparison_CH.txt`, caption: (Fold-induction for EsaO-mNG at 0.1 nM, with and without 8.7 nM added EsaR DNA template, n = 3, error bars show standard deviation.)] -->

<!--
:::{admonition} Open items on 2026-10-07
:class: warning
:name: review-20261007-open

**Resolved, 2026-10-12.** The author added `#| label:` tags
(`mbcn-20261007-fig1`, `mbcn-20261007-fig2`) to producing cells for
{numref}`fig-20261007-normalized` and {numref}`fig-20261007-fold`, which now
source directly from the notebook via the `quarto-label` pattern. The
overnight 25 ˚C endpoint figure was moved out of this tab-set entirely — it
now has its own producing cell (`mbcn-20261008-fig1`) and its own Results
section, {numref}`fig-20261008-overnight`, rather than being folded in here.

Original flagged text, kept for provenance: no cell in `platereader.ipynb`
produced any of the three figures. The notebook loaded the correct raw data
file and the correct platemap, through cell 6's Drive download block. Its own
plotting cells, 18 and 19, each charted one condition pair rather than the
four-condition overlay or the fold-change ratio shown here.

**The platemap date and the raw data date disagree.** The platemap,
`20261008-esao-mng-esar-ahsl.csv`, is dated 2026-10-08. The raw data file and
the folder name both read 2026-10-07. This is the same pattern already flagged
for the 2026-09-25 and 2026-09-26 platemaps.

**The raw data filename does not name this experiment.** It reads
`20261007-170653-YH Cytosol comparison_CH.txt`, which names neither EsaR nor
EsaO nor the folder's own authors, CN and MB. Confirm it is the right file.

**The stated EsaR concentration disagrees with the platemap and the figure
legends.** The log's own arithmetic gives "Final EsaR concentration is 3.4nM".
The platemap and both figure legends read `EsaR (8 nM)`. The two numbers could
describe different stages of the reaction, the pre-incubation mix against the
final reaction, which is the same distinction review cycle v2 settled for the
magnesium basis on 2026-10-01. Or one of the two numbers is wrong. Not
resolved here.

**Resolved, 2026-10-18.** Both numbers are correct and describe different
conditions, not different stages. 3.4 nM is the carryover-only baseline (no
added EsaR template); 8.7 nM (rounded to 8 nM in the platemap and figure
legends) is that same carryover plus the 5.3 nM EsaR template added to deepen
the 'off' state. The body text above now states both figures explicitly.

**One plot title in the notebook names the wrong construct.** Cell 18's title
reads "0.1 nM [Esao]2-mNG DNA titration", but the cell selects data named
`EsaO-mNG (0.1 nM)`, the single-operator construct, not `[EsaO]2-mNG`. The
plotted data and the platemap agree with each other; only the title text is
wrong.

**Resolved, 2026-10-18.** The producing cell for {numref}`fig-20261007-normalized`
(`mbcn-20261007-fig1`) now reads "EsaO-mNG" in both panel titles, matching the
single-operator construct actually plotted.
:::
-->

## Lower reaction temperatures increase sensor dynamic range

To test whether lower reaction temperatures could both stabilise EsaR-DNA binding, and slow T7 kinetics to limit EsaR being knocked off the sensor DNA, reactions were incubated at 25 ˚C overnight rather than 37 ˚C for 3 hrs. Ideally, this would reduce expression from sensor DNA that was insufficiently repressed. 

Reactions were incubated overnight in a thermocycler and measured on a platereader the following day. The highest fold change across all experiments was recorded at ~ 5.8. This suggests that temperature plays an important role in repression within the system. Timecourse reactions should be recorded in future to understand this in more detail.

:::{figure} #mbcn-20261008-fig1
:label: fig-20261008-overnight
:align: center
:width: 55%
Background-corrected GFP fluorescence for 0.1 nM [EsaO]2-mNG DNA after overnight incubation at 25 °C. Reactions were run with and without 5 µM AHSL. Reaction composition is in {numref}`tbl-composition-20261008`.
:::

<!-- [`fig-20261008-overnight`, notebook:`CN-MB-20261007-EsaR_template_competition/platereader.ipynb`, platemap:`20261008-esao-mng-esar-ahsl.csv`, data source:`20261007-170653-YH Cytosol comparison_CH.txt`, caption: (Background-corrected GFP fluorescence for 0.1 nM [EsaO]2-mNG DNA after overnight incubation at 25 °C. Reactions were run with and without 5 µM AHSL.)] -->

## Developer cells encapsulating sensor DNA detect AHSL in solution

To take a step towards producing a functional developer cell that can sense bacteria through the detection of secreted AHSL, GUVs were prepared encapsulating Nucleus cytosol, 5 nM EsaR template, and 0.1 nM sensor DNA. Note the EsaR template was present at a final concentration of 5 nM by increasing the EsaR template in the pre-expression reaction to 24 nM. This method of preparation had not previously been tested in bulk Nucleus cytosol; that characterisation will be done in future. GUVs samples were split, with 5 µM AHSL added to one half. Samples were loaded in a 384-well plate and imaged for 6 hrs at 37˚C. 

Images show the final timepoint for all conditions collected on a Cephla microscope. Each image was processed in Python using matplotlib applying a consistent vmin/vmax across all wells. GUVs in the + AHSL conditions are markedly brighter than the - AHSL conditions, demonstrating that GUV-encapsulated sensor DNA detects AHSL in solution and derepresses mNG production.

:::{figure} #microscopy-exp-01
:label: fig-20261009-guv-ahsl
:align: center
:width: 100%
Dual-operator [EsaO]2-mNG encapsulated in GUVs with pre-expressed EsaR, three replicate wells each minus and plus 5 µM AHSL. Green LUT, vmin/vmax 1200:4500, 20 µm scale bar. Reaction composition is in {numref}`tbl-volumes-20261009-esar` and {numref}`tbl-volumes-20261009-guv`.
:::

<!-- [`fig-20261009-guv-ahsl`, notebook:`CN-microscopy-01.ipynb`, platemap:`none`, data source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/201009o_EsaR_mNG_0.1_0.5_K_L_2026-10-09_19-47-50.861429.zarr`, caption: (Dual-operator [EsaO]2-mNG encapsulated in GUVs with pre-expressed EsaR, minus and plus AHSL.)] -->

<!--
:::{admonition} Open items on 2026-10-09
:class: warning
:name: review-20261009-open

**The log's cell label and the notebook's cell label disagree by one
character.** The log cites `microscopy-exp-0`; the actual `#| label:` tag in
`CN-microscopy-01.ipynb` reads `microscopy-exp-01`. The figure above sources
from the notebook's real label, carried verbatim — not the log's citation of
it, which appears to be a transcription slip.

**The log's own word choice reads "depression," likely meaning
"de-repression."** EsaR represses the [EsaO]2-mNG reporter; AHSL relieves
that repression, consistent with every other "on"/"off" result in this
DevNote where +AHSL wells are brighter. Carried as the log states it rather
than silently corrected, per the same convention applied to the 2026-09-26
cell-label year typo.
:::
-->

---

# What's next

- Engineer the {ref}`EsaR(D91G) construct <seq-esar-d91g>` for increased yield. Modify the
  5' UTR sequence and codon optimise to maximise the amount of protein
  produced.
- Test whether it is possible to increase repression by adding a
  third EsaO box to the sensor DNA. 
- Furthermore, search the literature / perform random mutagenesis to determine
  whether EsaO mutations can promote increased EsaR binding.
- Purchase recombinantly purified EsaR protein (available from [Cusabio](https://www.cusabio.com/Recombinant-Protein/Recombinant-Transcriptional-activator-protein-esaR--esaR--12936539.html)). Add
  purified EsaR to cytosol reactions containing sensor DNA in >100x excess in
  an attempt to achieve maximal gene repression. Test in bulk reactions first
  and then in GUVs.
- Once optimised, test sensor DNA in the [London Node: colour-change module](:https://devnotes.nucleus.engineering/articles/01a12e6c-b511-7d30-aa95-002d386f751e) to produce a visual rather than fluorescence-based readout.

---

# Resources

Reaction composition, one sidecar per day. No sidecar exists for 2026-10-01
or 2026-10-07, because neither folder has a build file.

- [`experiments/build-composition-20260924.csv`](./experiments/build-composition-20260924.csv)
- [`experiments/build-composition-20260925.csv`](./experiments/build-composition-20260925.csv)
- [`experiments/build-composition-20260926.csv`](./experiments/build-composition-20260926.csv)

Analysis notebooks.

- [`experiments/20260924-repressor-test/platereader.ipynb`](./experiments/20260924-repressor-test/platereader.ipynb)
- [`experiments/20260925-dna-titration/dna-titration.ipynb`](./experiments/20260925-dna-titration/dna-titration.ipynb)
- [`experiments/20260926-dna-titration-esar-spent/dna-titration-esar-spent.ipynb`](./experiments/20260926-dna-titration-esar-spent/dna-titration-esar-spent.ipynb)
- [`experiments/20261001-mg-osmo-sweep/20261001-mg-osmo-sweep.ipynb`](./experiments/20261001-mg-osmo-sweep/20261001-mg-osmo-sweep.ipynb)
- [`experiments/20261007-esar-template-competition/esar-template-competition.ipynb`](./experiments/20261007-esar-template-competition/esar-template-competition.ipynb)

Platemaps.

- [`experiments/20260924-repressor-test/build - 20260924_Platemap.csv`](./experiments/20260924-repressor-test/build%20-%2020260924_Platemap.csv)
- [`experiments/20260925-dna-titration/20260924-dna-titration-esar-fixed.csv`](./experiments/20260925-dna-titration/20260924-dna-titration-esar-fixed.csv)
- [`experiments/20260926-dna-titration-esar-spent/20260924-esao2-dna-titration.csv`](./experiments/20260926-dna-titration-esar-spent/20260924-esao2-dna-titration.csv)
- [`experiments/20261001-mg-osmo-sweep/20261001-mg-sweep-platemap.csv`](./experiments/20261001-mg-osmo-sweep/20261001-mg-sweep-platemap.csv)
- [`experiments/20261007-esar-template-competition/20261008-esao-mng-esar-ahsl.csv`](./experiments/20261007-esar-template-competition/20261008-esao-mng-esar-ahsl.csv)

Raw instrument data.

- [`experiments/20260924-repressor-test/20260924-151252-cytation5-pure-timecourse-gfp-repressor_test.txt`](./experiments/20260924-repressor-test/20260924-151252-cytation5-pure-timecourse-gfp-repressor_test.txt)
- [`experiments/20260925-dna-titration/20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`](./experiments/20260925-dna-titration/20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt)
- [`experiments/20260926-dna-titration-esar-spent/20260926-115326-synergy2-pure-timecourse-gfp-DNA_titration_EsaR_spent.txt`](./experiments/20260926-dna-titration-esar-spent/20260926-115326-synergy2-pure-timecourse-gfp-DNA_titration_EsaR_spent.txt)
- [`experiments/20261001-mg-osmo-sweep/20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.txt`](./experiments/20261001-mg-osmo-sweep/20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.txt)
- [`experiments/20261007-esar-template-competition/20261007-170653-YH Cytosol comparison_CH.txt`](<./experiments/20261007-esar-template-competition/20261007-170653-YH%20Cytosol%20comparison_CH.txt>)

---

# References

:::{bibliography}
:::
