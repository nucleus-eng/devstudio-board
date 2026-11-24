---
title: 'Understanding Liposome Behaviour in Hydrogel Matrices'
---

# Abstract

Vesicle-based synthetic cells and cell-free expression systems have so far been
characterized almost exclusively in bulk solution. Whether vesicles remain
stable and biochemically functional when embedded in a hydrogel, where they are
mechanically confined and in contact with a crosslinked polymer network, is
largely unexplored. This module addresses that gap and examines how hydrogel
formation and fabrication govern the integration of synthetic cells into soft
materials.

# Overview

We assessed vesicle functionality in hydrogels through two complementary
readouts: (i) quantification of T7-driven GFP expression yield in giant
unilamellar vesicles (GUVs), and (ii) release of encapsulated dye, Chlorophenol
red-β-D-galactopyranoside (CPRG) from large unilamellar vesicles (LUVs),
monitored in a panel of chemically and mechanically distinct hydrogels alongside
a solution control. Comparing across gel types allowed us to separate the
effects of network chemistry, stiffness, and mesh size on vesicle behavior.

:::{figure} ./general/schematic-hydrogel-overview.png
:label: fig-schematic-hydrogel-overview
:align: center
:width: 75%
Schematic representation of unilamellar vesicles contained in a hydrogel matrix.
:::

# Methods

## Vesicle preparation

::::{dropdown} LUVs

**Hydration**

1. Hydrate a dried POPC lipid film (~2 mg) in buffer containing glucose,
   50 mM HEPES, and 15 v/v% Optiprep, at a final osmolarity of 1200 mOsm. The
   buffer contains 15 mg/mL CPRG. The lipid film was dried under a nitrogen
   atmosphere and then dried under vacuum for ~2 hours before hydration.
2. Vortex, then sonicate for 15 min at room temperature.
3. Apply 5 freeze-thaw cycles, liquid nitrogen, then thaw in a
   room-temperature water bath.

**Clean-up by centrifugation**

1. Split the mixture into 5 tubes, each with 200 µL vesicles and 1 mL outer
   solution, glucose and 50 mM HEPES, at a final osmolarity of 1200 mOsm.
2. Spin at 15 000 g for 15 min at room temperature.
3. Resuspend the pellet in outer solution and wash again by pelleting at the
   same settings.
4. Repeat until the outer solution of the pellet looks clear, 2 to 4 washes.

:::{figure} ./general/photo-luv-pellet.png
:label: fig-photo-luv-pellet
:align: center
:width: 40%
Snapshot of the LUV pellet after 4 washes.
:::

::::

::::{dropdown} GUVs

**Lipid-in-oil mixture**

1. Resuspend a dried POPC film (~2 mg) in 500 µL mineral oil. The lipid film
   was dried under a nitrogen atmosphere and then dried under vacuum for
   ~2 hours before adding mineral oil.
2. Sonicate for ~20 min at 30 °C.

**Inner solution**

- 20 µL Nucleus cytosol with 5 v/v% Optiprep and 10 ng/mL DNA at either
  T7-EsaO-mNG or T7-EsaO-PLA1.

**Outer solution**

- Glucose and 50 mM HEPES, at a final osmolarity of ~1200 mOsm.

**Emulsion and transfer**

1. Pipette 20 µL cytosol reaction into 200 µL lipid-in-oil mixture.
2. Pipette up and down ~10 times to form a water-in-oil emulsion.
3. Layer the emulsion onto ~250 µL outer solution.
4. Centrifuge for 20 min at 9000 g at room temperature.
5. Gently remove the oil and most of the outer solution.
6. Resuspend the GUV pellet in outer solution or in a solution of dye-loaded
   LUVs.

::::

## Hydrogel preparation

Three hydrogels were prepared and plated using inputs shared across the London
and Chicago nodes.

:::{table} Overview of the different hydrogels used and description of their gelling behaviour
:label: tbl-gel-types

| Gel | Type | Crosslinking behaviour |
| --- | --- | --- |
| ULGA, ultra-low gelling agarose | Physical | Thermogelling, gelling ~8 to 15 °C |
| LGA, low gelling agarose | Physical | Thermogelling, gelling ~24 to 28 °C |
| PEG4Nb, 4-arm PEG-norbornene | Photocrosslinked | Crosslinks on light exposure |
:::

:::::{tab-set}

::::{tab-item} ULGA (1 w/v%)
:sync: ulga

1. Prepare ULGA at 1 w/v% in the outer solution used during vesicle preparation, that is, glucose and 50 mM HEPES, at a final osmolarity of \~1200 mOsm.
2. Microwave in 10 s bursts, 5 to 7 times, until fully dissolved.
3. Keep in the 55 °C bead bath until use.
4. Mix the ULGA solution with the vesicles at 55 °C, then dispense the mixture into a well plate to form a gel.&#x20;

::::

::::{tab-item} LGA (2.8 w/v%)
:sync: lga

1. Dissolve LGA at 2.8 w/v% in the outer solution used for vesicle preparation, glucose, and 50 mM HEPES, adjusting to a final osmolarity of \~1200 mOsm.
2. Heat the solution in a 95 °C heat block until fully dissolved, vortexing occasionally to facilitate dissolution.
3. Transfer an aliquot to an Eppendorf tube and maintain at 45 °C until use. Since LGA can undergo thermogelation at room temperature, keeping it warm prevents premature gelation during mixing.
4. Mix the LGA solution with the vesicles at 45 °C, then dispense the mixture into a well plate to form a gel.

::::

::::{tab-item} PEG4Nb (80 mM)
:sync: peg4nb

1. Prepare a precursor solution using the concentrations in {numref}`tbl-peg4nb-reagents-doc`. Briefly, dissolve 80 mM PEG4Nb, 20 mM PEG-4SH at a 1:1 stoichiometric ratio with PEG4Nb, and 16.9 mM LAP in 1 mL of PBS. You can even use DI water or any buffer. This is a photosensitive reaction, so prepare the precursor solution in a dark room and wrap the vial with foil for storage.
2. Vortex the solution at 2000 rpm for 1 min, then keep at RT for 3 to 5 min.
3. Vortex again for 2 to 4 min and ensure all the chemicals are dissolved well. Repeat this part until a clear solution is obtained.
4. Put the desired volume in a 96-well plate and photopattern for exactly 60 s at 405 nm using DLP projectors. If needed, you can also do a 1:1 dilution in the well, for example, 50 µL of precursor gel solution and 50 µL PBS in 1 well.

:::{figure} ./general/photo-photopatterning-peg4nb.jpg
:label: fig-photo-photopatterning-peg4nb
:align: center
:width: 45%
Photopatterning PEG4Nb hydrogels in a 96-well plate.
:::

\[`fig-photo-photopatterning-peg4nb`, file:`general/photo-photopatterning-peg4nb.jpg`, caption: (Photopatterning PEG4Nb hydrogels in a 96-well plate.)]

:::{table} Reagents used in the synthesis of PEG4Nb hydrogels
:label: tbl-peg4nb-reagents-doc

| Reagent                                    | Product Name                                     | Conc.   | Molecular weight | Storage Conditions                     | Supplier                                     |
| ------------------------------------------ | ------------------------------------------------ | ------- | ---------------- | -------------------------------------- | -------------------------------------------- |
| PEG4Nb                                     | 4-Arm-PEG-Norbornene                             | 80 mM   | 5000 Da          | freezer at -20 °C in the dark          | Creative Pegworks                            |
| PEG-4SH crosslinker                        | 4-Arm PEG-Thiol                                  | 20 mM   | 2000 Da          | freezer at -20 °C in the dark          | Creative Pegworks                            |
| LAP photoinitiator                         | Lithium phenyl-2,4,6-trimethylbenzoylphosphinate | 16.9 mM | 294.21 g/mol     | 2 to 8 °C, in the dark, photosensitive | Sigma-Aldrich                                |
| glucose in 50 mM HEPES buffer (\~1200 Osm) | —                                                | 1 mL    | —                | 4 °C                                   | Sigma-Aldrich                                |
| DLP projectors                             | —                                                | —       | —                | —                                      | Zwants Supplies Engineering (PRO4500-92-405) |
:::

::::

:::::

# Experimental design

Two vesicle conditions were tested, each in solution and in three hydrogels:

1. **CPRG-loaded LUVs and β-galactosidase enzyme**

:::{figure} ./general/diagram-cprg-cpr-reaction.png
:label: fig-diagram-cprg-cpr-reaction
:align: center
:width: 85%
CPRG is cleaved by β-galactosidase to CPR and galactose. CPRG is the substrate
and is initially yellow. CPR is the coloured product, red to pink-purple
depending on conditions.
:::

**Plating conditions**

- Vesicles in outer solution only, no gel, serve as the reference control.
- Mixed 15 µL vesicle solution with 15 µL gel stock (or 7.5 µL in the case of LGA), then plated 30 µL per well. Plated all samples in duplicate.

:::{table} Stock and final gel concentration
:label: tbl-stock-final-conc

| Gel    | Stock conc. | Final gel conc. |
| ------ | ----------- | --------------- |
| ULGA   | 1 w/v%      | 0.5 w/v%        |
| LGA    | 2.8 w/v%    | 0.7 w/v%        |
| PEG4Nb | 80 mM       | 40 mM           |
:::

# Results

## CPRG-loaded LUVs across hydrogels

:::{figure} ./figures/luv-stability-hydrogels-read2.jpg
:label: fig-luv-stability-hydrogels
:align: center
:width: 75%
Stability of CPRG-loaded LUVs across hydrogels. End-point absorbance ratio
A₅₇₀/A₄₁₂, CPR over CPRG, in four formats: PEG gel, ULGA, LGA and in solution.
Points are the individual wells, bars the mean of the duplicate, and error bars
their standard deviation.
:::

CPRG-loaded LUVs were embedded in each hydrogel, and the CPRG-to-CPR conversion
was read as the endpoint absorbance ratio A570/A412 (n = 2 wells per condition,
blank-corrected). Since CPRG is hydrolysed to the coloured product CPR only
when the substrate meets β-galactosidase, a higher ratio means more of the dye
has been exposed to the enzyme and converted. This reports loss of LUV
integrity or leakage of the encapsulated CPRG. The PEG4Nb hydrogel gave the
lowest ratio of all formats (about 0.4), so CPRG-loaded LUVs were most stable,
with the least leakage and colour change, in the PEG4Nb hydrogel. The
conversion was highest in LGA (about 1.5), above the free-in-solution LUV
control (about 1.2) and ULGA (about 1.0). LGA therefore showed the strongest
colour change, consistent with the greatest release of CPRG and its conversion
to CPR. These are endpoint measurements on duplicate wells, so the differences
are descriptive and not statistically tested.

## GFP-expressing GUVs

Wells, as the source lists them:

- E12: GFP-GUVs+LUVs in solution and G12 is control
- E15: GFP-GUVs+LUVs in ULGA and G15 is control
- E14 precursor PEG4Nb hydrogel and E21 PEG4Nb hydrogel conditions with G14 and
  G21 as controls
- E16 GFP-GUVs+LUVs in LGA and G16 as control

All four GFP-GUV gel conditions are shown as interactive viewers,
deep-linked by well, on [Interactive viewers](./viewers.md). So are the
solution condition and its control: E12, G12, E14, E15, E16 and E21.

Archival figures for the four gel conditions, one field of view each, are
below, stitched into one image with each well's label as its panel
header. Each panel is a single z-plane, a centre crop covering 1/9 of
the field's area. Brightfield is blended in at low weight for the gel
matrix as context.

GFP contrast is grouped where the two wells' signal levels allow it, and
kept per-well otherwise; see the figure caption below for the stretch
used per well, and `general/render-microscopy-fovs.py` with
`figures/fov-render-params.json` for the full method.

:::{figure} ./figures/fov-composite.png
:label: fig-fov-composite
:align: center
:width: 85%
GFP-GUVs+LUVs across the four gel conditions, one field of view each.
PEG4Nb pre-gel (E14) and PEG4Nb gel (E21) share a GFP stretch of 11864
to 20155 counts. ULGA (E15) is stretched at 8405 to 11247 counts, and
LGA (E16) at 4158 to 7020 counts, each on its own. The two wells' GFP
levels do not share a usable common window. Brightfield is blended in
at 25% weight as gel-matrix context.
:::

GFP expression was detected in GUVs encapsulated in all three hydrogel formats:
the photocrosslinked PEG4Nb hydrogel and the physical (thermogelling) hydrogels
ULGA and LGA. Cell-free expression was therefore supported inside each gel
network. GUVs have previously been shown to remain functional in thermogelling
hydrogels. To our knowledge, this is the first demonstration of GFP expression,
and therefore retained biological function, in a photocrosslinked hydrogel,
which indicates that GUV-based expression systems are compatible with
photocrosslinking. The PEG4Nb hydrogel showed considerably higher
autofluorescence than ULGA and LGA, which gave lower background fluorescence.
This reduces the signal-to-background ratio for GFP in PEG4Nb relative to the
thermogels.

# Discussion

This work shows that cell-free GFP expression can be carried out inside GUVs
encapsulated in all three hydrogel formats tested: the photocrosslinked PEG4Nb
hydrogel and the physical gels ULGA and LGA. We examined two vesicle types,
GUVs and LUVs, so the platform is not tied to a single vesicle architecture.
Earlier studies of vesicle-hydrogel interactions were largely limited to
physical, thermogelling networks. By extending the work to a photocrosslinked
gel, we widen the range of materials that can be combined with synthetic cells
and make material fabrication and processing more reliable across gel types.
Because expression was detected after gel formation, including exposure to
photoinitiator and 405 nm light during photopolymerization, the vesicles appear
to tolerate hydrogel formation and subsequent processing well enough to remain
functional. This is a functional readout, and we did not separately quantify
vesicle yield. How the crosslinking dynamics, such as light dose, crosslinking
rate and network density, affect vesicle functionality is an open question, and
a systematic study of it would be a worthwhile next step.

The formats also differ in how easily they can be handled. PEG4Nb and ULGA were
easy to pipette. PEG4Nb has a practical advantage because it gels only when
irradiated at 405 nm with a projector, not in response to temperature. The
precursor therefore stays liquid until crosslinking is triggered, so the sample
can be loaded and checked before gelation and expression begin. This is simpler
than handling thermogels, whose viscosity depends on temperature during
preparation.

Measurement remains the main limitation. Compared with solution-state assays,
gels introduce refractive-index mismatch and autofluorescence, which complicate
imaging and plate-reader quantification. PEG4Nb in particular showed
substantial background fluorescence. Metrology suited to hydrogels will need
further exploration, including alternative instruments, imaging modes, and
data-processing approaches, to expand the platform. Future work should also
quantify expression yield and GFP fluorescence, so that the conclusions rest on
numerical comparisons across gels and not on detection alone.

Finally, this platform is a practical starting point for groups without a
synthetic-biology background, because many of the control experiments needed to
establish baseline behaviour have already been carried out.
