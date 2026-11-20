---
title: 'Quorum Sensing in Nucleus Cytosol using EsaO/EsaR Transcriptional Regulation'
---

<!-- This page's own frontmatter title is required so MyST does not fall back
to this page's first heading ("Abstract") as the page title: without it, the
project title from `curvenote.yml` never renders. -->

# Abstract

Over an intense 3-week collaboration at DevStudio, we set out to build developer cells that sense a bacterial-derived acyl-homoserine lactone signal. We leveraged EsaR/EsaO transcriptional regulation, an established quorum-sensing system {cite}`shong2013,minogue2002` in which the EsaR repressor blocks transcription until its signal is present. Previous implementations of this system in PURE co-expressed EsaR alongside the sensor construct, allowing early unrepressed transcription before EsaR accumulated {cite}`tang2018,chizzolini2017`. We improved this by pre-expressing EsaR separately before use and by adding a second EsaO operator to deepen repression. EsaR is first expressed in Nucleus cytosol, then added to the sensor reaction afterward, keeping the EsaO operator sites occupied from the start. We optimised repression by exploring several reaction conditions such as EsaR template competition and lower reaction temperatures, with the best condition reaching a 5.8-fold change between 'on' and 'off' states. We then encapsulated the sensor inside GUVs, producing developer cells that successfully detected exogenously added AHSL. We present these developer cells as a starting point for the construction of a synthetic cell device capable of sensing contaminated surfaces.

# Overview

Nucleus cytosol is a cell-free system of defined composition that can be encapsulated inside giant-unilamellar vesicles (GUVs) to produce developer cells; a platform that new synthetic cell modules can be designed, tested, and built from. In addition, synthetic biology has leveraged natural modes of communication to produce DNA sensors for a range of signalling molecules. As such, developer cells encapsulating these sensors can be programmed to communicate with and sense their external environment. An example of detectable signalling molecules are the acyl-homoserine lactones (AHSLs), small molecules secreted by bacteria that regulate gene expression in response to population density. A developer cell programmed to sense AHSL and produce a detectable output could enable sensitive detection of bacteria in specific environments. We envision these developer cells detecting food spoilage or contamination in medical settings.

Towards this goal, we programme developer cells to sense AHSL using the *Pantoea stewartii* repressor protein, EsaR. In the absence of its cognate ligand, 3-oxo-C6-HSL, EsaR natively binds the EsaO operator where it is thought to occlude RNA polymerase and prevent transcription {cite}`minogue2002`. In our case, we insert one or two EsaO operators downstream of the T7 promoter, blocking transcription in Nucleus cytosol until AHSL is added ({numref}`fig-esar-sensing`). EsaR has previously been co-expressed with an EsaO-controlled reporter both in bulk PURE reactions, and inside synthetic cells; however, the lag in EsaR expression was thought to result in early unrepressed transcription producing variable outputs {cite}`tang2018,chizzolini2017`. An alternative system supplied EsaR to lysate-encapsulated synthetic cells by pre-expressing EsaR in *E. coli* prior to lysate harvesting {cite}`ding2018`. This ensured that EsaR was present throughout the entire reaction; however, lysate-based systems often pose a challenge to further engineering due to their undefined composition.

To benefit from a defined chemical composition, and to limit early unrepressed transcription, we instead pre-express EsaR in [Nucleus cytosol](xref:nucleus-docs/docs/modules/base-cytosol/spec#overview) and pre-incubate it with the sensor DNA so that operator sites are occupied before the template enters the final reaction. We test single and dual operator sensor DNA constructs, the latter inspired by {cite}`shong2013`, in bulk cytosol reactions, optimising reaction conditions for increased sensor dynamic range before constructing developer cells that can sense exogenously added AHSL. We hope to build upon this work by embedding the developer cells in a hydrogel matrix, increasing their stability and progressing towards a deployable device ([DevStudio: London Node LuxR demo](https://devnotes.nucleus.engineering/articles/01a1121a-7513-7ec7-8378-0326c6b3630b)).

:::{figure} figures/EsaR-sensing.png
:label: fig-esar-sensing

EsaO/EsaR-dependent transcriptional regulation. EsaR binds the EsaO box preventing T7 polymerase from transcribing an mNeonGreen reporter protein. Upon binding of a AHSL signal, EsaR leaves the DNA re-enabling transcription.
:::
---

# Objectives

- Establish the pre-expressed EsaR : sensor DNA molar ratio needed to produce a defined 'on'/'off' state.
- Optimise sensor dynamic range by varying reaction conditions.
- Validate the optimised sensor in GUVs, as a step toward a deployable developer cell sensor.

---

# Sensor Design

To quantify sensor output we chose mNeonGreen, a bright fluorescent protein commonly used to report on cell-free protein synthesis {cite}`copeland2022`. This would enable us to rapidly optimise the sensor using plate reader assays. To pre-express EsaR, we used the directed-evolution variant EsaR(D91G) ({cite}`shong2013-chembio`). This variant shows substantially increased 3-oxo-C6-HSL sensitivity relative to wild-type EsaR. For the sensor DNA constructs, we followed the design used by {cite}`chizzolini2017` in which the EsaO operator is placed directly adjacent to the T7 promoter for maximal repression. The EsaO is flanked by a leader sequence containing the epsilon enhancer sequence and a strong ribosomal binding site. To further deepen repression, a second EsaO operator was inserted upstream of the native operator in the dual-operator construct. The two operators are separated by a single thymine. This follows the P{sub}`esa`R-C design described by {cite}`shong2013`. P{sub}`esa`R-C showed tighter repression and greater derepression than the native promoter when tested in *E. coli*. We were interested to see whether this same behaviour would translate to Nucleus cytosol reactions.

---

# DNA Constructs

Four linear DNA templates were used throughout this work: the EsaR(D91G) template DNA used to pre-express EsaR, two EsaO-mNG sensor DNA constructs carrying either single or dual EsaO operator boxes, and an unrepressed mNG control. Linear templates were amplified from g-blocks using PCR and cleaned-up prior to their addition into cytosol reactions.

:::{table}  DNA constructs used throughout this work. Sequences with annotations are listed in the below viewers. All constructs contain mNeonGreen, a bright fluorescent protein commonly used to report on cell-free protein expression {cite}`copeland2022`.
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

The file encodes `EsaR(D91G)` an EsaR variant evolved by {cite}`shong2013-chembio` that exhibits higher sensitivity and derepression than the native EsaR protein. 

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

---

# Methods

## Materials

::::{admonition} List of consumables
:class: dropdown

:::{table} Reagents and equipment used throughout this work. In-house components (Small molecule mix, tRNA, Protein mix, Ribosomes) link to their b.next preparation processes in `nucleus-docs`; other components were purchased from vendors, with their product links provided.
:label: tbl-reagents
:align: center

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | Small Molecule Mix (SMix) | b.next (in-house) | N/A | N/A | -80 °C | [link](xref:nucleus-docs/docs/processes/make-small-molecule-mix/main#overview) |
| tRNA | Nucleus Total tRNA (35 µg/µL, 10×) | b.next (in-house) | N/A | N/A | -80 °C | [link](xref:nucleus-docs/docs/processes/make-trna/main#overview) |
| Protein mix | Protein Mix (PMix), 36 PURE proteins, 15 µg/µL | b.next (in-house) | N/A | N/A | -80 °C | [link](xref:nucleus-docs/docs/processes/make-36pot/main#overview) |
| Ribosomes | Ribosomes, 10 µM (5.55×) | b.next (in-house) | N/A | N/A | -80 °C | [link](xref:nucleus-docs/docs/processes/make-ribosomes/main#overview) |
| RNase inhibitor | RNase Inhibitor, Murine | NEB | M0314S | $87.00 | -25 °C to -15 °C | [link](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| Nuclease free water | Water, Nuclease-Free, for Molecular Biology | Sigma-Aldrich | W4502-1L | $88.40 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/w4502) |
| AHSL | N-(3-Oxohexanoyl)-L-homoserine lactone | Sigma-Aldrich (Aldrich) | K3007 | $40.70 | -20 °C | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/k3007) |
| Fluorescein | Fluorescein, NIST-Traceable Standard (50 µM nominal) | Invitrogen (Thermo Fisher Scientific) | F36915 | $554.00 | 2 °C to 8 °C, protect from light | [link](https://www.thermofisher.com/order/catalog/product/F36915) |
| Q5 polymerase | Q5® High-Fidelity 2X Master Mix | NEB | M0492S | $226.00 | -20 °C | [link](https://www.neb.com/en-us/products/m0492-q5-high-fidelity-2x-master-mix) |
| HF buffer | Included in Q5® High-Fidelity 2X Master Mix | NEB | M0492S | N/A (included) | -20 °C | [link](https://www.neb.com/en-us/products/m0492-q5-high-fidelity-2x-master-mix) |
| M13 Fwd primer | Custom DNA oligo: 5'-GTAAAACGACGGCCAGTG-3' | IDT | N/A (custom) | N/A | -20 °C | N/A |
| M13 Rev primer | Custom DNA oligo: 5'-CAGGAAACAGCTATGACCATG-3' | IDT | N/A (custom) | N/A | -20 °C | N/A |
| Magnesium | Magnesium acetate tetrahydrate | Sigma-Aldrich | M0631-100G | $34.80 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigald/m0631) |
| POPC | 16:0-18:1 PC (POPC), 25 mg/mL | Avanti Research | A80557 (formerly 850457) | $435.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Mineral oil | Mineral oil, light, BioReagent, for molecular biology | Sigma-Aldrich | M5904 | $80.90 | Room temperature | [link](https://www.sigmaaldrich.com/US/en/product/sigma/m5904) |
| Glucose | D-(+)-Glucose, ≥99.5% (GC) | Sigma-Aldrich | G8270-100G | $40.20 | Room temperature | [link](https://www.sigmaaldrich.com/US/en/product/sigma/g8270) |
| Optiprep | OptiPrep Density Gradient Medium, 60% (w/v) iodixanol | Sigma-Aldrich | D1556-250ML | $380.00 | Room temperature | [link](https://www.sigmaaldrich.com/US/en/product/sigma/d1556) |
| DMSO | Dimethyl sulfoxide, Hybri-Max, sterile-filtered, BioReagent, ≥99.7% | Sigma-Aldrich | D2650-100ML | $287.00 | Room temperature | [link](https://www.sigmaaldrich.com/US/en/product/sigma/d2650) |
:::
::::

---

## Protocols

### Preparing linear DNA templates

Linear DNA templates were amplified from gBlocks by PCR using universal M13 forward/reverse primers, then cleaned up before use in cytosol reactions.

1. Resuspend each 1000 ng gBlock in 100 µL nuclease-free water (10 ng/µL stock). Resuspend primers to 100 µM.
2. Prepare a 7.5× master mix (250 µL reactions) of Q5 High-Fidelity 2X Master Mix, M13 forward and reverse primers, and nuclease-free water, omitting template.
3. Distribute 249 µL of the master mix per tube, then add 1 µL of the appropriate 10 ng/µL gBlock template to each (final reaction 250 µL). Composition in {numref}`tbl-composition-pcr`.
4. Run PCR (30 cycles): 30 s initial denaturation, then cycle through 10 s denaturation, 30 s annealing at 64 °C, and 45 s extension; finish with a 120 s final extension.
5. Clean up PCR products (NEB Monarch, T1130L). All samples were eluted in 30 µL across two 15 µL cleanups, each yielding ~200 ng/µL.

::::{admonition} Reaction composition
:class: dropdown

:::{table} PCR reaction composition.
:label: tbl-composition-pcr
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | EsaO-mNG [µL] | [EsaO]2-mNG [µL] | EsaO-PLA1 [µL] | [EsaO]2-PLA1 [µL] | EsaR [µL] | mNG [µL] | PLA1 [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q5 High-Fidelity Master Mix | 2 | × | 1 | × | 125 | 125 | 125 | 125 | 125 | 125 | 125 |
| M13 Fwd primer | 100 | µM | 0.5 | µM | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 |
| M13 Rev primer | 100 | µM | 0.5 | µM | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 | 1.25 |
| Template (gBlock) | 10 | ng/µL | 0.04 | ng/µL | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Nuclease-free water | — | — | — | — | 121.5 | 121.5 | 121.5 | 121.5 | 121.5 | 121.5 | 121.5 |
| Total | | | | | 250 | 250 | 250 | 250 | 250 | 250 | 250 |
:::
::::
:::{div .dashed-hr}
:::

### Pre-expressing EsaR(D91G)

EsaR(D91G) is pre-expressed in a cell-free reaction containing the standard cytosol mastermix and EsaR(D91G) template DNA at a final concentration of 10 ng/µL (≈12 nM). The composition below is given per 10 µL; reactions were scaled up as needed for the day's total reaction volume and number of conditions.

::::{admonition} Reaction composition
:class: dropdown

:::{table} EsaR(D91G) pre-expression reaction, per 10 µL.
:label: tbl-composition-esar-preexpression
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume [µL] |
| --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 3 |
| tRNA | 10 | × | 1 | × | 1 |
| Protein mix | 8.33 | × | 1 | × | 1.2 |
| Ribosomes | 5.5 | × | 1 | × | 1.8 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.25 |
| EsaR(D91G) Template DNA | X | ng/µL | 10 | ng/µL | X |
| Nuclease-free water | — | — | — | — | X |
| Total | | | | | 10 |
:::
::::
:::{div .dashed-hr}
:::

### Base Nucleus cytosol protocol for sensor optimisation

Sensor optimisation reactions across all experiments in this DevNote shared a common base assembly:

1. Pre-express EsaR(D91G) in Nucleus cytosol as described above. Composition in {numref}`tbl-composition-esar-preexpression`.
2. Mix the pre-expressed EsaR with the sensor DNA and incubate for 15 min or 1 hr at 37 °C.

   :::{note}
   Volumes for pre-incubation can be calculated from each reaction composition as the sum of pre-expressed EsaR and sensor DNA. Typically, excess was prepared for each condition to ensure there was sufficient volume remaining post-incubation.
   :::
3. While the EsaR–DNA mixture incubates, prepare a mastermix of Nucleus cytosol, without DNA or water.
4. Add the premix to the Nucleus cytosol mastermix. Note: some conditions may require the premix to be topped-up with water prior to its addition.
5. Add AHSL (final 5 µM), either:
   - as a dedicated component pipetted directly into the mastermix at assembly (water in its place for the −AHSL condition), or
   - by splitting the fully assembled reaction in half and adding AHSL to one half.
6. Distribute in triplicate 10 µL volumes into a 384-well plate.
7. Read on a platereader (GFP, 37 °C, 6 hr timecourse).
:::{div .dashed-hr}
:::

*The following sections state how each experiment deviates from the above base protocol and include a reaction composition and platemap*

### EsaR titration into Nucleus cytosol reactions containing EsaO-mNG and [EsaO]2-mNG DNA

Deviates from the base protocol:
- Step 2: EsaR titrated across 0, 1, 4 or 7 µL per reaction, against a fixed 320.5 ng (12 nM) of either T7-\[EsaO\]-mNG-T7term or T7-\[EsaO\]2-mNG-t7term.
- Reaction scaled to 65 µL total.
- Step 5: AHSL added by splitting.

Reaction composition is in {numref}`tbl-composition-20260924`.

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
| Sensor DNA Template | 200 | ng/µL | 10 | ng/µL | 1.54 | 2.87 | 2.87 | 2.87 | 2.87 | 3.25 | 3.25 | 3.25 | 3.25 |
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

:::{div .dashed-hr}
:::

### Titrating EsaO-mNG and [EsaO]2-mNG DNA against fixed pre-expressed EsaR

Deviates from the base protocol:
- Step 2: pre-expressed EsaR fixed at 14 µL; sensor DNA titrated across 0.1–9 nM for each of T7-\[EsaO\]-mNG-T7term and T7-\[EsaO\]2-mNG-t7term.
- Reaction scaled to 65 µL total.
- Step 5: AHSL added by splitting.

Full reaction composition is in {numref}`tbl-composition-20260925`.

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
| Sensor DNA Template | 10 / 10 / 150 / 150 / 150 / 150 | ng/µL | 0.1 / 0.5 / 1 / 3 / 6 / 9 | nM | 1.54 | 0.44 | 2.12 | 0.28 | 0.85 | 1.69 | 2.46 | 0.43 | 2.16 | 0.29 | 0.86 | 1.73 | 2.59 |
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
:::{div .dashed-hr}
:::

### Comparing unspent and spent pre-expressed EsaR added to [EsaO]2-mNG DNA reactions

Deviates from the base protocol:
- Step 1: EsaR instead pre-expressed for 17 hrs at 30 °C and held at 4 °C (rather than the standard 3 hrs at 37 °C).
- Step 2: pre-expressed EsaR fixed at 14 µL; sensor DNA titrated across 0.1, 0.5 and 1 nM of T7-\[EsaO\]2-mNG-t7term only.
- Reaction scaled to 70 µL total.
- Step 5: AHSL added by splitting.

Full reaction composition is in {numref}`tbl-composition-20260926`.

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
| Sensor DNA Template | 10 / 50 / 100 | ng/µL | 0.1 / 0.5 / 1 | nM | 1.66 | 0.46 | 0.46 | 0.46 |
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
:::{div .dashed-hr}
:::

### Effect of additional Mg on EsaR-dependent repression of [EsaO]2-mNG DNA

Deviates from the base protocol:
- Step 2: incubated for 1 hr instead of 15 min, with 0, 5, 10 or 20 mM Mg²⁺ added during this step.
- Step 5: AHSL pipetted directly into the mastermix as a dedicated component, not via splitting.
- Step 6: distributed in duplicate instead of triplicate.

Sensor DNA was provided so that the concentration in the final reaction was 0.5 nM. Composition in {numref}`tbl-composition-20261001`.

::::{admonition} Reaction composition
:class: dropdown

:::{table} Reaction composition.
:label: tbl-composition-20261001
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | 0 mM Mg [µL] | 5 mM Mg [µL] | 10 mM Mg [µL] | 20 mM Mg [µL] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 3 | 3 | 3 | 3 |
| tRNA | 10 | × | 1 | × | 1 | 1 | 1 | 1 |
| Protein mix | 8.33 | × | 1 | × | 1.2 | 1.2 | 1.2 | 1.2 |
| Ribosomes | 5.5 | × | 1 | × | 1.8 | 1.8 | 1.8 | 1.8 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.25 | 0.25 | 0.25 | 0.25 |
| Sensor DNA Template | 22 | ng/µL | 0.5 | nM | 0.15 | 0.15 | 0.15 | 0.15 |
| Pre-expressed EsaR | — | — | — | — | 2.3 | 2.3 | 2.3 | 2.3 |
| Magnesium | — / 86.6 / 173.3 / 346.7 | mM | — / 5 / 10 / 20 | mM | 0 | 0.15 | 0.15 | 0.15 |
| Water (replacing Mg stock) | — | — | — | — | 0.15 | 0 | 0 | 0 |
| AHSL | — | — | 0 / 5 | µM | 0.15 | 0.15 | 0.15 | 0.15 |
| Total | | | | | 10 | 10 | 10 | 10 |
:::
::::

::::{admonition} Platemap
:class: dropdown

:::{platemap} ./experiments/20261001-mg-osmo-sweep/20261001-mg-sweep-platemap.csv
:height: 480px
:label: platemap-20261001
:::
::::
:::{div .dashed-hr}
:::

### Effect of increasing EsaR DNA concentration on [EsaO]2-mNG DNA repression

Deviates from the base protocol:
- Step 2: the DNA added to the reaction is sensor DNA (4 ng/µL) diluted 1:1, either with water (−EsaR DNA) or with a 213 ng/µL EsaR template DNA stock (+EsaR DNA). This keeps the final sensor DNA concentration at 0.1 nM while increasing the EsaR template DNA concentration from 3.4 nM to 8.7 nM. This increases the EsaR template excess from 34× to 87×.
- Step 5: AHSL pipetted directly into the mastermix as a dedicated component, not via splitting.

Reaction composition is in {numref}`tbl-composition-20261007`.

::::{admonition} Reaction composition
:class: dropdown

:::{table} Reaction composition.
:label: tbl-composition-20261007
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | − EsaR DNA [µL] | + EsaR DNA (8.7 nM) [µL] |
| --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 3 | 3 |
| tRNA | 10 | × | 1 | × | 1 | 1 |
| Protein mix | 8.33 | × | 1 | × | 1.2 | 1.2 |
| Ribosomes | 5.5 | × | 1 | × | 1.8 | 1.8 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.25 | 0.25 |
| Pre-expressed EsaR (template DNA carryover) | 15 | nM DNA | 3.4 | nM DNA | 2.27 | 2.27 |
| Sensor DNA ([EsaO]2-mNG) | 4 | ng/µL | 0.1 | nM | 0.165 | 0.165 |
| Added EsaR template | — / 320 | nM DNA | — / 5.3 | nM DNA | 0 | 0.165 |
| Water (replacing EsaR template) | — | — | — | — | 0.165 | 0 |
| AHSL | — | — | 0 / 5 | µM | 0.15 | 0.15 |
| Total | | | | | 10 | 10 |
:::
::::

::::{admonition} Platemap
:class: dropdown

:::{platemap} ./experiments/20261007-esar-template-competition/20261008-esao-mng-esar-ahsl.csv
:height: 480px
:fields: [EsaO-mNG] (nM), [EsaR] (nM), [AHSL] (uM)
:label: platemap-20261007
:::
::::
:::{div .dashed-hr}
:::

### Effect of lower reaction temperature on EsaR-dependent repression of [EsaO]2-mNG DNA

Deviates from the base protocol:
- Step 2: incubated for 1 hr instead of 15 min at 37 °C.
- Step 7: rather than the standard 3 hr incubation at 37 °C, reactions were instead incubated overnight at 25 °C and read the following day.
- Step 5: AHSL pipetted directly into the mastermix as a dedicated component, not via splitting.

Sensor DNA was provided so that the concentration in the final reaction was 0.1 nM. Reaction composition is in {numref}`tbl-composition-20261008`.

::::{admonition} Reaction composition
:class: dropdown

:::{table} Reaction composition.
:label: tbl-composition-20261008
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | − EsaR [µL] | + EsaR [µL] |
| --- | --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 3 | 3 |
| tRNA | 10 | × | 1 | × | 1 | 1 |
| Protein mix | 8.33 | × | 1 | × | 1.2 | 1.2 |
| Ribosomes | 5.5 | × | 1 | × | 1.8 | 1.8 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.25 | 0.25 |
| Sensor DNA Template ([EsaO]2-mNG) | 4 | ng/µL | 0.1 | nM | 0.15 | 0.15 |
| Pre-expressed EsaR | — | — | — | — | 0 | 2.45 |
| Water (replacing EsaR) | — | — | — | — | 2.45 | 0 |
| AHSL | — | — | 0 / 5 | µM | 0.15 | 0.15 |
| Total | | | | | 10 | 10 |
:::
::::

:::{div .dashed-hr}
:::

### Testing EsaR-dependent repression of [EsaO]2-mNG DNA in GUVs
:::{note}
 GUV synthesis follows the base protocol's early steps: pre-express EsaR, then incubate it with sensor DNA, before following its own procedure from there.
:::

**Stock preparation**

**Outer solution** is prepared by diluting a 2 M glucose stock with water to 1050 mM. *Ideally, this concentration would instead be matched to the osmolarity of the inner solution using an osmometer.* Dilution in {numref}`tbl-composition-outer`.

**AHSL** is dissolved directly in DMSO in the stock bottle to 50 mM. This is diluted to a 500 µM working solution using outer solution as the diluent and stored at −20 °C. Fresh working solutions are prepared every week.Dilution in {numref}`tbl-composition-ahsl`.

::::{admonition} Dilution tables
:class: dropdown

:::{table} Outer solution, per 10 mL prepared.
:label: tbl-composition-outer
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume per 10 mL [mL] |
| --- | --- | --- | --- | --- | --- |
| Glucose | 2 | M | 1050 | mM | 5.25 |
| Water | — | — | — | — | 4.75 |
| Total | | | | | 10 |
:::

:::{table} AHSL working solution, per 1 mL prepared, using the outer solution above as diluent.
:label: tbl-composition-ahsl
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume per 1 mL [µL] |
| --- | --- | --- | --- | --- | --- |
| AHSL | 50 | mM | 500 | µM | 10 |
| Outer solution (diluent) | 1050 | mM | 1039.5 | mM | 990 |
| Total | | | | | 1000 |
:::
::::

**EsaR-DNA mixture**

1. Pre-express EsaR(D91G) in a cell-free reaction at 24 nM template DNA, double the standard 12 nM, giving a final concentration of 5 nM in the GUV reaction. Composition in {numref}`tbl-volumes-20261009-esar`.
2. Incubate the pre-expressed EsaR with sensor DNA ([EsaO]2-mNG) for 1 hr at 37 °C to form the EsaR-DNA mixture.

**Emulsion phase transfer**

1. Dry 2 mg POPC under nitrogen, then under vacuum for at least 2 hours.
2. Resuspend the dried lipid film in 500 µL mineral oil (4 mg / mL).
3. Sonicate the lipid-in-oil mixture at room temperature for ~20 min.
4. Prepare the GUV inner solution in duplicate (2 × 20 µL), identical in both, including the EsaR-DNA mixture (above) in each. AHSL is not part of either inner solution — it is added at step 9. Composition per 20 µL prep in {numref}`tbl-volumes-20261009-guv`.
5. Add 200 µL of the lipid-in-oil mixture onto each inner solution and pipette up and down 9 times to form a water-in-oil emulsion.
6. Add each emulsion onto 250 µL outer solution (1050 mM glucose — ideally osmotically matched to the inner solution).
7. Centrifuge at 15 °C, 9,000 g, for 20 min to form GUVs.
8. Resuspend the resulting pellet in 100 µL outer solution.
9. For each condition:
   - **−AHSL**: add 1 µL outer solution to 99 µL GUV solution.
   - **+AHSL**: add 1 µL AHSL (500 µM) to 99 µL GUV solution.
10. Distribute in triplicate 30 µL vols in 384-well glass-bottom plate.
11. Image for 6 hrs at 37 °C.

::::{admonition} Reaction composition
:class: dropdown

:::{table} EsaR pre-expression reaction.
:label: tbl-volumes-20261009-esar
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume [µL] |
| --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 3 |
| tRNA | 10 | × | 1 | × | 1 |
| Protein mix | 8.33 | × | 1 | × | 1.2 |
| Ribosomes | 5.5 | × | 1 | × | 1.8 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.25 |
| EsaR DNA Template | 320 | nM DNA | 24 | nM DNA | 0.75 |
| Water | — | — | — | — | 1.85 |
| AHSL | — | — | — | — | 0.15 |
| Total | | | | | 10 |
:::

:::{table} GUV inner solution
:label: tbl-volumes-20261009-guv
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume [µL] |
| --- | --- | --- | --- | --- | --- |
| Small molecule mix | 3.33 | × | 1 | × | 6 |
| tRNA | 10 | × | 1 | × | 2 |
| Protein mix | 8.33 | × | 1 | × | 2.4 |
| Ribosomes | 5.5 | × | 1 | × | 3.6 |
| RNase inhibitor | 40 | U/µL | 1 | U/µL | 0.5 |
| Pre-expressed EsaR reaction | 24 | nM DNA | 5 | nM DNA | 4.17 |
| Sensor DNA ([EsaO]2-mNG) | 4 | ng/µL | 0.1 | nM | 0.33 |
| Optiprep | — | — | — | — | 1 |
| Total | | | | | 20 |
:::
::::

---

# Results

:::{note}
The following data were collected by the authors during an intense 3-week collaboration at DevStudio held at Nucleus labs at b.next, San Francisco. To learn more about this collaboration see [here](https://devnotes.nucleus.engineering/articles/devstudio/week2). Whilst many experiments contain n=3 technical replicates, there was insufficient time to perform biological replicates across different days. Further work is planned to support the reproducibility of these results. 
:::

## EsaR titration fails to repress EsaO-mNG at 12 nM DNA

To determine the ratio of pre-expressed EsaR repressor to sensor DNA constructs that gives a well-defined ‘on’/’off’ state, we titrated increasing amounts of pre-expressed EsaR protein into Nucleus cytosol reactions containing single-operator EsaO-mNG or dual-operator [EsaO]2-mNG constructs. The sensor DNA was held at 12.2 nM (10 ng/µL) in all reactions. Each reaction was split, with AHSL added to one half to a final concentration of 5 µM.

No difference between the ‘on’ and ‘off’ states was observed at any EsaR volume tested ({numref}`fig-20260924-esao-titration`). Note that 7 µL is the highest achievable amount of EsaR that could be added without affecting the stoichiometry of Nucleus cytosol. This suggests either that the pre-expressed EsaR was non-functional, or that the sensor DNA remained in excess even at the highest EsaR-to-DNA ratio tested.

:::{figure} #fig-20260924-esao
:label: fig-20260924-esao-titration
:align: center
:width: 75%
Single-operator EsaO-mNG and dual-operator [EsaO]2-mNG with 0 and 7 µL pre-expressed EsaR, minus and plus 5 µM AHSL (n = 3 replicate wells; shaded region shows standard deviation). Reaction composition is in {numref}`tbl-composition-20260924`.
:::

## Repression scales with the EsaR : sensor DNA ratio

To test whether the sensor DNA templates had previously been in excess, we titrated the sensor DNA concentration while holding pre-expressed EsaR at the highest achievable concentration in each reaction. Repression was observed at concentrations lower than 1 nM DNA. At 0.1 nM and 0.5 nM, the single-operator construct gave fold-changes of approximately 1.5 and 1 respectively, while the dual-operator construct gave approximately 2 and 1.6 (Figure {numref}`%s <fig-20260925-0p1nm>`–{numref}`%s <fig-20260925-fold>`). At both concentrations, the dual-operator [EsaO]2-mNG construct showed higher fold-induction than the single-operator EsaO-mNG, consistent with the tighter repression expected from the additional EsaO operator. This suggests that the repressor behaviour exhibited *in vivo* may translate to PURE systems such as Nucleus cytosol.

Additionally, we noticed that the mNG control present at 15.6 nM was matched or exceeded in fluorescence signal by sensor DNA at 0.5 nM and upwards ({numref}`%s <fig-20260925-0p5nm>`–{numref}`%s <fig-20260925-3nm>`). This was surprising as the sensor DNA was 5- to 30-fold lower in concentration. We hypothesise this may be due to the pre-expressed EsaR preparation carrying over unspent energy components as well as transcription and translation factors that may supply additional capacity to the reaction. 

:::::{tab-set}

::::{tab-item} 0.1 nM DNA
:::{figure} #cn-20260925-fig1
:label: fig-20260925-0p1nm
:align: center
:width: 75%
0.1 nM sensor DNA at 7 µL pre-expressed EsaR and 5 µM AHSL, single operator against dual operator, alongside the mNG control (15.63 nM) (n = 3; shaded region shows standard deviation). Reaction composition is in {numref}`tbl-composition-20260925`.
:::

::::

::::{tab-item} 0.5 nM DNA
:::{figure} #cn-20260925-fig2
:label: fig-20260925-0p5nm
:align: center
:width: 75%
0.5 nM sensor DNA at 7 µL pre-expressed EsaR and 5 µM AHSL, single operator against dual operator, alongside the mNG control (15.63 nM). Replicate wells are drawn individually rather than as a mean. Reaction composition is in {numref}`tbl-composition-20260925`.
:::

::::

::::{tab-item} 1 nM DNA
:::{figure} #cn-20260925-fig3
:label: fig-20260925-1nm
:align: center
:width: 75%
1 nM sensor DNA at 7 µL pre-expressed EsaR and 5 µM AHSL, single operator against dual operator, alongside the mNG control (15.63 nM) (n = 3; shaded region shows standard deviation). Reaction composition is in {numref}`tbl-composition-20260925`.
:::

::::

::::{tab-item} 3 nM DNA
:::{figure} #cn-20260925-fig4
:label: fig-20260925-3nm
:align: center
:width: 75%
3 nM sensor DNA at 7 µL pre-expressed EsaR and 5 µM AHSL, single operator against dual operator, alongside the mNG control (15.63 nM) (n = 3; shaded region shows standard deviation). Reaction composition is in {numref}`tbl-composition-20260925`.
:::

::::

::::{tab-item} Fold induction
:::{figure} #cn-20260925-fig5
:label: fig-20260925-fold
:align: center
:width: 75%
Steady-state AHSL fold induction (+AHSL / −AHSL) for EsaO-mNG and [EsaO]2-mNG at 0.1, 0.5, 1 and 3 nM sensor DNA (n = 3; n = 2 at 0.5 nM after excluding one low-outlier +AHSL well per construct; error bars show standard deviation).
:::

::::

:::::

## Prolonged EsaR pre-expression doesn't improve repression but reduces yield

To test whether pre-expressing EsaR for longer increases the amount of repressor available and improves repression, we pre-expressed EsaR at 30 °C for 17 hrs instead of 37 °C for 3 hrs. EsaR volumes added to Nucleus cytosol reactions containing sensor DNA matched the previous experiment, and sensor DNA was limited to 0.1 nM, 0.5 nM and 1 nM. Data was compared to previous experiments in which EsaR was pre-expressed at 37 ˚C for 3 hrs. To ensure an accurate comparison, all data was first normalized to an internal 0.5 µM fluorescein control, before a second normalization step to a constitutive [EsaO]2-mNG without EsaR. This accounted for any batch-to-batch variations in Nucleus cytosol yields.

The fold-change between ‘on’ and ‘off’ states remained consistent at each DNA concentration ({numref}`fig-20260926-fold`), so extending pre-expression didn't improve repression. We did notice, however, that overall fluorescent yield decreased across all conditions when EsaR was pre-expressed at 30 ˚C for 17 hrs ({numref}`fig-20260926-endpoint`). We hypothesise that byproducts accumulating during the extended pre-expression, such as inorganic phosphate, may lower the yield of the subsequent reaction. Subsequent experiments maintained the pre-expression at 37 ˚C for 3 hrs; however, it is possible that a pre-expression period between 3–17 hrs is more optimal. Despite this, we don't expect the gains to be substantial as Nucleus cytosol reactions typically reach their steady-state by 3 hrs.

:::::{tab-set}

::::{tab-item} Timecourse
:::{figure} #cn-20260926-fig1
:label: fig-20260926-normalized
:align: center
:width: 100%
Time-course fluorescence for dual-operator [EsaO]2-mNG, comparing EsaR pre-expressed for 3 hours at 37 °C against 17 hours at 30 °C. Fluorescence is calibrated to fluorescein and batch-corrected to the mNG control. Sensor DNA was tested at 0.1, 0.5 and 1 nM, with and without 5 µM AHSL. The mNG control is used only for the batch correction and is not plotted. Shaded regions show standard deviation across three replicate wells. Reaction composition is in {numref}`tbl-composition-20260926`.
:::

::::

::::{tab-item} Fold change (- AHSL / + AHSL)
:::{figure} #cn-20260926-fig2
:label: fig-20260926-fold
:align: center
:width: 55%
Fold-induction for [EsaO]2-mNG, comparing EsaR pre-expressed for 17 hours at 30 °C against 3 hours at 37 °C. Fluorescence is calibrated to 0.5 µM fluorescein. Sensor DNA was tested at 0.1, 0.5 and 1 nM. Error bars show standard deviation across three replicate wells, except at 1 nM for the 30 °C preparation and 0.5 nM for the 37 °C preparation. At each of these two conditions, one low-outlier +AHSL well was excluded, leaving two replicates.
:::

::::

::::{tab-item} End-point
:::{figure} #cn-20260926-fig3
:label: fig-20260926-endpoint
:align: center
:width: 55%
End-point fluorescence for [EsaO]2-mNG, comparing EsaR pre-expressed for 17 hours at 30 °C against 3 hours at 37 °C. Fluorescence is calibrated to fluorescein and batch-corrected to the mNG control. Sensor DNA was tested at 0.1, 0.5 and 1 nM. Error bars show standard deviation across three replicate wells, except at 1 nM for the 30 °C preparation and 0.5 nM for the 37 °C preparation. At each of these two conditions, the same low-outlier +AHSL well excluded in {numref}`fig-20260926-fold` was excluded here too, leaving two replicates.
:::

::::

:::::

## Magnesium doesn't improve dynamic range but longer pre-incubation does

With the assumption that additional Mg²⁺ could improve EsaR–DNA binding, we next tested whether supplementing the EsaR–DNA pre-incubation with magnesium could strengthen repression. Sensor DNA and EsaR were pre-incubated together with 0, 5, 10 or 20 mM additional Mg²⁺. Contrary to previous experiments, incubation time was increased from 15 minutes to 1 hour at 37 °C. Pre-incubations were then added to the final cytosol reaction.

Magnesium did not alter the dynamic range at any concentration tested ({numref}`fig-20261001-mg-sweep`), and 20 mM markedly reduced overall yield. The longer pre-incubation, however, improved the switch from two-fold induction with the standard 15-minute pre-incubation to approximately three-fold across all conditions tested, with individual replicates reaching as high as four-fold ({numref}`fig-20261001-mg-sweep-fold`).

:::::{tab-set}

::::{tab-item} Timecourse
:::{figure} #mbcn-20261001-fig1
:label: fig-20261001-mg-sweep
:align: center
:width: 100%
Time-course fluorescence for [EsaO]2-mNG, with 0, 5 or 10 mM additional magnesium added during the EsaR–DNA pre-incubation. Reactions were prepared with and without 5 µM AHSL (n = 2). Reaction composition is in {numref}`tbl-composition-20261001`.
:::

::::

::::{tab-item} Fold change
:::{figure} #mbcn-20261001-fig2
:label: fig-20261001-mg-sweep-fold
:align: center
:width: 55%
Fold-induction for [EsaO]2-mNG at 0, 5 and 10 mM magnesium, after pre-incubating EsaR with the DNA for 1 hour at 37 °C. Error bars show standard deviation across two replicate wells.
:::

::::

:::::

## EsaR DNA template competition improves sensor dynamic range but reduces yield

Thus far, any EsaR template present in the final cytosol reaction was carryover from the initial EsaR pre-expression. This gave a final concentration of ~3.4 nM, a 34-fold excess over the 0.1 nM sensor DNA. To further deepen the 'off' state, 5.3 nM EsaR template was added by diluting the sensor DNA stock in EsaR template rather than water. This brought the total EsaR template in the final reaction to 8.7 nM, an 87-fold excess over the sensor DNA. This served two purposes. It increased the overall amount of EsaR available to repress the sensor DNA, and it continuously diverted Nucleus cytosol resources away from sensor DNA expression.

As expected, expressing additional EsaR reduced overall fluorescence yield roughly four-fold ({numref}`fig-20261007-normalized`). This came with an improved dynamic range, rising from 2.8 without added EsaR template to a reliable 4-fold change with it ({numref}`fig-20261007-fold`).

:::::{tab-set}

::::{tab-item} Timecourse
:::{figure} #mbcn-20261007-fig1
:label: fig-20261007-normalized
:align: center
:width: 100%
Time-course fluorescence for EsaO-mNG at 0.1 nM, with and without 8.7 nM added EsaR DNA template, each with and without AHSL (n = 3). Fluorescence is raw RFU. Reaction composition is in {numref}`tbl-composition-20261007`.
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

## Lower reaction temperatures increase sensor dynamic range

To test whether lower reaction temperatures could both stabilise EsaR-DNA binding, and slow T7 kinetics to limit EsaR being knocked off the sensor DNA, reactions were incubated at 25 ˚C overnight rather than 37 ˚C for 3 hrs. Ideally, this would reduce expression from sensor DNA that was insufficiently repressed. 

Reactions were incubated overnight in a thermocycler and measured on a platereader the following day. The highest fold change across all experiments was recorded at ~ 5.8. This suggests that temperature plays an important role in repression within the system. Timecourse reactions should be recorded in future to understand this in more detail.

:::{figure} #mbcn-20261008-fig1
:label: fig-20261008-overnight
:align: center
:width: 55%
Background-corrected GFP fluorescence for 0.1 nM [EsaO]2-mNG DNA after overnight incubation at 25 °C. Reactions were run with and without 5 µM AHSL. Reaction composition is in {numref}`tbl-composition-20261008`.
:::

## Developer cells encapsulating sensor DNA detect AHSL in solution

To take a step towards producing a functional developer cell that can sense bacteria through the detection of secreted AHSL, GUVs were prepared encapsulating Nucleus cytosol, 5 nM EsaR template, and 0.1 nM sensor DNA. Note the EsaR template was present at a final concentration of 5 nM by increasing the EsaR template in the pre-expression reaction to 24 nM. This method of preparation had not previously been tested in bulk Nucleus cytosol; that characterisation will be done in future. GUVs samples were split, with 5 µM AHSL added to one half. Samples were loaded in a 384-well plate and imaged for 6 hrs at 37˚C. 

Images show the final timepoint for all conditions collected on a Cephla microscope. Each image was processed in Python using matplotlib applying a consistent vmin/vmax across all wells. GUVs in the + AHSL conditions are markedly brighter than the - AHSL conditions, demonstrating that GUV-encapsulated sensor DNA detects AHSL in solution and derepresses mNG production.

:::{figure} #microscopy-exp-01
:label: fig-20261009-guv-ahsl
:align: center
:width: 100%
Dual-operator [EsaO]2-mNG encapsulated in GUVs with pre-expressed EsaR, three replicate wells each minus and plus 5 µM AHSL. Green LUT, vmin/vmax 1200:4500, 20 µm scale bar. Reaction composition is in {numref}`tbl-volumes-20261009-esar` and {numref}`tbl-volumes-20261009-guv`.
:::

---

# What's next

- Engineer the {ref}`EsaR(D91G) construct <seq-esar-d91g>` for increased yield. Modify the
  5' UTR sequence and codon optimise to maximise the amount of protein
  produced.
- Test whether it is possible to increase repression by adding a
  third EsaO box to the sensor DNA. 
- Furthermore, search the literature / perform random mutagenesis to determine
  whether EsaO mutations can promote increased EsaR binding.
- Purchase recombinantly purified EsaR protein (available from [Cusabio](https://www.cusabio.com/Recombinant-Protein/Recombinant-Transcriptional-activator-protein-esaR--esaR--12936539.html)). Add
  purified EsaR to cytosol reactions containing sensor DNA in >100x excess in
  an attempt to achieve maximal gene repression. Test in bulk reactions first
  and then in GUVs.
- Once optimised, test sensor DNA in the [London Node: colour-change module](:https://devnotes.nucleus.engineering/articles/01a12e6c-b511-7d30-aa95-002d386f751e) to produce a visual rather than fluorescence-based readout.

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
