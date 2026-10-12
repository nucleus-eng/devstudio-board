<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.

Label convention. Every admonition carries a `:name:`, because
devstudio-devnote-g-to-devnote-m matches a reviewer's reply to an admonition
by that label. An unlabeled admonition cannot be answered. A `flags-` or
`gap-` label is a question for the reviewer. A `scope-` label is context, not
a question.

This file uses no `[PLEASE FILL IN]`. Every gap is a labeled admonition, so
every gap is answerable. A table cell cannot hold an admonition, so an unknown
cell reads an em dash and the labeled admonition sits above its table.

Structure. This file follows the "Draft devnote" Doc, Drive id
1TTuVHZ0Usc0HCjXA6OAVhx5ZKViIi1gN1NrQUtLWx1E, migrated in full on 2026-10-12.
The Doc is authoritative: where this file and the Doc disagree, the Doc wins.
Results come before Methods, Result 2 splits into two subsections (solution,
gels) per the Doc's own authors' instruction, and Discussion points is the
authors' own section.
-->

# Overview

<!--
:name: gap-overview

Please fill in an overview of the demo.

Answer, from the "Draft devnote" Doc, 2026-10-11: adopted verbatim below as a
first pass, superseded 2026-10-12 by a second, authoritative pass. The first
pass is kept here because the Doc itself still carries it, marked "Draft 1
intro" and "***Ignore":

> We present a GUV hydrogel device that can produce a fluorescent output in
> response to 3-oxo-C6-HSL, the quorum sensing molecule found in bacterial
> biofilms. The fluorescent biofilm-sensing hydrogel is made up of POPC giant
> unilamellar vesicles (GUVs) embedded in an agarose hydrogel. The GUVs
> contain cell-free E. coli lysate and the luxR-mNeonGreen plasmid which
> expresses the fluorescent protein mNeonGreen in response to 3-oxo-C6-HSL.
> mNeonGreen can then be detected using fluorescent microscopy or on a
> platereader. The GUVs are made using inverted emulsion phase transfer and
> mixed into ultra low gelling agarose (0.5% final concentration) on a 384
> well plate. These gels are incubated at 37C on either a platereader or
> microscope stage overnight for 16 hours.
-->

We present a synthetic-cell based hydrogel device which can sense bacterial
contamination through quorum sensor induced cell-free protein expression.
POPC GUVs encapsulating the *E. coli* S30 lysate and the LuxR-mNeonGreen
plasmid become fluorescent in the presence of purified 3-oxo-C6-HSL quorum
sensing molecule, verified using fluorescence microscopy. Additionally, GUVs
embedded within ultra low gelling agarose still sense and respond to the HSL,
offering a material with improved structural and mechanical properties.
Finally, the LuxI plasmid, which encodes for bacterial production of
3-oxo-C6-HSL, was transformed into *E. coli*, with supernatant derived from
overnight cultures used to induce protein expression within the synthetic
cells. A mixture of fluorescence microscopy, Z-stack fluorescence microscopy
and fluorescence well plate assays were used to verify HSL induced cell-free
protein expression in bulk lysate and vesicles.

:::{admonition}
:name: gap-overview-properties-wording

Niall flagged "improved structural and mechanical properties" for a rewrite
in the source Doc, with no replacement text yet. Carried as written.
:::

:::{admonition}
:name: gap-overview-image

Please choose the overview image. The Doc marks a second spot with a bare
`[image]` placeholder, directly under this new paragraph, separate from the
schematic already placed below.
:::

:::{figure} ./general/overview.png
:label: fig-overview-schematic
:align: center
:width: 90%
Bacterial supernatant carrying 3-oxo-C6-HSL diffuses into the LuxR-mNeonGreen
GUV hydrogel. Inside one GUV, constitutively expressed LuxR binds 3-oxo-C6-HSL
and activates pLux, driving mNeonGreen expression.
:::

[`fig-overview-schematic`, file:`general/overview.png`, caption: (Bacterial supernatant carrying 3-oxo-C6-HSL diffuses into the LuxR-mNeonGreen GUV hydrogel. Inside one GUV, LuxR binds 3-oxo-C6-HSL and activates pLux-driven mNeonGreen expression.)]

<!-- A schematic, not a data figure: no notebook, no platemap, no data
chain. Placed in general/ before the G stage, per
devstudio-author-myst-content's schematic convention, and referenced by
path rather than extracted from a Doc. Added 2026-10-11, kept as-is during
the 2026-10-12 migration: the Doc's second [image] placeholder is a separate,
still-open spot, not a replacement for this one. -->

:::{danger} Unresolved before publication
:name: flags-blocking

<!-- No result was written and no data was in the tree. Resolved, 2026-10-11
and again 2026-10-12: every result now carries real narrative and real data,
migrated from the "Draft devnote" Doc in full. Still missing: a platemap, a
notebook, and any build file for any result, so no composition table exists
yet anywhere. -->

<!-- Title and date were not sourced. Title resolved, 2026-10-11:
"Fluorescent Biofilm-Sensing GUV Hydrogel", unchanged in the Doc as of
2026-10-12. Date still open. -->

:::{admonition}
:name: gap-date

The DevNote slug reads `202609`, the source log folder reads 2026-10-06, the
chat-supplied date was 2026-10-12, and the Draft Doc names no date of its own.
Please say which date belongs to this DevNote.
:::

<!-- The reporter disagreement is resolved: every Result names LuxR-mNeonGreen
or constitutive mNeonGreen directly. -->

<!-- Two plasmids needed confirming; resolved, 2026-10-11. Both files are in
`dna/`, both lengths verified, both still referenced throughout the Doc as of
2026-10-12: kept unchanged in Constructs below, including the seqviz tab-set.
Not yet on nucleus-eng/DNA; flagged for submission there. -->

**The platemap is still missing for most results.** Two new platemap links
appeared in the 2026-10-12 migration: a notebook/raw-data/platemap folder for
Result 1, and a plate map Sheet for the solution half of Result 2. Neither the
bulk-lysate platemap nor the gel platemap (if one exists) has been located
yet. See each Result below.

**No build file, so no composition table anywhere.** No build file is linked
for any result. Each result needs its own `build-composition.csv`, written
by `devstudio-build-to-composition` from a build file. See the flag in each
result below.

**The gel experiment's own results are not written yet.** The Doc's gels
subsection of Result 2 has a full protocol, a real condition table, and
twelve real microscopy store links, but no interpretive text: the authors
left a bare `Results` heading followed by `***` where that text belongs.
Carried as absent, not invented. This is also the one place in this DevNote
that still needs a hands-on pass through microscopy data before it can be
written, per Anton, 2026-10-12.

**A stale gel figure was removed.** `figures/result2-gels-platereader.png`,
titled "LuxR-mNeonGreen Sensor Gels with 10uM Purified AHL", previously sat
under Result 2 with a flag that its own title disagreed with the text (10 µM
vs 100 µM). The 2026-10-12 Doc explains why: 10 µM in gels showed no
expression at all, so the real experiment moved to 100 µM, and this figure
belongs to the earlier, abandoned attempt. The Doc itself marks the
surrounding text `***Ignore`. Removed rather than kept and relabeled, since
nothing in the current Doc still claims it.
:::

:::{admonition} Open review items
:class: warning dropdown
:name: flags-review

**Notes and What's next overlap Discussion points.** `devstudio-log-to-devnote-m`
requires Notes and What's next on every DevNote; the Doc's own outline has
neither, only Discussion points. All three are kept here. Say which survive.

**Naming people in the text.** The Doc credits Charlie with plasmid
transformation work and describes Niall's and Julia's work in the first
person throughout. Decide whether that stays as narrative or moves to an
acknowledgement.

**A sentence in Result 1 is marked for a rewrite.** Niall tagged Charlie
directly in the Doc, 2026-10-12: "Fix this up please", on the sentence
explaining why HSL sensing requires two proteins. Carried as written; not
rewritten here.

**Where the general protocols live.** Still no published Nucleus protocol is
linked from Methods below.

**Author ORCIDs and order.** No source states either, and neither author has
an ORCID on file.

**Integration challenges and next steps, by name.** Anton asked, 2026-10-11,
that Discussion or What's next explicitly cover integration challenges and
where someone else could pick this work up. Not yet written; see What's next.
:::

# Reagents

:::{admonition}
:name: gap-reagents

Please fill in {numref}`tbl-reagents`. POPC (Avanti Polar Lipids), mineral oil
(Sigma Aldrich M5904), the S30 Extract System for circular DNA (Promega),
RNase Inhibitor Murine (New England Biolabs), and 3 M sucrose (Sigma Aldrich)
are already named by component. Run `devstudio-build-to-materials` against
the Materials Reference once a build file exists and it fills in the rest.
:::

:::{table} Reagents and equipment.
:label: tbl-reagents
:align: center

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| — | — | — | N/A | N/A | N/A | |
:::

# Constructs

:::{admonition}
:name: gap-constructs

Resolved, 2026-10-11: both files are in `dna/` and rendered as sequence maps
below, with both lengths verified. Still open: neither construct exists yet
on `nucleus-eng/DNA`, so submission there is a separate, unresolved step.
Both constructs are still referenced throughout the Doc as of 2026-10-12, by
the same names, so nothing here changes.
:::

:::{table} DNA constructs. Both sequences are reproduced in full as sequence maps below; both lengths were verified against their GenBank `LOCUS` line.
:label: tbl-constructs
:align: center

| Name | Sequence | Purpose |
| --- | --- | --- |
| [pUC-IDT-LuxR-mNG](./dna/pUC-IDT-LuxR-mNG.gbk) | [Sequence map below](#seqviz-constructs) | BBa_J23101 (constitutive) drives LuxR; LuxR drives pLux; pLux drives mNeonGreen. The sensor construct for every Result. pUC-IDT-AMP GoldenGate backbone, 4671 bp. |
| [pUC-IDT-constitutive_mNG](./dna/pUC-IDT-constitutive_mNG.gbk) | [Sequence map below](#seqviz-constructs) | BBa_J23101 drives mNeonGreen directly, no LuxR and no pLux. Constitutive expression control. pUC-IDT-AMP GoldenGate backbone, 3689 bp. |
:::

<!-- Neither construct exists yet on nucleus-eng/DNA, branch
devcells/devstudio-constructs, swept 2026-10-11 before asking. Flag for
submission there, per devstudio-verify-dna-constructs Step 2's benign case:
present in this DevNote's own folder, not yet upstream. Re-confirmed
2026-10-12: both names and both Drive links are unchanged in the Doc, so the
seqviz tab-set below is retained exactly as built. -->

(seqviz-constructs)=
:::::{tab-set}

::::{tab-item} pUC-IDT-LuxR-mNG
:::{seqviz} ./dna/pUC-IDT-LuxR-mNG.gbk
:height: 600px
:::
::::

::::{tab-item} pUC-IDT-constitutive_mNG
:::{seqviz} ./dna/pUC-IDT-constitutive_mNG.gbk
:height: 600px
:::
::::

:::::

<!-- Sequence maps, one tab per construct, per devstudio-author-myst-content's
rule to group >= 2 related sequential items into a tab-set rather than stack
them. Both files verified: pUC-IDT-LuxR-mNG declares 4671 bp and carries 4671
bases, pUC-IDT-constitutive_mNG declares 3689 bp and carries 3689 bases.
Neither is yet on nucleus-eng/DNA. -->

<!-- A purchased purified protein belongs in tbl-reagents, not here. Only DNA
built or ordered as a sequence goes in the table above. -->

# Results

## Result 1 — LuxR-mNeonGreen sensor plasmid in bulk lysate

<!--
:name: gap-result-1

Answer, from the "Draft devnote" Doc, migrated 2026-10-12: adopted verbatim below, replacing the 2026-10-11 pass.
-->

To verify whether *E. coli* lysate and the LuxR-mNeonGreen plasmid can detect
3-oxo-C6-HSL in bulk, a 12.5 µL bulk lysate fluorescence assay was conducted
in 384 well plates. The LuxR-mNeonGreen plasmid constitutively expresses the
LuxR transcription factor in *E. coli* lysate, which is activated by the HSL
signal. Upon activation, LuxR dimerizes, enabling it to bind to the Lux box
situated adjacent to the RNA polymerase promoter sequence. The activated LuxR
recruits the σ70 subunit of RNA polymerase, activating transcription. The
constitutive mNeonGreen plasmid does not contain the Lux box, so RNA
polymerase does not require activated LuxR for protein expression.

:::{admonition}
:name: gap-result-1-mechanism-sentence

Marked by Niall, 2026-10-12, for Charlie to rewrite: "This is due to HSL
sensing requiring the production of two proteins, firstly constitutive
expression of the transcription factor LuxR which binds with HSL to induce
expression of mNeonGreen." Carried as written, not rewritten here.
:::

Similar cell-free biosensors for bacterial detection using quorum sensing
have been developed in lysate-based systems with the LasR transcription
factor and 3-oxo-C12-HSL quorum sensor
([Wen, Garenne et al.](https://pubs.acs.org/asbcd6/article/6/12/2293/731020/A-Cell-Free-Biosensor-for-Detecting-Quorum-Sensing)).

:::{table} Bulk lysate assay experimental conditions. Triplicates performed for each run.
:label: tbl-bulk-lysate-conditions
:align: center

| Condition | Plasmid | Final HSL concentration (µM) | Wells |
| --- | --- | --- | --- |
| HSL sensing | LuxR-mNeonGreen | 10 | A1-3 |
| Negative control | LuxR-mNeonGreen | 0 | A4-6 |
| Constitutive control | Constitutive mNeonGreen | 0 | A7-9 |
:::

It is clear there is a significant difference in fluorescent signal in the
presence and absence of 10 µM 3-oxo-C6-HSL, confirming that the sensor
construct can successfully detect low concentrations of HSL in *E. coli*
lysate with minimal leaky expression ({numref}`fig-result1-platereader`).
Additionally, the constitutive control has significantly higher mNeonGreen
expression than the HSL induced reaction. Future experiments will focus on
lowering the HSL concentration to find the limit of detection for the
combined lysate and sensor construct.

:::{admonition}
:name: gap-result-1-open-threads

Three open threads sit on this paragraph in the Doc, unresolved as of
2026-10-12: Niall asks "where is this plot?" next to the limit-of-detection
sentence, meaning a further plot is expected here and not yet added; Niall
asks whether the lysate for this experiment was dissolved in water or outer
solution; Julia answers elsewhere in the Doc that it is water, and this
figure's legend has since been corrected to drop "(outer solution)"
accordingly. Niall also offers to write a short paragraph on constitutive
expression (higher signal, one protein, no dependence on HSL concentration)
once confirmed; not yet written.
:::

:::{figure} ./figures/result1-bulk-lysate-platereader.png
:label: fig-result1-platereader
:align: center
:width: 85%
Fluorescence intensity over time for the LuxR-mNeonGreen plasmid in bulk
lysate reactions with and without 10 µM HSL, and for the constitutive
mNeonGreen plasmid. + 10 µM and − 10 µM HSL refer to the HSL sensing and
negative control conditions in {numref}`tbl-bulk-lysate-conditions`.
:::

[`fig-result1-platereader`, platemap: none, data source: none, caption: (Fluorescence intensity over time for LuxR-mNeonGreen in bulk lysate, with and without 10 µM HSL, and constitutive mNeonGreen for comparison.)]

<!-- missing notebook -->

<!-- Extracted from the "Draft devnote" Doc's own .docx export,
word/media/image2.png as of the 2026-10-12 export (the file at this
relationship position changed between the 2026-10-11 and 2026-10-12 exports;
re-extracted rather than reused). Supersedes the earlier two-trace figure,
which carried an incorrect "Control (outer solution)" legend that Julia
corrected in the Doc's own comment thread to "water". -->

:::{danger} Missing build file
:name: flags-build-result-1

No `build-composition.csv` exists for this experiment, so no composition table
can go here. Run `devstudio-build-to-composition` on the build file.
:::

:::{admonition}
:name: gap-deviation-result-1

Please state how this run differed from the general protocol in {numref}`sec-methods`, if at all.
:::

Notebook, raw data and plate map:
<https://drive.google.com/drive/folders/1qj-nD5VPI9iQMVWTkelPlepb41rjsfsY>.

The log directory for this result:
<https://drive.google.com/drive/folders/1lK_ylF47jmR3pFxp-3bD9PqyszQyiTUX>.

## Result 2 — detecting purified HSL using lysate-based synthetic cells

<!--
:name: gap-result-2

Answer, from the "Draft devnote" Doc, migrated 2026-10-12. The Doc asks
Claude to give this result two subtitles, solution and gels; done below.
-->

To demonstrate the ability of synthetic cells to detect HSL, lysate-based
GUVs encapsulating the LuxR-mNeonGreen plasmid were resuspended in outer
solution containing HSL and visualized by brightfield and fluorescence
microscopy over time. Additionally, to improve vesicle stability and
robustness, the synthetic cells were embedded in 1 wt% (w/v) ultra-low
gelling temperature agarose (ULGA), with purified HSL added to the top of the
gel to induce mNeonGreen expression. Time point and Z-stack fluorescence
microscopy were used throughout this section.

3-oxo-C6-HSL has been shown elsewhere to passively diffuse across artificial
lipid bilayer membranes and induce protein expression in *E. coli*
lysate-based systems
([Garenne et al.](https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/syst.202300029)).
It would therefore be expected that HSL can permeate the GUV lipid membrane
into the synthetic cell. As HSL is non-fluorescent, this could not be
verified directly; it is instead verified indirectly through LuxR-induced
expression of a fluorescent protein.

### Detecting purified HSL using lysate-based synthetic cells in solution

Three experimental conditions were used for HSL sensing synthetic cells in
solution, shown in {numref}`tbl-solution-conditions`. Methods for
lysate-based synthetic cell formation are in {numref}`sec-methods`, under
Lysate GUVs preparation.

:::{table} Purified HSL sensing in GUVs, solution. Wells J12-14 were from a different experiment.
:label: tbl-solution-conditions
:align: center

| Condition | Plasmid | Solution GUV pellet was resuspended in | Wells |
| --- | --- | --- | --- |
| HSL sensing GUVs | LuxR-mNeonGreen | 10 µM HSL in outer solution | J3, J4, J5 |
| Negative control | LuxR-mNeonGreen | Outer solution | J6, J7, J8 |
| Constitutive control | Constitutive mNeonGreen | Outer solution | J9, J10, J11 |
:::

Microscopy images were acquired every 20 minutes across 17 time points, in
the store
[`Lysate_LuxR_Cytosol_EsaR_2026-10-05_18-59-02.423661.zarr`](https://data.nucleus.engineering/microscopy/nucleus-bnext-01/Lysate_LuxR_Cytosol_EsaR_2026-10-05_18-59-02.423661.zarr).
Plate map:
<https://docs.google.com/spreadsheets/d/17V5zdl5ebfRpTSc5XnVHenCmLCfFspMTcQ0KqSPfDu0/edit?gid=1906581583#gid=1906581583>.

:::{admonition}
:name: gap-solution-viewer

No interactive viewer or static figure has been built for this store yet.
Unlike the Result 3 store, this one has not had a crop, zoom or contrast
decision made for it. This is one of the hands-on microscopy items to work
through together, per Anton, 2026-10-12.
:::

From the endpoint microscopy data, the HSL sensing GUVs have increased
fluorescence output compared to the negative control without HSL. This shows
that the combined lysate and DNA template used for bulk assays in
{numref}`fig-result1-platereader` can be successfully encapsulated within
GUVs, and that HSL can permeate into the vesicles and induce protein
expression. Although not quantified, the difference in signal between the
negative control and HSL induced expression appears significantly lower than
the bulk lysate reactions. This suggests that either the HSL concentration is
significantly lower, or there is reduced concentration of essential
components for CFPS within the vesicles, such as the plasmid, which can occur
during vesicle encapsulation.

Similarly to the bulk lysate plate assays, the constitutive control has
significantly higher and quicker mNeonGreen expression than the HSL induced
system in GUVs. This is expected, due to only requiring the production of a
single protein and non-reliance on HSL membrane transport and binding for
mNeonGreen expression. Future work for this section will focus on reducing
the HSL concentration to quantify the limit of detection of the system within
synthetic cells.

### Detecting purified HSL using lysate-based synthetic cells in gels

Embedding synthetic cells within hydrogels allows a medium to distribute the
vesicle population evenly throughout the material, and lets it be placed on
solid surfaces for potential biosensing applications. Additionally, gel
materials offer mechanical support and should lead to increased stability of
GUVs compared with solution, with greater robustness broadening the scope for
potential applications. Throughout this section, HSL sensing GUVs are
embedded within 0.5% ULGA, following the same lysate-based GUV protocol as
the solution subsection above.

{numref}`sec-methods`, under GUV embedding in gels for synthetic AHL
experiment, covers the steps for embedding GUVs in 0.5% ULGA. In summary, 1
wt% ULGA is heated above its gelling temperature and mixed thoroughly with
the GUV pellet at equal volumes, then added to a 384 well plate. Z-stack
fluorescence microscopy is then used to assess fluorescence throughout the
gel after 16 hours. After gelling, 10 µL of stock HSL is added to the top of
the gel, corresponding to a final concentration of 100 µM; 10 µL of outer
solution was added to the top of gels for experiments without HSL.

:::{admonition}
:name: gap-gel-10um-attempt

The higher HSL concentration compared to solution was to account for slower
HSL diffusion through the material, and for having previously seen no
expression with 10 µM HSL in gels. That earlier attempt was only conducted
once and should be repeated in future. The figure from that attempt
(`LuxR-mNeonGreen Sensor Gels with 10uM Purified AHL`) is explicitly marked
`***Ignore` in the source Doc and has been removed from this DevNote rather
than kept.
:::

:::{table} Gel conditions, synthetic cells, HSL. Triplicates for each experiment; empty ULGA gels included to account for light scattering from vesicles.
:label: tbl-gel-conditions
:align: center

| Condition | Plasmid | Well |
| --- | --- | --- |
| HSL sensing gels | LuxR-mNeonGreen | D3, D4, D5 |
| Negative control gels | LuxR-mNeonGreen | D6, D7, D8 |
| Constitutive control gels | Constitutive mNeonGreen | D9, D10, D11 |
| Empty ULGA gels | N/A | D12, D13, D14 |
:::

:::{admonition}
:name: gap-confocal-note

Ideally, confocal microscopy would have been used for the Z-stacks through
the gels, to reduce light scattering from vesicles in different planes; this
was not possible due to equipment constraints. Carried as the Doc states it,
not resolved.
:::

Twelve microscopy stores exist for this subsection, one per well, grouped by
condition below. None has yet had a figure, crop, zoom or contrast decision
made, and no interpretive results text has been written for this subsection
at all: the Doc's own `Results` heading here is followed only by `***`. This
whole subsection is the hands-on microscopy pass still to do, per Anton,
2026-10-12.

:::{admonition}
:name: gap-gel-results-narrative

No interpretive text exists yet for the gel results. The condition table,
the protocol, and the twelve store links below are real; the narrative that
should follow them is not written. Do not invent it here.
:::

Constitutive mNeonGreen expression with no HSL added (wells D9, D10, D11):

- [`J_N_Consitutive_AHL_D9_gels`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_Consitutive_AHL_D9_gels_2026-10-07_14-52-02.837332.zarr)
- [`J_N_Consitutive_AHL_D10_gel_bigger_areas`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_Consitutive_AHL_D10_gel_bigger_areas_2026-10-07_14-55-47.101109.zarr) — a bigger area was measured because of a large air bubble
- [`J_N_Consitutive_AHL_D11_gels`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_Consitutive_AHL_D11_gels_2026-10-07_14-53-48.138799.zarr)

LuxR-mNeonGreen with no HSL added (wells D3, D4, D5):

- [`J_N_-100uM_AHL_D3_gels`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_-100uM_AHL_D3_gels_2026-10-07_14-48-25.644803.zarr)
- [`J_N_-100uM_AHL_D4_gels`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_-100uM_AHL_D4_gels_2026-10-07_14-46-52.618937.zarr)
- [`J_N_-100uM_AHL_D5_gels`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_-100uM_AHL_D5_gels_2026-10-07_14-44-55.273559.zarr)

LuxR-mNeonGreen with 100 µM HSL added (wells D6, D7, D8):

- [`J_N_+100uM_AHL_D6_gels`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_%2B100uM_AHL_D6_gels_2026-10-07_14-36-46.345035.zarr)
- [`J_N_+100uM_AHL_D7_gels`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_%2B100uM_AHL_D7_gels_2026-10-07_14-42-23.412204.zarr)
- [`J_N_+100uM_AHL_D8_gels`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_%2B100uM_AHL_D8_gels_2026-10-07_14-50-18.509646.zarr)

Empty ULGA gels (wells D12, D13, D14):

- [`J_N_just_gel_1`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_just_gel_1_2026-10-07_15-04-39.160520.zarr)
- [`J_N_just_gel_2`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_just_gel_2_2026-10-07_15-06-06.512744.zarr)
- [`J_N_just_gel_3`](https://bnext-bio.github.io/vizarr/?source=https://data.nucleus.engineering/microscopy/nucleus-bnext-01/J_N_just_gel_3_2026-10-07_15-07-38.879378.zarr)

<!-- The doc's naming for the +100uM wells literally reads "+100uM" in the
Drive filenames even though the gel's stated final concentration is 100 µM in
all three cases (D6, D7, D8); filenames carried verbatim, not corrected. -->

:::{danger} Missing build file
:name: flags-build-result-2

No `build-composition.csv` exists for this experiment, so no composition table
can go here. Run `devstudio-build-to-composition` on the build file.
:::

:::{admonition}
:name: gap-deviation-result-2

Please state how this run differed from the general protocol in {numref}`sec-methods`, if at all.
:::

Log directories: the GUVs-in-solution run (2nd/3rd October) is at
<https://drive.google.com/drive/folders/15EQ5kkf6LlnIJqQShonYNE3fKh8O3PgD>, and
the gel run is at
<https://drive.google.com/drive/folders/1j4vF36gjF_jpaGyI8fI-_uyUs-M6mC2d>.

## Result 3 — detecting bacterially produced HSL in solution

<!--
:name: gap-result-3

Answer, from the "Draft devnote" Doc, migrated 2026-10-12: adopted verbatim below, with one new comparative sentence added since the 2026-10-11 pass.
-->

To model bacterial sensing using GUVs, the LuxI plasmid was transformed into
DH5α *E. coli* (DH5α w/ LuxI) to encode production of 3-oxo-C6-HSL, the
small-molecule quorum sensor detected in the previous sections. The same
LuxR-mNeonGreen plasmid was used to verify whether lysate-based synthetic
cells are capable of detecting bacterially produced HSL, implemented through
resuspending the GUV pellet in bacterial supernatant. Control experiments
were performed with the DH5α strain without the LuxI plasmid (DH5α ΔLuxI),
which removes HSL from the supernatant.

:::{admonition}
:name: gap-constitutive-vs-positive-control-naming

Niall asked, 2026-10-11, whether "positive control" is the right name for
this condition; Julia replied "Yes I would say so" on 2026-10-11. The table
text itself was separately edited to read "Constitutive control" everywhere
by 2026-10-12. The comment thread and the document body now disagree.
Migrated here as "Constitutive control", matching the current table text, not
the comment thread's reply.
:::

:::{table} Three experimental conditions for HSL-induced mNeonGreen expression using bacterial supernatant in solution.
:label: tbl-supernatant-conditions
:align: center

| Condition | Plasmid | Supernatant used |
| --- | --- | --- |
| HSL sensing GUVs | LuxR-mNeonGreen | DH5α w/ LuxI |
| Negative control | LuxR-mNeonGreen | DH5α ΔLuxI |
| Constitutive control | Constitutive mNeonGreen | DH5α ΔLuxI |
:::

Lysate GUVs were prepared following the standard protocol in {numref}`sec-methods`
up to the resuspension step. The GUV pellets were resuspended in 100 µL of
1:10 supernatant to outer solution, and 30 µL was added to a 384 well plate
for visualization. One GUV preparation was run per condition, split into
three wells for microscopy. Brightfield and 488 nm fluorescence microscopy
were both run on each sample over time, images acquired every 20 minutes for
about 7 hours.

:::{table} Well plate mapping for the three conditions in {numref}`tbl-supernatant-conditions`.
:label: tbl-supernatant-wells
:align: center

| Condition | Wells |
| --- | --- |
| HSL sensing GUVs | C3, C4, C5 |
| Negative control | C6, C7, C8 |
| Constitutive control | C9, C10, C11 |
:::

Supernatant from DH5α carrying the LuxI plasmid induced mNeonGreen expression
within lysate GUVs carrying the LuxR-mNeonGreen plasmid, visible by
fluorescence microscopy at 488 nm (wells C3 to C5). After about 80 minutes,
mNeonGreen expression becomes visible within some GUVs, with more GUVs
expressing over time. Expression is clearly visible throughout the well, but
overlapping brightfield and 488 nm fluorescence shows that many GUVs had no
expression, likely because they did not encapsulate all the machinery
lysate-based TXTL needs.

Lysate GUVs carrying the same plasmid, resuspended in supernatant from
bacteria without the LuxI plasmid, had minimal expression over the 7 hour
experiment (wells C6 to C8). This shows that HSL is required to induce
expression within lysate GUVs, and that HSL made by *E. coli* can be detected
by synthetic cells. Interestingly, the fluorescence intensity of
LuxR-mNeonGreen lysate GUVs induced by bacterial supernatant was
significantly higher than with 10 µM purified HSL, indicating that
significantly more HSL is produced by overnight inoculation of DH5α w/ LuxI
than the 10 µM purified HSL used in {numref}`tbl-solution-conditions`. Future
work should include supernatant in the bulk lysate assays
({numref}`fig-result1-platereader`), with supernatant extracted at various
time points.

Synthetic cells carrying the constitutive mNeonGreen plasmid in DH5α ΔLuxI
supernatant expressed after about 40 minutes, with expression increasing over
the experiment (wells C9 to C11). The faster expression compared to
LuxR-mNeonGreen follows from synthesizing one protein only, with no
dependency on HSL entering the cell and activating mNeonGreen expression.

The three conditions are shown as interactive viewers, one well per
condition, on
[2026-10-08 — Interactive viewer](./2026-10-08-interactive-viewer.md). That
page carries the open questions on contrast and timepoint.

:::::{tab-set}

::::{tab-item} HSL sensing GUVs
:::{figure} ./figures/fov-c4.png
:label: fig-fov-c4
:align: center
:width: 75%
Well C4, HSL sensing GUVs (LuxR-mNeonGreen, DH5α w/ LuxI supernatant), T = 19,
GFP channel only, contrast windowed 30000 to 60000. 659 µm field of view,
cropped and zoomed to Anton's own Vizarr view state.
:::
::::

::::{tab-item} Negative control
:::{figure} ./figures/fov-c7.png
:label: fig-fov-c7
:align: center
:width: 75%
Well C7, negative control (LuxR-mNeonGreen, DH5α ΔLuxI supernatant), T = 19,
GFP channel only, contrast windowed 30000 to 60000. Same crop and zoom as the
other two panels; carried as imaged, near-empty as expected for this control.
:::
::::

::::{tab-item} Constitutive control
:::{figure} ./figures/fov-c10.png
:label: fig-fov-c10
:align: center
:width: 75%
Well C10, constitutive control (constitutive mNeonGreen, DH5α ΔLuxI
supernatant), T = 19, GFP channel only, contrast windowed 30000 to 60000. Same
crop and zoom as the other two panels.
:::
::::

:::::

[`fig-fov-c4`, platemap: none, data source:`nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/4/0`, caption: (Well C4, HSL sensing GUVs, T = 19, GFP channel only, cropped and zoomed.)]

[`fig-fov-c7`, platemap: none, data source:`nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/7/0`, caption: (Well C7, negative control, T = 19, GFP channel only, cropped and zoomed.)]

[`fig-fov-c10`, platemap: none, data source:`nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/10/0`, caption: (Well C10, constitutive control, T = 19, GFP channel only, cropped and zoomed.)]

<!-- missing notebook -->

<!-- All three rendered by general/render-microscopy-fovs.py, adapted from
devnote-swh-20260925-ph-sensor-in-solution's own script of the same name.
One well per condition, the triplicate's middle well (C4, C7, C10), chosen
because Anton's own Vizarr link named C4. One target and one zoom for all
three, copied verbatim from that link, so every panel sits at the same pixel
offset and scale. GFP channel only, T = 19, window 30000-60000 fixed rather
than computed, per Anton's instruction. No notebook or platemap exists yet
for this store, so asset_chain_complete is false in manifest.json.
Captions and tab labels updated 2026-10-12: "Positive control" renamed
"Constitutive control" to match the Doc's current table wording; see
gap-constitutive-vs-positive-control-naming above. -->

:::{admonition}
:name: gap-fov-rendering

Confirm the representative well choice (the middle well of each triplicate) and the fixed output size, 1080x1080 px, both chosen without a stated reason beyond consistency with the existing SWH script.
:::

:::{danger} Missing build file
:name: flags-build-result-3

No `build-composition.csv` exists for this experiment, so no composition table
can go here. Run `devstudio-build-to-composition` on the build file.
:::

:::{admonition}
:name: gap-deviation-result-3

Please state how this run differed from the general protocol in {numref}`sec-methods`, if at all.
:::

<!-- A microscopy result also needs the per-object parquet beside the store, if
one exists, and the analysis notebook. Niall's log carries two open TODOs for
exactly this: the zarr URLs and the analysis notebook. -->

(sec-methods)=
# Methods

:::{admonition}
:name: scope-methods

Each subsection below is a general protocol. Where one matches a published Nucleus protocol, link to that protocol and state only the differences. Each result above carries its own deviations rather than restating a protocol.
:::

## Bulk lysate (12.5 µL reaction)

Mix amino acids using equal volumes from each provided tube (−Met, −Cys,
−Lys). Assemble the following from the Promega circular lysate kit on ice:

:::{table} Bulk lysate reaction, 12.5 µL.
:label: tbl-bulk-lysate
:align: center

| Component | Volume (µL) |
| --- | --- |
| DNA | X (40 ng/µL final concentration) |
| Amino acids | 2.5 |
| S30 Premix | 10 |
| S30 Extract | 7.5 |
| Murine RNase Inhibitor | 1.25 |
| Nuclease free water | 3.75 − X |
| Total | 12.5 |
:::

Place 10 µL of the reaction in a 384 low volume plate and incubate in a plate
reader at 37 °C for 4 hours.

## Lysate GUVs preparation

Create lipid thin films in a glass vial using 160 µL of 25 mg/mL POPC
chloroform stock and dry under nitrogen gas. Place the films in a vacuum
desiccator overnight. Add 1 mL of mineral oil to each film.

Prepare the inner solution using the table below.

:::{table} Inner solution (lysate), 12.5 µL.
:label: tbl-inner-solution
:align: center

| Component | Volume (µL) |
| --- | --- |
| DNA | X (40 ng/µL final concentration) |
| Amino acids | 2.5 |
| S30 Premix | 10 |
| S30 Extract | 7.5 |
| Murine RNase Inhibitor | 1.25 |
| Sucrose (3 M) | 1.25 |
| Nuclease free water | 2.50 − X |
| Total | 12.5 |
:::

Prepare the outer solution with the concentrations in the table below.

:::{table} Outer solution, 5 mL.
:label: tbl-outer-solution
:align: center

| Sample | Stock concentration (M) | Volume added (mL) | Final concentration in outer solution (mM) |
| --- | --- | --- | --- |
| Potassium Glutamate | 1 | 2.89 | 578 |
| HEPES | 0.5 | 0.72 | 72 |
| Glucose | 1.8 | 0.83 | 299 |
| MQ water | N/A | 0.56 | N/A |
:::

Label two microcentrifuge tubes "inner" and "outer". Pipette 300 µL outer
solution into the outer tube and 200 µL lipid-in-oil into the inner tube. Add
20 µL of lysate solution to the lipid-in-oil and emulsify 20 to 25 times using
a P1000 pipette. Immediately layer the emulsion onto the outer solution and
let it sit at room temperature for 5 minutes, to let the monolayer form at the
aqueous-oil interface. Centrifuge at 9000 ×g for 15 minutes. Clear the oil
layer and the old outer solution. Resuspend the pellet with 100 µL outer
solution. Incubate overnight at 37 °C in a plate reader or microscope.

## GUV embedding in gels for synthetic AHL experiment

Make a 1% ULGA stock, with ULGA dissolved in the outer solution from
{numref}`tbl-outer-solution`. Heat in a microwave or on a hot plate until the
solution is bubbling. Allow it to cool to a temperature that can be held by
hand, and before it gels, pipette 25 µL of GUVs and 25 µL of ULGA into a 384
well plate and mix. Place on ice or in a fridge for 10 minutes. Add 10 µL of
600 µM AHL, giving a final gel concentration of 100 µM, and incubate at 37 °C
in a plate reader or microscope overnight.

## Supernatant preparation

Inoculate 5 mL LB (ampicillin) with the DH5α strain carrying the LuxI
producing plasmid. Incubate overnight at 37 °C. Centrifuge for 15 minutes.
Pipette the supernatant into a separate tube. Sterile filter the supernatant
with a 0.22 µm filter. Store at −20 °C until use.

# Discussion points

## Plate reader against microscopy

:::{admonition}
:name: gap-discussion-readout

Please write the pros and cons, including supernatant in the plate reader, which the outline raises as its own point.
:::

## Synthetic AHL against bacterial supernatant

:::{admonition}
:name: gap-discussion-ahl

Please write this comparison. Result 3 already notes that bacterial supernatant gave a significantly higher signal than 10 µM purified HSL; expand on that here.
:::

## Gel embedding and ULGA

:::{admonition}
:name: gap-discussion-gel

Please write the potential issues with gel embedding, which the outline names as ULGA.
:::

## Dynamic range in bulk vs GUVs

:::{admonition}
:name: gap-discussion-dynamic-range

Please write this comparison. Result 2's solution subsection already notes
that the signal difference in GUVs appears lower than in bulk lysate; expand
on that here.
:::

# Notes

:::{admonition}
:name: gap-notes

Please note any caveats or gotchas that do not belong in Discussion points.
:::

# What's next

:::{admonition}
:name: gap-whats-next

Based on what is described here, what comes next? Anton asked, 2026-10-11,
that this section or Discussion specifically cover integration challenges and
where someone else could pick this work up and take it forward.
:::

# Resources

:::{admonition}
:name: gap-resources

Please list the files this DevNote draws on beyond the links below. `devstudio-assemble-devnote-assets` writes one link per file in `experiments/` once the assets land.
:::

Log folders and data, one set per result, from the "Draft devnote" Doc:

- Result 1, bulk lysate log: <https://drive.google.com/drive/folders/1lK_ylF47jmR3pFxp-3bD9PqyszQyiTUX>
- Result 1, notebook, raw data and plate map: <https://drive.google.com/drive/folders/1qj-nD5VPI9iQMVWTkelPlepb41rjsfsY>
- Result 2, GUVs in solution log (2nd/3rd October): <https://drive.google.com/drive/folders/15EQ5kkf6LlnIJqQShonYNE3fKh8O3PgD>
- Result 2, solution microscopy store: <https://data.nucleus.engineering/microscopy/nucleus-bnext-01/Lysate_LuxR_Cytosol_EsaR_2026-10-05_18-59-02.423661.zarr>
- Result 2, solution plate map: <https://docs.google.com/spreadsheets/d/17V5zdl5ebfRpTSc5XnVHenCmLCfFspMTcQ0KqSPfDu0/edit?gid=1906581583#gid=1906581583>
- Result 2, gel log: <https://drive.google.com/drive/folders/1j4vF36gjF_jpaGyI8fI-_uyUs-M6mC2d>
- Result 2, twelve gel microscopy stores: listed inline under the gels subsection above, grouped by condition.
- Result 3, microscopy store: <https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr>; no separate log folder link was given.
