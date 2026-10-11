// `{platemap}` embeds a Nucleus platemap CSV/TSV as an interactive 96-well
// plate map, the same way `{seqviz}` embeds a sequence file:
//
//   :::{platemap} ./experiments/build-platemap.csv
//   :height: 560px
//   :::
//
// The directive stores the raw path/URL at parse time; the transform below
// reads and parses the file at build time and rewrites the node into a
// native anywidget node that `platemap-widget.mjs` renders in the browser.
// Column names and the `Type` vocabulary follow
// `nucleus-devnote-archive-1/devnotes/2026-bhasin-platemaps/main.md`, ported
// into `nucleus-skills`' `build-platemap` skill as `platemap_common.py` --
// keep the two lists below in sync with that source if it changes.
import { readFileSync } from 'node:fs';

function collectNodes(tree, predicate, results = []) {
  if (predicate(tree)) results.push(tree);
  if (tree.children) tree.children.forEach((child) => collectNodes(child, predicate, results));
  return results;
}

const GITHUB_BLOB_URL = /^https:\/\/github\.com\/([^/]+)\/([^/]+)\/blob\/([^/]+)\/(.+)$/;

// Rewrite a normal "view file on GitHub" URL to the raw content URL, so authors
// can paste the link straight from their browser's address bar.
function toRawUrl(url) {
  const match = url.match(GITHUB_BLOB_URL);
  if (!match) return url;
  const [, owner, repo, ref, path] = match;
  return `https://raw.githubusercontent.com/${owner}/${repo}/${ref}/${path}`;
}

async function readSource(file) {
  if (/^https?:\/\//.test(file)) {
    const url = toRawUrl(file);
    const res = await fetch(url);
    if (!res.ok) throw new Error(`${res.status} ${res.statusText} for ${url}`);
    return res.text();
  }
  return readFileSync(file, 'utf8');
}

function detectDelimiter(file, text) {
  if (/\.(tsv|tab)$/i.test(file)) return '\t';
  if (/\.csv$/i.test(file)) return ',';
  const firstLine = text.split(/\r?\n/, 1)[0] ?? '';
  const tabs = (firstLine.match(/\t/g) ?? []).length;
  const commas = (firstLine.match(/,/g) ?? []).length;
  return tabs > commas ? '\t' : ',';
}

// Minimal RFC4180-style reader: quoted fields, embedded delimiters, "" escapes.
function parseDelimited(text, delimiter) {
  const rows = [];
  let row = [];
  let field = '';
  let inQuotes = false;
  const normalized = text.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
  const pushField = () => { row.push(field); field = ''; };
  const pushRow = () => { pushField(); rows.push(row); row = []; };
  for (let i = 0; i < normalized.length; i++) {
    const c = normalized[i];
    if (inQuotes) {
      if (c === '"') {
        if (normalized[i + 1] === '"') { field += '"'; i++; } else inQuotes = false;
      } else field += c;
    } else if (c === '"') {
      inQuotes = true;
    } else if (c === delimiter) {
      pushField();
    } else if (c === '\n') {
      pushRow();
    } else {
      field += c;
    }
  }
  if (field.length || row.length) pushRow();
  return rows.filter((r) => !(r.length === 1 && r[0] === ''));
}

function rowsToObjects(rows) {
  const [header, ...body] = rows;
  return body.map((cells) => Object.fromEntries(header.map((h, i) => [h, cells[i] ?? ''])));
}

// `platemap_common.PLATEMAP_COLUMNS` (required + recommended): everything
// else in the header is a composition field.
const REQUIRED_COLUMNS = ['Date', 'Experiment', 'Well', 'Name', 'Type'];
const SHARED_COLUMNS = [...REQUIRED_COLUMNS, 'Rxn Volume (uL)'];

const WELL_RE = /^([A-Ha-h])0?(\d{1,2})$/;
function parseWell(well) {
  const m = String(well ?? '').trim().match(WELL_RE);
  if (!m) return null;
  const col = parseInt(m[2], 10);
  if (col < 1 || col > 12) return null;
  return { row: m[1].toUpperCase(), col };
}

const platemapDirective = {
  name: 'platemap',
  doc: 'Render a Nucleus platemap CSV/TSV as an interactive 96-well plate map.',
  arg: {
    type: String,
    doc: 'Path or URL (e.g. a GitHub file link) to the platemap CSV/TSV, parsed at build time.',
  },
  options: {
    height: { type: String, doc: 'Height of the viewer (default 560px).' },
  },
  run(data) {
    return [
      {
        type: 'block',
        kind: 'platemap',
        data: {
          import: './platemap-widget.mjs',
          file: data.arg,
          height: data.options?.height ?? '560px',
        },
        children: [],
      },
    ];
  },
};

const platemapTransform = {
  name: 'platemap-parse',
  doc: 'Parses an incoming platemap CSV/TSV and rewrites the block as a native anywidget node.',
  stage: 'document',
  plugin: () => async (tree) => {
    const nodes = collectNodes(tree, (n) => n.type === 'block' && n.kind === 'platemap');
    await Promise.all(
      nodes.map(async (node) => {
        const { file, import: widgetImport, height } = node.data;
        try {
          const text = await readSource(file);
          const delimiter = detectDelimiter(file, text);
          const rows = rowsToObjects(parseDelimited(text, delimiter));
          if (!rows.length) throw new Error('no data rows found');
          const header = Object.keys(rows[0]);
          const missing = REQUIRED_COLUMNS.filter((c) => !header.includes(c));
          if (missing.length) throw new Error(`missing required column(s): ${missing.join(', ')}`);

          const compositionColumns = header.filter((c) => !SHARED_COLUMNS.includes(c)).slice(0, 3);
          const experiment = rows[0].Experiment ?? '';
          const wells = [];
          for (const r of rows) {
            const pos = parseWell(r.Well);
            if (!pos) {
              console.error(`[platemap] skipping row with unreadable Well "${r.Well}" in ${file}`);
              continue;
            }
            wells.push({
              row: pos.row,
              col: pos.col,
              type: (r.Type ?? '').trim(),
              name: r.Name ?? '',
              fields: compositionColumns.map((c) => ({ label: c, value: r[c] ?? '' })),
            });
          }

          // MyST's native anywidget renderer expects `type: "anywidget"` with `esm` + `model`.
          // `type: "block", kind: "anywidget"` is Curvenote-specific and silently does nothing
          // in standard mystmd/myst-theme.
          node.type = 'anywidget';
          node.esm = widgetImport;
          node.model = { experiment, wells, height };
          node.id = Math.random().toString(36).slice(2, 10);
          delete node.kind;
          delete node.data;
          delete node.children;
        } catch (err) {
          console.error(`[platemap] failed to load ${file}: ${err.message}`);
        }
      }),
    );
  },
};

const plugin = {
  name: 'Platemap Plugin for MyST Markdown',
  directives: [platemapDirective],
  transforms: [platemapTransform],
};

export default plugin;
