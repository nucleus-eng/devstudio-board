# Platemap Viewer MVP

This page exists to test the `{platemap}` plugin end to end: a real build,
a real draft submission, not a DevNote. See `curvenote.yml`'s description.

The plate: an EsaO-mNG titration against EsaR and AHSL, 12 `Sample` wells,
from `experiments/platemap.csv`.

## Default field selection

No `:fields:` is given here. The viewer shows the first three columns outside
the required/recommended schema. In this plate, that is all three
composition columns.

:::{platemap} ./experiments/platemap.csv
:height: 420px
:::

## Explicit `:fields:`

`[EsaO-mNG] (nM)` holds constant at every well in this plate. `:fields:`
drops it and keeps only the two columns that actually vary.

:::{platemap} ./experiments/platemap.csv
:height: 420px
:fields: [EsaR] (nM), [AHSL] (uM)
:::
