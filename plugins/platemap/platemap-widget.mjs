// Renders the `{platemap}` anywidget model (see `platemap.mjs`) as an 8x12
// grid of wells, one circle per well, filled by `Type` and labeled with the
// composition fields `platemap.mjs` picked out, on hover.
//
// Plain SVG/DOM, no React: unlike seqviz, nothing here needs a third-party
// rendering library. Colors are the `dataviz` skill's default categorical
// palette, slots 1-6 in its fixed order; see the note above `TYPE_COLOR_VAR`
// for why every well also carries a text code, not color alone.

const ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
const COLS = Array.from({ length: 12 }, (_, i) => i + 1);

const TYPE_ORDER = ['Sample', 'Standard', 'Blank', 'Control', 'Positive Control', 'Negative Control'];
const TYPE_CODE = {
  Sample: 'SPL',
  Standard: 'STD',
  Blank: 'BLK',
  Control: 'CTL',
  'Positive Control': 'C+',
  'Negative Control': 'C-',
};
// Six categories on a dense grid means any two can sit side by side, so this
// needs all-pairs CVD separation -- `validate_palette.js --pairs all` only
// clears that bar for the palette's first three slots. Past three, the skill
// says fold to "Other" or facet; neither fits a fixed six-value vocabulary,
// so every well also carries its `TYPE_CODE` text label -- identity never
// rests on hue alone here, in both color vision and dark/light/print modes.
const TYPE_COLOR_VAR = {
  Sample: '--pm-type-sample',
  Standard: '--pm-type-standard',
  Blank: '--pm-type-blank',
  Control: '--pm-type-control',
  'Positive Control': '--pm-type-positive-control',
  'Negative Control': '--pm-type-negative-control',
};

function canonicalType(raw) {
  const needle = String(raw ?? '').trim().toLowerCase();
  return TYPE_ORDER.find((t) => t.toLowerCase() === needle) ?? null;
}

const SVG_NS = 'http://www.w3.org/2000/svg';
function svgEl(tag, attrs = {}) {
  const node = document.createElementNS(SVG_NS, tag);
  for (const [k, v] of Object.entries(attrs)) node.setAttribute(k, String(v));
  return node;
}

function render({ model, el }) {
  const wells = model.get('wells') ?? [];
  const experiment = model.get('experiment') ?? '';
  const height = model.get('height') ?? '560px';

  const byWell = new Map(wells.map((w) => [`${w.row}${w.col}`, w]));
  const presentTypes = TYPE_ORDER.filter((t) => wells.some((w) => canonicalType(w.type) === t));

  const cell = 46;
  const padLeft = 32;
  const padTop = 32;
  const gridW = padLeft + COLS.length * cell + 12;
  const gridH = padTop + ROWS.length * cell + 12;
  const legendH = presentTypes.length ? 40 : 0;
  const totalH = gridH + legendH;

  const root = document.createElement('div');
  root.className = 'pm-root';
  root.style.cssText = `position:relative; width:100%; height:${
    typeof height === 'number' ? `${height}px` : height
  }; display:flex; flex-direction:column; font-family:system-ui,-apple-system,"Segoe UI",sans-serif;`;

  const style = document.createElement('style');
  style.textContent = `
    .pm-root {
      --pm-surface: #fcfcfb;
      --pm-ink: #0b0b0b;
      --pm-ink-secondary: #52514e;
      --pm-ink-muted: #898781;
      --pm-gridline: #e1e0d9;
      --pm-empty: #fcfcfb;
      --pm-unknown: #c3c2b7;
      --pm-type-sample: #2a78d6;
      --pm-type-standard: #eb6834;
      --pm-type-blank: #1baf7a;
      --pm-type-control: #eda100;
      --pm-type-positive-control: #e87ba4;
      --pm-type-negative-control: #008300;
    }
    @media (prefers-color-scheme: dark) {
      :root:not([data-theme="light"]) .pm-root {
        --pm-surface: #1a1a19;
        --pm-ink: #ffffff;
        --pm-ink-secondary: #c3c2b7;
        --pm-ink-muted: #898781;
        --pm-gridline: #2c2c2a;
        --pm-empty: #1a1a19;
        --pm-unknown: #52514e;
        --pm-type-sample: #3987e5;
        --pm-type-standard: #d95926;
        --pm-type-blank: #199e70;
        --pm-type-control: #c98500;
        --pm-type-positive-control: #d55181;
        --pm-type-negative-control: #008300;
      }
    }
    :root[data-theme="dark"] .pm-root {
      --pm-surface: #1a1a19;
      --pm-ink: #ffffff;
      --pm-ink-secondary: #c3c2b7;
      --pm-ink-muted: #898781;
      --pm-gridline: #2c2c2a;
      --pm-empty: #1a1a19;
      --pm-unknown: #52514e;
      --pm-type-sample: #3987e5;
      --pm-type-standard: #d95926;
      --pm-type-blank: #199e70;
      --pm-type-control: #c98500;
      --pm-type-positive-control: #d55181;
      --pm-type-negative-control: #008300;
    }
    .pm-root svg { background: var(--pm-surface); width: 100%; height: 100%; }
    .pm-root .pm-header-text { fill: var(--pm-ink-muted); font-size: 11px; }
    .pm-root .pm-well circle { stroke: var(--pm-gridline); stroke-width: 1; cursor: pointer; }
    .pm-root .pm-well-empty circle { fill: var(--pm-empty); stroke-dasharray: 2 2; }
    .pm-root .pm-code {
      font-size: 8.5px; font-weight: 600; fill: #ffffff; text-anchor: middle;
      paint-order: stroke; stroke: rgba(0,0,0,0.45); stroke-width: 2px; pointer-events: none;
    }
    .pm-root .pm-legend-label { fill: var(--pm-ink-secondary); font-size: 11px; }
    .pm-root .pm-title { font-size: 13px; font-weight: 600; color: var(--pm-ink-secondary); margin-bottom: 4px; }
    .pm-root .pm-tooltip {
      position: absolute; pointer-events: none; z-index: 10;
      background: var(--pm-ink); color: var(--pm-surface);
      padding: 6px 8px; border-radius: 4px; font-size: 12px; line-height: 1.4;
      max-width: 240px; opacity: 0; transform: translate(-50%, -100%);
      transition: opacity 0.08s ease; white-space: nowrap;
    }
    .pm-root .pm-tooltip > div:first-child { font-weight: 600; }
  `;
  root.appendChild(style);

  if (experiment) {
    const title = document.createElement('div');
    title.className = 'pm-title';
    title.textContent = experiment;
    root.appendChild(title);
  }

  const svg = svgEl('svg', {
    viewBox: `0 0 ${gridW} ${totalH}`,
    role: 'img',
    'aria-label': `96-well plate map${experiment ? ` for ${experiment}` : ''}`,
  });

  COLS.forEach((c, i) => {
    const t = svgEl('text', {
      x: padLeft + i * cell + cell / 2,
      y: padTop - 12,
      'text-anchor': 'middle',
      class: 'pm-header-text',
    });
    t.textContent = String(c);
    svg.appendChild(t);
  });
  ROWS.forEach((r, i) => {
    const t = svgEl('text', {
      x: padLeft - 16,
      y: padTop + i * cell + cell / 2 + 4,
      'text-anchor': 'middle',
      class: 'pm-header-text',
    });
    t.textContent = r;
    svg.appendChild(t);
  });

  const tooltip = document.createElement('div');
  tooltip.className = 'pm-tooltip';
  root.appendChild(tooltip);

  function showTooltip(evt, well) {
    tooltip.replaceChildren();
    const lines = [
      `Well ${well.row}${well.col}`,
      well.name,
      canonicalType(well.type) ?? well.type ?? '(no type)',
      ...well.fields.filter((f) => f.value !== '').map((f) => `${f.label}: ${f.value}`),
    ].filter(Boolean);
    for (const text of lines) {
      const line = document.createElement('div');
      line.textContent = text;
      tooltip.appendChild(line);
    }
    const rect = root.getBoundingClientRect();
    tooltip.style.left = `${evt.clientX - rect.left}px`;
    tooltip.style.top = `${evt.clientY - rect.top - 8}px`;
    tooltip.style.opacity = '1';
  }
  function hideTooltip() {
    tooltip.style.opacity = '0';
  }

  ROWS.forEach((r, ri) => {
    COLS.forEach((c, ci) => {
      const well = byWell.get(`${r}${c}`);
      const cx = padLeft + ci * cell + cell / 2;
      const cy = padTop + ri * cell + cell / 2;
      const radius = cell * 0.36;
      const type = well ? canonicalType(well.type) : null;
      const g = svgEl('g', { class: well ? 'pm-well' : 'pm-well-empty' });
      const circle = svgEl('circle', { cx, cy, r: radius });
      circle.style.setProperty(
        'fill',
        well ? `var(${type ? TYPE_COLOR_VAR[type] : '--pm-unknown'})` : 'var(--pm-empty)',
      );
      g.appendChild(circle);
      if (well) {
        const code = svgEl('text', { x: cx, y: cy + 3, class: 'pm-code' });
        code.textContent = type ? TYPE_CODE[type] : (well.type || '?').slice(0, 4).toUpperCase();
        g.appendChild(code);
        g.addEventListener('pointerenter', (evt) => showTooltip(evt, well));
        g.addEventListener('pointermove', (evt) => showTooltip(evt, well));
        g.addEventListener('pointerleave', hideTooltip);
      }
      svg.appendChild(g);
    });
  });

  if (presentTypes.length) {
    const ly = gridH + 20;
    let lx = padLeft;
    for (const type of presentTypes) {
      const sw = svgEl('circle', { cx: lx + 6, cy: ly, r: 6 });
      sw.style.setProperty('fill', `var(${TYPE_COLOR_VAR[type]})`);
      svg.appendChild(sw);
      const label = svgEl('text', { x: lx + 16, y: ly + 4, class: 'pm-legend-label' });
      label.textContent = `${TYPE_CODE[type]} ${type}`;
      svg.appendChild(label);
      lx += 28 + label.textContent.length * 5.5;
    }
  }

  root.appendChild(svg);
  el.appendChild(root);

  return () => {};
}

export default { render };
