<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

<!-- This page stays close to `log-devnote-draft.docx`, re-read on 2026-10-11
after the authors revised it. `main-supplement.md` holds the full analysis
chain for `OP-20261001`, every disagreement found between sources, and the
review history, so that page and this one do not restate each other. Title and
authors live in `curvenote.yml`, per convention, and are not repeated here. -->

# Module overview

Vesicle-based synthetic cells and cell-free expression systems have so far been
characterized almost exclusively in bulk solution. Whether vesicles remain
stable and biochemically functional when embedded in a hydrogel, where they are
mechanically confined and in contact with a crosslinked polymer network, is
largely unexplored. This module addresses that gap and examines how hydrogel
formation and fabrication govern the integration of synthetic cells into soft
materials.

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

[`fig-schematic-hydrogel-overview`, file:`general/schematic-hydrogel-overview.png`, caption: (Schematic representation of unilamellar vesicles contained in a hydrogel matrix.)]

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

[`fig-photo-luv-pellet`, file:`general/photo-luv-pellet.png`, caption: (Snapshot of the LUV pellet after 4 washes.)]

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

<!-- Both dropdowns above are per an @claude comment left in this file:
"let's place the two different vesicle preps into drop down menus?" -->

:::{attention} Four preparation values changed in the 2026-10-11 revision
:name: gap-prep-values-changed

`log-devnote-draft.docx` was revised on 2026-10-11, after this DevNote first
folded it. Four values in the vesicle preparation differ from the version
folded on 2026-10-09. The current values are carried above.

| Step | Folded 2026-10-09 | Current source |
| --- | --- | --- |
| GUV lipid-in-oil sonication | ~30 min, no temperature | ~20 min at 30 °C |
| Emulsion pipetting | 9 times | ~10 times |
| Inner solution DNA | no concentration stated | 10 ng/mL |
| Construct names | T7-mNG, T7-PLA1 | T7-EsaO-mNG, T7-EsaO-PLA1 |

Confirm the current values are the ones used, and say which runs they apply to.
A protocol that changed across the two weeks of work is expected, and is a
different thing from a correction. Say which this is.
:::

:::{attention} The vesicle preparation has no extrusion step
:name: gap-no-extrusion

The LUV preparation above is hydration, vortex, sonication, 5 freeze-thaw
cycles, then washes. No extrusion step is stated, and no filter pore size is
given anywhere in the source. Confirm whether the vesicles were extruded. If
they were, give the pore size. If they were not, confirm that "LUV" is the
intended label for the population.
:::

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

1. Prepare ULGA at 1 w/v% in the outer solution used during vesicle
   preparation, that is, glucose and 50 mM HEPES, at a final osmolarity of
   ~1200 mOsm.
2. Microwave in 10 s bursts, 5 to 7 times, until fully dissolved.
3. Keep on the 55 °C bead bath until use.

::::

::::{tab-item} LGA (2.8 w/v%)
:sync: lga

1. Dissolve LGA at 2.8 w/v% in the outer solution used for vesicle
   preparation, glucose and 50 mM HEPES, adjusting to a final osmolarity of
   ~1200 mOsm.
2. Heat the solution in a 95 °C heat block until fully dissolved, vortexing
   occasionally to facilitate dissolution.
3. Transfer an aliquot to an Eppendorf tube and maintain at 45 °C until use.
   Since LGA can undergo thermogelation at room temperature, keeping it warm
   prevents premature gelation during mixing.
4. Mix the LGA solution with the vesicles at 45 °C, then dispense the mixture
   into a well plate for gel formation.

::::

::::{tab-item} PEG4Nb (80 mM)
:sync: peg4nb

1. Prepare a precursor solution using the concentrations in
   {numref}`tbl-peg4nb-reagents-doc`. Briefly, dissolve 80 mM PEG4Nb, 20 mM
   PEG-4SH, a 1:1 stoichiometric ratio with PEG4Nb, and 16.9 mM LAP in 1 mL of
   PBS. You can even use DI water or any buffer. This is a photosensitive
   reaction, so prepare the precursor solution in a dark room and wrap the vial
   with foil for storage.
2. Vortex the solution at 2000 rpm for a minute and then keep at RT for 3 to
   5 min.
3. Vortex again for 2 to 4 min and ensure all the chemicals are dissolved well.
   Repeat this part until a clear solution is obtained.
4. Put the desired volume in a 96-well plate and photopattern for exactly 60 s
   at 405 nm using DLP projectors. If needed, you can also do a 1:1 dilution in
   the well, for example 50 µL of precursor gel solution and 50 µL PBS in
   1 well.

:::{figure} ./general/photo-photopatterning-peg4nb.jpg
:label: fig-photo-photopatterning-peg4nb
:align: center
:width: 45%
Photopatterning PEG4Nb hydrogels in a 96-well plate.
:::

[`fig-photo-photopatterning-peg4nb`, file:`general/photo-photopatterning-peg4nb.jpg`, caption: (Photopatterning PEG4Nb hydrogels in a 96-well plate.)]

:::{table} Reagents used in the synthesis of PEG4Nb hydrogels
:label: tbl-peg4nb-reagents-doc

| Reagent | Product Name | Conc. | Molecular weight | Storage Conditions | Supplier |
| --- | --- | --- | --- | --- | --- |
| PEG4Nb | 4-Arm-PEG-Norbornene | 80 mM | 5000 Da | freezer at -20 °C in the dark | Creative Pegworks |
| PEG-4SH crosslinker | 4-Arm PEG-Thiol | 20 mM | 2000 Da | freezer at -20 °C in the dark | Creative Pegworks |
| LAP photoinitiator | Lithium phenyl-2,4,6-trimethylbenzoylphosphinate | 16.9 mM | 294.21 g/mol | 2 to 8 °C, in the dark, photosensitive | Sigma-Aldrich |
| glucose in 50 mM HEPES buffer (~1200 Osm) | — | 1 mL | — | 4 °C | Sigma-Aldrich |
| DLP projectors | — | — | — | — | Zwants Supplies Engineering (PRO4500-92-405) |
:::

<!-- This table keeps the source document's own six-column schema:
Reagent, Product Name, Conc., Molecular weight, Storage Conditions,
Supplier. It is not the DevNote's standard seven-column reagents schema.
The standard-schema version is in main-supplement.md, under
tbl-reagents. -->

::::

:::::

<!-- Tab-set per an @claude comment left in this file: "let's take ULGA,
LGA, and PEG4Nb as three tab sets". -->

:::{danger} The source states two different solvents for the PEG4Nb precursor
:name: gap-peg4nb-solvent

Step 1 above says the precursor is dissolved in 1 mL of PBS.
{numref}`tbl-peg4nb-reagents-doc`, in the same section of the same document,
gives the solvent as glucose in 50 mM HEPES buffer at ~1200 Osm. Both
statements are carried above because the source makes both.

This matters beyond bookkeeping. The precursor is half of every PEG4Nb well,
mixed 15 µL to 15 µL. PBS is about 290 mOsm. If PBS was used, those wells sit
near 745 mOsm against ~1200 mOsm everywhere else, which is a difference no
other condition carries. Say which solvent was used, for each plate.
:::

# Experimental design

Four vesicle conditions were tested, each in solution and in three hydrogels:

1. GFP-expressing GUVs
2. CPRG-loaded LUVs and β-galactosidase enzyme

<!-- The source lists two numbered items under a sentence that says four.
Carried as the source has it. See gap-design-list-truncated below. -->

:::{figure} ./general/diagram-cprg-cpr-reaction.png
:label: fig-diagram-cprg-cpr-reaction
:align: center
:width: 85%
CPRG is cleaved by β-galactosidase to CPR and galactose. CPRG is the substrate
and is initially yellow. CPR is the coloured product, red to pink-purple
depending on conditions.
:::

[`fig-diagram-cprg-cpr-reaction`, file:`general/diagram-cprg-cpr-reaction.png`, caption: (CPRG is cleaved by beta-galactosidase to CPR and galactose.)]

:::{attention} The design list names two of its four conditions
:name: gap-design-list-truncated

The sentence above says four vesicle conditions were tested. The list that
follows it has two items. {numref}`tbl-experimental-design` on the same page
carries four rows, so the list is truncated rather than the design being
smaller than stated.

`rough_devnote`, a second document in the same Drive folder, last edited at the
same time as `log-devnote-draft.docx`, gives all four:

1. **GFP-expressing GUVs** (T7 expression yield, as a baseline measure of
   intravesicular gene expression)
2. **GFP-expressing GUVs co-incubated with CPRG-loaded LUVs and
   β-galactosidase** (tests whether a non-lytic protein product affects LUV
   integrity, serving as a negative control for lysis)
3. **PLA-expressing GUVs co-incubated with CPRG-loaded LUVs and
   β-galactosidase** (tests protein-mediated lysis; CPRG hydrolysis by
   β-galactosidase gives a colorimetric readout of LUV permeabilization)
4. **CPRG-loaded LUVs alone** (quantifies baseline membrane leakiness in each
   environment)

Those four match {numref}`tbl-experimental-design` row for row. Confirm that
this is the intended list, and that it replaces the two-item list above.
:::

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

**Plating conditions**

- Vesicles in outer solution only, no gel, serve as the reference control.
- Mixed 15 µL vesicle solution with 15 µL gel stock, then plated 30 µL per
  well. Plated all samples in duplicate.

:::{table} Stock and final gel concentration
:label: tbl-stock-final-conc

| Gel | Stock conc. | Final gel conc. |
| --- | --- | --- |
| ULGA | 1 w/v% | 0.5 w/v% |
| LGA | 2.8 w/v% | 0.7 w/v% (7.5 µL + 7.5 µL OS) |
| PEG4Nb | 80 mM | 40 mM |
:::

Plate map: `1BI0gXBY33WXuJZO19aqzrlLL2ofd9EROV2j-iSKzwsE`.

<!-- Written as a plain identifier, not a link. Drive URLs are not
written as hyperlink hrefs here; see main-supplement.md's Resources for
why. -->

:::{danger} Which plate rows hold GFP-GUVs and which hold PLA-GUVs is not settled
:name: gap-rows-ij-conflict

Three sources describe the same plate and give two different answers for rows
I and J.

| Source | Row I | Row J |
| --- | --- | --- |
| `build.xlsx` Sheet1, in the DevNote Drive folder | PLA-GUVs + LUVs | GFP-GUVs + LUVs |
| `build.xlsx` Sheet2, same file | GFP-GUVs + LUVs | PLA-GUVs + LUVs |
| The `build` Google Sheet linked above | GFP-GUVs + LUVs in the gel columns, PLA-GUVs + LUVs in solution columns 6 and 7 | the reverse |
| `merged_plate.csv`, from the 2026-10-08 plate | PLA in every column | GFP in every column |

The `build` Google Sheet disagrees with itself between its gel columns and its
solution columns. Do not resolve this by taking the majority: two of the
sources share an origin. Only an author can say which assignment is correct.

A second item in the same sheets: cell K6 reads `GFP GUVs` and cell K7 reads
`GUVs`. They are a duplicate pair and should match.
:::

# Results

:::{figure} ./figures/luv-stability-hydrogels-read2.jpg
:label: fig-luv-stability-hydrogels
:align: center
:width: 75%
LUV stability in hydrogels. End-point absorbance ratio A₅₇₀/A₄₁₂, CPR over
CPRG, for CPRG-loaded LUVs in four formats: PEG gel, ULGA, LGA and in solution.
Points are the individual wells, bars the mean of the duplicate, and error bars
their standard deviation.
:::

[`fig-luv-stability-hydrogels`, notebook:`luv_stability_hydrogels_matlabcode.txt`, platemap:`none`, data source:`20261009-113443-synergy2-OJMB-gfp-pla-guv-luv-gels-16UmL-LacZ.txt`, caption: (LUV stability in hydrogels, end-point A570/A412 ratio across four formats.)]

<!-- The analysis for this figure is a MATLAB script, not a notebook. The
provenance line names it in the notebook field because that field has no other
spelling. See gap-figure4-analysis below. -->

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

:::{attention} The figure's analysis is a script that does not read its own data file
:name: gap-figure4-analysis

The analysis for {numref}`fig-luv-stability-hydrogels` is
`luv_stability_hydrogels_matlabcode.txt`, in the DevNote Drive folder. It is a
MATLAB script, not a notebook, so this figure cannot be referenced by a
notebook cell label and is carried as a static image.

The script does not load the data file named in the provenance line above. It
carries its absorbance values written into its own source, under a header
reading "Synergy 2, 384-well, read 2 (3:09 PM, 16 U/mL LacZ), LUV only
(row L)". Nothing connects those written-in numbers to
`20261009-113443-synergy2-OJMB-gfp-pla-guv-luv-gels-16UmL-LacZ.txt` except that
header. Confirm the numbers in the script came from that file, or change the
script to read it.
:::

:::{attention} The pre-gel condition was dropped from this figure
:name: gap-prepeg-dropped

An earlier version of this same figure, folded into this DevNote on 2026-10-09,
carried five bars. The fifth was "Pre-PEG solution", at a ratio of about 0.69.
The current version carries four, and the script states the reason in a
comment: "pre-PEG left out of this graph".

The prose above describes PEG4Nb as "the lowest ratio of all formats" while one
format is not shown. The pre-gel condition is also the one control that
separates the PEG4Nb precursor's own chemistry from the crosslinked gel, which
{ref}`gap-peg4nb-solvent` turns on. Say whether pre-PEG should be restored to
the figure.
:::

**GFP expression in hydrogels**

Plate map 2: `15F2gLuDLFGxJRSbk73k1AJpaMZUq_iTpFFEllDdRHug`.

GFP expression was detected in GUVs encapsulated in all three hydrogel
formats: the photocrosslinked PEG4Nb hydrogel and the physical,
thermogelling hydrogels ULGA and LGA. Cell-free expression was
therefore supported inside each gel network. GUVs have previously been
shown to remain functional in thermogelling hydrogels. To the authors'
knowledge, this is the first demonstration of GFP expression, and
therefore retained biological function, in a photocrosslinked hydrogel,
which indicates that GUV-based expression systems are compatible with
photocrosslinking. The PEG4Nb hydrogel showed considerably higher
autofluorescence than ULGA and LGA, which gave lower background
fluorescence. This reduces the signal-to-background ratio for GFP in
PEG4Nb relative to the thermogels.

- E12: GFP-GUVs+LUVs in solution, and G12 is the control.
- E15: GFP-GUVs+LUVs in ULGA, and G15 is the control.
- E14: GFP-GUVs+LUVs in PEG4Nb pre-gel, and E21 in PEG4Nb gel, with G14
  and G21 as controls.
- E16: GFP-GUVs+LUVs in LGA, and G16 is the control.

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/E/12/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/E/12/0`, caption: (GFP-GUVs+LUVs in solution, well E12.)]

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/G/12/0",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB_2026-10-06_12-23-15.511547.zarr/G/12/0`, caption: (Outer-solution-only control, well G12.)]

:::{anywidget} https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr",
    "height": "600px",
    "menuOpen": true
}
:::

[zarr-viewer, source:`https://data.nucleus.engineering/microscopy/nucleus-bnext-01/OP-20261006_endpoint-vescile-gel-MB-zstack-E15_2026-10-06_12-58-55.990402.zarr`, caption: (GFP-GUVs+LUVs in ULGA, well E15, z-stack.)]

:::{attention} Three of five GUV conditions have no microscopy store yet, and no viewer survives to the archive
:name: gap-figure5-missing

Resolved in part. `log-devnote-draft.docx` was edited again between
2026-10-11 23:28 and 2026-10-12 00:12, after this DevNote's prior fold-in
pass, which is why the heading previously read empty. It now carries real
Zarr and Parquet links for two of the five listed conditions: E12/G12 in
solution, and E15/G15 in ULGA. E14/E21 (PEG4Nb pre-gel and gel) and E16
(LGA) are still named with no store linked.

Separately, the three viewers above do not survive JATS conversion. The
archive's only record of these wells, once exported, will be this prose
and the well list. A static PNG export is still needed as the archival
figure, at least for the confirmed E12, G12 and E15 fields of view,
matching the convention used elsewhere in this pipeline.
:::

# Discussion

1. We showed that GFP expression in all 3 gels can be done
2. PLA lyses the vesicles in all gels
3. Enable reliable material fabrication
4. Understand whether vesicles tolerate hydrogel formation and subsequent
   processing, including exposure to photoinitiators and light during
   photopolymerization.
5. Easy to pipette gel

:::{attention} The Discussion mixes findings with aims
:name: gap-discussion-mixed

Items 1 and 2 state results. Items 3 and 4 read as aims of the work rather than
findings from it, and item 5 is an observation about handling. A reviewer
comment on the source asks "What are the key takeaways?" and another asks that
the results be presented "in parallel".

Two of these also need their evidence named. Item 1 says GFP expression worked
in all three gels. Two of the three now have a microscopy viewer, and one does
not, per {ref}`gap-figure5-missing`. Item 2 says PLA lyses vesicles in all
gels, and {numref}`fig-luv-stability-hydrogels` shows LUV-only wells, not the
PLA-GUV condition. Name the figure or the run each claim rests on.
:::

# Conclusion

[PLEASE FILL IN]

<!-- The source Conclusion heading carries no text. -->

# What's next

[PLEASE FILL IN]

:::{attention} What's next is unanswered, and was asked directly
:name: gap-whats-next

A reviewer comment on the source reads: "What's next here? What work does
someone need to do to take this a step further - I feel like there is a lot to
discuss re: metrology challenges or standardization of methods and this is just
a first step."

Write the next experiment, or say that this line of work stopped here.
:::

# Review questions

<!-- Rebuilt on 2026-10-11 against the revised `log-devnote-draft.docx`. Items
the revision closed are recorded as closed rather than deleted, so a reviewer
can see what moved. -->

Closed by the 2026-10-11 revision:

- "[Paste the graph here]" is filled. The graph is
  {numref}`fig-luv-stability-hydrogels`.
- "[link to dataset URL here; .txt of matlab code in directory; caption]" is
  filled. The dataset URL is named in the source, and the MATLAB code is in the
  DevNote Drive folder.
- PEG4Nb now has numbered preparation steps, as ULGA and LGA already did.
- The LGA transfer step is now stated: mix with vesicles at 45 °C, then dispense
  into the well plate.
- ULGA's formulation reference, previously "[insert link]", is now given as the
  outer solution used during vesicle preparation.
- Discussion no longer has blank numbered lines. It has five items.
- {numref}`fig-photo-luv-pellet` previously carried the placeholder caption
  "[Caption]". It now has the caption the source gives it.

Still open, and each has its own flag above:

- The Conclusion heading has no text.
- "Microscopy data" and "Figure 5" are no longer empty. Two of five GUV
  conditions now have a microscopy viewer; three still do not. See
  {ref}`gap-figure5-missing`.
- The plasmid question is open in words: is T7-EsaO-mNG linear or a plasmid, is
  T7-EsaO-PLA1 the same, and does either carry a tetO operator. Two sequence
  files were linked on the source on 2026-10-10, and they answer identity, not
  this. See {ref}`gap-constructs-unverified`.
- A reviewer comment asks for links to the relevant datasets, analysis notebooks
  and platemaps. One dataset URL is now named. The platemap for
  {numref}`fig-luv-stability-hydrogels` is not.

New in this revision:

- {ref}`gap-peg4nb-solvent`, two solvents stated for one precursor.
- {ref}`gap-design-list-truncated`, four conditions announced and two listed.
- {ref}`gap-rows-ij-conflict`, rows I and J unsettled across three sources.
- {ref}`gap-prepeg-dropped`, the pre-gel bar removed from the results figure.
- {ref}`gap-prep-values-changed`, four preparation values changed.
- {ref}`gap-no-extrusion`, no extrusion step in the LUV preparation.
- {ref}`gap-figure4-analysis`, the analysis script does not read its data file.

:::{danger} The two DNA constructs could not be verified
:name: gap-constructs-unverified

The methods name `T7-EsaO-mNG` and `T7-EsaO-PLA1`. Two GenBank files were
linked on the source document on 2026-10-10,
`t7pro-esao-ls1-mneongreen.gbk` and `t7pro-esao-ls1-pla1.gbk`. Neither is in
`nucleus-eng/DNA`, so both need submitting there before this publishes.

Verification could not be completed. Each file, as downloaded from Drive, is one
byte smaller than Drive reports for it, and holds one base fewer than its own
`LOCUS` line declares: 1349 against 1350 for the PLA1 file, 1097 against 1098
for the mNeonGreen file. In each, one block of the sequence holds nine
characters where every other block holds ten, and the file's own position
numbers run one ahead from that point. Both files end correctly, so the missing
byte is not a trailing newline.

This may be a fault in the download path rather than in the files themselves,
and the check cannot tell which. Open the originals and confirm them before
either construct is cited as a sequence.
:::

# Open questions

:::{admonition}

1. Are LUVs leaky?
2. Can PLA lyse?
3. Do only the gels lyse?

:::

<!-- Moved to the end of the page per an @claude comment left in this
file: "maybe open questions come at the end?" -->

<!-- # Resources

The full asset chain, the review history, and every flagged
disagreement between sources are in `main-supplement.md`, in this same
directory. It is not in `curvenote.yml`'s `toc`, so it does not publish
as a page of this DevNote. It is a plain file in the repository. -->
