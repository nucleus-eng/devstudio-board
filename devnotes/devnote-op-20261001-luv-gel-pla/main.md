<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

<!-- This page stays close to `log-devnote-draft.docx`, read on 2026-10-09.
`main-supplement.md` holds the full analysis chain for `OP-20261001`,
every disagreement found between sources, and the review cycle v1
history, so that page and this one do not restate each other. Title and
authors live in `curvenote.yml`, per convention, and are not repeated
here. -->

# Module overview

1. T7 GFP yield in different gels
2. Dyed-loaded vesicles in different gels

# Open questions

1. Are LUVs leaky?
2. Can PLA lyse?
3. Do only the gels lyse?

:::{figure} ./general/schematic-hydrogel-overview.png
:label: fig-schematic-hydrogel-overview
:align: center
:width: 75%
Hydrogel containing unilamellar vesicles.
:::

[`fig-schematic-hydrogel-overview`, file:`general/schematic-hydrogel-overview.png`, caption: (Hydrogel containing unilamellar vesicles.)]

# Methods

## Vesicle preparation

### LUVs

**Hydration**

1. Hydrate a dried, under nitrogen atmosphere, dry POPC lipid film (~2
   mg) in buffer containing glucose, 50 mM HEPES and 15 v/v% Optiprep, at
   a final osmolarity of 1200 mOsm. The buffer contains 15 mg/mL CPRG.
2. Vortex, then sonicate for 15 min at room temperature.
3. Apply 5 freeze-thaw cycles, liquid nitrogen, then thaw in a
   room-temperature water bath.

**Clean-up by centrifugation**

1. Split the mixture into 5 tubes, each with 200 µL vesicles and 1 mL
   outer solution, glucose and 50 mM HEPES, 1200 mOsm.
2. Spin at 15,000 g for 15 min at room temperature.
3. Resuspend the pellet in outer solution and wash again by pelleting at
   the same settings.
4. Repeat until the outer solution of the pellet looks clear, 2 to 4
   washes.

:::{figure} ./general/schematic-luv-prep-inline.png
:label: fig-schematic-luv-prep-inline
:align: center
:width: 40%
[Caption]
:::

[`fig-schematic-luv-prep-inline`, file:`general/schematic-luv-prep-inline.png`, caption: ([Caption])]

<!-- The caption above is "[Caption]" because the source leaves it
unfilled. Carried as-is, not invented. -->

### GUVs

**Lipid-in-oil mixture**

1. Resuspend a dried, under nitrogen atmosphere, POPC film (~2 mg) in
   500 µL mineral oil, and dry under vacuum for ~2 hours.
2. Sonicate for ~20 min at 30 °C.

**Inner solution**

- 20 µL Nucleus cytosol with 5 v/v% Optiprep and 10 ng/mL DNA at either
  T7-EsaO-mNG or T7-EsaO-PLA1.

**Outer solution**

- Glucose and 50 mM HEPES, 1200 mOsm.

**Emulsion and transfer**

1. Pipette 20 µL cytosol reaction into 200 µL lipid-in-oil mixture.
2. Pipette up and down 9 times to form a water-in-oil emulsion.
3. Layer the emulsion onto ~250 µL outer solution, glucose and 50 mM
   HEPES, 1200 mOsm.
4. Centrifuge for 20 min at 9,000 g.
5. Gently remove the oil and most of the outer solution.
6. Resuspend the GUV pellet in outer solution or in a solution of
   dye-loaded LUVs.

## Hydrogel preparation

Three hydrogels were prepared and plated using inputs shared across the
London and Chicago nodes.

:::{table} Gel types and crosslinking behavior
:label: tbl-gel-types

| Gel | Type | Crosslinking behavior |
| --- | --- | --- |
| ULGA, ultra-low gelling agarose | Physical | Thermogelling, gelling ~8 to 15 °C |
| LGA, low gelling agarose | Physical | Thermogelling, gelling ~24 to 28 °C |
| PEG4Nb, 4-arm PEG-norbornene | Photocrosslinked | Crosslinks on light exposure |
:::

### ULGA (1 w/v%)

1. Prepare ULGA at 1 w/v% in 1.2 M glucose solution. Formulation
   reference: [insert link].
2. Microwave in 10 s bursts, 5 to 7 times, until fully dissolved.
3. Keep on the 55 °C bead bath until use.

### LGA (2.8 w/v%)

1. Prepare LGA at 2.8 w/v% in 1.2 M glucose solution.
2. Heat in the 95 °C heat block until fully dissolved, vortexing
   occasionally.
3. Keep an aliquot in an Eppendorf tube at 45 °C.
4. Prepare vesicles in the sonicator bath and do the transfer there.

### PEG4Nb (80 mM)

:::{table} PEG4Nb gel reagents
:label: tbl-peg4nb-reagents-doc

| Reagent | Product Name | Conc. | Molecular weight | Storage Conditions | Supplier |
| --- | --- | --- | --- | --- | --- |
| PEG4Nb | 4-Arm-PEG-Norbornene | 80 mM | 5000 Da | freezer at -20 °C in the dark | Creative Pegworks |
| PEG-4SH crosslinker | 4-Arm PEG-Thiol | 20 mM | 2000 Da | freezer at -20 °C in the dark | Creative Pegworks |
| LAP photoinitiator | Lithium phenyl-2,4,6-trimethylbenzoylphosphinate | 16.9 mM | 294.21 g/mol | 2-8 °C, in the dark, photosensitive | |
| Glucose and 50 mM HEPES buffer | | 1 ml | | 4 °C | |
| DLP projectors | | | | | Zwants Supplies Engineering (PRO4500-92-405) |
:::

<!-- This table keeps the source document's own six-column schema:
Reagent, Product Name, Conc., Molecular weight, Storage Conditions,
Supplier. It is not the DevNote's standard seven-column reagents schema.
The standard-schema version is in main-supplement.md, under
tbl-reagents. -->

# Experimental design

We selected 2: GFP GUVs and LUVs.

- Gel conditions (4): pre-PEG4Nb gel solution, PEG4Nb gel, ULGA gel, LGA
  gel.
- Controls: one gel-only control per gel condition, pre-PEG4Nb, PEG4Nb,
  ULGA, LGA, and vesicles in outer solution, OS.

:::{table} Experimental design
:label: tbl-experimental-design

| | Outer solution | PEG4Nb pre-gel | PEG4Nb gel | ULGA | LGA |
| --- | --- | --- | --- | --- | --- |
| GFP-GUVs | | | | | |
| GFP-GUVs + LUVs | | | | | |
| PLA-GUVs + LUVs | | | | | |
| LUVs only | | | | | |
| Control | Outer solution only | Pre-gel only | Gel only | Gel only | Gel only |
:::

Vesicles in outer solution only, no gel, serve as the reference control.

Mix 15 µL vesicle solution with 15 µL gel stock, then plate 30 µL per
well. Plate all samples in duplicate.

:::{table} Stock and final gel concentration
:label: tbl-stock-final-conc

| Gel | Stock conc. | Final gel conc. |
| --- | --- | --- |
| ULGA | 1 w/v% | 0.5 w/v% |
| LGA | 2.8 w/v% | 0.7 w/v% (7.5 µL + 7.5 µL OS) |
| PEG4Nb | 80 mM | 40 mM |
:::

Buffer osmolarity: 1200 mOsm.

[Paste the graph here]

[link to dataset URL here; .txt of matlab code in directory; caption]

<!-- The two lines above are unfilled placeholders in the source,
left as the source has them. -->

Plate map: `1BI0gXBY33WXuJZO19aqzrlLL2ofd9EROV2j-iSKzwsE`.

<!-- Written as a plain identifier, not a link. Drive URLs are not
written as hyperlink hrefs here; see main-supplement.md's Resources for
why. -->

# Results

1. Plate reader data

LUVs are most stable in PEG gels.

:::{figure} ./figures/log-devnote-draft-luv-only-read2.jpg
:label: fig-luv-only-read2
:align: center
:width: 75%
LUV behaviour in hydrogels, Read 2, 3:09 PM, 16 U/mL LacZ. Absorbance
A570/A412, CPR/CPRG, for LUV only, across five conditions: pre-PEG
solution, PEG gel, ULGA, LGA, and in solution.
:::

[`fig-luv-only-read2`, notebook:`none`, platemap:`none`, data source:`none`, caption: (LUV behaviour in hydrogels, Read 2, 3:09 PM, 16 U/mL LacZ.)]

2. Microscopy data

Pics of PLA-lysed vesicles.

<!-- No microscopy image is in the source for this item. Not invented
here. -->

# Discussion

1. GFP expression in all 3 gels.
2. PLA lyses the vesicles in all gels.

# Conclusion

[PLEASE FILL IN]

<!-- The source Conclusion heading carries no text. -->

# Resources

The full asset chain, the review cycle history, and every flagged
disagreement between sources are in `main-supplement.md`.
