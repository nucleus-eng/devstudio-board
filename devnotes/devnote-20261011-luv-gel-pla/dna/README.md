# dna/

This directory holds the sequence files for the constructs `main.md` names.

Two GenBank files were linked on `log-devnote-draft.docx` on 2026-10-10:

| Construct in `main.md` | File |
| --- | --- |
| T7-EsaO-mNG | `t7pro-esao-ls1-mneongreen.gbk` |
| T7-EsaO-PLA1 | `t7pro-esao-ls1-pla1.gbk` |

Neither file is in `nucleus-eng/DNA`. Both still need submitting there before
this DevNote publishes.

Placed here 2026-10-22, after cross-checking both against this board's other
DevNotes. Each file's `ORIGIN` sequence matches its own `LOCUS` length
exactly: 1098 bp and 1350 bp. The one-byte-short defect that blocked
placement before is not present in these copies.

`t7pro-esao-ls1-mneongreen.gbk` is base-for-base identical to the verified
copy in
`devnotes/devnote-20261011-esao-esar-quorum-sensing/dna/t7pro-esao-ls1-mneongreen.gbk`
(Charlie Newell's EsaO/EsaR DevNote). This copy is missing two feature labels
the other carries, `epsilon enhancer` and `Strong RBS`. That is a labeling
gap, not a sequence difference.

`t7pro-esao-ls1-pla1.gbk` has no match in that DevNote, since its project
does not use PLA1. Its PLA1 CDS has an independent part-level match in
`devnotes/devnote-20261011-pla1-triggered-lysis-guvs/dna/pOpen-TetO-PLA.gb`.
That file carries the same 323-amino-acid translation, under T7/tetO instead
of T7/EsaO.
