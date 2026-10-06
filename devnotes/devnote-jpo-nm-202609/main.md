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
-->

# Overview

:::{admonition}
:name: gap-overview

Please fill in an overview section here describing what the system does. A nice overview image fits well here too.
:::

:::{danger} Unresolved before publication
:name: flags-blocking

**No source log exists yet.** This DevNote was drafted on 2026-10-05 from an
outline Anton supplied in chat, not from a Log folder in the DevStudio Shared
Drive. Every section below is a skeleton. No log, no build file, no platemap,
no notebook and no raw instrument data has been read, because none was
supplied.

**Title and description are not sourced.** The title "LuxR-GFP Sensor Demo"
came from the same chat outline. No Specification table exists. The
description in `curvenote.yml` restates the three planned results and is not a
quotation from any source.

**Date is assigned, not sourced.** Anton set `date: 2026-10-12` on 2026-10-05.
The DevNote slug carries `202609`, which is a month and not a date. The two
disagree. Settle which one is right before publication.

**No reagents data.** {numref}`tbl-reagents` carries placeholder rows only. Run
`devstudio-build-to-materials` against the Materials Reference once a build
file exists.

**No DNA sequences.** The title names a LuxR sensor and a GFP reporter.
{numref}`tbl-constructs` names neither, because no source states a construct
name, and this draft does not guess one. A DevNote must be self-contained, so
every sequence has to land inline and every `.gb` file has to land in `dna/`.

**No composition tables.** Each Methods subsection below needs a
`build-composition.csv`, written by `devstudio-build-to-composition` from that
experiment's build file. None of the three exists.

**No figures and no data.** Each Results subsection below is a planned
experiment, not a reported one.
:::

:::{admonition} Open review items
:class: warning dropdown
:name: flags-review

**Author affiliations.** Anton gave Imperial College London for both authors on
2026-10-05. No source document states it.

**Author ORCIDs.** Neither author supplied one.

**Author order.** `curvenote.yml` lists Julia Purrinos de Oliveira first,
following the order Anton wrote. No source states an intended order.

**HSL is named only by its abbreviation.** The outline writes "HSL". The
specific acyl-homoserine lactone the LuxR sensor responds to is not stated.
Name it, because it sets the x axis of Result 1.
:::

# Reagents

:::{admonition}
:name: gap-reagents

Please fill in {numref}`tbl-reagents`. Run `devstudio-build-to-materials` against the Materials Reference once a build file exists, and it populates the table from there.
:::

:::{table} Reagents and equipment. No source carries reagent data. Run `devstudio-build-to-materials` once a build file exists.
:label: tbl-reagents
:align: center

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| — | — | — | N/A | N/A | N/A | |
:::

# Constructs

:::{admonition}
:name: gap-constructs

Please identify the right sequences, include each one inline in the table below, and add the matching file to `dna/` in `.gb` format.
:::

:::{table} DNA. No source names a construct, so no row is populated.
:label: tbl-constructs
:align: center

| Name | Sequence | Purpose |
| --- | --- | --- |
| — | — | — |
:::

<!-- A purchased purified protein belongs in tbl-reagents, not here. Only DNA
built or ordered as a sequence goes in the table above. -->

# Protocol

:::{admonition}
:name: scope-protocol

Each of the four sections below needs its protocol written out. If a protocol matches a published Nucleus protocol, link to that protocol and state the differences. Otherwise describe it from scratch.
:::

## Lysate preparation

:::{admonition}
:name: gap-protocol-lysate-preparation

Please write the protocol for lysate preparation.
:::

## Making lysate-encapsulated GUVs

:::{admonition}
:name: gap-protocol-guv-encapsulation

Please write the protocol for making lysate-encapsulated GUVs.
:::

<!-- GUV: giant unilamellar vesicle. Define it at its first use in the Overview
once that section is written. -->

## Embedding GUVs in hydrogels

:::{admonition}
:name: gap-protocol-guv-hydrogel

Please write the protocol for embedding GUVs in hydrogels.
:::

## Preparing supernatant

:::{admonition}
:name: gap-protocol-supernatant

Please write the protocol for preparing supernatant.
:::

# Methods

## Result 1 — bulk lysate, HSL titration

:::{danger} Missing build file
:name: flags-build-result-1

No `build-composition.csv` was found for this experiment, so no composition
table can be produced. Run `devstudio-build-to-composition` on the build file
before this section is filled in.
:::

## Result 2 — GUVs in solution

:::{danger} Missing build file
:name: flags-build-result-2

No `build-composition.csv` was found for this experiment, so no composition
table can be produced. Run `devstudio-build-to-composition` on the build file
before this section is filled in.
:::

## Result 3 — GUVs in hydrogel

:::{danger} Missing build file
:name: flags-build-result-3

No `build-composition.csv` was found for this experiment, so no composition
table can be produced. Run `devstudio-build-to-composition` on the build file
before this section is filled in.
:::

# Results

## Result 1 — bulk lysate, HSL titration

:::{admonition} Planned scope
:class: note
:name: scope-result-1

Carried verbatim from the outline Anton supplied on 2026-10-05:

> Result 1: Plate - Bulk lysate with different conc of HSL and GFP expression - constitutive expression
:::

:::{admonition}
:name: gap-result-1

Please add a description of the results and motivation for this experiment
:::

<!-- Figures land here once the plate reader notebook exists. Each one carries a
figure-provenance line beneath it, and the matching entry goes into
manifest.json. See devstudio-log-to-devnote-m, Step 5.5. -->

## Result 2 — GUVs in solution

:::{admonition} Planned scope
:class: note
:name: scope-result-2

Carried verbatim from the outline Anton supplied on 2026-10-05:

> Result 2: GUV in solution (def microscopy data - time point microscope) + may plate data
:::

:::{admonition}
:name: gap-result-2

Please add a description of the results and motivation for this experiment
:::

<!-- Microscopy is definite here and plate reader data is not yet decided. A
microscopy result needs an OME-Zarr store on data.nucleus.engineering, the
per-object parquet beside it, and the wells worth showing as interactive
viewers. Name the wells before the viewer blocks can be written. -->

## Result 3 — GUVs in hydrogel

:::{admonition} Planned scope
:class: note
:name: scope-result-3

Carried verbatim from the outline Anton supplied on 2026-10-05:

> Result 3: Third GUVs in hydrogel + may include plate data
:::

:::{admonition}
:name: gap-result-3

Please add a description of the results and motivation for this experiment
:::

<!-- The hydrogel is not named. Name it, because it is the variable that
separates this result from Result 2. -->

# Notes

:::{admonition}
:name: gap-notes

Please note any caveats or gotchas
:::

# What's next

:::{admonition}
:name: gap-whats-next

Based on what's described here, what comes next?
:::

# Resources

:::{admonition}
:name: gap-resources

Please list the files this DevNote draws on. `devstudio-assemble-devnote-assets` writes one link per file in `experiments/` once the assets land.
:::

<!-- One link per file in experiments/, added by
devstudio-assemble-devnote-assets once the assets land. Drive URLs never appear
as hyperlink hrefs here: the Curvenote link checker reports them 401
Unauthorized, and a reader without Drive access cannot open them. -->
