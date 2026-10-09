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

:::{admonition}
:name: gap-overview

Please fill in an overview of the demo. What does the system do, and what does the set of four results demonstrate together. A nice overview image fits well here too.
:::

:::{danger} Unresolved before publication
:name: flags-blocking

**No result is written and no data is in the tree.** One source log exists,
`01-logs/NM_2026_10_6_LuxR_mNeonGreen_lysate_GUVs`, and it ends at a bare
`# results` heading with two TODO lines under it, for the zarr URLs and for
the analysis notebook. No platemap, no notebook, no build file and no raw data
has been read.

**Title and date are not sourced.** The title "LuxR-GFP Sensor Demo" and the
date 2026-10-12 both came from Anton in chat on 2026-10-05. No Specification
table exists. The DevNote slug reads `202609`, the source log folder reads
2026-10-06, and the fourth result has not run yet. Three values, no source.

**The reporter disagrees between sources.** The Draft devnote outline names
"luxRGFP" in Result 1. Niall's log says the plasmid is LuxR-mNeonGreen, with a
constitutive mNeonGreen control, and is explicit that LuxR-deGFP is an older
and different construct that gave noisier data. The title still says GFP.
Settle which reporter this DevNote is about.

**Two plasmids need confirming.** Anton asked on the log, 2026-10-08, whether
these two Drive files are the right sequences. Neither has been checked, and
neither is in `dna/`.

- LuxR-mNeonGreen: `https://drive.google.com/file/d/1e5L7jQ__aO_MeMcwlx6gr9byjV8Ajacy/view`
- constitutive mNeonGreen: `https://drive.google.com/file/d/13UvMR_uMa6FjVXUupdM4AvQvfDoaLTIz/view`

**The platemap is missing.** Anton asked on the log, 2026-10-08, for the
platemap of the microscopy experiment to be put in that log directory. It is
not there.

**No build file, so no composition table anywhere.** The log folder holds an
untitled, empty spreadsheet. Each result needs its own
`build-composition.csv`, written by `devstudio-build-to-composition` from a
build file. See the flag in each result below.

**Result 4 has not run.** The outline lists gels against bacterial
supernatant. Nothing in any source describes it yet.
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

**AHL is named only by its class.** The outline writes AHL and gives 10 µM for
Results 1 and 2 and 100 µM for Result 3. It does not say which acyl-homoserine
lactone. Niall's log writes "HSL" at 10 µM. Name the molecule.

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
:::

:::{table} DNA. No construct is confirmed yet.
:label: tbl-constructs
:align: center

| Name | Sequence | Purpose |
| --- | --- | --- |
| — | — | — |
:::

<!-- A purchased purified protein belongs in tbl-reagents, not here. Only DNA
built or ordered as a sequence goes in the table above. -->

# Results

## Result 1 — bulk lysate, luxRGFP with and without 10 µM AHL

:::{admonition} Planned scope
:class: note
:name: scope-result-1

Carried verbatim from the Draft devnote outline:

> Bulk lysate luxRGFP +/- 10uM AHL — platereader
:::

:::{admonition}
:name: gap-result-1

Please add the motivation and the result. Say what the no-AHL condition and the constitutive control each test.
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

## Result 2 — GFP sensor GUVs in solution, with and without 10 µM AHL

:::{admonition} Planned scope
:class: note
:name: scope-result-2

Carried verbatim from the Draft devnote outline:

> GFP sensor GUVs in solution +/-10uM AHL — Platereader & microscopy
:::

:::{admonition}
:name: gap-result-2

Please add the motivation and the result. Niall's log covers the microscopy half of this: time lapse to 6 hours plus endpoint bright field and 488 nm, at 50 µL in a clear bottom 384 well plate, N=3 per condition. Julia ran the plate reader half. Say what both showed.
:::

:::{danger} Missing build file
:name: flags-build-result-2

No `build-composition.csv` exists for this experiment, so no composition table
can go here. Run `devstudio-build-to-composition` on the build file.
:::

:::{admonition}
:name: gap-deviation-result-2

Please state how this run differed from the general protocol in {numref}`sec-methods`, if at all.
:::

The C wells of the 2026-10-08 store are shown as interactive viewers on
[2026-10-08 — Interactive viewer](./2026-10-08-interactive-viewer.md). That page
carries the open questions on contrast, timepoint and well filtering. A static
figure carrying the same result belongs here once one is chosen, as the archival
record, because a viewer does not survive JATS conversion.

:::{admonition}
:name: gap-figure-result-2

Please pick the well and the timepoint for the static archival figure, and say
whether it is a single channel or a composite.
:::

<!-- A microscopy result also needs the per-object parquet beside the store, if
one exists, and the analysis notebook. Niall's log carries two open TODOs for
exactly this: the zarr URLs and the analysis notebook. -->

## Result 3 — GFP sensor gels, with and without 100 µM AHL

:::{admonition} Planned scope
:class: note
:name: scope-result-3

Carried verbatim from the Draft devnote outline:

> GFP sensor Gels +/- 100uM AHL — Platereader & microscopy
:::

:::{admonition}
:name: gap-result-3

Please add the motivation and the result. Say why this result uses 100 µM AHL where Results 1 and 2 use 10 µM.
:::

:::{danger} Missing build file
:name: flags-build-result-3

No `build-composition.csv` exists for this experiment, so no composition table
can go here. Run `devstudio-build-to-composition` on the build file.
:::

:::{admonition}
:name: gap-deviation-result-3

Please state how this run differed from the general protocol in {numref}`sec-methods`, if at all. Name the gel.
:::

## Result 4 — GFP sensor gels, with and without bacterial supernatant

:::{admonition} Planned scope
:class: note
:name: scope-result-4

Carried verbatim from the Draft devnote outline:

> GFP sensor gels +/- bacterial supernatant — Platereader & microscopy
:::

:::{admonition}
:name: gap-result-4

Please add the motivation and the result. Say which organism the supernatant comes from and what it is being compared against.
:::

:::{danger} Missing build file
:name: flags-build-result-4

No `build-composition.csv` exists for this experiment, so no composition table
can go here. Run `devstudio-build-to-composition` on the build file.
:::

:::{admonition}
:name: gap-deviation-result-4

Please state how this run differed from the general protocol in {numref}`sec-methods`, if at all.
:::

(sec-methods)=
# Methods

:::{admonition}
:name: scope-methods

Each subsection below is a general protocol. Where one matches a published Nucleus protocol, link to that protocol and state only the differences. Each result above carries its own deviations rather than restating a protocol.
:::

## Lysate preparation

:::{admonition}
:name: gap-method-lysate

Please write the general lysate protocol. Niall's log gives a 25 µL reaction from the Promega S30 Extract System for circular DNA, with plasmid at a 40 ng/µL final stock, 2.50 µL amino acids, 10.00 µL S30 premix, 7.50 µL S30 extract, 1.25 µL RNase inhibitor, 2.50 µL 3 M sucrose and nuclease free water to volume, prepared on ice. Confirm it and say whether it is the general protocol or a deviation.
:::

## Thin film preparation

:::{admonition}
:name: gap-method-thin-film

Please write the general thin film protocol. Niall's log gives 25 mg/mL POPC in chloroform, evaporated under nitrogen and dried overnight in a vacuum desiccator, then mineral oil to 4 mg/mL, vortexed 1 minute and sonicated at 40 kHz for 30 minutes.
:::

## GUV preparation

:::{admonition}
:name: gap-method-guv

Please write the general GUV protocol. Niall's log gives the emulsion transfer: 200 µL lipid-in-oil into TUBE I, the lysate added and pipetted 20 times with a P1000, laid on the outer solution in TUBE O, left 2 minutes, then 9000 xg for 20 minutes, with the pellet resuspended in 50 µL.
:::

:::{danger} The source contradicts itself twice
:name: flags-solution-naming

Both of these are carried as the log writes them and neither is corrected
here.

The caption of the outer solution table reads "required for inner solution for
lysate GUVs", while the paragraph above it and the table's own last column
both call it the outer solution.

The same paragraph reads "200 µL of lipid-in-oil solution is added to the inner
solution (TUBE I) microcentrifuge tube. 300 µL of inner solution is added to
the outer centrifuge tube (TUBE O)."

Say which is right and I will write the table and the step accordingly.
:::

## Gel preparation

:::{admonition}
:name: gap-method-gel

Please write the general gel protocol. No source describes it. Name the gel, because it is what separates Results 3 and 4 from Result 2.
:::

## Supernatant preparation

:::{admonition}
:name: gap-method-supernatant

Please write the supernatant protocol. No source describes it. Say which organism it comes from and how it is prepared.
:::

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

Please list the files this DevNote draws on. `devstudio-assemble-devnote-assets` writes one link per file in `experiments/` once the assets land.
:::
