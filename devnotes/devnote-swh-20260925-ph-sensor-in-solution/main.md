<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

# Overview

The pH-sensing developer cells detect acidic conditions (pH 6.0–6.5) using a pH-responsive ssDNA system. Acidification releases a trigger ssDNA, which activates a toehold switch RNA and induces expression of the protein of interest. To generate a visible colorimetric output, a two-vesicle population system is used. Upon sensing acidic pH, the sensor cells express phospholipase A1 (PLA1), which disrupts neighboring CPRG-loaded vesicles and releases CPRG into the surrounding solution. External β-galactosidase then converts the yellow CPRG substrate into purple CPR, producing a visible color change.

:::{figure} /figures/thumbnail.png
This DevNote describes a two-vesicle system that changes visible color in response to pH.
:::

<!-- :::{danger} Unresolved before publication
:name: flags-blocking

**Date.** The Log folder is `SWH-20260924-pHsensor-in solution`. Every dated asset inside it carries `20260925`: the platemap, its provenance sidecar, the build sheet titled `260925 384 square plate map`, the `Date` column of all nine rows, and all four microscopy stores. This DevNote is slugged `20260925` on that evidence. Confirm the folder name is the error, not the assets.

**Lipid volume.** `[confirm]-PLA1-GUV-composition` sums to 2.5 µmol of lipid and its own cells state 5 mL at 0.5 mM, which agrees. Its Total note still reads "dried and taken up in 3 mL mineral oil to 0.5 mM lipid-in-oil". At 3 mL that is 1.5 µmol. The note is carried verbatim below and is not corrected.

**Sequences.** The two gate oligos are now inline in {numref}`tbl-constructs` and both verified against their `LOCUS` line. `pT7-toehold9-PLA1 DNA template` still has no sequence and no file.

**Construct identity.** `pT7-toehold9-PLA1 DNA template` carries the source note "sequence file not verified" and was not checked by length against a GenBank `LOCUS` line.
:::

:::{admonition} Open review items
:class: warning dropdown
:name: flags-review

**Five of nine wells have no recorded outcome.** The log reports `D4`, `D5`, `E4` and `E5` only. `F4`, `F5`, `G4`, `G5` and `H4` are retained in {numref}`tbl-conditions` marked "no", so the entire CPRG-LUV-only control arm is unreported.

**The GUV dose is not matched between sample and control.** Rows `E` and `F` take 3 µL of PLA1-GUVs; row `D`, the GUV-only control, takes 1 µL. Row `D` therefore does not isolate the effect of the CPRG-LUVs. The CPRG-LUV dose is matched at 2.1 µL.

**`H4` receives no pH buffer.** It takes 0 µL of the energy solution mix, and that mix carries the pH-setting buffer. Its recorded pH of 7.6 comes from the build sheet's column header, not from anything added to the well.

**The PLA1 construct is recorded as leaky.** `DevCell_Materials_Tracker.xlsx` lists the function test for `T7-toehol9-PLA1` as "Done/Leaky". The pH 7.6 arm is the condition leakiness would contaminate.

**The recipe's magnesium salt is not the stocked one.** The energy solution calls for magnesium acetate tetrahydrate, Millipore Sigma `M5661`. The tracker stocks magnesium glutamate and no magnesium acetate at either node.

**Notebooks not inspected.** `microscopy.ipynb` and `platereader.ipynb` are in the Log folder but exceed what the Drive connector can return. No figure here depends on a notebook.

**Composition source.** No `build-composition.csv` sidecar exists for this Log folder. Composition comes from the four `[confirm]`-prefixed Sheets, not reconstructed from log prose.

**Compartment vocabulary.** The outer solution source uses `OS-pH 7.6`, `OS-pH 6.3` and `Buffer mix for pH 6.3` rather than `IS`, `MB`, `OS`. Values are carried as written.

**"Energy solution" names two things.** In the build sheet it is the 52.8 µL mix. In the composition sheet it is the neat 30 µL component of that mix. Both meanings are kept distinct below.

**`E5` store name.** `SH-0925-E5-2` carries a `-2` suffix the other three do not.
::: -->

# Reagents

:::{table} Reagents and equipment. Vendor data for the energy solution components comes from the composition sheet; the remaining entries were matched against `DevCell_Materials_Tracker.xlsx`, which carries no manufacturer, price or storage columns.
:label: tbl-reagents
:align: center

| Reagent | Product Name | Manufacturer | Catalog No. | Price | Storage Conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| Spermidine | — | Millipore Sigma | S2626 | — | — | |
| Creatine phosphate | — | Millipore Sigma | 10621714001 | — | — | |
| Magnesium acetate tetrahydrate | — | Millipore Sigma | M5661 | — | — | |
| L-Glutamic acid potassium salt monohydrate | Potassium glutamate | Millipore Sigma | G1501 | — | — | |
| Folinic acid calcium salt hydrate | — | Millipore Sigma | F7878 | — | — | |
| ATP | — | Millipore Sigma | A6419-1G or 5G | — | — | |
| GTP | — | Millipore Sigma | G8877-250MG | — | — | |
| CTP | — | Millipore Sigma | C1506-250MG | — | — | |
| UTP | — | Millipore Sigma | U6750-1G or 500MG | — | — | |
| Amino acid mix (RTS Amino Acid Sampler) | — | Biotechrabbit | BR1401801 | — | — | |
| RNase Inhibitor | RNAse inhibitor murine | NEB | M0314S | $87.00 | -25 °C to -15 °C | [link](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| Mineral oil | Mineral oil | — | M5904 or M5310 | — | — | |
| Cy5 | Sulfo-Cyanine5 carboxylic acid | — | — | — | — | |
| CPRG | Chlorophenol Red-β-D-galactopyranoside | — | — | — | — | |
| POPC | 16:0-18:1 PC (POPC) | Avanti Lipids | A80557 | $435.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Rhod PE | Liss Rhod PE | Avanti Lipids | A81179 | $273.47 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/810179-180-liss-rhod-pe) |
| Cholesterol | Cholesterol | Avanti Research | A80100 | $261.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/700100-cholesterol-plant) |
| IDT duplex buffer | Nuclease Free Duplex Buffer | — | — | — | — | |
| UPDI (water) | — | — | — | — | — | |
| Optiprep | OptiPrep™ | STEMCELL Technologies | 07820 | $289.00 | RT | [link](https://www.stemcell.com/products/optipreptm.html) |
| SMix | — | — | — | — | — | |
| PMix | — | — | — | — | — | |
| Ribosomes | — | — | — | — | — | |
| tRNA | — | — | — | — | — | |
| Tris base | — | — | — | — | — | |
| HEPES | — | — | — | — | — | |
| HCl | — | — | — | — | — | |
:::

Two entries are ambiguous rather than missing. The tracker stocks two mineral oils, `M5904` and `M5310`, with a note that `M5310` is the higher quality one, and does not say which went into the lipid-in-oil. It also stocks two Cy5 materials, `Sulfo-Cyanine5 carboxylic acid` and the lipid-conjugated `18:1 Cyanine 5 PC`; the 100 µM soluble stock used here points at the first.

# Constructs

:::{table} DNA constructs. Sequences are reproduced in full; both oligo lengths were verified against their GenBank `LOCUS` line.
:label: tbl-constructs
:align: center

| Name | Sequence | Purpose |
| --- | --- | --- |
| pT7-toehold9-PLA1 DNA template | [PLEASE FILL IN] | DNA template for PLA1 expression in the GUV inner solution. 80 nM stock, 2 nM final. Source note: "sequence file not verified". |
| [pH-responsive_ssDNA#2](./dna/ph-responsive-ssdna2.gb) | TTCTCTTCTCGTTTGCTCTTCTCTTGTGTGGTATTGTCCAAGAGAAGAG | pH-responsive strand of the gate, 49 bp. |
| [Trigger_ssDNA#3](./dna/trigger-ssdna3.gb) | TATGCAAACAAGACAATACCACACAATTTTTTTTTT | Trigger strand, 36 bp. |
:::

The last two anneal 3:1 in IDT duplex buffer to form the construct listed as `pH-responsive:Trigger ssDNA (3:1) annealed construct` in {numref}`tbl-pla1-guv-is`, where the 25 µM stock concentration is that of the trigger strand. Both files verified: `pH-responsive_ssDNA#2` declares 49 bp and carries 49 bases, `Trigger_ssDNA#3` declares 36 bp and carries 36 bases.

The `seqviz` plugin exists at `plugins/seqviz/` in this repository but is not wired into any project, so these are linked as files rather than embedded viewers.

# Protocol

[PLEASE FILL IN]

# Methods

## Conditions

384-well square plate, nine wells, 60 µL each. The pH 7.6 arm is plate column 4, the pH 6.3 arm is plate column 5, and `H5` is empty in the build sheet, which is why one arm has five wells and the other four. The vesicle slot is a constant 7.2 µL on every well except `H4`: outer solution plus PLA1-GUV plus CPRG-LUV sums to 7.2 on rows `D`, `E`, `F` and `G`.

:::{table} Plate conditions. Per-component concentrations are in {numref}`tbl-pla1-guv-is`, {numref}`tbl-cprg-luv-is` and {numref}`tbl-outer-solution`. The full platemap is [`experiments/20260925-ph-lysis-cascade.csv`](./experiments/20260925-ph-lysis-cascade.csv).
:label: tbl-conditions
:align: center

| Well | Name | Type | pH | Energy solution mix (µL) | Outer solution (µL) | PLA1-GUV (µL) | CPRG-LUV (µL) | Total (µL) | Result recorded |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D4 | pH 7.6, PLA1-GUV only | Control | 7.6 | 52.8 | 6.2 | 1 | 0 | 60 | yes |
| D5 | pH 6.3, PLA1-GUV only | Control | 6.3 | 52.8 | 6.2 | 1 | 0 | 60 | yes |
| E4 | pH 7.6, PLA1-GUV + CPRG-LUV | Sample | 7.6 | 52.8 | 2.1 | 3 | 2.1 | 60 | yes |
| E5 | pH 6.3, PLA1-GUV + CPRG-LUV | Sample | 6.3 | 52.8 | 2.1 | 3 | 2.1 | 60 | yes |
| F4 | pH 7.6, PLA1-GUV + CPRG-LUV | Sample | 7.6 | 52.8 | 2.1 | 3 | 2.1 | 60 | no |
| F5 | pH 6.3, PLA1-GUV + CPRG-LUV | Sample | 6.3 | 52.8 | 2.1 | 3 | 2.1 | 60 | no |
| G4 | pH 7.6, CPRG-LUV only | Control | 7.6 | 52.8 | 5.1 | 0 | 2.1 | 60 | no |
| G5 | pH 6.3, CPRG-LUV only | Control | 6.3 | 52.8 | 5.1 | 0 | 2.1 | 60 | no |
| H4 | pH 7.6 arm, PLA1-GUV, no energy solution mix | Control | 7.6 | 0 | 59 | 1 | 0 | 60 | no |
:::

## PLA1-expressing GUVs

:::::{tab-set}
::::{tab-item} Inner solution
:sync: is

:::{table} PLA1-GUV inner solution.
:label: tbl-pla1-guv-is
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume (µL) | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| SMix | 3.33 | × | 1 | × | 6 | |
| PMix | 15 | mg/mL | 1.80 | mg/mL | 2.4 | |
| Ribosomes | 10 | µM | 1.8 | µM | 3.6 | |
| tRNA | 35 | mg/mL | 3.5 | mg/mL | 2 | |
| pT7-toehold9-PLA1 DNA template | 80 | nM | 2 | nM | 0.5 | sequence file not verified |
| pH-responsive:Trigger ssDNA (3:1) annealed construct | 25 | µM | 4.625 | µM | 3.7 | stock conc. is of the trigger ssDNA; annealed in IDT duplex buffer |
| Optiprep | 100 | % | 4.5 | v/v% | 0.9 | |
| RNase Inhibitor | 40000 | U/mL | 1000 | U/mL | 0.5 | |
| Cy5 | 100 | µM | 2 | µM | 0.4 | |
| Total | — | — | — | — | 20 | |
:::
::::

::::{tab-item} Membrane
:sync: mb

:::{table} PLA1-GUV membrane. Volumes are for the lipid-in-oil stock, not per well.
:label: tbl-pla1-guv-mb
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume (µL) | Moles (µmol) | MW (g/mol) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| POPC | 25 | mg/mL | 89.9 | mol% | 68.3308324 | 2.2475 | 760.076 |
| Cholesterol | 50 | mg/mL | 10 | mol% | 1.9333 | 0.25 | 386.66 |
| Rhod PE | 1 | mg/mL | 0.1 | mol% | 3.2542875 | 0.0025 | 1301.715 |
| Total | — | — | 100 | mol% | — | 2.5 | — |
:::

Source note, carried verbatim: "dried and taken up in 3 mL mineral oil to 0.5 mM lipid-in-oil". See the blocking flags at the top of this page — the sheet's own cells say 5 mL, which is what 2.5 µmol at 0.5 mM requires.
::::
:::::

## CPRG-loaded LUVs

:::::{tab-set}
::::{tab-item} Inner solution
:sync: is

:::{table} CPRG-LUV inner solution.
:label: tbl-cprg-luv-is
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume (µL) |
| --- | --- | --- | --- | --- | --- |
| CPRG | 30 | mg/mL | 14.25 | mg/mL | 237.5 |
| Optiprep | 100 | v/v% | 10 | v/v% | 50 |
| Tris1M-HEPES1.15M buffer (~2520 mOsm) | 2520 | mOsm | 1071 | mOsm | 212.5 |
| Total | — | — | — | — | 500 |
:::
::::

::::{tab-item} Membrane
:sync: mb

:::{table} CPRG-LUV membrane. Volumes are for the lipid stock, not per well.
:label: tbl-cprg-luv-mb
:align: center

| Component | Stock Conc. | Unit | Final Conc. | Unit | Volume (µL) | Moles (µmol) | MW (g/mol) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| POPC | 25 | mg/mL | 89.9 | mol% | 54.66466592 | 1.798 | 760.076 |
| Cholesterol | 50 | mg/mL | 10 | mol% | 1.54664 | 0.2 | 386.66 |
| Rhod-PE | 1 | mg/mL | 0.1 | mol% | 2.60343 | 0.002 | 1301.715 |
| Total | — | — | 100 | mol% | — | 2 | — |
:::

2 µmol in 0.5 mL at 4 mM.
::::
:::::

Both populations carry the same membrane, 89.9 / 10 / 0.1 mol% POPC, cholesterol and Rhod-PE, so the Rhodamine channel does not distinguish them. Cy5 is in the PLA1-GUV inner solution only.

## Outer solution

The whole 60 µL well. The first three rows are the 52.8 µL the build sheet records as one number under "Energy Solution". The fourth row is the 7.2 µL vesicle slot, which {numref}`tbl-conditions` splits into outer solution, PLA1-GUV and CPRG-LUV. The pH 7.6 arm takes the Tris-HEPES buffer stock directly; the pH 6.3 arm takes a separate buffer mix.

:::{table} Outer solution, both pH arms. Full recipe including the pH 6.3 buffer mix: [`experiments/outer-solution-composition.csv`](./experiments/outer-solution-composition.csv).
:label: tbl-outer-solution
:align: center

| Component | pH 7.6 volume (µL) | pH 6.3 volume (µL) | Final Conc. | Unit |
| --- | --- | --- | --- | --- |
| Energy solution | 30 | 30 | 50 | v/v% |
| Ultra-pure distilled water | 15.6 | 15.6 | 26 | v/v% |
| Tris1M-HEPES1.15M buffer stock (~2520 mOsm) | 7.2 | — | 12 | v/v% |
| Buffer mix for pH 6.3 | — | 7.2 | 12 | v/v% |
| Vesicles in 46.67% Tris1M-HEPES1.15M (1170–1180 mOsm) | 7.2 | 7.2 | 12 | v/v% |
| Total | 60 | 60 | 100 | % |
:::

The energy solution is a 2× sub-mix of ten components per Sun et al. 2013, made up to 4000 µL. It is not reproduced here: [`experiments/energy-solution-composition.csv`](./experiments/energy-solution-composition.csv), and its vendor data is in {numref}`tbl-reagents`.

## Microscopy

Two channels were acquired. The channel labelled `Alexa Fluor 647` in the acquisition metadata reports the Cy5 signal, because the microscope names the wavelength by a representative fluorophore; the reagent in the composition is Cy5. The channel labelled `Rhodamine` reports Rhod-PE in the vesicle membranes. Data are OME-Zarr version 0.5, one well per store, with a z-stack at 1.5 µm spacing and 0.333 µm pixels.

# Results

[PLEASE FILL IN]

:::{figure} ./figures/microscopy-summary.png
:label: fig-microscopy-summary
:align: center
:width: 100%
The four reported wells at 13 h: D4 and D5 across the top, E4 and E5 across the bottom, Rhodamine and Alexa Fluor 647 merged. This static montage is the archival record of the four interactive viewers below, which do not survive JATS conversion.
:::

The viewer control panels are visible in the capture above. <!-- REVIEW: recapture without the overlay before publication -->

:::{figure} ./figures/color-change-with-lacz.png
:label: fig-color-change
:align: center
:width: 40%
[PLEASE FILL IN]
:::

<!-- REVIEW: this photograph shows a yellow well beside a purple one, the CPRG to CPR conversion. Nothing in the source log records it. Which wells, which plate and which date are unrecorded, and the caption must not be written until they are. -->

The four viewers below are stacked rather than tabbed. The Vizarr widget creates its viewer on a detached element with no width and never re-measures, so any instance that is hidden when the page mounts renders blank permanently.

## D4 — pH 7.6, PLA1-GUV only

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/SH-0925-D4_2026-09-25_11-27-49.059491.zarr/D/4/0",
    "height": "600px"
}
:::

PLA1-expressing synthetic cells at pH 7.6 after 13 h at 37 °C. Cy5 signal is retained inside the vesicles, indicating that membrane integrity was preserved and PLA1 activity did not cause dye leakage. Vesicle membranes are labeled with Rhod-PE.

## D5 — pH 6.3, PLA1-GUV only

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/SH-0925-D5_2026-09-25_11-32-48.009691.zarr/D/5/0",
    "height": "600px"
}
:::

PLA1-expressing synthetic cells at pH 6.3 after 13 h at 37 °C. Cy5 signal is absent, indicating that acidic conditions triggered PLA1 expression, which disrupted the vesicle membrane and released the encapsulated dye.

## E4 — pH 7.6, PLA1-GUV + CPRG-LUV

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/SH-0925-E4_2026-09-25_12-03-09.447054.zarr/E/4/0",
    "height": "600px"
}
:::

CPRG-loaded vesicles co-incubated with PLA1-expressing synthetic cells at pH 7.6 after 13 h at 37 °C. Cy5 signal is detected only in the PLA1-expressing synthetic cells.

## E5 — pH 6.3, PLA1-GUV + CPRG-LUV

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/SH-0925-E5-2_2026-09-25_12-04-22.672843.zarr/E/5/0",
    "height": "600px"
}
:::

CPRG-loaded vesicles co-incubated with PLA1-expressing synthetic cells at pH 6.3 after 13 h at 37 °C. Cy5 signal is detected only in the PLA1-expressing synthetic cells. The fraction of vesicles retaining Cy5 is markedly reduced compared with E4, indicating PLA1-mediated Cy5 release.

# Notes

Here no gramicidin is used

# What's next

[PLEASE FILL IN]

# Resources

- Platemap: [`experiments/20260925-ph-lysis-cascade.csv`](./experiments/20260925-ph-lysis-cascade.csv)
- Outer solution recipe: [`experiments/outer-solution-composition.csv`](./experiments/outer-solution-composition.csv)
- Energy solution recipe: [`experiments/energy-solution-composition.csv`](./experiments/energy-solution-composition.csv)
- DevNote(G) draft and comment thread: [main](https://docs.google.com/document/d/1f4rQCJdwHtDht3kGLfpVGrbQVsZVtNWFGH3SfVIQ1Hs/edit)
