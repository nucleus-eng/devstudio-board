<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

# Overview

Developer cells encapsulating Nucleus Cytosol can be programmed to communicate with their external environment using genetically encoded sensors. Synthetic biology has produced DNA sensors for a range of natural signalling molecules. One example is acyl-homoserine lactones (AHSLs), small molecules secreted by bacteria that regulate gene expression in response to population density. A developer cell programmed to sense AHSL and produce a detectable output could enable sensitive detection of bacteria in specific environments. We envision these developer cells detecting food spoilage or contamination in medical settings.

Towards this goal, we programme developer cells to sense AHSL using the *Pantoea stewartii* repressor protein, EsaR. In the absence of its cognate ligand, 3-oxo-C6-HSL, EsaR natively binds the EsaO operator where it is thought to occlude RNA polymerase and prevent transcription. In our case, we insert one or two EsaO operators downstream of the T7 promoter, blocking transcription in Nucleus cytosol until AHSL is added ({numref}`fig-esar-sensing`). EsaR has previously been co-expressed with an EsaO-controlled reporter both in bulk PURE reactions, and inside synthetic cells; however, the lag in EsaR expression was thought to result in early unrepressed transcription producing variable outputs {cite}`tang2018,chizzolini2017`. An alternative system supplied EsaR to lysate-encapsulated synthetic cells by pre-expressing EsaR in *E. coli* prior to lysate harvesting {cite}`ding2018`. This ensured that EsaR was present throughout the entire reaction; however, lysate-based systems often pose a challenge to further engineering due to their undefined composition.

To benefit from a defined chemical composition, and to limit early unrepressed transcription, we instead pre-express EsaR in Nucleus cytosol and pre-incubate it with the reporter DNA so that operator sites are occupied before the template enters the final reaction. We test single and dual operator reporters, the latter inspired by {cite}`shong2013`, in bulk cytosol reactions, optimising reaction conditions for increased sensor dynamic range before constructing developer cells that can sense exogenously added AHSL. We hope to build upon this work by embedding the developer cells in a hydrogel matrix, increasing their stability and progressing towards a deployable device ([DevStudio: London Node LuxR demo](https://devnotes.nucleus.engineering/articles/01a1121a-7513-7ec7-8378-0326c6b3630b)).

:::{figure} figures/EsaR-sensing.png
:label: fig-esar-sensing

EsaO/EsaR-dependent transcriptional regulation. EsaR binds the EsaO box preventing T7 polymerase from transcribing an mNeonGreen reporter protein. Upon binding of a AHSL signal, EsaR leaves the DNA re-enabling transcription.
:::

---

# Objectives

- Establish the pre-expressed EsaR : reporter DNA molar ratio needed to produce a defined 'on'/'off' state.
- Optimise sensor dynamic range by varying reaction conditions.
- Validate the optimised sensor in GUVs, as a step toward a deployable developer-cell sensor.


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

**Title and authors.** No source log carries a Specification table or an
Authors table. `curvenote.yml` holds `[PLEASE FILL IN]` for both, with
candidate text in comments. Three Log folders are prefixed `CN`, one is
prefixed `MB` whose notebook names `JM-MB`, and the fifth,
`CN-MB-20261007-EsaR_template_competition`, is prefixed jointly.

**Answered in part, review cycle v2, prompt 1.** Three authors named, with
emails: Charlie Newell, Jonah McDonald and Manuel Bibrowski. The Doc first
wrote "Chalie"; the email the author then supplied reads `charlie`, so the
DevNote uses Charlie.

Each affiliation is inferred from the author's email domain, which is evidence
rather than a statement by the author. Confirm University College London,
King's College London and Imperial College London, and confirm the author
order.

The title is set, to "EsaO/R-deGFP AHL Detector". It was not supplied through
the review Doc. It appeared in `curvenote.yml` in the working tree and was
picked up by the asset-assembly commit.

Two things on it. It spells the signal "AHL", while prompt 12 ruled that
everything is written as AHSL, so the title and the body now disagree. And the
candidate titles this DevNote recorded from the platemap were never adopted,
which is correct, but nobody has confirmed this one against them.

No ORCID is recorded for any author.

 RESOLVED 2026-10-11: the author re-labelled the producing cell
(`#| label: fig-20260924-esao`) in `platereader.ipynb`
(`CN-20260924_repressor_test`), and {numref}`fig-20260924-esao-titration`
now sources directly from it via the `quarto-label` pattern. That cell's
plot already contains both the single- and dual-operator panels in one
image, so the formerly separate dual-operator figure (`fig-20260924-esao2`)
was removed rather than also relabelled to a second producing cell — the
same data shown twice would be redundant, not a second figure.

Original flagged text, kept for provenance:

**Two figures have no surviving producing cell.** {numref}`fig-20260924-esao`
and {numref}`fig-20260924-esao2` were pasted into the 2026-09-24 log. The
`platereader.ipynb` in `CN-20260924_repressor_test` loads the right data file
and the right platemap. Its cell 15 plots the same 0, 1, 4 and 7 µL EsaR
series. No cell in it produces the two-panel `EsaR/EsaO` figure that the log
shows. The notebook was saved on 2026-09-26, after the figures were pasted.
Restore those cells before publication.

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

**Resolved, 2026-10-12.** The three PLA1 templates (`T7-PLA1-t7term`,
`T7-\[EsaO\]-PLA1-T7term`, `T7-\[EsaO\]2-PLA1-t7term`) were dropped from
{numref}`tbl-constructs` — they were prepared on 2026-09-23 but appear in no
experiment in this DevNote, and chasing their sequences was not worth it for
unused constructs. `T7-mNG-t7term`, the unrepressed control on all three CN
days, was added back on 2026-10-18 once its source file was supplied, so
{numref}`tbl-constructs` now carries four supplied and verified constructs.

None of the four is in `nucleus-eng/DNA`, on `main` or on
`devcells/devstudio-constructs`. The repo carries the neighbouring
quorum-sensing family but nothing for EsaR or EsaO. These belong in that repo,
and once they are there the DevNote can reference them by GitHub URL and carry
no local copy.

 **Agarose gel image missing.** The 2026-09-24 log states that the
constructs were run on an agarose gel and instructs "Ask Manuel for image". No
gel image exists in any of the four Log folders.

**Resolved, review cycle v2, prompt 4.** The agarose gel is not relevant to
this DevNote and is not reported. 

**No build file for 2026-10-01.** The file named `build` in that folder is a
platemap. It holds `Well`, `Date`, `Experiment`, `Name` and `Type` and nothing
else, so it carries no component, no concentration and no volume. No sidecar
exists for this day.

**Answered, review cycle v2, prompt 5, and deferred.** This will be addressed
later. The volume table stands in the meantime.

**Superseded, 2026-10-18.** A reaction composition table
({numref}`tbl-composition-20261001`) was built by hand from the log's own
stock concentrations and volumes, since no build file will be supplied. This
also surfaced a transcription slip: the sensor DNA final concentration was
stated as 0.1 nM but calculates to 0.5 nM from the logged 22 ng/µL stock,
and has been corrected throughout.
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

To quantify sensor output we chose mNeonGreen, a bright fluorescent protein commonly used to report on cell-free protein synthesis {cite}`copeland2022`. This would enable us to rapidly optimise the sensor using plate reader assays. To pre-express EsaR, we used the directed-evolution variant EsaR(D91G) {cite}`shong2013-chembio`. This variant shows substantially increased 3-oxo-C6-HSL sensitivity relative to wild-type EsaR. For the reporter constructs, we followed the design used by {cite}`chizzolini2017` in which the EsaO operator is placed directly adjacent to the T7 promoter for maximal repression. The EsaO is flanked by a leader sequence containing the epsilon enhancer sequence and a strong ribosomal binding sit. To further deepen repression, a second EsaO operator was inserted upstream of the native operator in the dual-operator construct. The two operators are separated by a single thymine. This follows the P{sub}`esa`R-C design described by {cite}`shong2013`. P{sub}`esa`R-C showed tighter repression and greater derepression than the native promoter when tested in *E. coli*. We were interested to see whether this same behaviour would translate to Nucleus cytosol reactions.

# DNA Constructs

Four linear DNA templates were used throughout this work: the EsaR(D91G) template used to pre-express EsaR, two EsaO-mNG reporter constructs carrying either single or dual EsaO operator boxes, and an unrepressed mNG control. Linear templates were amplified from g-blocks using PCR and cleaned-up prior to their addition into cytosol reactions.

:::{table}  DNA constructs used throughout this work. Sequences with annotations are listed in the below viewers.
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

# Results


## EsaR titration fails to repress EsaO-mNG at 12 nM DNA

To determine the ratio of pre-expressed EsaR repressor to sensor construct that gives a well-defined ‘on’/’off’ state, we titrated increasing amounts of pre-expressed EsaR protein into Nucleus cytosol reactions containing single-operator EsaO-mNG or dual-operator [EsaO]2-mNG reporter DNA. The reporter construct was held at 12.2 nM (10 ng/µL) in all reactions. Each reaction was split, with AHSL added to one half to a final concentration of 5 µM.

No difference between the ‘on’ and ‘off’ states was observed at any EsaR volume tested ({numref}`fig-20260924-esao-titration`). Note that 7 µL is the highest achievable amount of EsaR that could be added without affecting the stoichiometry of Nucleus cytosol. This suggests either that the pre-expressed EsaR was non-functional, or that the reporter construct remained in excess even at the highest EsaR-to-DNA ratio tested.

:::{figure} #fig-20260924-esao
:label: fig-20260924-esao-titration
:align: center
:width: 75%
Single-operator EsaO-mNG and dual-operator [EsaO]2-mNG with 0 and 7 µL pre-expressed EsaR, minus and plus 5 µM AHSL (n = 3 replicate wells; shaded region shows standard deviation). Reaction composition is in {numref}`tbl-composition-20260924`.
:::

<!-- [`fig-20260924-esao-titration`, notebook:`CN-20260924_repressor_test/platereader.ipynb`, platemap:`build - 20260924_Platemap.csv`, data source:`20260924-151252-cytation5-pure-timecourse-gfp-repressor_test.txt`, caption: (Single-operator EsaO-mNG and dual-operator [EsaO]2-mNG with 0 and 7 µL pre-expressed EsaR, minus and plus 5 µM AHSL.)] -->

## Repression scales with the EsaR : reporter DNA ratio

To test whether the EsaO-mNG DNA templates had previously been in excess, we titrated the reporter construct concentration while holding pre-expressed EsaR at the highest achievable concentration of 7 µL in each reaction. Repression was lost above 1 nM DNA. At 0.1 nM and 0.5 nM, the single-operator construct gave fold-changes of approximately 1.5 and 1 respectively, while the dual-operator construct gave approximately 2 and 1.6 (Figure {numref}`%s <fig-20260925-0p1nm>`–{numref}`%s <fig-20260925-fold>`). At both concentrations, the dual-operator [EsaO]2-mNG construct showed higher fold-induction than the single-operator EsaO-mNG, consistent with the tighter repression expected from the additional EsaO operator. This suggests that the repressor behaviour exhibited *in vivo* translates to PURE systems such as Nucleus cytosol.

Additionally, we noticed that the mNG control present at 15.6 nM was matched or exceeded in fluorescence signal by reporter DNA constructs at 0.5 nM and upwards ({numref}`%s <fig-20260925-0p5nm>`–{numref}`%s <fig-20260925-3nm>`). This was surprising as the reporter DNA was 5- to 30-fold lower in concentration. We hypothesise this may be due to the pre-expressed EsaR preparation carrying over unspent energy components as well as transcription and translation factors that may supply additional capacity to the reaction. 


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

Thus far, any EsaR template present in the final cytosol reaction was carryover from the initial EsaR pre-expression. This gave a final concentration of ~3.4 nM, a 34-fold excess over the 0.1 nM reporter template. To further deepen the 'off' state, 5.3 nM EsaR template was added by diluting the reporter DNA stock in EsaR template rather than water. This brought the total EsaR template in the final reaction to 8.7 nM, an 87-fold excess over reporter. This served two purposes. It increased the overall amount of EsaR available to repress the reporter, and it continuously diverted Nucleus cytosol resources away from reporter production.

As expected, expressing additional EsaR reduced overall fluorescence yield roughly four-fold ({numref}`fig-20261007-normalized`). This came with an improved dynamic range, rising from 2.8 without added EsaR template to a reliable 4-fold change with it ({numref}`fig-20261007-fold`).

:::::{tab-set}

::::{tab-item} Timecourse
:::{figure} #mbcn-20261007-fig1
:label: fig-20261007-normalized
:align: center
:width: 100%
Time-course fluorescence for EsaO-mNG at 0.1 nM, with and without 8.7 nM added EsaR DNA template, each with and without AHSL (n = 3). Fluorescence is raw RFU.
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

To test whether lower reaction temperatures could both stabilise EsaR-DNA binding, and slow T7 kinetics to limit EsaR being knocked-off reporter templates, reactions were incubated at 25 ˚C overnight rather than 37 ˚C for 3 hrs. Ideally, this would reduce reporter expression from templates that were insufficiently repressed. 

Reactions were incubated overnight in a thermocycler and measured on a platereader the following day. The highest fold change across all experiments was recorded at ~ 5.8. This suggests that temperature plays an important role in repression within the system. Timecourse reactions should be recorded in future to understand this in more detail.

:::{figure} #mbcn-20261008-fig1
:label: fig-20261008-overnight
:align: center
:width: 55%
Background-corrected GFP fluorescence for 0.1 nM [EsaO]2-mNG DNA after overnight incubation at 25 °C. Reactions were run with and without 5 µM AHSL.
:::

<!-- [`fig-20261008-overnight`, notebook:`CN-MB-20261007-EsaR_template_competition/platereader.ipynb`, platemap:`20261008-esao-mng-esar-ahsl.csv`, data source:`20261007-170653-YH Cytosol comparison_CH.txt`, caption: (Background-corrected GFP fluorescence for 0.1 nM [EsaO]2-mNG DNA after overnight incubation at 25 °C. Reactions were run with and without 5 µM AHSL.)] -->

## Developer cells encapsulating sensor DNA detect AHSL in solution

To take a step towards producing a functional developer cell that can sense bacteria through the detection of secreted AHSL, GUVs were prepared encapsulating Nucleus cytosol, 5 nM EsaR template, and 0.1 nM sensor DNA. Note the EsaR template was present at a final concentration of 5 nM by increasing the EsaR template in the pre-expression reaction to 24 nM. This method of preparation had not previously been tested in bulk Nucleus cytosol; that characterisation will be done in future. GUVs samples were split, with 5 µM AHSL added to one half. Samples were loaded in a 384-well plate and imaged for 6 hrs at 37˚C. 

Images show the final timepoint for all conditions collected on a Cephla microscope. Each image was processed in Python using matplotlib applying a consistent vmin/vmax across all wells. GUVs in the + AHSL conditions are markedly brighter than the - AHSL conditions, demonstrating that GUV-encapsulated sensor DNA detects AHSL in solution and derepresses mNG production.

:::{figure} #microscopy-exp-01
:label: fig-20261009-guv-ahsl
:align: center
:width: 100%
Dual-operator [EsaO]2-mNG encapsulated in GUVs with pre-expressed EsaR, three replicate wells each minus and plus 5 µM AHSL. Green LUT, vmin/vmax 1200:4500, 20 µm scale bar.
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

- Engineer the T7-EsaR(D91G)-Term construct for increased yield. Modify the
  5' UTR sequence and codon optimise to maximise the amount of protein
  produced.
- Assess whether it is possible to increase repression further by adding a
  third EsaO box. 
- Furthermore, search the literature / perform random mutagenesis to determine
  whether EsaO mutations can promote increased EsaR binding.
- Purchase / recombinantly purify EsaR protein. Add purified EsaR to cytosol
  reactions containing sensor DNA in >100x excess in an attempt to achieve
  maximal gene repression. Test in bulk reactions first and then in GUVs.
- Once optimised, test sensor DNA in the colour change module to confirm a
  visible colour change upon GUVs sensing AHSL.

---

# Methods

## Reagents

:::{table} Reagents and equipment used throughout this work. In-house components (Small molecule mix, tRNA, Protein mix, Ribosomes) link to their b.next preparation processes in `nucleus-docs`; other components were purchased from vendors, with their product links provided.
:label: tbl-reagents
:align: center

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | Small Molecule Mix (SMix) | b.next (in-house) | N/A | N/A | -80 °C | [link](https://docs.nucleus.engineering/docs/processes/make-small-molecule-mix/main) |
| tRNA | Nucleus Total tRNA (35 µg/µL, 10×) | b.next (in-house) | N/A | N/A | -80 °C | [link](https://docs.nucleus.engineering/docs/processes/make-trna/main) |
| Protein mix | Protein Mix (PMix), 36 PURE proteins, 15 µg/µL | b.next (in-house) | N/A | N/A | -80 °C | [link](https://docs.nucleus.engineering/docs/processes/make-36pot/main) |
| Ribosomes | Ribosomes, 10 µM (5.55×) | b.next (in-house) | N/A | N/A | -80 °C | [link](https://docs.nucleus.engineering/docs/processes/make-ribosomes/main) |
| RNase inhibitor | RNase Inhibitor, Murine | NEB | M0314S | $87.00 | -25 °C to -15 °C | [link](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| Nuclease free water | Water, Nuclease-Free, for Molecular Biology | Sigma-Aldrich | W4502-1L | $88.40 | N/A | [link](https://www.sigmaaldrich.com/US/en/product/sigma/w4502) |
| AHSL | N-(3-Oxohexanoyl)-L-homoserine lactone | Sigma-Aldrich (Aldrich) | K3007 | N/A | N/A | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/k3007) |
| Fluorescein | Fluorescein, NIST-Traceable Standard (50 µM nominal) | Invitrogen (Thermo Fisher Scientific) | F36915 | $554.00 | 2 °C to 8 °C, protect from light | [link](https://www.thermofisher.com/order/catalog/product/F36915) |
| Q5 polymerase | Q5® High-Fidelity 2X Master Mix | NEB | M0492S | $226.00 | -20 °C | [link](https://www.neb.com/en-us/products/m0492-q5-high-fidelity-2x-master-mix) |
| HF buffer | Included in Q5® High-Fidelity 2X Master Mix | NEB | M0492S | N/A (included) | -20 °C | [link](https://www.neb.com/en-us/products/m0492-q5-high-fidelity-2x-master-mix) |
| M13 Fwd primer | Custom DNA oligo: 5'-GTAAAACGACGGCCAGTG-3' | IDT | N/A (custom) | N/A | -20 °C | N/A |
| M13 Rev primer | Custom DNA oligo: 5'-CAGGAAACAGCTATGACCATG-3' | IDT | N/A (custom) | N/A | -20 °C | N/A |
| Magnesium | Magnesium acetate tetrahydrate | Sigma-Aldrich | M0631-100G | $34.80 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/m0631) |
| POPC | 16:0-18:1 PC (POPC), 25 mg/mL | Avanti Research | A80557 (formerly 850457) | $435.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Mineral oil | Mineral oil, light, BioReagent, for molecular biology | Sigma-Aldrich | M5904 | N/A | Room temperature | [link](https://www.sigmaaldrich.com/US/en/product/sigma/m5904) |
:::

<!-- STYLE: the source heading was the underlined run-in label "Day #2
(20260924)". It is promoted to a subsection heading here. -->

## Protocols

Reactions across the EsaR titration, sensor DNA titration, and overnight EsaR
pre-expression experiments shared a common assembly: a mastermix of
Nucleus cytosol was prepared without DNA or water. Pre-expressed EsaR(D91G) was mixed with the DNA construct(s) and incubated at 37 ˚C for 15 min then topped up with water and added to the cytosol mastermix. Reactions were split in half and AHSL added to one half to a final concentration of 5 µM. Each reaction was distributed in triplicate 10 µL vols into a 384-well plate and read on a platereader set to detect GFP at 37 ˚C for 6 hrs. The following sections state specific information relating to the associated experiment, and any changes from this base procedure.

### Titrating pre-expressed EsaR into cytosol reactions containing mNG with single or dual EsaO operators

To ensure either 0, 1, 4, or 7 µL of pre-expressed EsaR was added to the final cytosol reaction. Varying amounts of pre-expressed EsaR were mixed with 320.5 ng of either T7-\[EsaO\]-mNG-T7term or T7-\[EsaO\]2-mNG-t7term to a total reaction volume of 65 µL. The final sensor DNA concentration was 12 nM. Reaction composition is in {numref}`tbl-composition-20260924`.

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
| DNA Template | 200 | ng/µL | 10 | ng/µL | 1.54 | 2.87 | 2.87 | 2.87 | 2.87 | 3.25 | 3.25 | 3.25 | 3.25 |
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

### Titrating single and dual operator EsaO-mNG DNA against fixed pre-expressed EsaR

 14 µL of pre-expressed EsaR was combined with varying amounts of T7-\[EsaO\]-mNG-T7term and T7-\[EsaO\]2-mNG-t7term sensor constructs to a total reaction volume of 65 µL. Full reaction composition is in {numref}`tbl-composition-20260925`.

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
| DNA Template | 10 / 10 / 150 / 150 / 150 / 150 | ng/µL | 0.1 / 0.5 / 1 / 3 / 6 / 9 | nM | 1.54 | 0.44 | 2.12 | 0.28 | 0.85 | 1.69 | 2.46 | 0.43 | 2.16 | 0.29 | 0.86 | 1.73 | 2.59 |
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

### Comparing unspent and spent pre-expressed EsaR added to [EsaO]2-mNG DNA reactions

EsaR(D91G) was instead pre-expressed for 17 hrs at 30 ˚C and held at 4 ˚C.
14 µL of pre-expressed EsaR was mixed with varying amounts of
T7-\[EsaO\]2-mNG-t7term only to a total reaction volume of 70 µL. Sensor DNA was provided so that the concentrations in the final reaction were 0.1, 0.5 and 1 nM. Full reaction composition is in {numref}`tbl-composition-20260926`.

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
| DNA Template | 10 / 50 / 100 | ng/µL | 0.1 / 0.5 / 1 | nM | 1.66 | 0.46 | 0.46 | 0.46 |
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

### Effect of additional Mg on EsaR-dependent repression of [EsaO]2-mNG DNA

EsaR(D91G) was instead incubated with sensor DNA for 1 hr at 37 ˚C instead of 15 mins at 37 ˚C. Sensor DNA was provided so that the concentration in the final reaction was 0.5 nM. Varying amounts of magnesium was added reaching concentrations of 0, 5, 10, and 20 mM during the incubation step. Final reaction volumes were 33 µL with and without 5 µM AHSL. Reactions were therefore directly distributed in triplicate 10 µL vols into a 384-well plate without splitting. 

::::{admonition} Reaction composition
:class: dropdown

:::{table} Reaction composition.
:label: tbl-composition-20261001
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume [µL] | Scaled [µL] |
| --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 3 | 9.9 |
| tRNA | 10 | × | 1 | × | 1 | 3.3 |
| Protein mix | 8.33 | × | 1 | × | 1.2 | 3.96 |
| Ribosomes | 5.5 | × | 1 | × | 1.8 | 5.94 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.25 | 0.825 |
| DNA Template | 22 | ng/µL | 0.5 | nM | 0.15 | 0.495 |
| Pre-expressed EsaR | — | — | — | — | 2.3 | 7.59 |
| Magnesium | — / 86.6 / 173.3 / 346.7 | mM | 0 / 5 / 10 / 20 | mM | 0.15 | 0.495 |
| AHSL | — | — | 0 / 5 | µM | 0.15 | 0.495 |
| Total | | | | | 10 | 33 |
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

### Effect of increasing EsaR DNA concentration on [EsaO]2-mNG DNA repression

We ran our EsaR repression reactions at the same conditions as before with
0.1nM DNA template and preincubating the DNA for 1h at 37C with a cell free
pre expressed EsaR (15nM DNA, 3h at37C).

EsaR DNA was 15nM. Final EsaR concentration is 3.4nM in the cell free reaction
where 2.27µL of EsaR were added and around 0.33 of the DNA stock -\> 2.6µL of
EsaR-DNA mixture added on 7.4µL mix of Nucleus cytosol+RNase inhibitor and
AHSL(5µM)/ DI water (0.15µL)

To improve the amounts of EsaR in the final reaction and introduce a higher
off switch:

we added more EsaR DNA template:

We diluted the mNG DNA template not in DI water but in the DNA template of
EsaR:

Of mixing a 2x DNA stock with the raw PCR template that was at 320nM in a
50:50 manner so we have 5.3nM extra added enhancing the 34x excess of DNA
template up to 77x

<!-- No build file exists for this day either. `build` in
`CN-MB-20261007-EsaR_template_competition` is an empty default Sheet, same
shape as the 2026-10-01 gap. 2.27 + 0.33 = 2.6, which matches the "2.6µL"
the log states, so that part of the arithmetic checks out. Whether the 0.15µL
AHSL/water volume sits inside the stated 7.4µL or on top of it is not stated,
and is not inferred here. -->

::::{admonition} Platemap
:class: dropdown

:::{platemap} ./experiments/20261007-esar-template-competition/20261008-esao-mng-esar-ahsl.csv
:height: 480px
:fields: [EsaO-mNG] (nM), [EsaR] (nM), [AHSL] (uM)
:label: platemap-20261007
:::
::::

### Effect of lower reaction temperature on EsaR-dependent repression of [EsaO]2-mNG DNA

<!-- No build file exists for this day either, same gap as 2026-10-01 and
2026-10-07. Both tables are carried verbatim from the log. -->

::::{admonition} Reaction volumes
:class: dropdown

:::{table} Preexpression of EsaR, as the log writes it. Not a composition table — no stock or final concentrations, and no build file to source one from.
:label: tbl-volumes-20261008-preexpression
:align: center

| Component | Volume (µL) |
| --- | --- |
| S-mix | 3 |
| Ribosomes | 1.8 |
| P-mix | 1.2 |
| T rna | 1 |
| DNA | 0.15 |
| Rnase inhibitor | 0.25 |
| DI Water | 2.45 |
| AHSL | 0.15 |
| Total | 10 |
:::

:::{table} Reaction mix, same for all sensing reactions in this log.
:label: tbl-volumes-20261008-reaction
:align: center

| Component | Volume (µL) |
| --- | --- |
| S-mix | 3 |
| Ribosomes | 1.8 |
| P-mix | 1.2 |
| T rna | 1 |
| DNA | 0.15 |
| Rnase inhibitor | 0.25 |
| EsaR | 2.45 |
| AHSL | 0.15 |
| Total | 10 |
:::
::::

### Testing EsaR-dependent repression of [EsaO]2-mNG DNA in GUVs

2 mg of POPC was dried under nitrogen and further dried under vacuum for at
least two hours. Lipids were resuspended in 500 µL mineral oil and the
mixture was sonicated at room temperature for around 20 minutes.

EsaR was pre-expressed in a cell-free reaction at a template concentration of
24 nM, double the 12 nM used previously, resulting in a final concentration
of 5 nM. The reporter construct, (*esa*)₂-mNG, was held at 0.1 nM. Following
completion of EsaR pre-expression, the reporter DNA was incubated with the
pre-expressed EsaR for approximately 1 h at 37 °C prior to encapsulation. The
EsaR reaction itself was incubated for 3 h at 37 °C before being supplemented
with the DNA and incubated for a further 1 h. This mixture was used as a
supplement to the inner solution of the GUVs, as an EsaR-DNA mixture.

<!-- No build file exists for this day either, same gap as 2026-10-01,
2026-10-07 and 2026-10-08. Both tables are carried verbatim from the log. -->

::::{admonition} Reaction volumes
:class: dropdown

:::{table} Pre-expressed EsaR, as the log writes it. Not a composition table — no stock or final concentrations, and no build file to source one from.
:label: tbl-volumes-20261009-esar
:align: center

| Component | Volume (µL) |
| --- | --- |
| S-mix | 3 |
| Ribosomes | 1.8 |
| P-mix | 1.2 |
| T rna | 1 |
| EsaR DNA | 0.15 |
| Rnase inhibitor | 0.25 |
| DI water | 2.45 |
| AHSL | 0.15 |
| Total | 10 |
:::

:::{table} GUV inner solution.
:label: tbl-volumes-20261009-guv
:align: center

| Component | Volume (µL) |
| --- | --- |
| S-mix | 3 |
| Ribosomes | 1.8 |
| P-mix | 1.2 |
| T rna | 1 |
| DNA-EsaR mixture | 2.25 |
| Rnase inhibitor | 0.25 |
| Optiprep | 0.5 |
| Total | 10 |
:::
::::

The inner solution was prepared as 20 µL. The water-in-oil emulsion was
prepared by adding 200 µL of lipid-in-oil mixture onto the inner solution and
pipetting up and down 9 times. The emulsion was added onto 250 µL of outer
solution. GUVs were formed by spinning the two phases in a centrifuge at
15 °C for 20 min at 9,000 g. The resulting pellet was resuspended in 100 mL
outer solution. 7.5 µL of GUV solution were added into 22.5 µL of outer
solution in a 384-well plate and imaged for 6 hrs at 37 °C.

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
