---
title: 'First Nucleus Cytosol Testing'
---

+++ { "part": "abstract" }
<!-- REVIEW: Abstract drafted from Overview — confirm or revise before publishing. -->
The cytosol is the internal compartment of a synthetic cell containing proteins, RNAs, small organic molecules, and salts that collectively define its biochemical environment and support user-defined biological functions. Nucleus Cytosol is based on the PURE system, consisting of a defined set of proteins and small molecules that reconstitute the essential transcription and translation machinery required for protein synthesis from DNA templates. Here, we demonstrate that Nucleus Cytosol performs comparably to commercial PURExpress system in terms of final protein yield, and we identify optimal magnesium acetate conditions for the system.
+++

# Overview

The cytosol is the internal compartment of a synthetic cell containing proteins, RNAs, small organic molecules, and salts that collectively define its biochemical environment and support user-defined biological functions ({ref}`fig-schematic`). Nucleus Cytosol is based on the PURE system, consisting of a defined set of proteins and small molecules that reconstitute the essential transcription and translation machinery required for protein synthesis from DNA templates ([doi:10.1038/90802](https://doi.org/10.1038/90802)) <!-- REVIEW: add author/year citation string -->. Nucleus Cytosol comprises the essential components required for *in vitro* protein synthesis: a protein mix (PMix), a small-molecule mix (SMix), A19 tRNAs, A19 ribosomes, Mg²⁺ ions (magnesium acetate), and a pOpen-deGFP gene expression template driven by the T7 transcription system.

Here, we demonstrate that Nucleus Cytosol performs comparably to commercial PURExpress system in terms of final protein yield. We also performed a magnesium acetate titration to determine the optimal Mg²⁺ concentration for the system. Some component concentrations are still being standardized; therefore, detailed manufacturing protocols for each component of Nucleus Cytosol will be released later through Nucleus Distribution.

:::::{tab-set}

::::{tab-item} Schematic

:::{figure} ./general/schematic.png
:name: fig-schematic
:align: center
:width: 80%
A schematic representation of PURE converting template DNA into a fluorescent reporter.
:::

::::

::::{tab-item} Sequence (pOpen-deGFP)

<!-- REVIEW: Run devstudio-verify-dna-constructs on pOpen-deGFP to confirm construct identity and file extension (.gb vs .gbk) before submission. GitHub blob URL auto-rewritten to raw at build time (nucleus-eng/devnote-template#5). -->
:::{seqviz} https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-deGFP.gbk
:height: 600px
:::

::::

:::::

# Design

Nucleus Cytosol is designed to reconstitute cell-free gene expression from a minimal set of defined components, targeting functional equivalence with commercial PURE-based systems while remaining open and reproducible. The formulation tested here uses PMix, SMix, A19 tRNAs, A19 ribosomes, and magnesium acetate to support transcription and translation. This DevNote characterizes the initial Cytosol formulation against PURExpress as a commercial benchmark (Experiment 1) and identifies the optimal Mg²⁺ concentration for the current component set (Experiment 2). Microscopy was used to verify encapsulation and expression in liposomes (Experiment 3).

<!-- REVIEW: No dedicated Design section in source DevNote(G) — this section was inferred from Overview and Results content. Expand with design rationale, component design records, or a link to the formulation specification before publishing. -->

# Methods

<!-- RENAMED: "Materials and equipment" → "Methods" -->

## Reagents

<!-- REVIEW: Reagent table not populated — all fields are placeholders in source DevNote(G). A workflow to autofill from https://docs.nucleus.engineering/guides/materials-reference/ based on reaction table components is planned but not yet built. -->

:::{table} Reagents used in this experiment.
:label: tbl-reagents
:align: center
<!-- vale nucleus.magnitude-unit-spacing = NO -->
| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| 4X SMix | N/A | N/A | N/A | N/A | N/A | |
| Pmix (08-02) | N/A | N/A | N/A | N/A | N/A | |
| Nucleus Ribosome | N/A | N/A | N/A | N/A | N/A | |
| pOpen-deGFP DNA | N/A | N/A | N/A | N/A | N/A | |
| Nucleus tRNA | N/A | N/A | N/A | N/A | N/A | |
| Mg-Acetate | N/A | N/A | N/A | N/A | N/A | |
| SolA (PURExpress) | N/A | N/A | N/A | N/A | N/A | |
| Sol B (PURExpress) | N/A | N/A | N/A | N/A | N/A | |
<!-- vale nucleus.magnitude-unit-spacing = YES -->
:::

## Constructs

:::{table} DNA constructs used in this experiment.
:label: tbl-constructs
:align: center
| Name | Sequence | Purpose |
| --- | --- | --- |
| pOpen-deGFP | [pOpen-deGFP.gbk](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-deGFP.gbk) | Template for deGFP expression; used across all conditions in Experiments 1 and 2 |
:::

<!-- REVIEW: Run devstudio-verify-dna-constructs on pOpen-deGFP before DevNote(M) submission. -->

## Protocols followed

All experiments were performed following Nucleus protocols:

- Assemble base cytosol: <https://docs.nucleus.engineering/docs/processes/assemble-base-cell/main/>
- Encapsulation: phase transfer: <https://docs.nucleus.engineering/docs/processes/assemble-base-cell/main/>

Modifications consisted only of changing the composition as described in each experiment below.

## pOpen-deGFP in Nucleus Cytosol and PURExpress

For each condition, 35 µL of mastermix was prepared and aliquoted 3 × 10 µL into a Greiner 384-well SV NoBind plate. Fluorescence kinetics were measured over 6 hours at 37 °C (interval: 5 min; 73 reads). Read modes: GFP-F-G35 (Ex 485/20, Em 528/20; Gain 35) and GFP-M-G100 (Ex 485, Em 528; Gain 100).

:::::{tab-set}

::::{tab-item} Nucleus Cytosol

:::{table} Nucleus Cytosol reaction composition, Experiment 1.
:label: tbl-exp1-cytosol
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | NC + maxi+etOH [µL] | NC + maxi only [µL] | NC w/o DNA — Negative Control [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4X SMix | 4.00 | × | 1 | × | 8.75 | 8.75 | 8.75 |
| Pmix (08-02) | 15 | mg/mL | 1.80 | mg/mL | 4.20 | 4.20 | 4.20 |
| Nucleus Ribosome | 10 | µM | 1.8 | µM | 6.30 | 6.30 | 6.30 |
| pOpen-deGFP DNA | 231 / 155 / 115 | ng/µL | 3 / 3 / 0 | nM | 0.83 | 1.24 | 0.00 |
| Nucleus tRNA | 35 | mg/mL | 3.5 | mg/mL | 3.50 | 3.50 | 3.50 |
| Mg-Acetate | 200 | mM | 8 | mM | 1.40 | 1.40 | 1.40 |
| Water | — | — | — | — | 10.02 | 9.61 | 10.85 |
| **Total volume [µL]** | | | | | **35** | **35** | **35** |
:::

*DNA concentration calculation: pOpen-deGFP, 2812 bp, avg. MW 650 g/mol per bp. Stock conc.: 231 ng/µL (maxi+etOH), 155 ng/µL (maxi only), 115 ng/µL (neg. ctrl, 0 nM final).*

::::

::::{tab-item} PURExpress

:::{table} PURExpress reaction composition, Experiment 1.
:label: tbl-exp1-pure
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | PURE + maxi+etOH [µL] | PURE + maxi only [µL] |
| --- | --- | --- | --- | --- | --- | --- |
| SolA | 2.50 | × | 1 | × | 14.00 | 14.00 |
| Sol B | 8 | mg/mL | 2.40 | mg/mL | 10.50 | 10.50 |
| pOpen-deGFP DNA | 231 / 155 | ng/µL | 3 | nM | 0.83 | 1.24 |
| Water | — | — | — | — | 9.67 | 9.26 |
| **Total volume [µL]** | | | | | **35** | **35** |
:::

*DNA concentration calculation: pOpen-deGFP, 2812 bp, avg. MW 650 g/mol per bp. Stock conc.: 231 ng/µL (maxi+etOH), 155 ng/µL (maxi only).*

::::

:::::

## Mg²⁺ sweep in Nucleus Cytosol

Mg-acetate titration across 4–12 mM in 2 mM increments. 35 µL per condition, aliquoted 3 × 10 µL into a 384-well plate. All reactions used maxiprepped pOpen-deGFP with ethanol precipitation.

:::::{tab-set}

::::{tab-item} Nucleus Cytosol Mg²⁺ titration

:::{table} Nucleus Cytosol Mg-acetate titration composition, Experiment 2.
:label: tbl-exp2-mg-sweep
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | 4 mM [µL] | 6 mM [µL] | 8 mM [µL] | 10 mM [µL] | 12 mM [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4X SMix | 4.00 | × | 1 | × | 8.75 | 8.75 | 8.75 | 8.75 | 8.75 |
| Pmix (08-02) | 15 | mg/mL | 1.80 | mg/mL | 4.20 | 4.20 | 4.20 | 4.20 | 4.20 |
| Nucleus Ribosome | 10 | µM | 1.8 | µM | 6.30 | 6.30 | 6.30 | 6.30 | 6.30 |
| pOpen-deGFP DNA | 231 | ng/µL | 3 | nM | 0.83 | 0.83 | 0.83 | 0.83 | 0.83 |
| Nucleus tRNA | 29.6 | mg/mL | 3.5 | mg/mL | 4.14 | 4.14 | 4.14 | 4.14 | 4.14 |
| Mg-Acetate | 200 | mM | 4 / 6 / 8 / 10 / 12 | mM | 0.70 | 1.05 | 1.40 | 1.75 | 2.10 |
| Water | — | — | — | — | 10.08 | 9.73 | 9.38 | 9.03 | 8.68 |
| **Total volume [µL]** | | | | | **35** | **35** | **35** | **35** | **35** |
:::

*DNA concentration calculation: pOpen-deGFP, 2812 bp, avg. MW 650 g/mol per bp.*

::::

::::{tab-item} PURExpress positive control

:::{table} PURExpress positive control, Experiment 2.
:label: tbl-exp2-pure-ctrl
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | PURExpress Positive Control [µL] |
| --- | --- | --- | --- | --- | --- |
| SolA | 2.50 | × | 1 | × | 14.00 |
| Sol B | 8 | mg/mL | 2.40 | mg/mL | 10.50 |
| pOpen-deGFP DNA | 231 | ng/µL | 3 | nM | 0.83 |
| Water | — | — | — | — | 9.67 |
| **Total volume [µL]** | | | | | **35** |
:::

*DNA concentration calculation: pOpen-deGFP, 2812 bp, avg. MW 650 g/mol per bp.*

::::

:::::

## Microscopy

Cells from Experiment 2 conditions were imaged under microscopy to verify liposome formation and expression results.

<!-- REVIEW: No composition table or platemap for Experiment 3 (microscopy observation only). Add sample layout if available before submission. -->

# Results

<!-- RENAMED: "Results and Observations" → "Results" -->

## Experiment 1 — pOpen-deGFP in Nucleus Cytosol and PURExpress

To evaluate the activity of Nucleus Cytosol, we expressed deGFP using the pOpen-deGFP plasmid. The plasmid was prepared with the ZymoPURE II Plasmid Maxiprep Kit (Cat. #D4203) following the manufacturer's protocol, with an additional ethanol precipitation step to remove residual salts and impurities.

<!-- REVIEW: Source DevNote(G) references "the ethanol precipitation protocol used is attached to this DevNote." Confirm this file is included in the experiments/ bundle before submission. -->

Two preparations of pOpen-deGFP were tested: one obtained directly from the maxiprep and another that underwent the additional ethanol precipitation step. This comparison was performed to assess any notable differences in performance between the two DNA preparations. Both DNA samples were also tested in a commercial PURExpress system as controls to benchmark Cytosol performance. A negative control Cytosol reaction lacking the pOpen-deGFP template was included. Reactions were prepared as described in {ref}`tbl-exp1-cytosol` and {ref}`tbl-exp1-pure`. Cytosol reactions were carried out with a final magnesium acetate concentration of 8 mM, added exogenously during setup.

The protein expression results indicate that Nucleus Cytosol performs comparably to the PURExpress system, achieving similar final protein yields ({ref}`fig-kinetics-exp1` and {ref}`fig-endpoint-exp1`). Minor differences were observed between the two DNA preparations — maxiprep alone and maxiprep followed by ethanol precipitation — but these variations were not significant enough to establish one method as superior. Interestingly, the maxiprep + ethanol precipitation template yielded slightly higher expression in PURExpress, whereas the maxiprep-only template performed better in Nucleus Cytosol. Subsequent experiments described in this DevNote were conducted using the maxiprep + ethanol precipitation DNA template.

<!-- REVIEW: assets — [platemap](experiments/20251104-NucleusPURE_deGFP/20251104-NucleusPURE-deGFP-platemap.csv) | [raw data](experiments/20251104-NucleusPURE_deGFP/biotek-cdk.txt) | [notebook](experiments/20251104-NucleusPURE_deGFP/Analysis.ipynb) — remove before submission -->

:::::{tab-set}

::::{tab-item} Time series
:sync: exp1-ts-ep

:::{figure} #fig:kinetics-exp1
:name: fig-kinetics-exp1
:align: center
:width: 75%
Translation kinetics of Cytosol and PURExpress reactions using two different pOpen-deGFP DNA preps. Cytosol w/o DNA refers to the Cytosol reaction lacking the pOpen-deGFP template.
:::

::::

::::{tab-item} Steady state
:sync: exp1-ts-ep

:::{figure} #fig:endpoint-exp1
:name: fig-endpoint-exp1
:align: center
:width: 75%
Final protein yields of the reactions measured at steady state.
:::

::::

:::::

## Experiment 2 — Mg²⁺ sweep in Nucleus Cytosol

The concentration of magnesium ions is a critical determinant of protein synthesis efficiency in PURE reactions ([doi:10.1080/21690731.2017.1327006](https://doi.org/10.1080/21690731.2017.1327006)) <!-- REVIEW: add author/year citation string -->. To assess the performance of Nucleus Cytosol across varying magnesium acetate concentrations and identify optimal conditions for future experiments, we performed a titration over a range of 4–12 mM in 2 mM increments. This range was selected based on prior results showing that 8 mM magnesium acetate yielded performance comparable to PURExpress, allowing us to explore both lower and higher concentrations for potential improvement. Reactions were prepared as described in {ref}`tbl-exp2-mg-sweep` and {ref}`tbl-exp2-pure-ctrl`. For each condition, a 35 µL mastermix was prepared, and 10 µL aliquots were dispensed in triplicate into a 384-well plate for fluorescence measurements. Magnesium acetate titration revealed that the initially used concentration of 8 mM was optimal for achieving the highest deGFP protein yield, comparable to the PURExpress positive control ({ref}`fig-kinetics-exp2` and {ref}`fig-endpoint-exp2`). Deviations from this concentration, either lower or higher, resulted in reduced overall protein expression.

<!-- REVIEW: LABEL COLLISION — Analysis.ipynb (EXP-sy-20251107) cells are labeled fig:kinetics-exp1 and fig:endpoint-exp1 in the notebook source. Rename them to fig:kinetics-exp2 and fig:endpoint-exp2 in the notebook before building, or the MyST anchors below will resolve to Experiment 1 figures. See figure-provenance-manifest.json findings. -->

<!-- REVIEW: assets — [platemap](experiments/20251107-NucleusPURE_deGFP_MgSweep/20251107-NucleusPURE-deGFP-MgSweep-platemap.csv) | [raw data](experiments/20251107-NucleusPURE_deGFP_MgSweep/biotek-cdk.txt) | [notebook](experiments/20251107-NucleusPURE_deGFP_MgSweep/Analysis.ipynb) — remove before submission -->

:::::{tab-set}

::::{tab-item} Time series
:sync: exp2-ts-ep

:::{figure} #fig:kinetics-exp2
:name: fig-kinetics-exp2
:align: center
:width: 75%
Magnesium acetate titration in Nucleus Cytosol showed that a final concentration of 8 mM in the reaction produced the highest deGFP protein yield.
:::

::::

::::{tab-item} Endpoint
:sync: exp2-ts-ep

:::{figure} #fig:endpoint-exp2
:name: fig-endpoint-exp2
:align: center
:width: 75%
Final protein yields of the reactions measured at steady state across Mg-acetate concentrations.
:::

::::

:::::

## Experiment 3 — Microscopy

To verify encapsulation and expression, liposomes from Experiment 2 conditions were imaged under microscopy. Most liposomes formed correctly and expression levels were nominal.

<!-- REVIEW: assets — [notebook](experiments/20251107-Microscopy/microscopy_20251107.ipynb) | no platemap — add sample layout if available. asset_chain_complete: false — remove this comment before submission -->

:::::{tab-set}

::::{tab-item} Microscopy image

:::{figure} ./figures/microscopy_image.png
:name: fig-microscopy-image
:align: center
:width: 75%
<!-- missing notebook cell label — static-PNG fallback. REVIEW: add #| label: tag to microscopy_20251107.ipynb to enable quarto-label pattern. -->
Microscopy image of liposomes from Experiment 2 conditions. Most liposomes formed correctly and expression levels were nominal.
:::

::::

::::{tab-item} Interactive viewer

<!-- REVIEW: Vizarr viewer included per figure-provenance-manifest.json (zarr URL from microscopy_20251107.ipynb annotation). Confirm zarr URL is correct and dataset should be embedded before submission. No platemap for Experiment 3 — add if available. -->
:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/valine/20260821-biotic-liposomes_2026-08-21_12-21-54.333371.zarr",
    "height": "600px"
}
:::

::::

:::::

# Notes

<!-- STYLE: non-standard top-level section "Notes" — preserved per participant intent -->

This experiment was performed without a platemap but we believe the results are informative and worth sharing as is.

# Acknowledgements

This work is part of the project titled "Developer Cells as a Scalable Platform for Predictable Engineering of (Non-Living) Biological Machines," and is funded by the Schmidt Sciences Foundation.

# Conclusions and next steps

<!-- RENAMED: "What's next" → "Conclusions and next steps" -->

Here, we showed that Nucleus Cytosol performs equivalently to other commercially available PURExpress system and characterizes the pOpen-T7-deGFP DNA template. Next steps will involve characterizing other Nucleus Modules in Cytosol.

+++ { "part": "data_availability" }
<!-- REVIEW: Confirm data files are bundled before publishing. Update statement if data will not be included in the bundle. -->
All data supporting this DevNote are included in the accompanying data bundle, available for download above.
+++
