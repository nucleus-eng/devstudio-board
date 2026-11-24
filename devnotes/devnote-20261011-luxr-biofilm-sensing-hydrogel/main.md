---
title: 'Bacterial Sensing in Hydrogel Embedded Synthetic Cells using LuxR Dependent Transcriptional Regulation'
thumbnail: ./figures/fov-c4.png
---

# Overview

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

:::{figure} ./general/overview.png
:label: fig-overview-schematic
:align: center
:width: 90%
Bacterial supernatant carrying 3-oxo-C6-HSL diffuses into the LuxR-mNeonGreen
GUV hydrogel. Inside one GUV, constitutively expressed LuxR binds 3-oxo-C6-HSL
and activates pLux, driving mNeonGreen expression. The inset shows the
phospholipid bilayer HSL crosses to enter the GUV.
:::

# Constructs

:::{table}
:label: tbl-constructs
:align: center

| Name | Sequence | Purpose |
| --- | --- | --- |
| [pUC-IDT-LuxR-mNG](./dna/pUC-IDT-LuxR-mNG.gbk) | [Sequence map below](#seqviz-constructs) | BBa_J23101 (constitutive) drives LuxR; LuxR drives pLux; pLux drives mNeonGreen. The sensor construct for every Result. pUC-IDT-AMP GoldenGate backbone, 4671 bp. |
| [pUC-IDT-constitutive_mNG](./dna/pUC-IDT-constitutive_mNG.gbk) | [Sequence map below](#seqviz-constructs) | BBa_J23101 drives mNeonGreen directly, no LuxR and no pLux. Constitutive expression control. pUC-IDT-AMP GoldenGate backbone, 3689 bp. |
:::

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

# Results

## Result 1 — LuxR-mNeonGreen sensor plasmid in bulk lysate

To verify whether *E. coli* lysate and the LuxR-mNeonGreen plasmid can detect
3-oxo-C6-HSL in bulk, a 12.5 µL bulk lysate fluorescence assay was conducted
in 384 well plates. The LuxR-mNeonGreen plasmid constitutively expresses the
LuxR transcription factor in *E. coli* lysate, which is activated by the HSL
signal. Upon activation, LuxR dimerizes, enabling it to bind to the Lux box
situated adjacent to the RNA polymerase promoter sequence. The activated LuxR
recruits the σ70 subunit of RNA polymerase, activating transcription. The
constitutive mNeonGreen plasmid does not contain the Lux box, so RNA
polymerase does not require activated LuxR for protein expression.

Similar cell-free biosensors for bacterial detection using quorum sensing
have been developed in lysate-based systems with the LasR transcription
factor and 3-oxo-C12-HSL quorum sensor
([10.1021/acssynbio.7b00219](https://doi.org/10.1021/acssynbio.7b00219)).

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

:::{figure} ./figures/result1-bulk-lysate-platereader.png
:label: fig-result1-platereader
:align: center
:width: 85%
Fluorescence intensity over time for the LuxR-mNeonGreen plasmid in bulk
lysate reactions with and without 10 µM HSL, and for the constitutive
mNeonGreen plasmid. + 10 µM and − 10 µM HSL refer to the HSL sensing and
negative control conditions in {numref}`tbl-bulk-lysate-conditions`.
:::

## Result 2 — detecting purified HSL using lysate-based synthetic cells

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
([10.1002/syst.202300029](https://doi.org/10.1002/syst.202300029)).
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

:::{figure} ./figures/solution-wells.png
:label: fig-solution-wells
:align: center
Left to right: J4 (HSL sensing GUVs, LuxR-mNeonGreen, 10 µM HSL in outer
solution), J7 (negative control, LuxR-mNeonGreen, outer solution), J10
(constitutive control, constitutive mNeonGreen, outer solution). Images were
acquired every 20 minutes across 17 time points, in the store
[`Lysate_LuxR_Cytosol_EsaR_2026-10-05_18-59-02.423661.zarr`](https://data.nucleus.engineering/microscopy/nucleus-bnext-01/Lysate_LuxR_Cytosol_EsaR_2026-10-05_18-59-02.423661.zarr),
plate map
[`20261005-solution-hsl-platemap.csv`](./experiments/20261005-solution-hsl-platemap.csv).
T = 17 (endpoint), GFP channel only, center crop, about one field of view,
for each well.
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

:::{table} Gel conditions, synthetic cells, HSL. Triplicates for each experiment; empty ULGA gels included to account for light scattering from vesicles.
:label: tbl-gel-conditions
:align: center

| Condition | Plasmid | Well |
| --- | --- | --- |
| HSL sensing gels | LuxR-mNeonGreen | D6, D7, D8 |
| Negative control gels | LuxR-mNeonGreen | D3, D4, D5 |
| Constitutive control gels | Constitutive mNeonGreen | D9, D10, D11 |
| Empty ULGA gels | N/A | D15, D16, D17 |
:::

:::{figure} ./figures/gel-wells.png
:label: fig-gel-wells
:align: center
Left to right: D6 (HSL sensing gels, LuxR-mNeonGreen, +100 µM AHL; the
triplicate well, D7, has its own
[interactive viewer](./2026-10-07-interactive-viewer.md#d7-hsl-sensing-gels)),
D5 (negative control gels, LuxR-mNeonGreen, no AHL; the triplicate well, D4,
has its own
[interactive viewer](./2026-10-07-interactive-viewer.md#d4-negative-control-gels)),
D11 (constitutive control gels, Constitutive mNeonGreen; the triplicate
well, D10, has its own
[interactive viewer](./2026-10-07-interactive-viewer.md#d10-constitutive-control-gels)).
z = 50 of 101, GFP channel only, contrast windowed 4526 to 12204, center
crop, about one field of view, for each well.
:::

The empty ULGA gels condition (D15, D16, D17) has no figure of its own, but
each of its three wells has its own interactive viewer:
[D15](./2026-10-07-interactive-viewer.md#d15-empty-ulga-gel),
[D16](./2026-10-07-interactive-viewer.md#d16-empty-ulga-gel),
[D17](./2026-10-07-interactive-viewer.md#d17-empty-ulga-gel).

## Result 3 — detecting bacterially produced HSL in solution

To model bacterial sensing using GUVs, the LuxI plasmid was transformed into
NEB5α *E. coli* (NEB5α w/ LuxI) to encode production of 3-oxo-C6-HSL, the
small-molecule quorum sensor detected in the previous sections. The same
LuxR-mNeonGreen plasmid was used to verify whether lysate-based synthetic
cells are capable of detecting bacterially produced HSL, implemented through
resuspending the GUV pellet in bacterial supernatant. Control experiments
were performed with the NEB5α strain without the LuxI plasmid (NEB5α ΔLuxI),
which removes HSL from the supernatant.

:::{table} Three experimental conditions for HSL-induced mNeonGreen expression using bacterial supernatant in solution.
:label: tbl-supernatant-conditions
:align: center

| Condition | Plasmid | Supernatant used |
| --- | --- | --- |
| HSL sensing GUVs | LuxR-mNeonGreen | NEB5α w/ LuxI |
| Negative control | LuxR-mNeonGreen | NEB5α ΔLuxI |
| Constitutive control | Constitutive mNeonGreen | NEB5α ΔLuxI |
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

Supernatant from NEB5α carrying the LuxI plasmid induced mNeonGreen expression
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
significantly more HSL is produced by overnight inoculation of NEB5α w/ LuxI
than the 10 µM purified HSL used in {numref}`tbl-solution-conditions`. Future
work should include supernatant in the bulk lysate assays
({numref}`fig-result1-platereader`), with supernatant extracted at various
time points.

Synthetic cells carrying the constitutive mNeonGreen plasmid in NEB5α ΔLuxI
supernatant expressed after about 40 minutes, with expression increasing over
the experiment (wells C9 to C11). The faster expression compared to
LuxR-mNeonGreen follows from synthesizing one protein only, with no
dependency on HSL entering the cell and activating mNeonGreen expression.

The three conditions are shown as interactive viewers, one well per
condition, on
[2026-10-08 — Interactive viewer](./2026-10-08-interactive-viewer.md).

:::{figure} ./figures/fov-wells.png
:label: fig-fov-wells
:align: center
Left to right: C4 (HSL sensing GUVs, LuxR-mNeonGreen, NEB5α w/ LuxI
supernatant; has its own
[interactive viewer](./2026-10-08-interactive-viewer.md#c4-hsl-sensing-guvs)),
C7 (negative control, LuxR-mNeonGreen, NEB5α ΔLuxI supernatant, carried as
imaged, near-empty as expected for this control; has its own
[interactive viewer](./2026-10-08-interactive-viewer.md#c7-negative-control)),
C10 (constitutive control, constitutive mNeonGreen, NEB5α ΔLuxI
supernatant; has its own
[interactive viewer](./2026-10-08-interactive-viewer.md#c10-constitutive-control)).
T = 19, GFP channel only, contrast windowed 30000 to 60000, 659 µm field of
view, each panel cropped and zoomed to the same Vizarr view state.
:::

(sec-methods)=
# Methods

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

Inoculate 5 mL LB (ampicillin) with the NEB5α strain carrying the LuxI
producing plasmid. Incubate overnight at 37 °C. Centrifuge for 15 minutes.
Pipette the supernatant into a separate tube. Sterile filter the supernatant
with a 0.22 µm filter. Store at −20 °C until use.

# Summary

1. *E. coli* lysate-based cell-free protein expression with the
   LuxR-mNeonGreen plasmid can successfully detect 3-oxo-C6-HSL in bulk.
2. The same system can be successfully encapsulated in synthetic cells, which
   is activated with 10 µM purified HSL in solution, visible using
   fluorescence microscopy.
3. Lysate-containing synthetic cells encapsulated within ULGA hydrogels can
   sense 100 µM HSL added to the top of the gels.
4. Bacterial supernatant collected from *E. coli* containing the LuxI
   plasmid induced GFP expression in lysate GUVs containing the
   LuxR-mNeonGreen plasmid.

# What's next

1. Test bacterial supernatant with lysate GUVs embedded in agarose hydrogel.
2. Test orthogonal sensing with 3-oxo-C6-HSL and 3-oxo-C12-HSL quorum sensors
   using LuxR and LasR to regulate transcriptional regulation.
3. Investigate whether the LuxR system can be used for visible colorimetric
   detection of bacterial contamination, through encapsulation of a
   substrate and expression of an enzyme.
4. Perform tests around the mechanical stability of GUVs embedded in
   hydrogel.
