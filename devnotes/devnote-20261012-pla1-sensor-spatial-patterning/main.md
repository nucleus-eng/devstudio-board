---
title: 'TetO-Regulated PLA1 Sensor in Vesicles: aTc Titration and Spatial Patterning'
thumbnail: ./figures/fig7-patterned-gel.png
---

<!--
Editing convention: a section marked `@claude please don't rewrite this section`,
or commented out, is protected. Claude will not regenerate, reflow or reword it.
-->

<!-- Drafted 2026-10-12 from the Google Doc "TetO-PLA in NB_CPRG".
Source: https://docs.google.com/document/d/11Rcrw1_6U45LPC8VNe6-34ztsteZ8Qu-XwIrUvVDDtQ
Prose, tables, step lists and all eight figures are carried verbatim from
that Doc, including its own section order. The Doc's own title/byline
block is not repeated in the body: title, authors and their emails live in
this file's frontmatter and in curvenote.yml instead. Figure captions drop
the literal "Figure N." prefix the Doc gives them, since MyST auto-numbers
the `:::{figure}` directive. Inline "(Figure N)" citations already in the
Doc's own prose became {ref} cross-links to the same figure, rather than
new sentences. The Doc's own "Sequences:" subsection, a bulleted list
carrying each construct's raw sequence inline, became a "Plasmid maps"
subsection in the same position: a two-item tab-set, one tab per
construct, each with a seqviz view and the same raw sequence in a
dropdown. No sequence character changed; only where it sits and how it is
wrapped changed.

Renamed from `mk-mb-devnote-5` to this slug on 2026-10-22 (Anton Molina),
to drop author initials from the naming scheme corpus-wide. The git
branch name was not renamed, since the original PR (#21) is merged. -->

<!-- :::{admonition} Open items from the draft
:class: warning dropdown
:name: flags-review

**The source Doc gives no date anywhere in its text.** `curvenote.yml`
uses the Drive file's own creation date, 2026-10-11, checked 2026-10-12.

**Neither plasmid is built from an existing file on this board.** Both
`dna/pJL1-T7-TetO-GFP.gb` and `dna/pJL1-T7-TetO-PLA1.gb` are built fresh
from this Doc's own inline sequences — a different backbone (pJL1) from
the pOpen backbone this board's other DevNotes use for a similarly named
PLA1/deGFP pair. Lengths match the Doc's construct table exactly (2,486 bp
and 3,223 bp). The GFP cassette sits on the given sequence's forward
strand; the PLA1 cassette sits on the reverse strand, as the Doc's own
table states, confirmed by locating the promoter, operator, RBS and CDS
on the reverse complement and converting back to forward-strand
coordinates for the GenBank file. Both CDS translations were checked
against the Doc's own claims: the GFP CDS is 240 aa ending in WSHPQFEK,
the Strep-tag II the Doc's table names; the PLA1 CDS is 320 aa, and
translates identical to the PLA1 protein this board's `devnote-20261011-pla1-triggered-lysis-guvs` and
`devnote-20261011-co-encapsulated-pla1-lysis` carry on the pOpen backbone (MSMSLSFTSAIAPAAIQPP...ANA)
— the same enzyme, a different vector. Neither AmpR nor KanR is annotated,
since the Doc gives no landmark for either. Drive this devnote's own
{ref}`seqviz-pjl1-teto-gfp` and {ref}`seqviz-pjl1-teto-pla1`.

**The Cell-free system table carried Google Docs export artifacts
(`\#\#\#`, `\*\*`) around every cell in the source pull.** Removed here as
a formatting fix; no value, unit, or row changed.

**Figure 5's chart title reads "pOpen-PLA," not "TetO-PLA1."** The source
image for {ref}`fig-5-encapsulated-atc-titration-confocal` is titled
"CF TetR and pOpen-PLA in a Two Vesicle System," but every other mention in
this Doc, including its own caption for this figure, calls the construct
TetO-PLA1 (pJL1_T7-TetO-PLA1). Carried as supplied; this looks like a
leftover label from a chart template rather than a claim that this run
used the pOpen backbone.

**The Protocol cites "(OP DevNote)" and the Sources list cites "Ojaswita's
devnote," neither linked.** Both likely point to this board's own
`devnote-op-20261001-luv-gel-pla` (still an open draft PR), which covers
PEG-4NB hydrogel preparation — the same gel chemistry this Doc's Protocol
describes. Not linked here, since that identification is inferred, not
stated in the source.
::: -->

# Abstract

aTc works as an inducer for this system only in a narrow window around 0.25 µM; above that, its own effects on the cell-free reaction and on the membrane dominate the response.

We built a TetO-regulated phospholipase sensor in GUVs, encapsulating a pJL1_T7-TetO-PLA1 construct together with purified β-galactosidase, and placed the vesicles either in outer solution (OS) or in a photopolymerized PEG-4NB hydrogel. Induction with aTc should express PLA1, permeabilize the membrane, release β-gal, and cleave CPRG to a red product. At the aTc concentrations first tried (1–10 µM), the sensor ran backward: more aTc gave less color change. Cell-free poisoning, aTc autofluorescence, and partitioning of aTc into the membrane all scale with concentration and account for the inversion. Dropping to 0.25 µM recovered the intended behavior, and a spatially patterned gel at that concentration gave a clean programmed color change confined to the patterned region.

# Overview

We used two constructs, both under a T7 promoter with a tetO operator: pJL1_T7-TetO-GFP as a reporter to characterize expression and repression, and pJL1_T7-TetO-PLA1 as the sensor output. Reactions were run in Nucleus Base Cytosol.

Both plasmids place the tetO operator immediately downstream of the T7 promoter, ahead of the standard pJL1 5′UTR and ribosome binding site, so TetR blocks transcription by obstructing the operator region and preventing the RNA polymerase from working properly.

:::{table} Constructs.
:label: tbl-constructs
:align: center

| Construct | Length | Promoter and operator | Coding sequence | Marker |
| --- | --- | --- | --- | --- |
| pJL1_T7-TetO-GFP | 2,486 bp | T7 followed directly by tetO | 240 aa deGFP with a C-terminal Strep-tag II | Kan |
| pJL1_T7-TetO-PLA1 | 3,223 bp | T7 followed directly by tetO, on the reverse strand | 320 aa phospholipase A1 | Amp |
:::

CF-TetR was added as the repressor throughout.

The PLA1 sensor is meant to work as a three-step chain. TetR keeps the TetO-PLA1 off and prevents expression. Adding aTc releases TetR, allowing PLA1 expression, and the phospholipase permeabilizes the vesicle membrane. Purified β-galactosidase co-encapsulated inside the vesicles then reaches the CPRG supplied outside, cleaving it and shifting the color from yellow to red. The color change therefore serves as the readout for aTc-triggered lysis, measured as absorbance at 575 nm.

## Plasmid maps

:::::{tab-set}

::::{tab-item} pJL1-T7-TetO-GFP
:sync: gfp

(seqviz-pjl1-teto-gfp)=

:::{seqviz} ./dna/pJL1-T7-TetO-GFP.gb
:::

:::{admonition} Full sequence
:class: dropdown

```text
TTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCTTGCAAACAAAAAAACCACCGCTACCAGCGGTGGTTTGTTTGCCGGATCAAGAGCTACCAACTCTTTTTCCGAAGGTAACTGGCTTCAGCAGAGCGCAGATACCAAATACTGTTCTTCTAGTGTAGCCGTAGTTAGGCCACCACTTCAAGAACTCTGTAGCACCGCCTACATACCTCGCTCTGCTAATCCTGTTACCAGTGGCTGCTGCCAGTGGCGATAAGTCGTGTCTTACCGGGTTGGACTCAAGACGATAGTTACCGGATAAGGCGCAGCGGTCGGGCTGAACGGGGGGTTCGTGCACACAGCCCAGCTTGGAGCGAACGACCTACACCGAACTGAGATACCTACAGCGTGAGCTATGAGAAAGCGCCACGCTTCCCGAAGGGAGAAAGGCGGACAGGTATCCGGTAAGCGGCAGGGTCGGAACAGGAGAGCGCACGAGGGAGCTTCCAGGGGGAAACGCCTGGTATCTTTATAGTCCTGTCGGGTTTCGCCACCTCTGACTTGAGCGTCGATTTTTGTGATGCTCGTCAGGGGGGCGGAGCCTATGGAAAAACGCCAGCAACGCGATCCCGCGAAATTAATACGACTCACTATAGGGATCCCTATCAGTGATAGAGATAGAAATAATTTTGTTTAACTTTAAGAAGGAGATATACATATGAGCAAAGGTGAAGAACTGTTTACCGGCGTTGTGCCGATTCTGGTGGAACTGGATGGCGATGTGAACGGTCACAAATTCAGCGTGCGTGGTGAAGGTGAAGGCGATGCCACGATTGGCAAACTGACGCTGAAATTTATCTGCACCACCGGCAAACTGCCGGTGCCGTGGCCGACGCTGGTGACCACCCTGACCTATGGCGTTCAGTGTTTTAGTCGCTATCCGGATCACATGAAACGTCACGATTTCTTTAAATCTGCAATGCCGGAAGGCTATGTGCAGGAACGTACGATTAGCTTTAAAGATGATGGCAAATATAAAACGCGCGCCGTTGTGAAATTTGAAGGCGATACCCTGGTGAACCGCATTGAACTGAAAGGCACGGATTTTAAAGAAGATGGCAATATCCTGGGCCATAAACTGGAATACAACTTTAATAGCCATAATGTTTATATTACGGCGGATAAACAGAAAAATGGCATCAAAGCGAATTTTACCGTTCGCCATAACGTTGAAGATGGCAGTGTGCAGCTGGCAGATCATTATCAGCAGAATACCCCGATTGGTGATGGTCCGGTGCTGCTGCCGGATAATCATTATCTGAGCACGCAGACCGTTCTGTCTAAAGATCCGAACGAAAAAGGCACGCGGGACCACATGGTTCTGCACGAATATGTGAATGCGGCAGGTATTACGTGGAGCCATCCGCAGTTCGAAAAATAAGTCGACCGGCTGCTAACAAAGCCCGAAAGGAAGCTGAGTTGGCTGCTGCCACCGCTGAGCAATAACTAGCATAACCCCTTGGGGCCTCTAAACGGGTCTTGAGGGGTTTTTTGCTGAAAGCCAATTCTGATTAGAAAAACTCATCGAGCATCAAATGAAACTGCAATTTATTCATATCAGGATTATCAATACCATATTTTTGAAAAAGCCGTTTCTGTAATGAAGGAGAAAACTCACCGAGGCAGTTCCATAGGATGGCAAGATCCTGGTATCGGTCTGCGATTCCGACTCGTCCAACATCAATACAACCTATTAATTTCCCCTCGTCAAAAATAAGGTTATCAAGTGAGAAATCACCATGAGTGACGACTGAATCCGGTGAGAATGGCAAAAGCTTATGCATTTCTTTCCAGACTTGTTCAACAGGCCAGCCATTACGCTCGTCATCAAAATCACTCGCATCAACCAAACCGTTATTCATTCGTGATTGCGCCTGAGCGAGACGAAATACGCGATCGCTGTTAAAAGGACAATTACAAACAGGAATCGAATGCAACCGGCGCAGGAACACTGCCAGCGCATCAACAATATTTTCACCTGAATCAGGATATTCTTCTAATACCTGGAATGCTGTTTTCCCGGGGATCGCAGTGGTGAGTAACCATGCATCATCAGGAGTACGGATAAAATGCTTGATGGTCGGAAGAGGCATAAATTCCGTCAGCCAGTTTAGTCTGACCATCTCATCTGTAACATCATTGGCAACGCTACCTTTGCCATGTTTCAGAAACAACTCTGGCGCATCGGGCTTCCCATACAATCGATAGATTGTCGCACCTGATTGCCCGACATTATCGCGAGCCCATTTATACCCATATAAATCAGCATCCATGTTGGAATTTAATCGCGGCTTCGAGCAAGACGTTTCCCGTTGAATATGGCTCATAACACCCCTTGTATTACTGTTTATGTAAGCAGACAGTTTTATTGTTCATGATGATATATTTTTATCTTGTGCAATGTAACATCAGAGATTTTGAGACACAACGTGAGATCAAAGGATCTTC
```
:::

::::

::::{tab-item} pJL1-T7-TetO-PLA1
:sync: pla1

(seqviz-pjl1-teto-pla1)=

:::{seqviz} ./dna/pJL1-T7-TetO-PLA1.gb
:::

:::{admonition} Full sequence
:class: dropdown

```text
TTGAGATCGTTTTGGTCTGCGCGTAATCTCTTGCTCTGAAAACGAAAAAACCGCCTTGCAGGGCGGTTTTTCGAAGGTTCTCTGAGCTACCAACTCTTTGAACCGAGGTAACTGGCTTGGAGGAGCGCAGTCACCAAAACTTGTCCTTTCAGTTTAGCCTTAACCGGCGCATGACTTCAAGACTAACTCCTCTAAATCAATTACCAGTGGCTGCTGCCAGTGGTGCTTTTGCATGTCTTTCCGGGTTGGACTCAAGACGATAGTTACCGGATAAGGCGCAGCGGTCGGACTGAACGGGGGGTTCGTGCATACAGTCCAGCTTGGAGCGAACTGCCTACCCGGAACTGAGTGTCAGGCGTGGAATGAGACAAACGCGGCCATAACAGCGGAATGACACCGGTAAACCGAAAGGCAGGAACAGGAGAGCGCACGAGGGAGCCGCCAGGGGGAAACGCCTGGTATCTTTATAGTCCTGTCGGGTTTCGCCACCACTGATTTGAGCGTCAGATTTCGTGATGCTTGTCAGGGGGGCGGAGCCTATGGAAAAACGGCTTTGCCGCGGCCCTCTCACTTCCCTGTTAAGTATCTTCCTGGCATCTTCCAGGAAATCTCCGCCCCGTTCGTAAGCCATTTCCGCTCGCCGAACTGAACTCCACCTAATGTCTTGGAGATTGTCGGATAGCGCGGAATAGGATTGTGCCCTCTGAGCGGATAACAATTTCACACAGGAAACAGCTATGACCATGACACATGCATCCACCATCGCAGACTTATCATCACTGAGCCTCCACCTAGCCTTCATGCGTTGGCCATTGCTTCCCACGGCTTCTGTTCCGCCATACTCGAGATAACTTTATCGATACCATGTGCAGTCAGTGAACGATCCAGGTGTTTTGAGGGACGCCAGTCATCAATGCCACTCAATGTATCGTTGTTCGCTAAGGTAATTTTATGACCAATAGCGTCTGGGATGAGGCTTGTTGATTCTTGTGTCCCAGTAAGCATATCGTATTGTTCGCTATAGCGACGGATCCCACCGGCCTGGGCATCCTGTTTGGCTGCCGCAGGGTCAATTCCCATACGATTAAGCGTATAATCTGACACCCCAGCTGCGTTAAAAGTAACAGCCACAGTCCCTGTAGCCAATGCAGCCGTTGCGGCGAGGCCGCCCCCTAAGCTATGGCCGGCAATAACAAGCGCGTCGCCGAAGGCGGCTTTAGCAGATTTTGCCAAGCTGACAGCCTGATTATACTGTACATCGTCGTATCCGGTCGCTTGACGGACGTTGCTCAACCAATCTCGCATATCATTGGTCCCAGCAAAAGCAAGAACGTACTGCTGGTTATCCGTATAAATCCCTGCTTGAAAGCCGGAAGCGGCGTCCTGCAGACTTGCCGGATCTATACCTGCTCCTAACAACGCATCAGCTGACAGGCGGTTGAACCCTTCGACACCCTGTGAACCGGTTGAATAAACATCTTTAGCGAGCAGCGCCAAAGTATAGTCTCCTTTCTGTGGCTGCTGCCCGCGCGTGACTCCTTGATTAGCTGCCGCCGGAGCGGCGGCAGAGATTTCGGAGACGAGGGTATTGAGCAATGATTGGGCATTGAGGGAGTTCTGACTCAGGGTTGCGACAGGGGCTTTTGTAGCGCTCGCTTCCACAGGCTGACTAGAAGACAACGGTTCCGGCTGTGTACGGACCATTGGCGGTTGAATAGCAGCGGGCGCGATAGCCGATGTAAAAGACAGTGACATAGACATATGTATATCTCCTTCTTAAAGTTAAACAAAATTATTTCTAGAGGGAAACCGTTGTGGTCTCTCTATCACTGATAGGGATCCCTATAGTGAGTCGTATTAAGGTCAGGCGGAATGGCACTTCCTTATTCCAGATGCGTGCGGATTATGCATGACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGCTTGTGGTGGATCACAGTTATTGGAGACTTCCTTGGCCGTACGATGGGTTTTGTTTCAGGTATCTGGCACTTTTCGGGGAAATGTGCGCGGAACCCCTATTTGTTTATTTTTCTAAATACATTCAAATATGTATCCGCTCATGAGACAATAACCCTGATAAATGCTTCAATAATATTGAAAAAGGAAGAGTATGAGTATTCAACATTTCCGTGTCGCCCTTATTCCCTTTTTTGCGGCATTTTGCCTTCCTGTTTTTGCTCACCCAGAAACGCTGGTGAAAGTAAAAGATGCTGAAGATCAGTTGGGTGCACGAGTGGGTTACATCGAACTGGATCTCAACAGCGGTAAGATCCTTGAGAGTTTTCGCCCCGAAGAACGTTTTCCAATGATGAGCACTTTTAAAGTTCTGCTATGTGGCGCGGTATTATCCCGTATTGACGCCGGGCAAGAGCAACTCGGTCGCCGCATACACTATTCTCAGAATGACTTGGTTGAGTACTCACCAGTCACAGAAAAGCATCTTACGGATGGCATGACAGTAAGAGAATTATGCAGTGCTGCCATAACCATGAGTGATAACACTGCGGCCAACTTACTTCTGACAACGATCGGAGGACCGAAGGAGCTAACCGCTTTTTTGCACAACATGGGGGATCATGTAACTCGCCTTGATCGTTGGGAACCGGAGCTGAATGAAGCCATACCAAACGACGAGCGTGACACCACGATGCCTGTAGCAATGGCAACAACGTTGCGCAAACTATTAACTGGCGAACTACTTACTCTAGCTTCCCGGCAACAATTAATAGACTGGATGGAGGCGGATAAAGTTGCAGGACCACTTCTGCGCTCGGCCCTTCCGGCTGGCTGGTTTATTGCTGATAAATCTGGAGCCGGTGAGCGTGGCTCTCGCGGTATCATTGCAGCACTGGGGCCAGATGGTAAGCCCTCCCGTATCGTAGTTATCTACACGACGGGGAGTCAGGCAACTATGGATGAACGAAATAGACAGATCGCTGAGATAGGTGCCTCACTGATTAAGCATTGGTAACTGTCAGACCAAGTTTACTCATATATACTTTAGATTGATTTAAAACTTCATTTTTAATTTAAAAGGATCTAGGTGAAGATCCTTGAATTGCCATTATCAACAAGTTTGTACAAAAAAGCAGGCTCCGAATTGGTATCACGAGGACGATTTGAAGCCCCCTACCCATGGACGGCGGCTTTGTTGAATAGAGCGTCAGACTTAATAAGATGATCTTC
```
:::

::::

:::::

# Protocol

Vesicles were prepared at a 9:1 POPC:cholesterol ratio at a final lipid concentration of 20 mM, hydrated in 200 µL of BioUltra Mineral Oil, with 0.1 mol% 18:1 Liss Rhodamine PE as a membrane dye. We omitted the membrane dye for microscopy samples and replaced it with a volume marker, Albumin from Bovine Serum (BSA), Alexa Fluor™ 647 conjugate (OA647). For plating, we combined vesicles 1:1 with either OS or hydrogel, and we crosslinked the gel samples under 405 nm light for 60 s. The gel consisted of 4-arm PEG-norbornene (PEG-4NB) at 80 mM, 4-arm Poly(ethylene glycol) Thiol (PEG-4SH) at 70 mM, and the photoinitiator lithium phenyl-2,4,6-trimethylbenzoylphosphinate (LAP) at 16.9 mM, all dissolved in PBS buffer (OP DevNote). CPRG and aTc were added after gelation rather than before, because CPRG bleaches after 60 s of exposure to 405 nm light.

We made GUVs by double emulsion following the Nucleus Developer Note mk0407 (Kelly, 2026) and resuspended them in 100 µL of OS. OS contained 400 mM glucose and 800 mM HEPES, prepared from 2 M glucose and 1 M HEPES stocks, and was used throughout for both the suspended and gel-embedded samples.

Cell-free reactions were assembled in Nucleus Base Cytosol, following the Nucleus [Assemble Base Cytosol](https://docs.nucleus.engineering/docs/processes/assemble-base-cytosol/main) process, at the reference ratios, scaled to a 25 µL reaction.

:::{table} Cell-free reaction, per 25 µL.
:label: tbl-cellfree
:align: center

| Component | Per 25 µL reaction |
| --- | --- |
| Small Molecule Mix (SMix) | 7.5 µL |
| tRNA | 2.5 µL |
| Protein Mix (PMix) | 3.0 µL |
| Ribosomes | 4.5 µL |
| RNase Inhibitor | 1.25 µL |
| Sucrose | 3.4 mg, weighed in as solid |
| Plasmid DNA | to 1 nM final |
| CF-TetR | sample dependent; 2.5 µL worked best ({ref}`fig-2-tetr-source-comparison`) |
| β-galactosidase (Stock 125 U/mL) | 0.5 µL |
| OA647 | 0.5 µL, confocal samples only |
| Nuclease-free H₂O | to 25 µL |
:::

We weighed sucrose directly into the tube as a solid (3.4 mg per 25 µL of reaction volume), scaled by the number of reactions, then added the remaining master mix components and dissolved the sucrose by pipetting. For the encapsulated TetO-PLA1 sensor, we added 0.5 µL of purified β-galactosidase (125 U/mL stock) to the master mix to a final concentration of 2.5 U/mL in each 25 µL reaction. We also added the volume marker OA647 at 0.5 µL per 25 µL reaction when preparing confocal samples. Before adding an equal volume of master mix to each condition, we combined the DNA, CF-TetR, and water in separate tubes per condition and incubated them at 37 °C for 10 min to let the repressor bind the operator.

After gelation or suspension, we added CPRG to the outside of the vesicles to a final concentration of 5 mM, along with aTc, and read the samples for 3–5 h. We kept everything on ice from assembly until the sample went onto the plate reader or confocal.

# Data acquisition and analysis

All measurements were on encapsulated samples, except the aTc poisoning control in {ref}`fig-4-bulk-atc-poisoning`, which we ran in bulk reactions.

We read all samples in 96-well glass-bottom black plates treated with 2 wt% bovine serum albumin (BSA) for at least 20 min, then removed the BSA before adding the sample. On the plate reader (SpectraMax iD3, 37 °C, high gain), we measured color change as absorbance at 575 nm for the CPRG cleavage product, CPR, and GFP as fluorescence at ex/em 475/515.

We imaged encapsulated samples on a Nikon Eclipse Ti2 confocal with a 20× air objective, exciting GFP at 488 nm (ex/em 510/550, intensity 10.00, gain 60) and OA647 at 640 nm (ex/em 644/720, intensity 3.00, gain 90). These samples used OA647 as a volume marker instead of the membrane dye. We imaged at room temperature rather than 37 °C, so expression rates here aren't directly comparable to the plate-reader time courses.

We corrected microscopy signal for background and vesicle size: corrected fluorescence = (integrated density − (total vesicle area × mean background fluorescence)), referenced to t₀. This correction normalizes for vesicle size and background fluorescence.

# Results

## GUVs survive photopolymerization

Before testing induction, we confirmed that vesicles remain stable and allow for expression after embedding and crosslinking. We encapsulated a constitutive GFP cell-free reaction, then either pipetted the vesicles into OS or set them in PEG-4NB gel ({ref}`fig-1-guv-gfp-gel-vs-os`). We exposed both samples to 405 nm light for 60 s; only the PEG-4NB samples crosslinked, so the OS samples serve as a light-exposure control, and any difference between the two is attributable to the gel rather than light exposure.

Encapsulated GFP was expressed for over 10 h in both gel and solution, and the hydrogel samples reached higher corrected fluorescence than the OS samples ({ref}`fig-1-guv-gfp-gel-vs-os`). No-DNA controls both had minimal signal. Confocal imaging showed GFP signal colocalized with the OA647-labelled vesicles, so expression is happening inside intact vesicles rather than in leaked lysate. Neither light exposure nor the gel destroys the vesicles or the cell-free reaction inside them, making the patterned-gel format viable.

:::{figure} ./figures/fig1-guv-gfp-gel-vs-os.png
:label: fig-1-guv-gfp-gel-vs-os
:align: center
:width: 95%
Constitutive GFP expression in GUVs in PEG-4NB hydrogel or OS. Left: corrected fluorescence over 10 h, with and without DNA, in each format. Corrected fluorescence = (integrated density − (total vesicle area × mean background fluorescence))_t₀. The confocal image on the right shows GUVs embedded in a crosslinked PEG-4NB hydrogel. Left micrograph: OA647 volume marker (pink); middle micrograph: cell-free expressed GFP (green); right micrograph: overlay of both channels. Scale bars 20 µm.
:::

## CF-TetR provides the tightest repression

We compared repressor sources on TetO-deGFP at 1 nM DNA: commercially purified TetR, TetR purified in-house through a Northwestern University core facility, and CF-TetR at two volumes. We compared each on repression relative to the constitutive control and on recovery after adding 20 µM aTc.

CF-TetR provided the best repression and signal recovery with aTc induction ({ref}`fig-2-tetr-source-comparison`). It repressed deGFP far more than the commercial preparation, while the core-facility preparation showed almost no repression, and expression still recovered on aTc. Here, 2.5 µL of CF-TetR gave the best repression and induction and was used in all subsequent reactions.

:::{figure} ./figures/fig2-tetr-source-comparison.png
:label: fig-2-tetr-source-comparison
:align: center
:width: 80%
TetR source comparison. TetO-deGFP RFU at 2 h with 1 nM DNA, 9:1 POPC:cholesterol membranes, and 20 µM aTc. MedChem is commercially purified TetR at 500 nM; Foundry is TetR purified in-house through a Northwestern University core facility, at 200 nM; CFPS is CF-TetR, at 1.5 and 2.5 µL. Bars indicate TetO-regulated GFP expression with repression with TetR added, and sensor induction with aTc. The boxed condition was used in all subsequent reactions.
:::

## TetO-PLA1 responded backwards

With TetO-PLA1 and β-galactosidase encapsulated, and CPRG supplied externally, adding aTc should increase absorbance at 575 nm, but the opposite occurred. Across a titration from 0 to 5 µM in gel, absorbance fell steadily with increasing aTc in both the +TetR and −TetR samples.

The −TetR control is informative because, without a repressor, aTc has nothing to act on to alter absorbance. Since absorbance still decreases, this suggests aTc may be interacting with another part of the system.

:::{figure} ./figures/fig3-teto-pla1-dose-response.png
:label: fig-3-teto-pla1-dose-response
:align: center
:width: 70%
TetO-PLA1 response in gel, ±TetR. Absorbance at 575 nm after 5 h. Dotted lines mark the low-aTc region examined later.
:::

Three separate aTc effects were identified. Each becomes more pronounced as aTc increases, and each drives the readout in the opposite direction we would expect, with decreased absorbance and GFP expression.

**Cell-free poisoning.** In bulk with no TetR present at all, 20 µM aTc cut TetO-deGFP expression by roughly a quarter ({ref}`fig-4-bulk-atc-poisoning`). With no repressor to bind, this is a direct cost to the cell-free reaction. Less protein made means less PLA1, less lysis, and less color change, which leads to the inversion we see in {ref}`fig-3-teto-pla1-dose-response`.

**Autofluorescence.** In the encapsulated GFP titration, the t = 0 signal rose roughly three-fold from 0 to 1 µM aTc, before any expression could have occurred ({ref}`fig-5-encapsulated-atc-titration-confocal`). This shows that aTc fluoresces in the GFP channel, and so at high concentrations some of the measured signal comes from aTc itself rather than expressed GFP.

**Membrane partitioning.** Confocal imaging of the same TetO-GFP vesicles shows where the GFP signal sits, not just how much of it there is. At 1 µM, the signal fills the vesicle lumens. As aTc increases, progressively less GFP is in the lumen, and more green outlines the membrane, until at 10 µM most of the signal appears as rings and scattered puncta rather than filled vesicles ({ref}`fig-5-encapsulated-atc-titration-confocal`). This supports the hypothesis that aTc partitions into the bilayer and inhibits expression inside the vesicle.

:::{figure} ./figures/fig4-bulk-atc-poisoning.png
:label: fig-4-bulk-atc-poisoning
:align: center
:width: 70%
aTc inhibits expression without TetR. 0 nM TetR, ± 20 µM aTc, bulk reaction.
:::

:::{figure} ./figures/fig5-encapsulated-atc-titration-confocal.png
:label: fig-5-encapsulated-atc-titration-confocal
:align: center
:width: 95%
Encapsulated TetR-regulated expression with varying aTc concentrations. Left: GFP fluorescence at t = 0 and t = 10 h over 0–1 µM aTc, mean ± SD. The t = 0 trace climbs with aTc before any expression has occurred. Right: confocal images at 1, 5 and 10 µM aTc; green is GFP, pink is the OA647 volume marker. Lumenal signal at 1 µM gives way to membrane-associated rings and puncta by 10 µM. Scale bars 50 µm.
:::

## aTc titration identifies 0.25 µM as the usable concentration

All three effects scale with increasing aTc, so we titrated finely from 0 to 0.75 µM across encapsulated reactions in OS and in PEG-4NB gel to see whether any concentration induces the sensor before poisoning takes over. The signal holds steady up to about 0.25 µM, then declines above it ({ref}`fig-6-fine-atc-titration`). Encapsulated reactions in OS and in gel turn over at the same concentration, indicating that aTc, rather than the gel, sets the limit of concentration.

0.25 µM was picked as the working concentration, with 0.1–0.5 µM as the usable range. This is an order of magnitude below the 1–10 µM first tested, and well below the concentrations at which poisoning, autofluorescence, and membrane partitioning become significant.

:::{figure} ./figures/fig6-fine-atc-titration.png
:label: fig-6-fine-atc-titration
:align: center
:width: 80%
Fine aTc titration in both formats. TetO-PLA1 reactions read as absorbance at 575 nm: encapsulated in PEG-4NB hydrogel (first panel) and encapsulated in OS (second). Dotted line marks 0.25 µM in each; both OS and gel maintain steady expression levels until aTc concentrations above 0.25 µM.
:::

## Programmed color change in a patterned gel

We then tested the working concentration in a spatially patterned gel: a central cross and four corner squares, each gelled with encapsulated TetO-PLA1 reactions, with or without TetR inside the vesicles. We supplied CPRG at 5 mM and aTc outside the vesicles, as in the other experiments, with aTc present in some regions and absent in others.

The result is the first clean demonstration of the intended behavior ({ref}`fig-7-patterned-gel`). The cross, carrying TetR and 0.25 µM aTc, went bright red over 2.5 h while the corner squares with TetR and no aTc stayed orange-yellow. Color change was confined to the patterned region and followed the program rather than diffusing across the gel. The lower corners are the control that matters here: same gel, same TetR, no aTc, and little to no color developed in them. The cross against those corners is therefore a ±aTc comparison within the gel format, and it runs in the intended direction, which the dose series in {ref}`fig-3-teto-pla1-dose-response` never did at 1 to 10 µM.

The constitutive corners with 0.25 µM aTc came out less red than expected. We hypothesize that, without TetR to bind free aTc, it may impose the same cost on the cell-free reaction seen in {ref}`fig-4-bulk-atc-poisoning`, which would explain why those wells underperform while the induced cross does not.

:::{figure} ./figures/fig7-patterned-gel.png
:label: fig-7-patterned-gel
:align: center
:width: 95%
Spatially patterned PEG-4NB gel at 0.25 µM aTc. Each region contains encapsulated TetO-PLA1 reactions in PEG-4NB, with 5 mM CPRG outside the vesicles throughout. Cross: vesicles carrying TetR, 0.25 µM aTc outside. Upper corners: vesicles carrying constitutive PLA1 and no TetR, 0.25 µM aTc outside. Lower corners: vesicles carrying TetR, no aTc. Images at t = 0, 30 min, and 2.5 h.
:::

## Reproduced aTc poisoning effect at b.next lab

As all previous experiments were performed at our home laboratory at Northwestern University, we repeated the aTc titration in {ref}`fig-6-fine-atc-titration` at b.next. We wanted to again test encapsulated reactions in OS at low aTc concentrations to observe poisoning effects. However, this system differed in one respect: we moved β-galactosidase into its own vesicle population at 50 U/mL, separate from the vesicles carrying the TetO-PLA1 reaction, to reduce sensor leakage. CPRG was supplied outside at 5 mM, with aTc across the titration. Color developed fastest at 0.1 µM aTc and nearly as fast at 0.025 µM, while 0.5 µM finished below the uninduced control ({ref}`fig-8-two-vesicle-bnext`). The same poisoning seen in the earlier encapsulated studies appears here at 0.5 µM.

:::{figure} ./figures/fig8-two-vesicle-bnext.png
:label: fig-8-two-vesicle-bnext
:align: center
:width: 80%
CF-TetR and pOpen-PLA in a two-vesicle system at b.next. Vesicles in OS, with one population carrying β-galactosidase at 50 U/mL and the other the TetO-PLA1 reaction, and 5 mM CPRG outside. Absorbance at 575 nm over 15 h at 0, 0.025, 0.1, and 0.5 µM aTc.
:::

# Conclusion

The backward response is what sent us looking at aTc itself. Once we found that poisoning of the cell-free reaction, autofluorescence, and partitioning into the bilayer all scaled with aTc, we reduced the aTc concentration, and patterning worked once we dropped to 0.25 µM.

So the system works, but only in a window much narrower and much lower than the concentrations usually quoted for aTc induction. Here, at 1–10 µM, those three effects outweigh the induction they were meant to drive. At 0.25 µM, the reaction runs as designed and, on a patterned gel, produces a spatially confined color change. We saw the same concentration dependence when we repeated the titration at b.next in a two-vesicle system, where 0.5 µM aTc already finished below the uninduced control, so this does not appear to be specific to one lab.

Three observations are worth recording even though none is tested here. The commercial TetR preparation contains surfactants, which may inhibit the cell-free reaction and explain part of its underperformance relative to CF-TetR. The commercial TetR also has a His-SUMO tag, which could cause steric hindrance and prevent proper binding to the operator required for repression. Additionally, the constitutive corners of the patterned gel came out less red than expected, potentially due to a few reasons: the corner squares hold less material than the central cross, so fewer vesicles contribute to the color, and with no TetR present, there is nothing for the aTc to bind, leaving it free to act on the reaction rather than being titrated out by the repressor.

We should note that CF-TetR is added as a volume of cell-free material rather than as purified protein in buffer, so the comparison in {ref}`fig-2-tetr-source-comparison` is confounded with whatever else that volume carries. Running a matched preparation without the repressor would separate what the repressor contributes from what the material it arrives in contributes. Until we run that control, we cannot say whether the surfactants or the His-SUMO tag actually account for the difference.

# Sources

- [Assemble Base Cytosol](https://docs.nucleus.engineering/docs/processes/assemble-base-cytosol/main) — Nucleus process for the cytosol lysate and its components
- [Detector: tetR-aTc](https://docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec) — Nucleus module specification for TetR-regulated expression and aTc induction
- Plasmid sequences: pJL1_T7-TetO-GFP (2,486 bp, Kan) and pJL1_T7-TetO-PLA1 (3,223 bp, Amp), verified in-house
- [MedChemExpress TetR Protein, E.coli (His-SUMO)](https://www.medchemexpress.com/recombinant-proteins/tetr-protein-e-coli-his-sumo.html?srsltid=AU7gw4VALCBnREgbDIcQuhxO7wnq7zq9gReuYQD5GwSqa0H9yv51-7sS)
- Lipids: POPC and cholesterol (ovine) 9:1, 0.1 mol% 18:1 Liss Rhodamine PE (Avanti)
- CPRG, chlorophenol red-β-D-galactopyranoside, with purified β-galactosidase (Sigma-Aldrich)
- Kelly, M. (2026). [Double emulsion optimization: inner solution, lipid concentration, and composition](https://devnotes.nucleus.engineering/articles/mk0407). Nucleus Developer Notes, mk0407 — GUV preparation protocol and outer solution formulation
- Ojaswita's devnote — REVIEW: not linked in the source; likely this board's `devnote-op-20261001-luv-gel-pla`, see Open items
