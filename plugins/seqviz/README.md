Shared MyST plugin (`seqviz.mjs`) for the `{seqviz}` directive, used to render an
interactive plasmid map inline from a local `.gb`/`.dna` file in a devnote's `main.md`.

`node_modules/` is committed here (small, ~3M) because the CI pipeline
(`curvenote/actions`) never runs `npm install` for a devnote's own `package.json` —
without a real, installed `seqparse` dependency, any devnote using `{seqviz}` fails
in CI with `Cannot find package 'seqparse'`.

## Using this in a devnote

In the devnote's `curvenote.yml`, reference this file by relative path instead of
keeping a local copy:

```yaml
plugins:
  - lorem.mjs
  - ../../plugins/seqviz/seqviz.mjs
```

Don't add a local `seqviz.mjs`/`package.json` to the devnote itself — this shared
copy is the only one that should exist.

## Updating the dependency

```
cd plugins/seqviz
npm install <new-version>
```

Commit the updated `node_modules/`, `package.json`, and `package-lock.json` together.
