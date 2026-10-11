<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

# Overview

We are attempting to detect a bacterial-derived signal, alpha
homoserine-lactone, in Nucleus cytosol reactions using a DNA sensing construct.
The EsaR/EsaO system has previously been tested in the literature using PURE,
with a weak on/off state. In this case, the EsaR repressor protein was
co-expressed alongside reporter DNA controlled by the EsaO operator. Our work
builds on this by attempting to supplement Nucleus cytosol reactions expressing
EsaO controlled protein, with pre-expressed EsaR repressor protein to improve
the dynamic range between the 'on' and 'off' states. We use a fluorescent
reporter to quantify the performance of the system, varying parameters such as
the ratio of pre-expressed EsaR protein to reporter DNA construct, and
concentration of magnesium ions.

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

**Every construct used in this DevNote is supplied and verified, except the
control.** The three that carry the experiments are in the tree:
`T7-EsaR(D91G)-T7term` in {ref}`seq-esar-d91g`, `T7-\[EsaO\]-mNG-T7term` in
{ref}`seq-esao-mng` and `T7-\[EsaO\]2-mNG-t7term` in {ref}`seq-esao2-mng`.
The three agree with each other: both reporters share one mNeonGreen coding
sequence byte for byte, and all three operator boxes are the same 19 bp.

Four are still missing, and only one of them is used here. `T7-mNG-t7term` is
the unrepressed control on all three CN days and has no source. The three PLA1
templates, `T7-PLA1-t7term`, `T7-\[EsaO\]-PLA1-T7term` and
`T7-\[EsaO\]2-PLA1-t7term`, were prepared on 2026-09-23 and appear in no
experiment in this DevNote. Supply the control, and either supply the PLA1
sequences or drop those three rows from {numref}`tbl-constructs`.

The three PLA1 templates were prepared on 2026-09-23 and are used in no
experiment here. Dropping them from {numref}`tbl-constructs` is one
alternative to chasing their sequences. T7-mNG-t7term is the unrepressed
control on all three CN days and does belong.

None of the seven is in `nucleus-eng/DNA`, on `main` or on
`devcells/devstudio-constructs`. The repo carries the neighbouring
quorum-sensing family but nothing for EsaR or EsaO. These belong in that repo,
and once they are there the DevNote can reference them by GitHub URL and carry
no local copy.

<!-- **Agarose gel image missing.** The 2026-09-24 log states that the
constructs were run on an agarose gel and instructs "Ask Manuel for image". No
gel image exists in any of the four Log folders.

**Resolved, review cycle v2, prompt 4.** The agarose gel is not relevant to
this DevNote and is not reported. -->

**No build file for 2026-10-01.** The file named `build` in that folder is a
platemap. It holds `Well`, `Date`, `Experiment`, `Name` and `Type` and nothing
else, so it carries no component, no concentration and no volume. No
composition table can be produced for that day and no sidecar exists.
{numref}`tbl-volumes-20261001` carries the log's own volume table instead, and
that table has no stock or final concentrations in it. Supply a build file in
the canonical format.

**Answered, review cycle v2, prompt 5, and deferred.** This will be addressed
later. The volume table stands in the meantime.
:::

:::{admonition} Open review items
:class: warning dropdown
:name: flags-review

<!-- **Date labels on two platemaps.** `CN-20260925-DNA_titration` holds
`20260924-dna-titration-esar-fixed.csv` and
`CN-20260926-DNA_titration_spent_EsaR` holds `20260924-esao2-dna-titration.csv`.
Both carry 20260924 inside a later folder. Each is the file that folder's own
notebook loads, so both read as naming slips rather than wrong data. The folder
date and the filename date still disagree, and that is a human call. The `Date`
column inside all three CN platemaps also reads `2026-09-24`.

**Resolved, review cycle v2, prompt 6.** Each file holds the correct
information. The filenames are the slip, not the folders. -->

<!-- **Template residue in every `test-data/` subfolder.** All four folders hold an
identical `20251111-122213-cytation5-pure-timecourse-gfp-MFG-98-tRNA-QC.txt`
plus `platemap-microscopy.csv` and `platemap-platereader.csv`. These look like
unedited copies from `00-template-LOG`, not run data. Nothing here links them.

**Resolved, review cycle v2, prompt 7.** They can be ignored if unedited. All
three files report identical byte counts in all four folders, which is the
evidence that none was edited. -->

<!-- **EsaR volume labels in {numref}`tbl-composition-20260924`.** The condition
names read 0, 1, 4 and 7 µL EsaR. The `Pre-expressed EsaR` row reads 0, 2, 8
and 14 µL. The reactions are 65 µL against a 32.5 µL standard reaction, so the
row is the per-65-µL volume and the name is the per-32.5-µL volume. Both are
carried as the build file writes them.

**Resolved, review cycle v2, prompt 8.** That reading is correct. -->

**DNA stock disagreements.** The 2026-09-24 build sheet states one 200 ng/µL
stock, yet EsaO takes 2.87 µL and \[EsaO\]2 takes 3.25 µL. The 2026-09-25 sheet
states 200 ng/µL in its standard-reaction block and 10 and 150 ng/µL in its own
comment. The comment values are the ones carried in
{numref}`tbl-composition-20260925`. The 2026-09-26 conditions all take 0.46 µL
because their stocks differ at 10, 50 and 100 ng/µL. The 2026-10-01 log states
22 ng/µL.

**Deferred, review cycle v2, prompt 9.** The reviewer passed on this question.
Every stock value above is still carried as its own source writes it.

<!-- **Pre-expressed EsaR has no concentration.** No build sheet records a stock or
final concentration for it. All four concentration cells are `—`. The 2026-09-24
log states a final EsaR concentration of 576 nM from back-of-the-napkin maths,
which is narrative, not a build-file value.

**Resolved, review cycle v2, prompt 10.** The concentration of pre-expressed
EsaR is not known. The dash stands, and the 576 nM figure stays narrative
only. -->

**Stale sheets in the 2026-09-24 build file.** `build` in
`CN-20260924_repressor_test` also contains sheets named `20260926_DNA_titration`
and `Sheet6` whose contents duplicate the 2026-09-25 titration. Only
`20260924_Repression_test_rxns` was used here.

**Answered, review cycle v2, prompt 11, and hedged.** The reviewer says those
sheets are "probably stale". That is not a confirmation, so this stays open.

<!-- **AHL and AHSL.** Before this cycle, the 2026-09-24 and 2026-09-25 logs
wrote "AHL", every platemap wrote "AHSL", the 2026-09-26 log wrote "AHL" in its
reaction preparation and "AHSL" in its result, and the 2026-10-01 volume table
wrote "AHL optional".

**Resolved and applied, review cycle v2, prompt 12.** Everything is written as
AHSL. Seven occurrences of "AHL" were replaced across Protocol, Methods,
Results and the 2026-10-01 volume table. This is the one place where verbatim
source wording was changed, and it was changed on the author's explicit
instruction. -->

**The reagents table cannot be filled from the Materials Reference.**
`devstudio-build-to-materials` has now run, and matched 0 of 14 components. The
detail, the two near misses and what to do about them are in
{ref}`review-materials-unmatched`. Construct purposes are still deferred to a
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

<!-- **The 2026-10-01 platemap date disagrees with everything around it.** The
folder is `2026/10/01 - MB - MgSweepof preeincubation` and the data file is
`20261001-181311-...`. Every row of the platemap reads `2026-10-02`.

**Resolved, review cycle v2, prompt 15.** The run date is 2026-10-01. The
platemap was written the day after, which is why it reads 2026-10-02. -->

**An unused platemap copy sits in the 2026-10-01 folder.**
`build-platemap-csv.csv` holds the same sixteen wells as the `build` Sheet. Its
`Type` column is empty where the Sheet reads `Sample`. The notebook loads the
Sheet. Delete the copy, or say which one is authoritative.

**Answered, review cycle v2, prompt 16, and deferred.** That platemap will be
rebuilt. The Sheet export is the copy vendored into this DevNote.

<!-- **Authorship of the 2026-10-01 experiment.** The folder and the notebook
name MB and JM. The cell label reads `mbcn-20261001-fig1`.

**Resolved, review cycle v2, prompt 17.** MB is Manuel Bibrowski. Several sets
of initials appear because multiple experiments share one plate. The author
list itself is still open, under the blocking title-and-authors item. -->

**All three sequence files say circular, and the constructs are linear.** The
`LOCUS` line of every file in `dna/` reads `circular`. The 2026-09-23
protocol amplifies these from gBlocks, which gives a linear product.
{numref}`tbl-constructs` calls all seven linear templates. Correct the topology
in all three files.

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

# Reagents

:::{table} Reagents and equipment. Every row is unmatched against the Materials Reference, so no column is filled. Component names come from the three CN build sheets, the 2026-10-01 log's own volume table, and the 2026-09-23 construct preparation.
:label: tbl-reagents
:align: center

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| tRNA | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| Protein mix | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| Ribosomes | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| RNase inhibitor | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| Nuclease free water | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| AHSL | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| Fluorescein | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| Q5 polymerase | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| HF buffer | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| M15 Fwd primer | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| M15 Rev primer | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| Magnesium | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
| E.coli pol | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] | [PLEASE FILL IN] |
:::

:::{admonition} No reagent is in the Materials Reference
:class: warning
:name: review-materials-unmatched

`devstudio-build-to-materials` matched 0 of 14 components against the
distribution-wide Materials Reference. The sidecar is
[`experiments/build-materials.csv`](./experiments/build-materials.csv), which
carries a `Provenance` column this table drops.

The reference was read from the published page,
<https://docs.nucleus.engineering/guides/materials-reference/>, because no
`nucleus-docs` checkout was available. That costs two things. The page is one
deploy behind `main`, and it carries no conflicts list, so disagreements
between source pages are collapsed into whichever value won. It held 100
entries at the time of this run. The matcher was checked against a known entry,
`Glucose`, which resolved to `A16828-36`, so the zero is a measurement and not
a failed lookup.

Matching is exact equality on the normalized name and nothing looser, because a
part number inferred from a near name reads as checked precisely when it is
wrong. Two components came close and are recorded as suggestions only:

`RNase inhibitor` against `RNase Inhibitor, Murine`, part `M0314S` from NEB.
The names differ by ", Murine", so this is not a match. It is very likely the
same item, and confirming it is one edit.

`Magnesium` against `Magnesium acetate`, part `M0631-100G`, and `Magnesium
chloride`, part `M2670-500G`. Two candidates, and the 2026-10-01 log records
only "Mg" with its stock molarity, so the salt is not recoverable from the
source.

Several of these will never carry a catalog number. Small molecule mix, protein
mix and ribosomes are made in-house. The rest are real gaps: add a row to the
`bom-<slug>` table on the Process page each belongs to in `nucleus-docs`, which
is a human edit in another repository and not something this pipeline does.
:::

# Constructs

:::{table} Linear DNA templates prepared on 2026-09-23. No sequence and no sequence file was found for any of the seven.
:label: tbl-constructs
:align: center

| Name | Sequence | Purpose |
| --- | --- | --- |
| T7-mNG-t7term | [PLEASE FILL IN] | [PLEASE FILL IN] |
| [T7-\[EsaO\]-mNG-T7term](./dna/t7pro-esao-ls1-mneongreen.gbk) | {ref}`seq-esao-mng` | [PLEASE FILL IN] |
| [T7-\[EsaO\]2-mNG-t7term](./dna/t7pro-esao2-ls1-mneongreen.gbk) | {ref}`seq-esao2-mng` | [PLEASE FILL IN] |
| T7-PLA1-t7term | [PLEASE FILL IN] | [PLEASE FILL IN] |
| T7-\[EsaO\]-PLA1-T7term | [PLEASE FILL IN] | [PLEASE FILL IN] |
| T7-\[EsaO\]2-PLA1-t7term | [PLEASE FILL IN] | [PLEASE FILL IN] |
| [T7-EsaR(D91G)-T7term](./dna/t7pro-ls1-esard91g.gbk) | {ref}`seq-esar-d91g` | [PLEASE FILL IN] |
:::

::::{admonition} T7-\[EsaO\]2-mNG-t7term, full sequence
:class: dropdown
:name: seq-esao2-mng

Source file:
[`dna/t7pro-esao2-ls1-mneongreen.gbk`](./dna/t7pro-esao2-ls1-mneongreen.gbk),
1118 bp. Verified against its own header and against the single-operator file.
The `LOCUS` line declares 1118 bp and the `ORIGIN` block holds exactly 1118
bases. The CDS at 171..881 translates to 236 residues plus a stop, with no
internal stops, starting `MVSKGEEDNM`.

Its mNeonGreen coding sequence is byte-identical to the one in
{ref}`seq-esao-mng`, so the two reporters differ only in the operator region.

The file carries two `EsaO` features, 19 bp each, at 62..80 and 82..100. Both
read `CCTGTACTATAGTGCAGGT`, which is also the single box in
{ref}`seq-esao-mng`. One `T` separates them, at position 81. The file is
exactly 20 bp longer than the single-operator construct, which is one operator
plus that spacer base.

Features, in order: 5' spacer, M13_Fwd, T7pro, +1, EsaO, EsaO, LS1,
mNeonGreen, T7 terminator, M13_Rev, 3' spacer.

```
GGGACCATTACGGAGGCAGTGTAAAACGACGGCCAGTGCCGGTTAATACGACTCACTATA
GCCTGTACTATAGTGCAGGTTCCTGTACTATAGTGCAGGTGGAGATTGTGAGCGGATAAC
AATTCCCCTCTAGAAATAATTTTGTTTAACTTTAAGAAGGAGATATACATATGGTGAGCA
AAGGCGAAGAGGATAATATGGCAAGCCTGCCTGCAACACATGAACTGCATATTTTTGGTA
GCATTAACGGCGTGGATTTTGATATGGTTGGTCAAGGCACCGGTAATCCGAATGATGGTT
ATGAAGAACTGAATCTGAAAAGCACCAAAGGCGATCTGCAGTTTAGCCCGTGGATTCTGG
TTCCGCATATTGGTTATGGTTTTCATCAGTATCTGCCGTATCCGGATGGTATGAGCCCGT
TTCAGGCAGCAATGGTTGATGGTAGCGGTTATCAGGTTCATCGTACCATGCAGTTTGAAG
ATGGTGCAAGCCTGACCGTTAATTATCGTTATACCTATGAAGGCAGCCACATTAAAGGTG
AAGCACAGGTTAAAGGTACAGGTTTTCCGGCAGATGGTCCGGTTATGACCAATAGTCTGA
CCGCAGCAGATTGGTGTCGTAGCAAAAAAACCTATCCGAACGATAAAACCATCATCAGCA
CCTTCAAATGGTCATATACCACCGGCAATGGTAAACGTTATCGTAGCACCGCACGTACCA
CCTATACCTTTGCAAAACCGATGGCAGCAAACTATCTGAAAAATCAGCCGATGTATGTGT
TTCGCAAAACGGAACTGAAACATTCCAAAACCGAGCTGAACTTTAAAGAATGGCAGAAAG
CATTTACCGATGTGATGGGCATGGATGAACTATACAAATAAGGATCCCGGGAATTCTCGA
GTAAGGTTAACCTGCAGGAGGCCTTTAATTAAGGTGGTGCGGCCGCGCTAGCGGTCCCGG
GGGATCGATCCGGCTGCTAACAAAGCCCGAAAGGAAGCTGAGTTGGCTGCTGCCACCGCT
GAGCAATAACTAGCATAACCCCTTGGGGCCTCTAAACGGGTCTTGAGGGGTTTTTTGCAT
GGTCATAGCTGTTTCCTGCCTGATGCATGAGCTAGCAG
```
::::

::::{admonition} T7-\[EsaO\]-mNG-T7term, full sequence
:class: dropdown
:name: seq-esao-mng

Source file:
[`dna/t7pro-esao-ls1-mneongreen.gbk`](./dna/t7pro-esao-ls1-mneongreen.gbk),
1098 bp. Verified three ways. The `LOCUS` line declares 1098 bp and the
`ORIGIN` block holds exactly 1098 bases. The CDS at 151..861 translates to 236
residues plus a stop, with no internal stops. That translation starts
`MVSKGEEDNM` and runs 236 residues, which is the mNeonGreen N-terminus at
mNeonGreen's own length.

The file carries exactly one `EsaO` feature, 19 bp at 62..80, which is what
makes this the single-operator construct. It sits between the +1 transcription
start and the leader sequence.

Features, in order: 5' spacer, M13_Fwd, T7pro, +1, EsaO, Leader sequence 1,
mNeonGreen, T7 terminator, M13_Rev, 3' spacer. That is the same layout as
{ref}`seq-esar-d91g` with the operator inserted and the coding sequence
swapped.

```
GGGACCATTACGGAGGCAGTGTAAAACGACGGCCAGTGCCGGTTAATACGACTCACTATA
GCCTGTACTATAGTGCAGGTGGAGATTGTGAGCGGATAACAATTCCCCTCTAGAAATAAT
TTTGTTTAACTTTAAGAAGGAGATATACATATGGTGAGCAAAGGCGAAGAGGATAATATG
GCAAGCCTGCCTGCAACACATGAACTGCATATTTTTGGTAGCATTAACGGCGTGGATTTT
GATATGGTTGGTCAAGGCACCGGTAATCCGAATGATGGTTATGAAGAACTGAATCTGAAA
AGCACCAAAGGCGATCTGCAGTTTAGCCCGTGGATTCTGGTTCCGCATATTGGTTATGGT
TTTCATCAGTATCTGCCGTATCCGGATGGTATGAGCCCGTTTCAGGCAGCAATGGTTGAT
GGTAGCGGTTATCAGGTTCATCGTACCATGCAGTTTGAAGATGGTGCAAGCCTGACCGTT
AATTATCGTTATACCTATGAAGGCAGCCACATTAAAGGTGAAGCACAGGTTAAAGGTACA
GGTTTTCCGGCAGATGGTCCGGTTATGACCAATAGTCTGACCGCAGCAGATTGGTGTCGT
AGCAAAAAAACCTATCCGAACGATAAAACCATCATCAGCACCTTCAAATGGTCATATACC
ACCGGCAATGGTAAACGTTATCGTAGCACCGCACGTACCACCTATACCTTTGCAAAACCG
ATGGCAGCAAACTATCTGAAAAATCAGCCGATGTATGTGTTTCGCAAAACGGAACTGAAA
CATTCCAAAACCGAGCTGAACTTTAAAGAATGGCAGAAAGCATTTACCGATGTGATGGGC
ATGGATGAACTATACAAATAAGGATCCCGGGAATTCTCGAGTAAGGTTAACCTGCAGGAG
GCCTTTAATTAAGGTGGTGCGGCCGCGCTAGCGGTCCCGGGGGATCGATCCGGCTGCTAA
CAAAGCCCGAAAGGAAGCTGAGTTGGCTGCTGCCACCGCTGAGCAATAACTAGCATAACC
CCTTGGGGCCTCTAAACGGGTCTTGAGGGGTTTTTTGCATGGTCATAGCTGTTTCCTGCC
TGATGCATGAGCTAGCAG
```
::::

::::{admonition} T7-EsaR(D91G)-T7term, full sequence
:class: dropdown
:name: seq-esar-d91g

Source file: [`dna/t7pro-ls1-esard91g.gbk`](./dna/t7pro-ls1-esard91g.gbk),
1118 bp. Verified three ways. The `LOCUS` line declares 1118 bp and the
`ORIGIN` block holds exactly 1118 bases. The CDS at 132..881 translates to 249
residues plus a stop, with no internal stops. Residue 91 is glycine, codon
`GGC`, which confirms the D91G the construct name claims.

Features, in order: 5' spacer, M13_Fwd, T7pro, +1, LS1, EsaR, T7 terminator,
M13_Rev, 3' spacer.

```
GGGACCATTACGGAGGCAGTGTAAAACGACGGCCAGTGCCGGTTAATACGACTCACTATA
GGGAGATTGTGAGCGGATAACAATTCCCCTCTAGAAATAATTTTGTTTAACTTTAAGAAG
GAGATATACATATGTTCTCTTTCTTCCTTGAAAACCAAACAATAACGGATACGCTTCAGA
CTTACATACAGAGAAAGTTATCTCCGCTGGGTAGTCCGGATTACGCTTACACTGTTGTGA
GCAAAAAAAATCCTTCAAATGTTCTGATTATTTCCAGTTATCCTGACGAATGGATTAGGT
TATACCGCGCTAACAACTTTCAGCTGACCGATCCGGTTATTCTCACGGCCTTTAAACGCA
CCTCGCCGTTTGCCTGGGATGAGAATATTACGCTGATGTCCGGCCTGCGGTTCACCAAAA
TTTTCTCTTTATCCAAGCAATACAACATCGTTAACGGCTTTACCTATGTCCTGCATGACC
ACATGAACAACCTTGCTCTGTTGTCCGTGATCATTAAAGGCAACGATCAGACTGCGCTGG
AGCAACGCCTTGCTGCCGAACAGGGCACGATGCAGATGCTGCTGATTGATTTTAACGAGC
AGATGTACCGACTGGCAGGCACCGAAGGTGAACGAGCACCGGCGTTAAATCAGAGCGCGG
ACAAAACGATATTTTCCTCGCGTGAAAATGAGGTGTTGTACTGGGCGAGTATGGGCAAAA
CCTATGCTGAGATTGCCGCTATTACGGGCATTTCTGTGAGTACCGTGAAGTTTCACATCA
AGAATGTGGTCGTGAAACTGGGCGTCAGTAACGCCCGACAGGCTATCAGACTGGGTGTAG
AACTGGATCTTATCAGACCGGCAGCGTCAGCAGCAAGGTAAGGATCCCGGGAATTCTCGA
GTAAGGTTAACCTGCAGGAGGCCTTTAATTAAGGTGGTGCGGCCGCGCTAGCGGTCCCGG
GGGATCGATCCGGCTGCTAACAAAGCCCGAAAGGAAGCTGAGTTGGCTGCTGCCACCGCT
GAGCAATAACTAGCATAACCCCTTGGGGCCTCTAAACGGGTCTTGAGGGGTTTTTTGCAT
GGTCATAGCTGTTTCCTGCCTGATGCATGAGCTAGCAG
```
::::

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
total volume of 65 µL. Reactions were split in half before adding AHSL to one
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
Reactions were split in half before adding AHSL to one set of reactions to a
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
total volume of 70 µL. Reactions were split in half before adding 0.35 µL AHSL
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
| AHSL optional | 0.15 | 0.495 |
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

## 2026-10-07 — EsaR DNA template competition

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

# Results

## 2026-09-24 — EsaR titration at fixed sensor DNA

We first sought to determine the ratio of pre-expressed EsaR repressor protein
to DNA sensor construct at which there was a defined "on"/"off" state in signal
output. We therefore titrated varying amounts of pre-expressed EsaR protein
into Nucleus cytosol reactions containing two different EsaO-mNeonGreen
reporter constructs each with either one, or two EsaO operator regions. The
reporter construct concentration was held at 12.2 nM in each reaction.

There was no difference in the "on"/"off" states with any number of EsaO
operators. This suggested either that the EsaR protein was non-functional, or
that the DNA sensor construct was in excess even at the highest ratio of EsaR
protein to DNA sensor.

The log's own pre-analysis note, carried verbatim:

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

To test whether the EsaR was functional, we decided to titrate the DNA sensor
construct concentration whilst maintaining the highest possible concentration
of pre-expressed EsaR in each reaction. If the EsaR was functional, this would
enable us to empirically determine the EsaR:DNA ratio at which there was an
observable difference in "on"/"off" states. 1 nM DNA was shown to be the
concentration at which the fold-change between "on"/"off" states decreased to
~1. 0.1 nM DNA, and 0.5 nM DNA produced fold-changes of ~ 1.5 / 2. A separate
observation was that samples containing ~10 fold less DNA relative to the
constitutively expressed control, were reaching equivalent yields in final
reporter protein. We hypothesized that adding pre-expressed EsaR protein to
reactions was increasing reaction yield by virtue of adding unspent energy
components. We were interested to determine whether this was having any effect
on the performance of repression in the system.

The log's own pre-analysis note, carried verbatim:

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

:::{figure} ./figures/20260925-esao-all-concentrations.png
:label: fig-20260925-all-conc
:align: center
:width: 100%
Single-operator EsaO-mNG across all six sensor DNA concentrations, 0.1 to 9 nM, minus and plus AHSL. Added for review cycle v2, prompt 19.
:::

[`fig-20260925-all-conc`, notebook:`CN-20260925-DNA_titration/platereader.ipynb`, platemap:`20260924-dna-titration-esar-fixed.csv`, data source:`20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`, caption: (Single-operator EsaO-mNG across all six sensor DNA concentrations, minus and plus AHSL.)]

:::{figure} ./figures/20260925-fold-induction.png
:label: fig-20260925-fold
:align: center
:width: 55%
Steady-state AHSL fold induction, plus AHSL over minus AHSL, for both constructs at 0.1, 0.5 and 1 nM sensor DNA. This is the plot the 2026-09-26 log asks for in its closing note.
:::

[`fig-20260925-fold`, notebook:`CN-20260925-DNA_titration/platereader.ipynb`, platemap:`20260924-dna-titration-esar-fixed.csv`, data source:`20260925-153022-synergy2-pure-timecourse-gfp-DNA_titration.txt`, caption: (Steady-state AHSL fold induction for both constructs at 0.1, 0.5 and 1 nM sensor DNA.)]

:::{admonition} Three of six DNA concentrations are unreported
:class: warning
:name: review-20260925-missing-panels

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
cell outputs, because none of those cells carries a `#| label:` tag.
:::

## 2026-09-26 — Sensor DNA titration with overnight EsaR

To determine whether adding unspent EsaR reactions, incubated at 37 ˚C for 3
hours, to fresh Nucleus cytosol reactions containing sensor DNA, we instead
pre-expressed EsaR for 30 ˚C for 17 hours. EsaR volumes added to each reaction
were kept consistent with previous experiments, and sensor DNA concentrations
were limited to 0.1 nM, 0.5 nM and 1 nM. Relative to the previous experiment,
the overall fold change between "on"/"off" remained consistent for each DNA
concentration, whilst the overall yield decreased. We hypothesise that in this
case the added byproducts of the pre-expressed EsaR reaction, e.g inorganic
phosphate, poisoned the reactions, lowering the overall yield.

The log's own pre-analysis note, carried verbatim:

Results: \*Prior to analysis - The constructs are being repressed similarly to
the previous experiment. Adding "spent" EsaR reactions doesn't appear to be
improving the amount of repression noticeably.

:::{figure} #cn-20260926-fig1
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

:::{figure} ./figures/20260926-fold-induction.png
:label: fig-20260926-fold
:align: center
:width: 55%
Steady-state AHSL fold induction for \\[EsaO\\]2-mNG with EsaR pre-expressed overnight. Added for review cycle v2, prompt 19.
:::

[`fig-20260926-fold`, notebook:`CN-20260926-DNA_titration_spent_EsaR/platereader.ipynb`, platemap:`20260924-esao2-dna-titration.csv`, data source:`20260926-115326-synergy2-pure-timecourse-gfp-DNA_titration_EsaR_spent.txt`, caption: (Steady-state AHSL fold induction for [EsaO]2-mNG with EsaR pre-expressed overnight.)]

## 2026-10-01 — Magnesium sweep with EsaR and DNA pre-incubation

In an attempt to increase the fold-change between "on/off" states, we held the
pre-expressed EsaR concentration consistent with previous experiments, and
maintained the DNA concentrations at 0.1 nM, 0.5 nM, and 1 nM. In this case,
the pre-expressed EsaR reactions were incubated with sensor DNA constructs for
1 hr, 37 ˚C prior to being added to each reaction. We then supplemented
reactions with 0 mM, 5 mM, 10 mM and 20 mM magnesium to influence the DNA
binding properties of EsaR. We found that the addition of magnesium had very
little influence on the dynamic range between the "on"/"off" states, yet across
all DNA concentrations tested, the fold change had increased to 5 fold, in
comparison to ~ 2 in previous experiments at the lowest DNA concentrations
tested. We attributed this to the increased EsaR:DNA pre-incubation time which
may enable EsaR to occupy more EsaO operator sites on the sensor DNA.

<!-- Results narrative supplied by the reviewer in review cycle v2, prompt 22,
and carried verbatim. The source log carries no results narrative. -->

:::{figure} #mbcn-20261001-fig1
:label: fig-20261001-mg-sweep
:align: center
:width: 100%
Added magnesium at 0, 5 and 10 mM, each minus and plus 5 µM AHSL, after pre-incubating EsaR with the DNA. Reaction volumes are in {numref}`tbl-volumes-20261001`.
:::

[`fig-20261001-mg-sweep`, notebook:`2026-10-01-MB-MgSweep/20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.ipynb`, platemap:`20261001-mg-sweep-platemap.csv`, data source:`20261001-181311-cytation5-pure-timecourse-gfp-JM-MB-Mg-Osmo-Sweep.txt`, caption: (Added magnesium at 0, 5 and 10 mM, minus and plus 5 µM AHSL.)]

The 20 mM magnesium arm was run and is not plotted. Adding that much magnesium
to a Nucleus cytosol reaction poisons it.

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

## 2026-10-07 — EsaR DNA template competition

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

:::::{tab-set}

::::{tab-item} Normalized curves
:::{figure} ./figures/20261007-normalized-curves.png
:label: fig-20261007-normalized
:align: center
:width: 100%
Normalized signal for EsaO-mNG at 0.1 nM, minus and plus 8 nM pre-expressed EsaR, each minus and plus AHSL.
:::
::::

::::{tab-item} Fold change
:::{figure} ./figures/20261007-fold-change.png
:label: fig-20261007-fold
:align: center
:width: 100%
Fold change over time, ratio of the plus-AHSL mean to the minus-AHSL mean, with and without the added EsaR DNA template.
:::
::::

::::{tab-item} Overnight endpoint, 25 ˚C
:::{figure} ./figures/20261007-overnight-endpoint-25c.png
:label: fig-20261007-overnight
:align: center
:width: 65%
t0-subtracted GFP fluorescence after overnight incubation at 25 ˚C, minus and plus 5 µM AHSL.
:::
::::

:::::

[`fig-20261007-normalized`, notebook:`CN-MB-20261007-EsaR_template_competition/platereader.ipynb`, platemap:`20261008-esao-mng-esar-ahsl.csv`, data source:`20261007-170653-YH Cytosol comparison_CH.txt`, caption: (Normalized signal for EsaO-mNG at 0.1 nM, minus and plus 8 nM pre-expressed EsaR, each minus and plus AHSL.)]

[`fig-20261007-fold`, notebook:`CN-MB-20261007-EsaR_template_competition/platereader.ipynb`, platemap:`20261008-esao-mng-esar-ahsl.csv`, data source:`20261007-170653-YH Cytosol comparison_CH.txt`, caption: (Fold change over time, with and without the added EsaR DNA template.)]

[`fig-20261007-overnight`, notebook:`CN-MB-20261007-EsaR_template_competition/platereader.ipynb`, platemap:`20261008-esao-mng-esar-ahsl.csv`, data source:`20261007-170653-YH Cytosol comparison_CH.txt`, caption: (t0-subtracted GFP fluorescence after overnight incubation at 25 ˚C.)]

25C reactions were incubated in a thermocycler giving a 5.8 fold change as the
strongest sensor after over night incubation ({numref}`fig-20261007-overnight`:
19 800 / 3 400 ≈ 5.8, checked against the figure's own bars).

:::{admonition} Open items on 2026-10-07
:class: warning
:name: review-20261007-open

**No cell in `platereader.ipynb` produces these three figures.** The notebook
loads the correct raw data file and the correct platemap, through cell 6's
Drive download block. Its own plotting cells, 18 and 19, each chart one
condition pair rather than the four-condition overlay or the fold-change ratio
shown here. The overnight 25 ˚C endpoint figure has no matching cell at all.
The notebook never loads a thermocycler or endpoint read. This is the same
shape as the two unresolved 2026-09-24 figures. A notebook exists, loads the
right files, and still does not produce the figure the log shows.

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

**One plot title in the notebook names the wrong construct.** Cell 18's title
reads "0.1 nM [Esao]2-mNG DNA titration", but the cell selects data named
`EsaO-mNG (0.1 nM)`, the single-operator construct, not `[EsaO]2-mNG`. The
plotted data and the platemap agree with each other; only the title text is
wrong.
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

Reaction composition, one sidecar per day. No sidecar exists for 2026-10-01
or 2026-10-07, because neither folder has a build file.

- [`experiments/build-composition-20260924.csv`](./experiments/build-composition-20260924.csv)
- [`experiments/build-composition-20260925.csv`](./experiments/build-composition-20260925.csv)
- [`experiments/build-composition-20260926.csv`](./experiments/build-composition-20260926.csv)

Analysis notebooks.

- [`experiments/20260924-repressor-test/platereader.ipynb`](./experiments/20260924-repressor-test/platereader.ipynb)
- [`experiments/20260925-dna-titration/platereader.ipynb`](./experiments/20260925-dna-titration/platereader.ipynb)
- [`experiments/20260926-dna-titration-esar-spent/platereader.ipynb`](./experiments/20260926-dna-titration-esar-spent/platereader.ipynb)
- [`experiments/20261001-mg-osmo-sweep/20261001-mg-osmo-sweep.ipynb`](./experiments/20261001-mg-osmo-sweep/20261001-mg-osmo-sweep.ipynb)
- [`experiments/20261007-esar-template-competition/platereader.ipynb`](./experiments/20261007-esar-template-competition/platereader.ipynb)

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
