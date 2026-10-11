// Vizarr anywidget for DevNotes.
//
// A local copy of https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
// with two changes, each explained where it is made: styles are mirrored into
// the shadow root, and a viewer can set its own channel colors and contrast
// limits. The upstream file is kept beside this one as
// vizarr-viewer.upstream.js so the diff stays visible.
//
// THE BUG. Vizarr's control panel is built with Material-UI, which injects its
// rules as <style> tags in document.head. myst-theme mounts an anywidget inside
// a shadow root. A style tag in the document does not cross a shadow boundary,
// so the panel's markup arrives with none of its rules.
//
// Measured in a built DevNote on 2026-10-11. The shadow root held 18 MuiSlider
// elements and no style tags at all, against 21 style tags in document.head:
// 13 mentioning Mui, and 8 more carrying data-jss that mention it nowhere.
// Each set breaks something different. Without the Mui rules a slider is 0x0
// and only its label shows. Without the data-jss rules, which are vizarr's own
// makeStyles output, the panel has no stacking of its own and paints under
// deck.gl's canvas: elementFromPoint at a slider's centre returned the CANVAS,
// so the canvas took the pointer and the slider could not be dragged even
// though it now looked correct. With both sets copied, that same point returns
// the slider.
//
// THE FIX. Mirror both sets into the shadow root after the viewer is built,
// and keep mirroring, because Material-UI injects lazily as components first
// render.
//
// This is not the "detached element" problem recorded elsewhere for this
// widget. That one is real and separate: a viewer that is hidden when the page
// mounts renders blank for good, which is why these viewers are stacked rather
// than put in a tab-set or a dropdown.
import * as vizarr from 'https://hms-dbmi.github.io/vizarr/index.js';

// Copy the host document's Material-UI and JSS rules into `root`, now and as
// more arrive. Two kinds have to come across, and missing either one breaks a
// different thing:
//
//   - tags whose text mentions `Mui`, which carry component rules. Without
//     them a slider has no size at all.
//   - tags carrying a `data-jss` attribute, which are vizarr's own makeStyles
//     output and carry the panel's position and stacking. Without them the
//     panel paints under deck.gl's canvas, so the canvas wins hit-testing and
//     a slider cannot be dragged even though it looks right. Eight such tags
//     in a built DevNote mention no `Mui` at all, which is why filtering on
//     that string alone is not enough.
//
// Only these two are copied. Mirroring every stylesheet would drag the page
// theme into the widget with them.
function mirrorWidgetStyles(root) {
  if (!(root instanceof ShadowRoot)) return () => {};
  const seen = new WeakSet();
  const wanted = (node) =>
    node.hasAttribute('data-jss') || (node.textContent || '').includes('Mui');
  const copy = () => {
    for (const node of document.head.querySelectorAll('style')) {
      if (seen.has(node) || !wanted(node)) continue;
      seen.add(node);
      root.appendChild(node.cloneNode(true));
    }
  };
  copy();
  const observer = new MutationObserver(copy);
  observer.observe(document.head, { childList: true });
  return () => observer.disconnect();
}

// Per-viewer channel colors and contrast limits.
//
// Vizarr will not take these from `addImage`. It reads a channel's color and
// window from the store's `omero` metadata whenever that block exists, and
// ignores the `colors` and `contrast_limits` it is handed. Measured on
// 2026-10-11 against SH-0925-D4, outside any shadow root: passing both keys,
// with and without `channel_axis`, left every contrast slider at 0 to 65535.
//
// So the values are applied to the metadata instead, on its way in. One fetch
// wrapper watches for a store's own metadata document and rewrites the `omero`
// channels before vizarr parses them. Nothing else is touched: a request that
// matches no registered source is passed straight through, and so is a
// metadata document with no `omero` block.
//
// Measured with the wrapper in place, same store: the two contrast sliders
// read 2410 to 50690 and 1904 to 30863, and the channel swatches are
// rgb(255, 220, 60) and rgb(255, 60, 40), which are the values
// figures/fov-render-params.json records for the static figures.
//
// Overriding the store's own metadata is worth doing knowingly. It changes
// what a reader sees without changing what is stored, so a viewer and the
// store can disagree. Where the store can be rewritten, write the values into
// its `omero` block and leave these keys out.
const overrides = new Map();
let fetchPatched = false;

const METADATA = /\/(zarr\.json|\.zattrs)$/;

function patchFetchOnce() {
  if (fetchPatched) return;
  fetchPatched = true;
  const realFetch = globalThis.fetch.bind(globalThis);
  globalThis.fetch = async (input, init) => {
    const url = typeof input === 'string' ? input : input?.url ?? '';
    const response = await realFetch(input, init);
    if (!METADATA.test(url)) return response;
    let entry;
    for (const [prefix, value] of overrides) {
      if (url.startsWith(prefix)) { entry = value; break; }
    }
    if (!entry) return response;
    try {
      const meta = JSON.parse(await response.clone().text());
      const omero = meta?.attributes?.ome?.omero ?? meta?.omero;
      if (!Array.isArray(omero?.channels)) return response;
      omero.channels.forEach((channel, i) => {
        const color = entry.colors?.[i];
        const limits = entry.contrast_limits?.[i];
        if (color) channel.color = String(color).replace(/^#/, '');
        if (limits) {
          channel.window = { ...channel.window, start: limits[0], end: limits[1] };
        }
      });
      return new Response(JSON.stringify(meta), {
        status: response.status,
        headers: response.headers,
      });
    } catch {
      // A metadata document we cannot read is one we leave alone.
      return response;
    }
  };
}

function overrideChannels(source, { colors, contrast_limits: limits }) {
  if (!colors && !limits) return () => {};
  patchFetchOnce();
  overrides.set(source, { colors, contrast_limits: limits });
  return () => overrides.delete(source);
}

export default {
  async render({ model, el }) {
    const div = document.createElement('div');
    Object.assign(div.style, {
      height: model.get('height') ?? '500px',
      width: '100%',
      backgroundColor: 'black',
    });
    el.appendChild(div);

    const viewer = await vizarr.createViewer(div, {
      menuOpen: model.get('menuOpen') ?? false,
    });

    const source = model.get('source');
    const unregister = overrideChannels(source, {
      colors: model.get('colors'),
      contrast_limits: model.get('contrast_limits'),
    });
    viewer.addImage({ source });

    const stopMirroring = mirrorWidgetStyles(el.getRootNode());

    return () => {
      unregister();
      stopMirroring();
      viewer.destroy?.();
    };
  },
};
