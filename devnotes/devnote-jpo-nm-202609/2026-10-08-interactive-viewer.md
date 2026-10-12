# 2026-10-08 — Interactive viewer

Per-well microscopy for the C wells of `nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782`,
as interactive viewers. The store is one OME-NGFF plate holding C3 through C11 and D3
through D17. This page shows the C wells only.

:::{admonition} Why the D wells are not on this page, and why each C well is its own viewer
:class: warning
:name: flags-viewer-no-well-filter

Vizarr has no option to open a plate filtered to a subset of wells. Reading its own
source confirms this: opening a plate source always renders every well the store's
`rows`, `columns` and `wells` metadata lists, with no row, column or well-pattern
argument anywhere in `addImage`. The only filter it recognizes is `acquisition`, for a
plate with more than one acquisition run, which is a different thing and not what this
store has.

The only way to show the C wells alone is to open each one as its own well-level viewer,
never the plate root, which is what this page does.
:::

:::{danger} Custom contrast and the T = 19 start are not live in these viewers yet
:name: flags-viewer-metadata

Vizarr reads the initial channel contrast and the initial timepoint from the store's own
`omero` metadata, specifically `channels[].window.start`/`.end` per channel and
`rdefs.defaultT`. Neither the Curvenote viewer block nor a URL query string can carry
either value: the widget's block passes the viewer nothing but `source`, `height` and
`menuOpen`, and vizarr's own deep-link mechanism recognizes only a `source` and an
`acquisition` query parameter.

This store's GFP channel currently carries `window.start` 0 and `window.end` 65535,
which is the full 16-bit range, so every viewer below opens looking flat. It carries no
`rdefs`, so every viewer opens at T = 0.

Getting a GFP window of 30000 to 60000 and a T = 19 start requires writing
`omero.channels[1].window` and `omero.rdefs.defaultT` into the store itself. That is a
write to a live, shared store that other viewers of the same data would also see.
Confirm before it is done, and say whether it goes on this store or on a separate copy
made for this DevNote.
:::

Stacked rather than tabbed, per the Vizarr widget's own limit: it creates its viewer on
a detached element with no width and never re-measures, so an instance hidden when the
page mounts renders blank for good.

Each viewer sets `"menuOpen": true`, so the contrast sliders are visible without a click.

:::{admonition} Every slider below is served by a patched copy of the widget
:class: warning
:name: flags-viewer-patched-widget

Vizarr's own sliders (opacity, timepoint, per-channel contrast) render collapsed
to 0x0 pixels under the unpatched `vizarr-viewer.js` from
`curvenote.github.io/widgets`. Confirmed directly in the browser rather than
guessed: the sliders are styled by Material-UI's JSS runtime, which injects one
`<style>` tag into the document and fills it afterward with CSSOM
`insertRule()` calls, as each component first renders. The `myst-anywidget`
wrapper mounts this widget inside an open shadow root, and a shadow root
inherits none of the light DOM's stylesheets, so the slider markup has no
layout CSS at all.

`adoptedStyleSheets` does not fix this directly: it throws "Can't adopt
non-constructed stylesheets" on a parsed `<style>` tag's own sheet, confirmed
from the thrown error, even though it is same-origin. And `insertRule()` adds
no DOM node, so a `MutationObserver` never sees JSS's later rule insertions.

Every viewer below instead loads
[`general/vizarr-viewer-patched.js`](./general/vizarr-viewer-patched.js), a
copy of the same widget that mirrors each document stylesheet into one
constructed `CSSStyleSheet` per source, adopts those, and keeps them in sync
by polling rule count every 400 ms for the life of the widget, because no
event fires when JSS inserts a rule. Diffed against the original at
`https://curvenote.github.io/widgets/widgets/vizarr-viewer.js`; nothing else
changed.
:::

These viewers do not survive JATS conversion. A static figure carrying the same result
belongs on [the main page](./main.md), under Results, as the archival record.

No platemap exists yet for this store (see `flags-blocking` on the main page), so each
well below is named by its position only. A condition will replace that heading once the
platemap lands.

## C3

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/3/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C4

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/4/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C5

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/5/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C6

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/6/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C7

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/7/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C8

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/8/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C9

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/9/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C10

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/10/0",
    "height": "600px",
    "menuOpen": true
}
:::

## C11

:::{anywidget} ./general/vizarr-viewer-patched.js
:class: w-full

{
    "source": "https://data.nucleus.engineering/microscopy/nucleus-bnext-01/nc_lysate_cyt_c_d_2026-10-08_20-00-25.520782.zarr/C/11/0",
    "height": "600px",
    "menuOpen": true
}
:::
