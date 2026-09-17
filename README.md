# DevStudio board

A local status board for the DevStudio pipeline: Log folders in Google Drive,
DevNote(G) drafts, DevNote(M) MyST builds, and Curvenote draft submissions.
It runs on your machine, reads and writes Google Drive through the Claude
Code CLI, and never runs a step without you clicking a button first.

## What it does

- Shows every Log folder in `San Francisco Node/log` and every DevNote in
  `San Francisco Node/devnotes`, read live from Drive.
- Shows which Log folders feed into which DevNote, from a shared map kept in
  Drive so every teammate reads the same answer.
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

## Requirements

- Python 3, no extra packages.
- The `claude` CLI on your PATH, signed in, with the `nucleus` plugin loaded
  (the skills this board calls: `devstudio-new-log`,
  `devstudio-log-to-devnote-g`, `devstudio-devnote-g-to-devnote-m`,
  `devstudio-assemble-devnote-assets`).
- The `curvenote` CLI on your PATH, signed in, for the preview and draft
  submission buttons.
- A local checkout of a DevNote archive repo (see
  [nucleus-eng/devnotes-archive-devstudio](https://github.com/nucleus-eng/devnotes-archive-devstudio)),
  for `--out`.

## Run it

```bash
python3 board.py --repo /path/to/a/nucleus-skills-plugin/checkout \
                  --out /path/to/devnotes-archive-devstudio/devnotes \
                  --port 8765
```

Open `http://localhost:8765`.

`--repo` is the working directory the `claude` CLI runs in for each button
press. It only needs the DevStudio skills loaded; it does not need to be a
DevNote repo itself.

`--out` is where DevNote(M) directories get written and rebuilt. It must be
inside a git repository. The board refuses to rebuild a DevNote if that
directory has uncommitted changes, so commit after a build you want to keep.

### Demo mode

```bash
python3 board.py --demo --port 8765
```

Runs the same interface against a made-up set of Logs and DevNotes. Nothing
in Drive is touched. Use this to show someone the tool before they connect
it to real data, or to check a UI change with no Drive round trip.

## Files

| File | Holds |
| --- | --- |
| `board.py` | The server: Drive reads and writes, skill invocations, job tracking, the 3-way merge, the Curvenote calls |
| `fleet.html` | The multi-DevNote board (Log / DevNote / Docs columns) |
| `board.html` | The single-DevNote detail view |
| `demo.py` | Synthetic data for `--demo` mode |
| `passport.py` | A record format for a DevNote's history (author, decisions, checks) — not yet wired into the skills that would write it |

## Known gaps

- The Docs column is a placeholder. Nothing writes to it yet.
- The shared Log-to-DevNote map is derived by asking `claude -p` to read
  every DevNote's manifest, which can take several minutes cold. The board
  caches the result to disk and to a file in Drive
  (`devnotes/devnote-log-map.json`) so this cost is paid once, not once per
  person who opens the board.
- The Curvenote draft submit button runs `curvenote submit --draft` from
  your machine under your own token. It is a fast path for testing. The
  production path is a pull request to the archive repo, where GitHub
  Actions build the preview and later the real submission — see that repo's
  README.
- `passport.py` is written but no skill appends to it yet.
