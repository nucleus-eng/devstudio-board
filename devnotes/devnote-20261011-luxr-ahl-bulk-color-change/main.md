---
title: 'Implementing of a bulk color change module into bacterial quorum sensing'
thumbnail: ./figures/colorchange-overnight.png
---

<!-- review-notes.yml#main-01 -->

<!-- review-notes.yml#main-02 -->

<!-- review-notes.yml#main-03 -->

# Abstract

It has previously been shown that developer cells can use the LuxR quorum sensing system to detect AHSL (C6) a diffusible molecule bacteria use to communicate with each other, to sense bacteria and report that. Demonstrated by GFP. Here we wish to extend this system, by using the genetic sensor module and implement a novel module for visible color change, based on the production of PLA1 that lyses storage compartments that result in the release of CPRG (Chlorophenol Red-β-D-galactopyranoside) which then can be cleaved into CPR by beta galactosidase which is in the outer solution.

# Overview

We made dye loaded LUVs that were stable over long time incubation without leaking dye, and induced GUV lysis by expression of PLA1 in GUVs containing bacterial 30S lysate. We induced the expression of PLA1 by addition of AHSL, allowing us to distinguish a visible by eye difference of the induced and the non-induced condition.

# Materials

<!-- review-notes.yml#main-04 -->

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

<!-- review-notes.yml#main-05 -->

<!-- review-notes.yml#main-06 -->

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

<!-- review-notes.yml#main-07 -->

<!-- review-notes.yml#main-08 -->

# Protocol

## Genetic circuit

The reporter plasmid, built in the pOpen backbone, constitutively expresses LuxR, which in the presence of AHL binds the lux box promoter and activates expression of PLA1. PLA1 expression therefore occurs only when AHL is present.

## Plasmid map

(seqviz-popen-luxr-pla1)=
:::{seqviz} ./dna/pOpen-LuxR-PLA1.gb
:::

<!-- review-notes.yml#main-09 -->

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

<!-- review-notes.yml#main-10 -->

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

<!-- review-notes.yml#main-11 -->

<!-- review-notes.yml#main-12 -->

<!-- review-notes.yml#main-13 -->

Key to making the colorchange module work sufficiently well is that the dye loaded vesicle concentration should exceed the amount of vesicles the DevCells are able to lyse, so the maximum CPR absorbance will not be reached and the conditions stay distinguishable.

CPRG absorbance could not be measured as the absorbance in the 412 channel was too strong.

# Resources

- [Assemble Base Cytosol](https://docs.nucleus.engineering/docs/processes/assemble-base-cytosol/main) — Nucleus process, component names and reference composition
- Yadav, S. (2025). First Nucleus Cytosol Testing: Evaluation of Nucleus Cytosol v0.5 Through deGFP Expression. [10.63765/fppr8928](https://doi.org/10.63765/fppr8928)
- [RNase Inhibitor, Murine — NEB #M0314S](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine)

<!-- review-notes.yml#main-14 -->
