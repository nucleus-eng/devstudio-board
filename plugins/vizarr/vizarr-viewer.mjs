// Vizarr anywidget for DevNotes.
//
// A local copy of https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
// with one real change. The upstream file is kept beside this one as
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

    // `colors` and `contrast_limits` are vizarr's own ImageLayerConfig keys,
    // one entry per channel in the store's channel order. The upstream widget
    // forwards neither.
    //
    // They only take effect on a store with no `omero` metadata. Vizarr reads
    // a channel's color and window from `omero` whenever that block exists and
    // ignores what it was handed. Measured on 2026-10-11 against
    // SH-0925-D4, outside any shadow root: passing both keys, with and without
    // `channel_axis`, left every contrast slider at 0 to 65535. Matching a
    // viewer to a figure therefore means fixing the store's own `omero` block,
    // not the viewer. These two are forwarded for the stores that carry no
    // such block.
    const image = { source: model.get('source') };
    const colors = model.get('colors');
    const limits = model.get('contrast_limits');
    if (colors) image.colors = colors;
    if (limits) image.contrast_limits = limits;
    viewer.addImage(image);

    const stopMirroring = mirrorWidgetStyles(el.getRootNode());

    return () => {
      stopMirroring();
      viewer.destroy?.();
    };
  },
};
