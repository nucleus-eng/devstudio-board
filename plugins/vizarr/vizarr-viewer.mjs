// Vizarr anywidget for DevNotes.
//
// A local copy of https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
// with one real change. The upstream file is kept beside this one as
// vizarr-viewer.upstream.js so the diff stays visible.
//
// THE BUG. Vizarr's control panel is built with Material-UI, which injects its
// rules as <style> tags in document.head. myst-theme mounts an anywidget inside
// a shadow root. A style tag in the document does not cross a shadow boundary,
// so the panel's markup arrives with none of its rules. The labels show,
// because text needs no CSS, and the sliders collapse to zero by zero, because
// a MuiSlider gets all of its size from a class.
//
// Measured in a built DevNote on 2026-10-11: the shadow root held 18 MuiSlider
// elements and no style tags, while document.head held 13 style tags
// mentioning Mui. Cloning those 13 into the shadow root took the first slider
// from 0x0 to 121x28.
//
// THE FIX. Mirror the Mui style tags into the shadow root after the viewer is
// built, and keep mirroring, because Material-UI injects lazily as components
// first render.
//
// This is not the "detached element" problem recorded elsewhere for this
// widget. That one is real and separate: a viewer that is hidden when the page
// mounts renders blank for good, which is why these viewers are stacked rather
// than put in a tab-set or a dropdown.
import * as vizarr from 'https://hms-dbmi.github.io/vizarr/index.js';

// Copy the host document's Material-UI rules into `root`, now and as more
// arrive. Only Mui rules are copied; mirroring every stylesheet would drag the
// page theme in with them.
function mirrorMuiStyles(root) {
  if (!(root instanceof ShadowRoot)) return () => {};
  const seen = new WeakSet();
  const copy = () => {
    for (const node of document.head.querySelectorAll('style')) {
      if (seen.has(node)) continue;
      if (!(node.textContent || '').includes('Mui')) continue;
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
    viewer.addImage({ source: model.get('source') });

    const stopMirroring = mirrorMuiStyles(el.getRootNode());

    return () => {
      stopMirroring();
      viewer.destroy?.();
    };
  },
};
