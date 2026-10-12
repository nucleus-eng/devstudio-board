<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

<!-- Drafted 2026-10-12 from the Google Doc "DevNote Color Change.docx"
(Drive id 1H_HKs-vO0Blq0_-j5dPGsJgNuphQ34H1), together with three supporting
photographs from the same Drive folder (1T88O7efBfV3kbHOSqbnmY0_FNC_ViFY9):
LUVpellet.png, 1h.png and overnight.png. The folder holds no other file.
It holds no notebook, no platemap, no raw instrument data, no DNA sequence
file, and no build file. Prose, tables and both figures are carried
verbatim from the Doc. The content is restructured into this board's
section order: Abstract, Overview, Materials, Protocol, Methods, Results.
The Doc's own Reagents and stocks table sat under Protocol. It is moved to
Materials below, to match this pipeline's standard schema. The three
photographs are renamed from their generic Drive names (LUVpellet.png,
1h.png, overnight.png) to luv-pellet.png, colorchange-1h.png and
colorchange-overnight.png. -->

<!-- :::{admonition} Open review items
:class: warning dropdown
:name: flags-review

**The title is confirmed. The date is not.** Anton confirmed the title in
chat, 2026-10-12, matching the Doc's own first line. No Specification
table exists in the source Doc, and no date appears anywhere in it. See
{ref}`gap-date` below.

**The Reagents table names a plasmid that does not match the circuit in
Protocol.** The table's reporter-plasmid row names "pT7-tetO-plamGFP
reporter plasmid". It links to the `detector-tetr-atc` module spec, a
tetR/aTc-induced GFP reporter. The Protocol section describes a different
circuit. That circuit is LuxR-driven, uses a lux-box promoter, and
expresses PLA1, not GFP, in response to AHL. No sequence file for either
construct exists yet. See {ref}`gap-constructs` below. This is a blocking
identity question, not a renaming or formatting issue.

**The source Doc flags its own missing data.** Its Results section ends
with this sentence: "Plot of platereader is missing." That missing trace
is the quantitative 570 nm kinetic absorbance data for
{ref}`fig-colorchange`. The data was never produced, or it was lost before
the author wrote this Doc. The two photographs in Results are a
qualitative stand-in, not a replacement for that data.

**No platemap, no notebook, and no raw instrument data exist in the
supporting folder.** This gap applies to both figures. `asset_chain_complete`
reads `false` for both entries in `manifest.json`.

**Two uncertainty markers in the source table carry forward unresolved.**
The first is a "Beta-Gal?" stock row with no concentration given. The
second is a "CPRG" abstract mention the author tagged "(write long name)".
That tag is the author's own reminder to spell out the reagent's full
chemical name. The source never supplies that name, so it is not added
here.

**The Sources list ends with two open items the author left unresolved.**
The first reads: "Some citation on quorum sensing and AHSL LuxR in cell
free?" The second reads: "Cite GFP devnote." The source Doc does not name
that DevNote directly. One candidate is `devstudio/devnote-jpo-nm-202609`
on this same board. That DevNote covers the same LuxR quorum-sensing
system in a mNeonGreen GUV hydrogel. It also shares two authors with this
Doc: Niall McIntyre and Julia Purrinos de Oliveira. This link is a
candidate only. See Resources.

**The source Doc uses two spellings for what appears to be one molecule,
AHSL and AHL.** Both forms appear across the title, abstract, protocol,
reagents, and results. Each instance is carried exactly as written in its
own location. No spelling is normalized to match the other.
:::

<!-- Title resolved, 2026-10-12: Anton confirmed "Implementing of a bulk
color change module into bacterial quorum sensing" in chat, matching the
Doc's own first line verbatim, including its phrasing. Thumbnail set to
figures/colorchange-overnight.png (the last figure), per the same request.
-->

(gap-date)=
<!-- :::{admonition}
:name: gap-date

Please confirm the date. No date appears anywhere in the Doc.
`curvenote.yml` currently carries the Drive file's own creation date,
2026-10-12, as a placeholder.
::: -->
-->

# Abstract

It has previously been shown that developer cells can use the LuxR quorum sensing system to detect AHSL (C6) a diffusible molecule bacteria use to communicate with each other, to sense bacteria and report that. Demonstrated by GFP. Here we wish to extend this system, by using the genetic sensor module and implement a novel module for visible color change, based on the production of PLA1 that lyses storage compartments that result in the release of CPRG (write long name) which then can be cleaved into CPR by beta galactosidase which is in the outer solution.

# Overview

We made dye loaded LUVs that were stable over long time incubation without leaking dye, and induced GUV lysis by expression of PLA1 in GUVs containing bacterial 30S lysate. We induced the expression of PLA1 by addition of AHSL, allowing us to distinguish a visible by eye difference of the induced and the non-induced condition.

# Materials

<!-- REORDERED: moved from "Protocol", where the source Doc placed its
"Reagents and stocks" subsection. Relocated to Materials per this board's
standard section order; no value, unit or row changed. -->

## Reagents and stocks

Reactions were run in b.next Nucleus Base Cytosol, a PURE-type reconstituted system supplied as a premade reagent kit, and assembled following the Nucleus [Assemble Base Cytosol](https://docs.nucleus.engineering/docs/processes/assemble-base-cytosol/main) process. Per 10 µL of reaction the component ratios match that reference composition: 3.0 µL SMix, 1.0 µL tRNA, 1.2 µL PMix, 1.8 µL ribosomes and 0.25 µL RNase inhibitor.

:::{table} Reagents and equipment.
:label: tbl-reagents
:align: center

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| Small Molecule Mix (SMix) | Nucleus Base Cytosol component | — | N/A | N/A | N/A | |
| tRNA | — | — | N/A | N/A | N/A | |
| Protein Mix (PMix) | — | — | N/A | N/A | N/A | |
| Ribosomes | — | — | N/A | N/A | N/A | |
| RNase Inhibitor, Murine (RIM) | — | New England Biolabs | M0314L | N/A | N/A | [NEB #M0314L](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| Optiprep | — | — | N/A | N/A | N/A | |
| pT7-tetO-plamGFP reporter plasmid | — | — | N/A | N/A | N/A | [detector-tetr-atc spec](https://docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec/) |
| Nuclease-free H₂O | — | — | N/A | N/A | N/A | |
| AHSL | — | — | N/A | N/A | N/A | |
| CPRG | — | — | N/A | N/A | N/A | |
| Beta-Gal | — | — | N/A | N/A | N/A | |
:::

<!-- :::{admonition}
:name: gap-reagents-link

The pT7-tetO-plamGFP row's Link points to a GFP reporter module spec that
does not match this experiment's circuit — see {ref}`gap-constructs`. Kept
here because it is the reagent the source table names; not corrected.
::: -->

The source table's own Stock and Notes columns carry concentrations that do not map to the schema above and are retained here rather than dropped:

:::{table} Reagents and stocks — stock concentrations and notes, as given in the source Doc.
:label: tbl-reagents-source
:align: center

| Component | Stock | Notes |
| --- | --- | --- |
| Small Molecule Mix (SMix) | working stock | Nucleus Base Cytosol component |
| tRNA | working stock | |
| Protein Mix (PMix) | working stock | |
| Ribosomes | working stock | |
| RNase Inhibitor, Murine (RIM) | working stock | [NEB #M0314L](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| Optiprep | | |
| pT7-tetO-plamGFP reporter plasmid | 129.6 nM | Final concentration: 0 or 1 nM depending on sample |
| Nuclease-free H₂O | — | to volume |
| AHSL | 80 mM in DMSO | Diluted in DI water for experiment |
| CPRG | Dry powder | Dissolved in aqueous buffer |
| Beta-Gal? | | |
:::

<!-- The "Beta-Gal?" row's question mark is the source Doc's own uncertainty
marker, carried as written, not resolved. -->

<!-- # Constructs -->

(gap-constructs)=
<!-- :::{admonition}
:name: gap-constructs

No DNA sequence file was supplied for either construct this Doc names.
The Reagents table's "pT7-tetO-plamGFP reporter plasmid" links to the
`detector-tetr-atc` module (a tetR/aTc-induced GFP reporter), but the
Protocol section below describes a different circuit: "The reporter
plasmid, built in the pOpen backbone, constitutively expresses LuxR, which
in the presence of AHL binds the lux box promoter and activates expression
of PLA1." These two descriptions name different genetic programs. Please
confirm which plasmid (or plasmids) were actually used, and supply its
sequence file, before a Constructs table or sequence map can be added here.
::: -->

# Protocol

## Genetic circuit

The reporter plasmid, built in the pOpen backbone, constitutively expresses LuxR, which in the presence of AHL binds the lux box promoter and activates expression of PLA1. PLA1 expression therefore occurs only when AHL is present.

# Methods

## 1.1 LUVs

### Hydration

Hydrate a dried POPC lipid film (~2 mg) in buffer containing glucose and 15 v/v% Optiprep, at a final osmolarity of 1200 mOsm. The buffer contains 15 mg/mL CPRG. (The lipid film was dried under a nitrogen atmosphere and then dried under vacuum for ~2 hours before hydration)

1. Vortex, then sonicate for 15 min at room temperature.
2. Apply 5 freeze-thaw cycles (liquid nitrogen, then thaw in a room-temperature water bath).

### Clean-up by centrifugation

1. Split the mixture into 5 tubes, each with 200 µL vesicles and 1 mL outer solution (glucose at a final osmolarity of 1200 mOsm).
2. Spin at 15,000 g for 15 min at room temperature.
3. Resuspend the pellet in outer solution and wash again by pelleting at the same settings.
4. Repeat until the outer solution of the pellet looks clear (2-4 washes).

The final pellet was resuspended in a buffer containing 1mM CaCl2 and 50mM Hepes and 1149mOsm of Glucose and 15U/µL of Beta Galactosidase. Calcium is needed for efficient PLA activity and Hepes is needed for an efficient color change.

:::{figure} ./figures/luv-pellet.png
:label: fig-luv-pellet
:align: center
:width: 60%
Snapshot of the LUV pellet after 4 washes.
:::

<!-- missing notebook -->

[`fig-luv-pellet`, notebook:`none`, platemap:`none`, data source:`none`, caption: (Snapshot of the LUV pellet after 4 washes.)]

Ions were added after formation of the vesicles and the cleanup as it affects stability and overall yield. The average pellet will be a lot smaller when using a solution with high ionic strength.

## 1.2 GUVs

### Lipid-in-oil mixture

1. Resuspend a dried POPC film (~2 mg) in 500 µL mineral oil. (The lipid film was dried under a nitrogen atmosphere and then dried under vacuum for ~2 hours before adding mineral oil)
2. Sonicate for ~20 min at 30°C.

### Inner solution

:::{table} GUV inner solution.
:label: tbl-guv-inner-solution
:align: center

| Component | Volume |
| --- | --- |
| Extract | 6 |
| Premix | 8 |
| AA mix | 2 |
| Rnase Inhibitor | 0.5 |
| Plasmid | 2.5 |
| Optiprep | 1 |
| V total | 20 |
:::

### Outer solution

Glucose and 50 mM HEPES, at a final osmolarity of ~1200 mOsm.

### Emulsion and transfer

1. Pipette 20 µL cytosol reaction into 200 µL lipid-in-oil mixture.
2. Pipette up and down ~9 times to form a water-in-oil emulsion.
3. Layer the emulsion onto ~250 µL outer solution.
4. Centrifuge for 20 min at 9,000 g at room temperature.
5. Gently remove the oil and most of the outer solution.
6. Resuspend the GUV pellet in around 120µL of dye-loaded LUVs.

### Incubation

Vesicles have been incubated in a sealed clear bottom 384 well plate at 37 degrees.

Vesicles were prepared twice and then pipetted into the plate into four wells each where two of them were induced with AHSL at a final concentration of 5µM.

LUVs alone were added as a control onto which AHSL was also added.

The protocol has been altered to match the osmolarity of nucleus cytosol vesicles, and to reduce overall ionic strength. Previous protocol used Potassium glutamate instead of glucose. And the weight gradient was sucrose and glucose. As plasmid concentration was not very high, we used optiprep to have more volume available to add plasmid.

### Data acquisition and analysis

Reactions were plated in a Greiner 384-well small-volume NoBind plate and read on a BioTek Cytation 3 plate reader (serial 130723A) held at 37 °C (gradient 0 °C). CPR absorbance was recorded at 570 as a kinetic run over night.

Images were taken with a phone camera.

# Results

After less than 1h changes in color could be observed between the induced and the non-induced condition. Even though differences between GUVs can be distinguished, there is a quite high leakage in gene expression in the uninduced condition, where GUVs also seem to lyse over time. The control of LUVs with AHSL appear to be very stable indicating that AHSL at given DMSO concentration does not affect membrane integrity. It is unknown if the color change/lysis is exclusively PLA1 activity, as bursting of GUVs upon increased transcriptional activity could give high background signal. The addition of unencapsulated cytosol was able to lyse vesicles.

(fig-colorchange)=
:::::{tab-set}

::::{tab-item} Overnight incubation
:sync: overnight

:::{figure} ./figures/colorchange-overnight.png
:label: fig-colorchange-overnight
:align: center
:width: 90%
Bulk color change, overnight incubation. Top row: DevCells induced with 5µM AHSL. Middle row: DevCells not induced. Bottom row: LUVs alone induced with 5µM AHSL.
:::

::::

::::{tab-item} 1 h
:sync: 1h

:::{figure} ./figures/colorchange-1h.png
:label: fig-colorchange-1h
:align: center
:width: 90%
Bulk color change, 1 h incubation. Top row: DevCells induced with 5µM AHSL. Middle row: DevCells not induced. Bottom row: LUVs alone induced with 5µM AHSL.
:::

::::

:::::

<!-- missing notebook -->

[`fig-colorchange-1h`, notebook:`none`, platemap:`none`, data source:`none`, caption: (Bulk color change, 1 h incubation. Top row: DevCells induced with 5µM AHSL, Middle row DevCells not induced, Bottom row: LUVs alone induced with 5µM AHSL.)]

[`fig-colorchange-overnight`, notebook:`none`, platemap:`none`, data source:`none`, caption: (Bulk color change, overnight incubation. Top row: DevCells induced with 5µM AHSL, Middle row DevCells not induced, Bottom row: LUVs alone induced with 5µM AHSL.)]

<!-- :::{danger} Unresolved before publication
:name: flags-missing-platereader -->

<!-- The source Doc states: "Plot of platereader is missing." The
quantitative 570 nm kinetic absorbance trace referenced in Data acquisition
and analysis above was never produced or was lost; only the two photographs
above exist. ::: -->

Key to making the colorchange module work sufficiently well is that the dye loaded vesicle concentration should exceed the amount of vesicles the DevCells are able to lyse, so the maximum CPR absorbance will not be reached and the conditions stay distinguishable.

CPRG absorbance could not be measured as the absorbance in the 412 channel was too strong.

# Notes

<!-- :::{admonition}
:name: gap-notes

Please fill in a Notes section. The source Doc has no Notes or failure-modes
section of its own.
::: -->

# What's next

<!-- :::{admonition}
:name: gap-whats-next

Please fill in what's next. The source Doc has no forward-looking section of
its own beyond the dye-concentration point already carried into Results.
::: -->

# Resources

- [Assemble Base Cytosol](https://docs.nucleus.engineering/docs/processes/assemble-base-cytosol/main) — Nucleus process, component names and reference composition
- Yadav, S. (2025). First Nucleus Cytosol Testing: Evaluation of Nucleus Cytosol v0.5 Through deGFP Expression. [10.63765/fppr8928](https://doi.org/10.63765/fppr8928)
- [RNase Inhibitor, Murine — NEB #M0314L](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine)

<!-- :::{admonition}
:name: gap-resources-citations

Two open items from the source Doc's own Sources list, carried as written,
not resolved:

"Some citation on quorum sensing and AHSL LuxR in cell free?" — no citation
was supplied.

"Cite GFP devnote" — no specific DevNote is named. `devstudio/devnote-jpo-nm-202609`
on this board (two shared authors, same LuxR quorum-sensing system,
demonstrated by GFP) is a plausible candidate, but this is not stated in the
source and is not assumed here. Please confirm which DevNote this refers to.
::: -->
