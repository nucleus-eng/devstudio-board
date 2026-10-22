// Patched copy of https://curvenote.github.io/widgets/widgets/vizarr-viewer.js
// Vizarr's own UI (sliders, menu) is styled by Material-UI's JSS runtime,
// which injects one <style> tag per document and fills it incrementally,
// using CSSOM insertRule() calls, as each component type first renders. The
// myst-anywidget wrapper mounts this widget inside an open shadow root, and a
// shadow root does not inherit light-DOM stylesheets, so the slider renders
// with no layout CSS at all: a collapsed 0x0 element.
//
// adoptedStyleSheets only accepts a "constructed" CSSStyleSheet (one made
// with `new CSSStyleSheet()`), confirmed directly from the browser: adopting
// a parsed <style> tag's own sheet throws "Can't adopt non-constructed
// stylesheets", even same-origin. And insertRule() does not add or change any
// DOM node, so a MutationObserver never sees JSS's later rule insertions.
// The fix mirrors each source sheet's rules into one constructed sheet per
// source, kept in sync by polling rule count, and adopts the constructed
// sheet once.
import * as vizarr from 'https://hms-dbmi.github.io/vizarr/index.js';

function readableRules(sheet) {
  try {
    return Array.from(sheet.cssRules).map((r) => r.cssText).join('\n');
  } catch {
    return null; // cross-origin sheet; cssRules is not readable
  }
}

function syncShadowStyles(shadowRoot, mirrors) {
  for (const sheet of Array.from(document.styleSheets)) {
    const text = readableRules(sheet);
    if (text === null) continue;
    let mirror = mirrors.get(sheet);
    if (!mirror) {
      mirror = new CSSStyleSheet();
      mirrors.set(sheet, mirror);
      shadowRoot.adoptedStyleSheets = [...shadowRoot.adoptedStyleSheets, mirror];
    }
    if (mirror.__lastText !== text) {
      mirror.replaceSync(text);
      mirror.__lastText = text;
    }
  }
}

export default {
  async render({ model, el }) {
    let div = document.createElement('div');
    Object.assign(div.style, {
      height: model.get('height') ?? '500px',
      backgroundColor: 'black',
    });
    const shadowRoot = el.getRootNode();
    const mirrors = new Map();

    syncShadowStyles(shadowRoot, mirrors);
    // JSS inserts rules lazily, as each component first renders (e.g. the
    // channel menu, opened for the first time), with no DOM mutation to
    // observe. Poll for the life of the widget; it is a handful of sheets
    // and a cheap string comparison.
    const interval = setInterval(() => syncShadowStyles(shadowRoot, mirrors), 400);

    let viewer = await vizarr.createViewer(div, { menuOpen: !!model.get('menuOpen') ?? false });
    viewer.addImage({ source: model.get('source') });
    el.appendChild(div);
    return () => {
      clearInterval(interval);
      viewer.destory?.();
    };
  },
};
