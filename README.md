# devstudio-board

A local status board for the DevStudio pipeline, and the DevNote archive it
writes to. Clone this repo, run the board, and it reads Google Drive
(Log folders, DevNote drafts) and writes DevNote(M) builds into `devnotes/`
in this same repo.

## What the board does

- Shows every Log folder in `San Francisco Node/log` and every DevNote in
  `San Francisco Node/devnotes`, read live from Drive.
- Shows which Log folders feed into which DevNote, from a shared map kept in
  Drive (`devnotes/devnote-log-map.json`) so every teammate reads the same
  answer instead of re-deriving it.
- Lets you create a new Log folder from the template.
- Lets you pool a set of Log folders into a new DevNote draft.
- Lets you convert a reviewed DevNote(G) draft into a MyST build
  (`devnote-g-to-devnote-m`), fetch its supporting assets
  (`assemble-devnote-assets`), preview it locally, and submit a Curvenote
  draft for review.
- Rebuilds a DevNote(M) in place on a second run. It refuses to rebuild over
  uncommitted changes, and it 3-way merges your hand edits (a changed figure
  caption, a reordered table of contents) against the newly generated file
  instead of overwriting them.

Every step waits for a click. The board never runs a pipeline step on its
own.

## Layout

| Path | Holds |
| --- | --- |
| `board.py` | The server: Drive reads and writes, skill invocations, job tracking, the 3-way merge, the Curvenote calls |
| `fleet.html` | The multi-DevNote board (Log / DevNote / Docs columns) |
| `board.html` | The single-DevNote detail view |
| `demo.py` | Synthetic data for `--demo` mode |
| `passport.py` | A record format for a DevNote's history (author, decisions, checks) — not yet wired into the skills that would write it |
| `devnotes/` | DevNote(M) builds. One folder per DevNote. See `devnotes/README.md`. |
| `docs/` | Docs(M) pages produced from a reviewed DevNote. Not wired up yet. |
| `resources/` | Material shared across DevNotes: templates, reference constructs. |
| `plugins/seqviz/` | Shared Curvenote plugin, referenced from a DevNote as `../../plugins/seqviz/seqviz.mjs` |
| `.devstudio/` | Config the board reads: venue name, Drive folder ids, naming conventions |
| `.github/workflows/` | Curvenote CI, copied from `nucleus-eng/nucleus-devnote-archive-1` — see below |

## Requirements

- Python 3, no extra packages.
- The `claude` CLI on your PATH, signed in, with the `nucleus` plugin loaded
  (the skills this board calls: `devstudio-new-log`,
  `devstudio-log-to-devnote-g`, `devstudio-devnote-g-to-devnote-m`,
  `devstudio-assemble-devnote-assets`).
- The `curvenote` CLI on your PATH, signed in, for the preview and draft
  submission buttons.
- This repo cloned as a git checkout (not a zip). The board's rebuild guard
  needs git.

## Run it

```bash
python3 board.py --repo /path/to/a/nucleus-skills-plugin/checkout \
                  --out ./devnotes \
                  --port 8765
```

Open `http://localhost:8765`.

`--repo` is the working directory the `claude` CLI runs in for each button
press. It only needs the DevStudio skills loaded; it does not need to be
this repo.

`--out` is where DevNote(M) directories get written and rebuilt. Point it at
`./devnotes` in this checkout so builds are versioned by this repo's own
git history.

### Demo mode

```bash
python3 board.py --demo --port 8765
```

Runs the same interface against a made-up set of Logs and DevNotes. Nothing
in Drive is touched, and nothing is written to `devnotes/`. Use this to show
someone the tool before connecting it to real data.

## How Curvenote submission works

`.github/workflows/draft.yml` and `submit.yml` are copied from
`nucleus-eng/nucleus-devnote-archive-1` and are meant to stay identical to
it. If that repo's workflows change, copy the change here too — this repo
exists to test the same CI path, and a difference between the two makes the
test meaningless.

| Workflow | Fires on | Does |
| --- | --- | --- |
| `draft.yml` | pull request to `main` | Curvenote draft preview, link posted to the PR |
| `submit.yml` | push to `main` | the real submission to the venue |

So the production path is: branch, commit a DevNote(M) build, open a draft
PR, read the preview link CI posts to it, a TA merges, published. Nothing is
submitted from a laptop that way; `CURVENOTE_TOKEN` lives in this repo's
secrets, not on anyone's machine.

The board's own **Curvenote draft** button is a shortcut for testing: it
runs `curvenote submit --draft` directly from your machine, under your own
Curvenote token, bypassing the PR. It is faster to iterate with, but it is
not the production path above, and it does not go through this repo's CI.

Both workflows expect `path: devnotes/*`, so a DevNote(M) must sit directly
at `devnotes/<slug>/` — which is where the board writes it.

## Required secrets

`CURVENOTE_TOKEN`, set in this repo's settings, for both workflows. Without
it neither the draft preview nor the submission runs.

## Known gaps

- The Docs column and the `docs/` directory are placeholders. Nothing writes
  to them yet.
- The shared Log-to-DevNote map is derived by asking `claude -p` to read
  every DevNote's manifest, which can take several minutes cold. The board
  caches the result to disk and to Drive so this cost is paid once, not once
  per person who opens the board.
- `passport.py` is written but no skill appends to it yet.
- The venue in `.devstudio/board.json` and in the workflows is the real
  `bnext-devnotes` venue, the same one `nucleus-devnote-archive-1` submits
  to. A merge to `main` here publishes to the same place a merge there does.
  Change the venue name in both places if you want this repo isolated from
  the real venue.
