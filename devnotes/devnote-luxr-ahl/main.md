---
title: 'Implementing of a bulk color change module into bacterial quorum sensing'
thumbnail: ./figures/colorchange-overnight.png
---

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

**The Reagents table's plasmid identity is now resolved, and its sequence
file exists.** The source Doc named a "pT7-tetO-plamGFP reporter plasmid"
and linked it to the `detector-tetr-atc` module, a tetR/aTc-induced GFP
reporter, which did not match the LuxR-driven, PLA1-expressing circuit the
Protocol section describes. `DevCell_Materials_Tracker.xlsx` (the Drive
materials tracker) maps this DevNote to construct "pOpen-LuxR-PLA1", and
`nucleus-eng/DNA` holds its real file, `dna/pOpen-LuxR-PLA1.gb`, now copied
in and rendered under Protocol, Genetic circuit, Plasmid map. Its features
(a `BBa_J23101` promoter driving `luxR`, a `Plux`/`lux box` promoter driving
`PLA1`, the `pOpen` backbone) match that section's description directly.
The Reagents table is updated to this plasmid.

**The source Doc flags its own missing data.** Its Results section ends
with this sentence: "Plot of platereader is missing." That missing trace
is the quantitative 570 nm kinetic absorbance data for
{ref}`fig-colorchange`. The data was never produced, or it was lost before
the author wrote this Doc. The two photographs in Results are a
qualitative stand-in, not a replacement for that data.

**No platemap, no notebook, and no raw instrument data exist in the
supporting folder.** This gap applies to both figures. `asset_chain_complete`
reads `false` for both entries in `manifest.json`.

**One of two uncertainty markers in the source table is now resolved.**
The Abstract's "CPRG (write long name)" tag was the author's own reminder
to spell out the reagent's full chemical name. The source Doc never
supplied it, but the Nucleus materials reference does: CPRG is
Chlorophenol Red-β-D-galactopyranoside. The Abstract is updated with this
name. The "Beta-Gal?" stock row, with no concentration given, carries
forward unresolved; neither source names a concentration for it.

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

# Abstract

It has previously been shown that developer cells can use the LuxR quorum sensing system to detect AHSL (C6) a diffusible molecule bacteria use to communicate with each other, to sense bacteria and report that. Demonstrated by GFP. Here we wish to extend this system, by using the genetic sensor module and implement a novel module for visible color change, based on the production of PLA1 that lyses storage compartments that result in the release of CPRG (Chlorophenol Red-β-D-galactopyranoside) which then can be cleaved into CPR by beta galactosidase which is in the outer solution.

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
| Small Molecule Mix (SMix) | Nucleus Small Molecule Mix (see [Make Small Molecule Mix](https://docs.nucleus.engineering/docs/processes/make-small-molecule-mix/main)) | b.next | N/A | N/A | N/A | [Make Small Molecule Mix](https://docs.nucleus.engineering/docs/processes/make-small-molecule-mix/main) |
| tRNA | Nucleus Total tRNA (see [Make tRNAs](https://docs.nucleus.engineering/docs/processes/make-trna/main)) | b.next | N/A | N/A | -80 °C | [Make tRNAs](https://docs.nucleus.engineering/docs/processes/make-trna/main) |
| Protein Mix (PMix) | Nucleus Protein Mix, 36 PURE system proteins (see [Make Protein Mix](https://docs.nucleus.engineering/docs/processes/make-36pot/main)) | b.next | N/A | N/A | N/A | [Make Protein Mix](https://docs.nucleus.engineering/docs/processes/make-36pot/main) |
| Ribosomes | Nucleus 70S ribosomes (see [Make Ribosomes](https://docs.nucleus.engineering/docs/processes/make-ribosomes/main)) | b.next | N/A | N/A | -80 °C | [Make Ribosomes](https://docs.nucleus.engineering/docs/processes/make-ribosomes/main) |
| RNase Inhibitor, Murine (RIM) | RNase Inhibitor, Murine | New England Biolabs | M0314S | $87.00 | -25 °C to -15 °C | [NEB #M0314S](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| Optiprep | OptiPrep™ | STEMCELL Technologies | 07820 | $289.00 | Room temperature | [STEMCELL #07820](https://www.stemcell.com/products/optipreptm.html) |
| pOpen-LuxR-PLA1 reporter plasmid | LuxR-PLA1 insert in a pOpen backbone (Golden Gate Assembly) | b.next (in-house construct) | N/A | N/A | Glycerol stock | |
| Nuclease-free H₂O | — | — | N/A | N/A | N/A | |
| AHSL | N-(3-Oxohexanoyl)-L-homoserine lactone | Sigma-Aldrich | K3007 | $40.70 (10 mg) / $590.00 (50 mg) | -20 °C | [Sigma-Aldrich #K3007](https://www.sigmaaldrich.com/US/en/product/aldrich/k3007) |
| CPRG | Chlorophenol Red-β-D-galactopyranoside | Roche (via Sigma-Aldrich) | 10884308001 | $160.00 | -20 °C in water at 20 mg/mL | [Sigma-Aldrich #10884308001](https://www.sigmaaldrich.com/US/en/product/roche/10884308001) |
| Beta-Gal | β-Galactosidase from Escherichia coli, Grade VIII, lyophilized powder, ≥500 units/mg protein | Sigma-Aldrich | G5635 | N/A | -20 °C | [Sigma-Aldrich #G5635](https://www.sigmaaldrich.com/US/en/product/sigma/g5635) |
:::

<!-- Materials pass, 2026-11-10: filled against two sources, in the order
Anton asked for. First, the Drive spreadsheet `DevCell_Materials_Tracker.xlsx`
(id 1S5AEJnl6sMWUU7Yof3lFIO8tpLtEgvEa) — its "Reagent Prep" tab (gid
1064417783, the tab the given link opens to) is empty, so matches were taken
from its "London Node", "Chicago Node", "DNA Sequences" and "Sheet2" tabs
instead. Second, https://docs.nucleus.engineering/guides/materials-reference/,
which supplied the ribosome/tRNA/protein-mix process links, the Optiprep and
Beta-Gal catalog data, and the AHSL and CPRG identities (both confirmed
against the same catalog numbers the Drive spreadsheet already uses for those
two reagents). The reporter-plasmid row is updated using the Drive
spreadsheet: its "Sheet2" tab maps construct "pOpen-LuxR-PLA1" to DevNote
"Bulk color change module" (this DevNote), and its "DNA Sequences" tab records
"LuxR-PLA1" as cloned into the pOpen backbone by Golden Gate Assembly, held in
glycerol stock, with its plasmid-level function test still "In progress...".
This replaces the source Doc's "pT7-tetO-plamGFP reporter plasmid" name and
its `detector-tetr-atc` link, which matched a different, tetR/aTc-induced GFP
circuit (see the resolved flag below). No match was found in either source
for Small Molecule Mix (SMix) or Nuclease-free H₂O beyond what is shown;
their Catalog No., Price and (for SMix) Storage Conditions stay N/A, flagged
rather than guessed.

PR review (jecalles, 2026-11-10): the Protein Mix row originally linked
"Make OnePot Protein Mix" (`make-1pot`). That process makes a *different*,
functionally-equivalent mix with uncontrolled molar ratios between its
proteins. The [PMix module spec](https://docs.nucleus.engineering/docs/modules/pmix/spec/)
names the default, controlled-ratio process as "Make Protein Mix"
(`make-36pot`), which is what this DevNote's PMix row now links to. -->

<!-- Reporter-plasmid identity, resolved 2026-11-10. The source Doc's
Reagents table named a "pT7-tetO-plamGFP reporter plasmid" and linked it to
the `detector-tetr-atc` module, a tetR/aTc-induced GFP reporter, which did
not match the LuxR-driven, PLA1-expressing circuit the Protocol section
describes; no sequence file existed yet for either, so this was a blocking
identity question. `DevCell_Materials_Tracker.xlsx` maps this DevNote to
construct "pOpen-LuxR-PLA1" (its "Sheet2" tab) and records it as cloned into
the pOpen backbone by Golden Gate Assembly (its "DNA Sequences" tab). The
real file, `dna/pOpen-LuxR-PLA1.gb`, now confirms this directly: see
{ref}`Plasmid map <seqviz-popen-luxr-pla1>` under Protocol, Genetic circuit,
for the feature-by-feature match and sourcing note. The Reagents table below
is updated to this plasmid. -->

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
| RNase Inhibitor, Murine (RIM) | working stock | [NEB #M0314S](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| Optiprep | | |
| pOpen-LuxR-PLA1 reporter plasmid | 129.6 nM | Final concentration: 0 or 1 nM depending on sample |
| Nuclease-free H₂O | — | to volume |
| AHSL | 80 mM in DMSO | Diluted in DI water for experiment |
| CPRG | Dry powder | Dissolved in aqueous buffer |
| Beta-Gal? | | |
:::

<!-- The "Beta-Gal?" row's question mark is the source Doc's own uncertainty
marker, carried as written, not resolved. -->

<!-- RNase Inhibitor catalog number, 2026-11-10: the source Doc named pack
size "M0314L". Both `DevCell_Materials_Tracker.xlsx` and the Nucleus
materials reference name "M0314S" instead, same NEB product page. Set to
M0314S below, matching both independent sources. -->

# Protocol

## Genetic circuit

The reporter plasmid, built in the pOpen backbone, constitutively expresses LuxR, which in the presence of AHL binds the lux box promoter and activates expression of PLA1. PLA1 expression therefore occurs only when AHL is present.

## Plasmid map

(seqviz-popen-luxr-pla1)=
:::{seqviz} ./dna/pOpen-LuxR-PLA1.gb
:::

<!-- `dna/pOpen-LuxR-PLA1.gb` is the real file of record, copied unmodified
from `nucleus-eng/DNA`, path `effectors/detector-3oc6-hsl/pOpen-LuxR-PLA1.gb`
(identical on branches `main` and `devcells/devstudio-constructs`), checked
2026-11-10. It is 4175 bp, circular, and its features match the Genetic
circuit paragraph above feature for feature: a `BBa_J23101` constitutive
promoter driving a `luxR` CDS, a `Plux` promoter carrying the `lux box`
element, a `PLA1` CDS downstream of it, and the `pOpen` backbone's own `ori`
and `AmpR`. Its sibling file in the same directory, `LuxR-PLA1-linear.gb`
(2237 bp), is the same cassette without the backbone; this DevNote's GUV
route uses bacterial S30 lysate (S30 degrades linear DNA, no GamS), so the
circular form here, not the linear one, is the correct file for this
protocol. This also confirms the directory it is filed under,
`detector-3oc6-hsl`: the AHSL reagent above (Sigma-Aldrich K3007,
3-oxo-C6-HSL) is the molecule this circuit actually responds to, not generic
C6-HSL as the Abstract's "(C6)" might suggest. -->

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

<!-- :::{danger} Unresolved before publication
:name: flags-missing-platereader -->

<!-- The source Doc states: "Plot of platereader is missing." The
quantitative 570 nm kinetic absorbance trace referenced in Data acquisition
and analysis above was never produced or was lost; only the two photographs
above exist. ::: -->

Key to making the colorchange module work sufficiently well is that the dye loaded vesicle concentration should exceed the amount of vesicles the DevCells are able to lyse, so the maximum CPR absorbance will not be reached and the conditions stay distinguishable.

CPRG absorbance could not be measured as the absorbance in the 412 channel was too strong.

# Resources

- [Assemble Base Cytosol](https://docs.nucleus.engineering/docs/processes/assemble-base-cytosol/main) — Nucleus process, component names and reference composition
- Yadav, S. (2025). First Nucleus Cytosol Testing: Evaluation of Nucleus Cytosol v0.5 Through deGFP Expression. [10.63765/fppr8928](https://doi.org/10.63765/fppr8928)
- [RNase Inhibitor, Murine — NEB #M0314S](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine)

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
