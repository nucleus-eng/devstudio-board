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

Structure. This file follows the "Draft devnote" outline, Drive id
1TTuVHZ0Usc0HCjXA6OAVhx5ZKViIi1gN1NrQUtLWx1E, as restructured on 2026-10-08.
Results come before Methods, there are four results, Methods holds the general
protocols, and Discussion points is the authors' own section.
-->

# Overview

<!--
:name: gap-overview

Please fill in an overview of the demo. What does the system do, and what does the set of four results demonstrate together. A nice overview image fits well here too.

Answer, from the "Draft devnote" Doc (1TTuVHZ0Usc0HCjXA6OAVhx5ZKViIi1gN1NrQUtLWx1E), 2026-10-11: adopted verbatim below.
-->

We present a GUV hydrogel device that can produce a fluorescent output in
response to 3-oxo-C6-HSL, the quorum sensing molecule found in bacterial
biofilms. The fluorescent biofilm-sensing hydrogel is made up of POPC giant
unilamellar vesicles (GUVs) embedded in an agarose hydrogel. The GUVs contain
cell-free *E. coli* lysate and the LuxR-mNeonGreen plasmid, which expresses the
fluorescent protein mNeonGreen in response to 3-oxo-C6-HSL. mNeonGreen can
then be detected using fluorescent microscopy or on a plate reader. The GUVs
are made using inverted emulsion phase transfer and mixed into ultra-low
gelling agarose (0.5% final concentration) on a 384 well plate. These gels are
incubated at 37 °C on either a plate reader or microscope stage overnight for
16 hours.

<!--
:name: gap-overview-image

Please choose the overview image. The source Doc marks the spot with a bare `[image]` placeholder and names no file.

Answer, Anton, 2026-10-11: adopted below.
-->

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
path rather than extracted from a Doc. Added 2026-10-11. -->

:::{danger} Unresolved before publication
:name: flags-blocking

<!-- No result was written and no data was in the tree. One source log
existed, 01-logs/NM_2026_10_6_LuxR_mNeonGreen_lysate_GUVs, ending at a bare
"# results" heading with two TODO lines, for the zarr URLs and the analysis
notebook.

Resolved, 2026-10-11, by the "Draft devnote" Doc
(1TTuVHZ0Usc0HCjXA6OAVhx5ZKViIi1gN1NrQUtLWx1E): all three results now carry
real narrative, and Result 3 carries real microscopy data from the zarr store
named in that log. Still missing: a platemap, a notebook, and any build file,
so no composition table exists yet for any result. -->

<!-- Title and date were not sourced. The working title "LuxR-GFP Sensor
Demo" and the date 2026-10-12 both came from Anton in chat on 2026-10-05, with
no Specification table.

Title resolved, 2026-10-11: "Fluorescent Biofilm-Sensing GUV Hydrogel", from
the Draft Doc, confirmed by Anton. Date still open: the DevNote slug reads
202609, the source log folder reads 2026-10-06, and the Draft Doc names no
date of its own. -->

<!-- The reporter disagreed between sources. The outline named "luxRGFP" in
Result 1; Niall's log said LuxR-mNeonGreen, with LuxR-deGFP named as an older,
different, noisier construct. The title said GFP.

Resolved, 2026-10-11: the new title names neither GFP nor mNeonGreen
specifically, and every Result now names LuxR-mNeonGreen or constitutive
mNeonGreen directly, confirmed against the sequence files in dna/. -->

:::{admonition}
:name: gap-date

The DevNote slug reads `202609`, the source log folder reads 2026-10-06, the
chat-supplied date was 2026-10-12, and the Draft Doc names no date of its own.
Please say which date belongs to this DevNote.
:::

<!-- Two plasmids needed confirming. Anton asked on the log, 2026-10-08,
whether two Drive files were the right sequences:
LuxR-mNeonGreen (https://drive.google.com/file/d/1e5L7jQ__aO_MeMcwlx6gr9byjV8Ajacy/view)
and constitutive mNeonGreen
(https://drive.google.com/file/d/13UvMR_uMa6FjVXUupdM4AvQvfDoaLTIz/view).

Resolved, 2026-10-11: Anton added pUC-IDT-LuxR-mNG.gbk (4671 bp) and
pUC-IDT-constitutive_mNG.gbk (3689 bp) to dna/. Both declared LOCUS lengths
match their actual base counts exactly. Feature labels confirm identity:
pUC-IDT-LuxR-mNG carries BBa_J23101 (constitutive) driving LuxR, LuxR driving
pLux, and pLux driving mNeonGreen. pUC-IDT-constitutive_mNG carries
BBa_J23101 driving mNeonGreen directly, with no LuxR and no pLux, matching its
role as the constitutive control. Both sit on a pUC-IDT-AMP GoldenGate
backbone (AmpR). Not verified: byte-identity against the two Drive files
originally linked, since this check compares length and feature labels, not
file contents.

Swept nucleus-eng/DNA, branch devcells/devstudio-constructs, before asking:
neither construct is there. That branch carries J23101-luxR-linear.gb (the
sensor alone), LuxR-deGFP and pOpen-LuxR-deGFP (the older deGFP reporter
Niall's log says this work replaces), and two PLA1 effectors, all tagged
detector-3oc6-hsl. No mNeonGreen reporter variant exists upstream yet. Per
devstudio-verify-dna-constructs Step 2, this is the benign case: present in
this DevNote's own folder, not yet in the canonical repo. Flag for
submission to nucleus-eng/DNA before or alongside this DevNote's own
publication. -->

**The platemap is missing.** Anton asked on the log, 2026-10-08, for the
platemap of the microscopy experiment to be put in that log directory. It is
not there.

**No build file, so no composition table anywhere.** The log folder holds an
untitled, empty spreadsheet. Each result needs its own
`build-composition.csv`, written by `devstudio-build-to-composition` from a
build file. See the flag in each result below.

<!-- Result 4 has not run. The outline listed gels against bacterial
supernatant, and nothing in any source described it. Resolved, 2026-10-11, by
the "Draft devnote" Doc: the real experiment is GUVs resuspended in
supernatant and read in solution, not gels, and it has run. It is now Result
3, with real narrative, a condition table, a well map and three figures. -->
:::

:::{admonition} Open review items
:class: warning dropdown
:name: flags-review

**Structure changed on 2026-10-08.** This file previously carried three
results, a `# Protocol` section ahead of a `# Methods` section of composition
tables, and no Discussion. It now follows the authors' own outline. Results
moved ahead of Methods, a fourth result was added, Protocol and Methods merged
under the name Methods, and Discussion points was added. Composition tables
move into the result they belong to, because Methods now holds protocols.

**Notes and What's next overlap Discussion points.** The outline has Discussion
points and neither of the other two. `devstudio-log-to-devnote-m` requires
Notes and What's next on every DevNote. All three are kept here. Say which
survive and I will drop the others.

**Naming people in the text.** Anton asked on the log, 2026-10-08, how much
the DevNote should call out specific people. The log credits Charlie with the
transformations and describes Julia's parallel run in the first person. Decide
whether that stays as narrative or moves to an acknowledgement.

<!-- AHL was named only by its class. The outline wrote AHL and gave 10 µM for
Results 1 and 2 and 100 µM for Result 3, under the old four-result numbering.
It did not say which acyl-homoserine lactone. Niall's log wrote "HSL" at 10
µM.

Proposed, 2026-10-11, rather than asked: every LuxR-tagged construct on
nucleus-eng/DNA's devcells/devstudio-constructs branch is tagged
`detector-3oc6-hsl`, the canonical LuxR ligand 3OC6-HSL
(N-(3-oxohexanoyl)-L-homoserine lactone).

Confirmed, 2026-10-11, by the "Draft devnote" Doc's own Overview paragraph,
which names 3-oxo-C6-HSL directly. Resolved. -->

**Where the general protocols live.** Anton asked on the log, 2026-10-08,
where the GUV prep protocol lives. If a Methods subsection below matches a
published Nucleus protocol, it links to that protocol and states only the
differences. None is linked yet.

**Author ORCIDs and order.** `curvenote.yml` lists Julia Purrinos de Oliveira
first, then Niall McIntyre, both at Imperial College London. Anton supplied all
of it on 2026-10-05. No source states it and neither author has an ORCID.
:::

# Reagents

:::{admonition}
:name: gap-reagents

Please fill in {numref}`tbl-reagents`. Niall's log already names POPC from Avanti Polar Lipids, mineral oil from Sigma Aldrich M5904, the S30 Extract System for circular DNA from Promega, RNase Inhibitor Murine from New England Biolabs, and 3 M sucrose from Sigma Aldrich. Run `devstudio-build-to-materials` against the Materials Reference once a build file exists and it fills in the rest.
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

Please confirm the two plasmids named in {numref}`flags-blocking`, include each sequence inline in the table below, and add the matching file to `dna/` in `.gb` format. `devstudio-verify-dna-constructs` checks each one by length against its GenBank LOCUS line.

Resolved, 2026-10-11: both files are in `dna/` and rendered as sequence maps
below, with both lengths verified. Still open: neither construct exists yet
on `nucleus-eng/DNA`, so submission there is a separate, unresolved step.
:::

:::{table} DNA constructs. Both sequences are reproduced in full as sequence maps below; both lengths were verified against their GenBank `LOCUS` line.
:label: tbl-constructs
:align: center

| Name | Sequence | Purpose |
| --- | --- | --- |
| [pUC-IDT-LuxR-mNG](./dna/pUC-IDT-LuxR-mNG.gbk) | [Sequence map below](#seqviz-constructs) | BBa_J23101 (constitutive) drives LuxR; LuxR drives pLux; pLux drives mNeonGreen. The sensor construct for Results 1 through 4. pUC-IDT-AMP GoldenGate backbone, 4671 bp. |
| [pUC-IDT-constitutive_mNG](./dna/pUC-IDT-constitutive_mNG.gbk) | [Sequence map below](#seqviz-constructs) | BBa_J23101 drives mNeonGreen directly, no LuxR and no pLux. Constitutive expression control. pUC-IDT-AMP GoldenGate backbone, 3689 bp. |
:::

<!-- Neither construct exists yet on nucleus-eng/DNA, branch
devcells/devstudio-constructs, swept 2026-10-11 before asking. Flag for
submission there, per devstudio-verify-dna-constructs Step 2's benign case:
present in this DevNote's own folder, not yet upstream. -->

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
them. Plain tab-set, no extra wrapper directive, so the fence depth is
:::::/::::/::: per that skill. Both files verified: pUC-IDT-LuxR-mNG declares
4671 bp and carries 4671 bases, pUC-IDT-constitutive_mNG declares 3689 bp and
carries 3689 bases. Neither is yet on nucleus-eng/DNA; both are the files
Anton added to this DevNote's own dna/ directory on 2026-10-11. -->

<!-- A purchased purified protein belongs in tbl-reagents, not here. Only DNA
built or ordered as a sequence goes in the table above. -->

# Results

## Result 1 — LuxR-mNeonGreen sensor plasmid in bulk lysate

:::{admonition} Planned scope
:class: note
:name: scope-result-1

Carried verbatim from the Draft devnote outline:

> Bulk lysate luxRGFP +/- 10uM AHL — platereader
:::

<!--
:name: gap-result-1

Please add the motivation and the result. Say what the no-AHL condition and the constitutive control each test.

Answer, from the "Draft devnote" Doc, 2026-10-11: adopted verbatim below.
-->

To test the output of the LuxR-mNeonGreen plasmid construct in the presence of
HSL, a plate reader assay was performed to quantify fluorescence in response
to 10 µM AHL.

:::{admonition}
:name: gap-result-1-controls

The Draft names no explicit no-AHL or constitutive control for this specific
run, though both exist for the other results. Please confirm whether this
plate reader run included them, and what each tests.
:::

:::{danger} Missing build file
:name: flags-build-result-1

No `build-composition.csv` exists for this experiment, so no composition table
can go here. Run `devstudio-build-to-composition` on the build file.
:::

:::{admonition}
:name: gap-deviation-result-1

Please state how this run differed from the general protocol in {numref}`sec-methods`, if at all.
:::

<!--
:name: gap-figure-result-1

Please choose the plate reader figure for this result. The Draft marks the spot with a bare `[image]` placeholder.

Answer, 2026-10-11: the Draft Doc embeds this figure inline, extracted from its own .docx export rather than a notebook. Adopted below.
-->

:::{figure} ./figures/result1-bulk-lysate-platereader.png
:label: fig-result1-platereader
:align: center
:width: 85%
LuxR-mNeonGreen sensor in bulk lysate (10 µL), fluorescence fold change over
4 hours, control against 10 µM AHL.
:::

[`fig-result1-platereader`, platemap: none, data source: none, caption: (LuxR-mNeonGreen sensor in bulk lysate, fluorescence fold change over 4 hours, control against 10 µM AHL.)]

<!-- missing notebook -->

<!-- Extracted from the "Draft devnote" Doc's own .docx export
(word/media/image3.png, confirmed against word/document.xml's relationship
order to be the second of three embedded images, after the Overview
schematic), not from a notebook or a Log folder. No raw data file is named
for it. -->

The log directory for this result:
<https://drive.google.com/drive/folders/1lK_ylF47jmR3pFxp-3bD9PqyszQyiTUX>.

## Result 2 — detecting purified HSL in solution and in gels

:::{admonition} Planned scope
:class: note
:name: scope-result-2

Carried verbatim from the Draft devnote outline, originally two bullets. The
"Draft devnote" Doc writes solution and gel as one combined narrative, so this
DevNote now follows that merge rather than the outline's split:

> GFP sensor GUVs in solution +/-10uM AHL — Platereader & microscopy
>
> GFP sensor Gels +/- 100uM AHL — Platereader & microscopy
:::

<!--
:name: gap-result-2

Please add the motivation and the result. Niall's log covers the microscopy half of this: time lapse to 6 hours plus endpoint bright field and 488 nm, at 50 µL in a clear bottom 384 well plate, N=3 per condition. Julia ran the plate reader half. Say what both showed.

Answer, from the "Draft devnote" Doc, 2026-10-11: adopted verbatim below.
-->

To demonstrate the ability of a synthetic cell to detect HSL, lysate-based
GUVs encapsulating the LuxR-mNeonGreen plasmid were resuspended in outer
solution containing 10 µM HSL and visualized by brightfield and fluorescent
microscopy over time. To improve vesicle stability and robustness, the
synthetic cells were also embedded in 1% w/v ultra-low gelling temperature
agarose (ULGA), with purified HSL added to the top of the gel to induce
mNeonGreen expression. End point and time lapse fluorescence microscopy,
Z-stack fluorescence microscopy, and fluorescent plate reader experiments were
run to check whether purified HSL induces protein expression inside synthetic
cells.

3-oxo-C6-HSL has been shown elsewhere to passively diffuse across artificial
lipid bilayer membranes and induce protein expression in *E. coli*
lysate-based systems
([Garenne et al.](https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/syst.202300029)).
HSL would therefore be expected to permeate the GUV lipid membrane into the
synthetic cell. HSL is non-fluorescent and carries no reactive group, so this
could not be verified directly; LuxR-induced expression of mNeonGreen is the
indirect verification.

:::{danger} Missing build file
:name: flags-build-result-2

No `build-composition.csv` exists for this experiment, so no composition table
can go here. Run `devstudio-build-to-composition` on the build file.
:::

:::{admonition}
:name: gap-deviation-result-2

Please state how this run differed from the general protocol in {numref}`sec-methods`, if at all.
:::

<!--
:name: gap-figure-result-2

Please choose the figure for this result. The Draft marks the spot with a bare `[image]` placeholder.

Answer, 2026-10-11: the Draft Doc embeds this figure inline, extracted from its own .docx export rather than a notebook. Adopted below.
-->

:::{figure} ./figures/result2-gels-platereader.png
:label: fig-result2-platereader
:align: center
:width: 85%
LuxR-mNeonGreen sensor gels, fluorescence fold change over 16 hours, control
against purified AHL.
:::

[`fig-result2-platereader`, platemap: none, data source: none, caption: (LuxR-mNeonGreen sensor gels, fluorescence fold change over 16 hours, control against purified AHL.)]

<!-- missing notebook -->

<!-- Extracted from the "Draft devnote" Doc's own .docx export
(word/media/image2.png, confirmed against word/document.xml's relationship
order to be the third of three embedded images), not from a notebook or a Log
folder. No raw data file is named for it. -->

:::{danger} The figure's own title disagrees with the text on AHL concentration
:name: flags-gel-ahl-concentration

This figure is titled "LuxR-mNeonGreen Sensor Gels with 10uM Purified AHL" in
the source Doc. Every other mention of the gel experiment in this DevNote,
the outline, the Methods gel protocol (10 µL of 600 µM AHL into the gel, a
100 µM final concentration), says 100 µM. Carried as the figure names it;
not corrected here. Say which concentration this plot actually shows.
:::

Log directories: the GUVs-in-solution run (2nd/3rd October) is at
<https://drive.google.com/drive/folders/15EQ5kkf6LlnIJqQShonYNE3fKh8O3PgD>, and
the gel run is at
<https://drive.google.com/drive/folders/1j4vF36gjF_jpaGyI8fI-_uyUs-M6mC2d>. The
gel run's raw plate reader data:
<https://data.nucleus.engineering/platereader/devstudio/20261006-164718-cytation5-pure-timecourse-gfp-julia-lysategels100uM.txt>.

## Result 3 — detecting bacterially produced HSL in solution

:::{admonition} Planned scope
:class: note
:name: scope-result-3

Carried verbatim from the Draft devnote outline, as its third and fourth
bullets. The outline bullet below reads "gels"; the Draft's own narrative and
well map describe GUVs resuspended in bacterial supernatant and read in
solution, not embedded in a gel, so this DevNote follows the narrative:

> GFP sensor gels +/- bacterial supernatant — Platereader
:::

<!--
:name: gap-result-3

Please add the motivation and the result. Say which organism the supernatant comes from and what it is being compared against.

Answer, from the "Draft devnote" Doc, 2026-10-11: adopted verbatim below.
-->

To model bacterial sensing using GUVs, the LuxI plasmid was transformed into
DH5α *E. coli* (DH5α w/ LuxI) to encode production of 3-oxo-C6-HSL, the
small-molecule quorum sensor detected in Result 2. The same LuxR-mNeonGreen
plasmid was used to check whether lysate-based synthetic cells can detect
bacterially produced HSL, by resuspending the GUV pellet in bacterial
supernatant. Control experiments used the DH5α strain without the LuxI
plasmid (DH5α ΔLuxI), which removes HSL from the supernatant.

:::{table} Three experimental conditions for HSL-induced mNeonGreen expression using bacterial supernatant in solution.
:label: tbl-supernatant-conditions
:align: center

| Condition | Plasmid | Supernatant used |
| --- | --- | --- |
| HSL sensing GUVs | LuxR-mNeonGreen | DH5α w/ LuxI |
| Negative control | LuxR-mNeonGreen | DH5α ΔLuxI |
| Positive control | Constitutive mNeonGreen | DH5α ΔLuxI |
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
| Positive control | C9, C10, C11 |
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
by synthetic cells. Synthetic cells carrying the constitutive mNeonGreen
plasmid in DH5α ΔLuxI supernatant expressed after about 40 minutes, with
expression increasing over the experiment (wells C9 to C11). The faster
expression compared to LuxR-mNeonGreen follows from synthesizing one protein
only, with no dependency on HSL entering the cell and activating mNeonGreen
expression.

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

::::{tab-item} Positive control
:::{figure} ./figures/fov-c10.png
:label: fig-fov-c10
:align: center
:width: 75%
Well C10, positive control (constitutive mNeonGreen, DH5α ΔLuxI supernatant),
T = 19, GFP channel only, contrast windowed 30000 to 60000. Same crop and zoom
as the other two panels.
:::
::::

:::::

[`fig-fov-c4`, platemap: none, data source:`nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/4/0`, caption: (Well C4, HSL sensing GUVs, T = 19, GFP channel only, cropped and zoomed.)]

[`fig-fov-c7`, platemap: none, data source:`nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/7/0`, caption: (Well C7, negative control, T = 19, GFP channel only, cropped and zoomed.)]

[`fig-fov-c10`, platemap: none, data source:`nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/10/0`, caption: (Well C10, positive control, T = 19, GFP channel only, cropped and zoomed.)]

<!-- missing notebook -->

<!-- All three rendered by general/render-microscopy-fovs.py, adapted from
devnote-swh-20260925-ph-sensor-in-solution's own script of the same name
rather than written fresh: same crop math, same scale-bar convention. One
well per condition, the triplicate's middle well (C4, C7, C10), chosen
because Anton's own Vizarr link named C4. One target and one zoom for all
three, copied verbatim from that link
(https://bnext-bio.github.io/vizarr/?source=.../C/4&viewState=...), so every
panel sits at the same pixel offset and scale and no panel was positioned to
favour a result. GFP channel only (channel index 1, confirmed against the
store's own omero.channels order), T = 19, window 30000-60000 fixed rather
than computed, per Anton's instruction. Field of view and scale bar are
computed from the store's own per-level pixel scale, not hardcoded. No
notebook or platemap exists yet for this store, so asset_chain_complete is
false in manifest.json. -->

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

## Lysate preparation

<!--
:name: gap-method-lysate

Please write the general lysate protocol. Niall's log gives a 25 µL reaction from the Promega S30 Extract System for circular DNA, with plasmid at a 40 ng/µL final stock, 2.50 µL amino acids, 10.00 µL S30 premix, 7.50 µL S30 extract, 1.25 µL RNase inhibitor, 2.50 µL 3 M sucrose and nuclease free water to volume, prepared on ice. Confirm it and say whether it is the general protocol or a deviation.

Answer, Anton, 2026-10-11: the 12.5 µL reaction below, from the "Draft devnote"
Doc, is the bulk lysate reaction. The 25 µL figure in Niall's log is believed
to be the volume of GUV suspension added to a gel, not a lysate reaction; see
the flag on Gel preparation below.
-->

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

## Thin film preparation

<!--
:name: gap-method-thin-film

Please write the general thin film protocol. Niall's log gives 25 mg/mL POPC in chloroform, evaporated under nitrogen and dried overnight in a vacuum desiccator, then mineral oil to 4 mg/mL, vortexed 1 minute and sonicated at 40 kHz for 30 minutes.

Answer, from the "Draft devnote" Doc, 2026-10-11: adopted verbatim below.
-->

Create lipid thin films in a glass vial using 160 µL of 25 mg/mL POPC
chloroform stock and dry under nitrogen gas. Place the films in a vacuum
desiccator overnight. Add 1 mL of mineral oil to each film.

:::{admonition}
:name: gap-method-thin-film-concentration

Niall's log gives the mineral oil concentration as 4 mg/mL. The Draft gives a
1 mL volume added to each film rather than a concentration. Confirm whether
these describe the same step.
:::

## GUV preparation

<!--
:name: gap-method-guv

Please write the general GUV protocol. Niall's log gives the emulsion transfer: 200 µL lipid-in-oil into TUBE I, the lysate added and pipetted 20 times with a P1000, laid on the outer solution in TUBE O, left 2 minutes, then 9000 xg for 20 minutes, with the pellet resuspended in 50 µL.

Answer, from the "Draft devnote" Doc, 2026-10-11: adopted verbatim below.
-->

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

<!--
:name: flags-solution-naming

Resolved, 2026-10-11, by the "Draft devnote" Doc's own clearer wording. Inner
tube holds the lipid-in-oil, into which the lysate is added; outer tube holds
the outer solution recipe above. This matches the outer solution table's own
caption and last column, and corrects the contradiction in Niall's log, which
named the tubes the opposite way in one paragraph.
-->

## Gel preparation

<!--
:name: gap-method-gel

Please write the general gel protocol. No source describes it. Name the gel, because it is what separates Results 3 and 4 from Result 2.

Answer, from the "Draft devnote" Doc, 2026-10-11: adopted verbatim below. This
is the step Anton believes Niall's log's "25 µL" figure describes, not a
lysate reaction; see the flag on Lysate preparation above.
-->

Make a 1% ULGA stock, with ULGA dissolved in the outer solution from
{numref}`tbl-outer-solution`. Heat in a microwave or on a hot plate until the
solution is bubbling. Allow it to cool to a temperature that can be held by
hand, and before it gels, pipette 25 µL of GUVs and 25 µL of ULGA into a 384
well plate and mix. Place on ice or in a fridge for 10 minutes. Add 10 µL of
600 µM AHL, giving a final gel concentration of 100 µM, and incubate at 37 °C
in a plate reader or microscope overnight.

## Supernatant preparation

<!--
:name: gap-method-supernatant

Please write the supernatant protocol. No source describes it. Say which organism it comes from and how it is prepared.

Answer, from the "Draft devnote" Doc, 2026-10-11: adopted verbatim below.
-->

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

Please write this comparison.
:::

## Gel embedding and ULGA

:::{admonition}
:name: gap-discussion-gel

Please write the potential issues with gel embedding, which the outline names as ULGA.
:::

## Dynamic range in bulk vs GUVs

:::{admonition}
:name: gap-discussion-dynamic-range

Please write this comparison. Added to the outline on 2026-10-11; no source describes it yet.
:::

# Notes

:::{admonition}
:name: gap-notes

Please note any caveats or gotchas that do not belong in Discussion points.
:::

# What's next

:::{admonition}
:name: gap-whats-next

Based on what is described here, what comes next?
:::

# Resources

:::{admonition}
:name: gap-resources

Please list the files this DevNote draws on beyond the Log folders below. `devstudio-assemble-devnote-assets` writes one link per file in `experiments/` once the assets land.
:::

Log folders, one per result, from the "Draft devnote" Doc:

- Result 1, bulk lysate: <https://drive.google.com/drive/folders/1lK_ylF47jmR3pFxp-3bD9PqyszQyiTUX>
- Result 2, GUVs in solution (2nd/3rd October): <https://drive.google.com/drive/folders/15EQ5kkf6LlnIJqQShonYNE3fKh8O3PgD>
- Result 2, gels: <https://drive.google.com/drive/folders/1j4vF36gjF_jpaGyI8fI-_uyUs-M6mC2d>
- Result 3, bacterial supernatant: the microscopy store itself, `nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr`; no separate Log folder link was given.

Raw data:

- Result 2 gel run, plate reader: <https://data.nucleus.engineering/platereader/devstudio/20261006-164718-cytation5-pure-timecourse-gfp-julia-lysategels100uM.txt>
- Result 3, microscopy store: <https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr>
