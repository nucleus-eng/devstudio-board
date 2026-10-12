<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

<!-- This page stays close to `log-devnote-draft.docx`, re-read on 2026-10-12
after the authors revised it a second time. `main-supplement.md` holds the full
analysis chain for `OP-20261001`, every disagreement found between sources, and
the review history, so that page and this one do not restate each other. Title
and authors live in `curvenote.yml`, per convention, and are not repeated
here. -->

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

:::{note} The PEG4Nb concentrations are settled; the ratio sentence beside them is not
:name: gap-peg4nb-units

**Settled on 2026-10-11.** `80 mM` counts molecules, and both PEG4Nb and
PEG-4SH are four-armed. The concentrations in
{numref}`tbl-peg4nb-reagents-doc` are the record of what was run: PEG4Nb
80 mM at 5000 g/mol, which is 0.4 g in 1 mL; PEG-4SH 20 mM at 2000 g/mol,
0.04 g; LAP 16.9 mM, 4.97 mg. No molar ratio and no group ratio is asserted
anywhere on this page, by instruction.

**Still open, and it is the authors' own sentence.** Step 1 above describes the
20 mM PEG-4SH as "a 1:1 stoichiometric ratio with PEG4Nb". The concentrations
it cites in the same sentence give 4:1, in molecules and in reactive groups
alike, because both reagents carry four arms. The sentence is carried verbatim
because it is what the authors wrote, and this DevNote does not edit its
source. Say whether that clause should be struck from the source document, and
the authors will have to be the ones to strike it.

**The fix is to the sentence, not to the formulation.** Satisfying a 1:1 group
ratio by raising the thiol instead would need 320 mM PEG-4SH, which at
2000 g/mol is 0.64 g. With the 0.4 g of PEG4Nb already in the same millilitre
that is about 1.04 g of polymer, leaving roughly 0.1 mL for everything else —
a paste, in a step whose own instruction is to repeat "until a clear solution
is obtained". So the concentrations above cannot be rescaled to match the
clause. Recorded here because the arithmetic that reaches 0.64 g is correct at
every line, and three sessions followed it before anyone asked whether the
answer would dissolve.
:::

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

**The step may not describe this run at all.** Two signs in the step's own
text, both visible above. It hedges its solvent — "You can even use DI water or
any buffer" — which is how a general method is written, not how a run is
recorded. And it specifies a 96-well plate, while every data source for this
work is a 384-well plate: the analysis script's header reads "Synergy 2,
384-well", the Cytation5 raw file records "Greiner 384 SensoPlate Plus glass
bottom", and the build sheet uses rows I to M and columns up to 20, which do
not exist on a 96-well plate.

So the PEG4Nb step reads as a general protocol copied in, rather than a record
of what was done here. If that is right, the PBS line is a default rather than
evidence, and the contradiction with the table above is not a contradiction
about this run. Confirm the solvent and the plate format actually used.

Separately, a second session reports finding the same wording in a hydrogel
protocol PDF in the DevStudio Drive, and a notebook entry recording a different
solvent for this run. That is recorded here as a pointer only. It is not folded
in, because neither document is part of this DevNote's sources.
:::

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

[`fig-diagram-cprg-cpr-reaction`, file:`general/diagram-cprg-cpr-reaction.png`, caption: (CPRG is cleaved by beta-galactosidase to CPR and galactose.)]

Plate map: `15-QRtbOExMxpLzzK5mwe1lvsUzQgJlNAuqf9PWi7KRs`.

<!-- Drive identifiers are written as plain text, not as hyperlink hrefs; see
main-supplement.md's Resources for why. -->

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

:::{attention} The design narrowed from four conditions to two, and both plate maps changed
:name: gap-design-narrowed

The 2026-10-11 version of the source said "Four vesicle conditions were tested"
and listed two. This revision says **two** and lists two, so the sentence and
the list now agree. What changed is the scope, not the wording: the two
conditions kept are the two that carry a figure.

Two consequences a reviewer should see.

The four-condition design grid folded in on 2026-10-09 is gone from the source.
It listed GFP-GUVs, GFP-GUVs + LUVs, PLA-GUVs + LUVs and LUVs only, against
five environments. It is preserved in `main-supplement.md` as
{numref}`tbl-experimental-design-doc`. The PLA-GUV arm in particular is no
longer described anywhere on this page, and it has never carried a figure.

Both plate map links were replaced. The earlier map,
`1BI0gXBY33WXuJZO19aqzrlLL2ofd9EROV2j-iSKzwsE`, is no longer cited by the
source. Two new maps are, one per condition. The row conflict recorded in
{ref}`gap-rows-ij-conflict` was found in the earlier map and in files derived
from it, so confirm whether it carries over to the new ones before either is
used.
:::

:::{danger} Which plate rows hold GFP-GUVs and which hold PLA-GUVs is not settled
:name: gap-rows-ij-conflict

Three sources describe the same plate and give two different answers for rows
I and J.

| Source | Row I | Row J |
| --- | --- | --- |
| `build.xlsx` Sheet1, in the DevNote Drive folder | PLA-GUVs + LUVs | GFP-GUVs + LUVs |
| `build.xlsx` Sheet2, same file | GFP-GUVs + LUVs | PLA-GUVs + LUVs |
| `build.csv`, from the 2026-10-08 plate | GFP-GUVs + LUVs in the gel columns, PLA-GUVs + LUVs in solution columns 6 and 7 | the reverse |
| `merged_plate.csv`, same plate | PLA-GUVs + LUVs in every column | GFP-GUVs + LUVs in every column |

The disagreement is confined to the gel columns. `build.csv` and
`merged_plate.csv` agree that row I holds PLA in solution columns 6 and 7, and
disagree about all eight gel column-pairs, which is 16 wells. `build.csv`
therefore disagrees with itself between its solution and its gel columns, while
`merged_plate.csv` is internally consistent.

Do not resolve this by taking the majority: two of the sources share an origin.
Only an author can say which assignment is correct.

A second item in the same sheets: cell K6 reads `GFP GUVs` and cell K7 reads
`GUVs`. They are a duplicate pair and should match.
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

[`fig-luv-stability-hydrogels`, notebook:`luv_stability_hydrogels_matlabcode.txt`, platemap:`none`, data source:`20261009-113443-synergy2-OJMB-gfp-pla-guv-luv-gels-16UmL-LacZ.txt`, caption: (Stability of CPRG-loaded LUVs across hydrogels, end-point A570/A412 ratio in four formats.)]

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
header. Those values were reconciled against the instrument file on 2026-10-11
and reported to match; that was done elsewhere and is not repeated here. The
flag stays open until the script reads the file instead of carrying its
numbers.
:::

:::{attention} The pre-gel condition was dropped from this figure
:name: gap-prepeg-dropped

An earlier version of this same figure, folded into this DevNote on 2026-10-09,
carried five bars. The fifth was "Pre-PEG solution", at a ratio of about 0.69.
The current version carries four, and the script states the reason in a
comment: "pre-PEG left out of this graph".

**The pre-gel bar cannot be restored from this read, and should not be.** The
script carries a quality gate, `minSignal = 0.01` on blank-corrected A412, and
both pre-gel wells fail it: their blank-corrected A412 is -0.013 and -0.014.
The sample reads lower than its own matrix-only control at 412 nm, so the ratio
has a negative denominator and no value. The omission is a data failure, not an
editorial choice.

The cause is in the matrix, and it is scattering rather than absorbance. Among
the ten matrix-only control wells, which hold matrix alone with no vesicles and
no CPRG, the two pre-gel controls are the highest at **both** wavelengths:
0.361 and 0.319 at 412 nm, and 0.285 and 0.242 at 570 nm. Against the mean of
the other eight controls the pre-gel excess is +0.146 at 412 nm and +0.091 at
570 nm, a ratio of 1.6. A substance absorbing near the 405 nm photopatterning
wavelength would show a large excess at 412 nm and almost none at 570 nm. Two
thirds carrying over to 570 nm is broadband attenuation, which is what light
scattering from a turbid medium does.

The sample well then reads 0.327 against a control of 0.340, within noise and
with an arbitrary sign. The crosslinked gel's own controls are ordinary, 0.208
and 0.261 at 412 nm, so the effect belongs to the uncrosslinked precursor
specifically and not to PEG4Nb chemistry in general.

This makes the pre-gel condition a measurement question rather than a plating
one. Re-running the same assay in the same matrix is likely to fail the same
way. Because the interference is scattering, a reference read at a wavelength
where neither CPRG nor CPR absorbs, around 700 nm, subtracted from both
channels before the ratio is taken, is the correction that would make this
condition measurable. That is worth deciding before the plate is rebuilt.
:::

## GFP-expressing GUVs

Plate map 2: `15F2gLuDLFGxJRSbk73k1AJpaMZUq_iTpFFEllDdRHug`.

Wells, as the source lists them:

- E12: GFP-GUVs+LUVs in solution and G12 is control
- E15: GFP-GUVs+LUVs in ULGA and G15 is control
- E14 precursor PEG4Nb hydrogel and E21 PEG4Nb hydrogel conditions with G14 and
  G21 as controls
- E16 GFP-GUVs+LUVs in LGA and G16 as control

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

<!-- Viewer form, deep links and captions in this block are carried from
commit bacde77 by the parallel fold, where `curvenote check bnext-devnotes`
was run against them and passed. The widget is referenced by its published
URL rather than a local plugin file; `myst build` cannot resolve the
`anywidget` directive either way, and the venue can. -->


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

:::{danger} The microscopy has no archival figure, and the viewers will not survive export
:name: gap-microscopy-no-static

The three viewers above read the microscopy live from
`data.nucleus.engineering`. No image file exists for this result anywhere: the
source document carries the stores as links and embeds no picture, and the
DevNote folder holds no microscopy image.

**Two of five conditions have a store.** `log-devnote-draft.docx` was edited
again between 2026-10-11 23:28 and 2026-10-12 00:12, which is why an earlier
pass over this page found no GFP figure at all. The edit brought Zarr and
Parquet links for E12/G12 in solution and E15/G15 in ULGA. E14 and E21, the
PEG4Nb pre-gel and gel, and E16 in LGA are named in the well list with no store
linked.

An interactive viewer does not survive conversion to JATS, which is the format
this DevNote exports for the venue. On that path the GFP result becomes a
section with prose and no visible evidence, and the archive's only record of
these wells will be that prose and the well list. Supply a static export as the
archival figure, at least for the confirmed E12, G12 and E15 fields of view,
and say in each caption that it is the archival record of the viewer.

The stores themselves are deliberately not committed to this repository, and
must not be. A viewer pointed at the served URL is the supported pattern.

Two further items. The parquet companion of each store is named in the source
and is not referenced here, because nothing on this page reads it; say if it
should be. And the served paths contain `vescile`, a misspelling of `vesicle`,
copied exactly because a URL is not text to correct.
:::

:::{attention} Three claims in this section need their evidence named
:name: gap-gfp-claims

**All three gels.** The prose reports GFP in PEG4Nb, ULGA and LGA. The three
viewers cover solution (E12, with its control G12) and ULGA (E15). No store is
given for the LGA well
(E16) or for either PEG4Nb well (E14, E21), so three of the four reported
conditions have no linked data on this page.

**A priority claim.** "To our knowledge, this is the first demonstration of GFP
expression ... in a photocrosslinked hydrogel" is a claim about the literature,
and the DevNote cites nothing for it. Supply the citations the claim was
checked against, or soften it.

**Autofluorescence.** PEG4Nb is reported as considerably higher than ULGA and
LGA. No number, channel or exposure is given, and no PEG4Nb store is linked, so
the claim cannot be checked from this page.
:::

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

:::{attention} One Discussion claim is not supported by this DevNote's own figure
:name: gap-discussion-vs-figure

The Discussion says the vesicles "appear to tolerate hydrogel formation and
subsequent processing well enough to remain functional", on a GFP readout.
{numref}`fig-luv-stability-hydrogels` reports the other readout, and LUVs leak
in every format, most of all in LGA. Both can be true, because they measure
different vesicles by different means, but the page does not say so. Say
explicitly that the GFP conclusion is about GUV expression and not about LUV
retention.

The earlier Discussion also stated "PLA lyses the vesicles in all gels". That
sentence is gone from the source and no figure ever supported it. It is
recorded here so the removal is visible rather than silent.
:::

# Conclusion

[PLEASE FILL IN]

<!-- The source Conclusion heading carries no text. -->

# What's next

[PLEASE FILL IN]

:::{attention} What's next is unanswered, though the Discussion now carries part of it
:name: gap-whats-next

A reviewer comment on the source reads: "What's next here? What work does
someone need to do to take this a step further - I feel like there is a lot to
discuss re: metrology challenges or standardization of methods and this is just
a first step."

The rewritten Discussion answers part of that: a systematic study of
crosslinking dynamics, metrology suited to hydrogels, and quantification of
expression yield. None of it sits under this heading, and the source still has
no What's next section. Either move those statements here, or say the
Discussion is where they belong and this heading comes out.
:::

# Review questions

<!-- Rebuilt on 2026-10-12 against the second revision of
`log-devnote-draft.docx`. Items the revisions closed are recorded as closed
rather than deleted, so a reviewer can see what moved. -->

Closed by the two revisions of 2026-10-11 and 2026-10-12:

- "[Paste the graph here]" and "[link to dataset URL here...]" are both filled.
- PEG4Nb has numbered preparation steps, as ULGA and LGA already did.
- The LGA transfer step is stated.
- ULGA's formulation reference, previously "[insert link]", is given.
- {numref}`fig-photo-luv-pellet` previously carried the placeholder caption
  "[Caption]". It now has the caption the source gives it.
- The Discussion was five sentence fragments. It is now three written
  paragraphs.
- Figure 5 was an empty heading. It is now microscopy, carried as two viewers.
- The design list said four and listed two. It now says two and lists two. See
  {ref}`gap-design-narrowed` for what that cost.
- The PEG4Nb concentrations are settled. See {ref}`gap-peg4nb-units`.

Still open, and each has its own flag above:

- The Conclusion heading has no text.
- The plasmid question is open in words: is T7-EsaO-mNG linear or a plasmid, is
  T7-EsaO-PLA1 the same, and does either carry a tetO operator. Two sequence
  files were linked on the source on 2026-10-10, and they answer identity, not
  this. See {ref}`gap-constructs-unverified`.
- Rows I and J, in {ref}`gap-rows-ij-conflict`, and whether that conflict
  carries into the two new plate maps.
- The PEG4Nb solvent and the plate format, in {ref}`gap-peg4nb-solvent`.
- The microscopy has no archival figure, in {ref}`gap-microscopy-no-static`.
- Three GFP claims need their evidence named, in {ref}`gap-gfp-claims`.
- The pre-gel condition cannot be measured by this assay, in
  {ref}`gap-prepeg-dropped`.

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
byte is not a trailing newline. The defect is identical across two independent
fetches, so re-fetching the same way will not resolve it.

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
