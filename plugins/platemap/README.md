Shared MyST plugin (`platemap.mjs`) for the `{platemap}` directive, used to render an
interactive 96- or 384-well plate map inline from a local (or GitHub-linked) Nucleus
platemap CSV/TSV in a devnote's `main.md`.

Pulled from `nucleus-eng/devnote-template` at commit `72b9987`
(2026-10-11, "Add platemap interactive plate map viewer as a standard feature"),
which is where this viewer was built and is kept canonical. Re-pull from there rather
than hand-editing a divergent copy here.

Unlike `../seqviz/`, this plugin has no third-party dependency (`platemap-widget.mjs`
renders plain SVG, no React, no `seqviz`-style npm package), so there is no
`node_modules/` to commit and no install step to run.

## Using this in a devnote

In the devnote's `curvenote.yml`, reference this file by relative path instead of
keeping a local copy:

```yaml
plugins:
  - ../../plugins/platemap/platemap.mjs
```

The widget file (`platemap-widget.mjs`, in this same directory) still needs its own
copy beside each devnote's `main.md` — mystmd resolves an anywidget's `esm` path
against the *document's* folder, not the plugin's, the same gotcha `seqviz-widget.mjs`
has. Copy `platemap-widget.mjs` into the devnote root alongside `main.md`; don't
reference it by a `../../` path.

## Required columns

`Date`, `Experiment`, `Well`, `Name`, `Type` — the Nucleus platemap schema,
`platemap_common.PLATEMAP_COLUMNS` in `nucleus-skills`' `build-platemap` skill. A file
missing any of these fails at build time with a clear error naming which column.
Anything else in the header is treated as a composition field; `:fields:` names which
ones to show on hover if the default (first three outside the required/recommended
columns) isn't right.

## Updating

Pull the two files fresh from `nucleus-eng/devnote-template` rather than editing here;
this copy exists only because mystmd plugins loaded by relative path can't be an
npm dependency of the host devnote project, the same reason `seqviz.mjs` is vendored
instead of installed.
