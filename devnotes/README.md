# devnotes/

Each subfolder here is one DevNote(M): `main.md`, `curvenote.yml`, and the
`experiments/`, `figures/`, `plasmids/`, `general/` directories the DevStudio
board writes and rebuilds.

A DevNote is not versioned by folder name. A rebuild writes over the same
folder, and git carries the history. Commit before you rebuild: the board
refuses to rebuild over uncommitted changes, and it 3-way merges your hand
edits (a changed figure caption, a reordered table of contents) against the
newly regenerated file. Uncommitted work cannot be merged against, only
committed work can.

To see what changed in a rebuild: `git diff -- devnotes/<slug>`
To undo a rebuild you have not committed yet:
`git restore --source=HEAD -- devnotes/<slug>`
