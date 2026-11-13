# Validation DevNote registry

Tracks the running `Validation-NN` number, the `subtitle` field in each
validation DevNote's `curvenote.yml`. Two guests must never get the same
number. A later run must know where to pick up.

**Read this table before you assign a number.** Add a row to it after
you build a devnote, in the same commit or PR. The next number is always
one past the highest `#` listed below. Never derive it from a slug, a
branch name, or a guest list position.

| # | Guest | Slug | Branch | Well | Status |
| --- | --- | --- | --- | --- | --- |
| 01 | Neha Kamat | `20261013-validation-nk` | `devstudio/20261013-validation-nk` | K18 | Draft submitted, not merged |
| 02 | Claudia Contini | `20261013-validation-cc` | `devstudio/20261013-validation-cc` | K19 | Branch opened, devnote not yet built |
| 03 | Michael Booth | `20261013-validation-mb` | `devstudio/20261013-validation-mb` | K20 | Branch opened, devnote not yet built |
| 04 | Leopold Green | `20261013-lg-validation-04` | none yet | none yet | Google Doc created, devnote not yet built |
| 05 | Richard Murray | `20261013-rm-validation-05` | none yet | none yet | Google Doc created, devnote not yet built |
| 06 | Michael Clear | `20261013-mc-validation-06` | none yet | none yet | Google Doc created, devnote not yet built |
| 07 | Becky Pferdehirt | `20261013-bp-validation-07` | none yet | none yet | Google Doc created, devnote not yet built |
| 08 | Andrew Ellington | `20261013-ae-validation-08` | none yet | none yet | Google Doc created, devnote not yet built |

**The Slug column mixes two naming orders on purpose.** Rows 01-03 use
the git devnote slug, `validation` before initials, already live as real
branches. Rows 04-08 use the Google Drive doc name, initials before
`validation`, given directly for that batch. When 04-08 get their own
devnote branches, pick one order. Say so here. Do not let both orders
keep drifting.

## Why a plain table, not a generated number

The slug and branch names use each guest's initials (`-nk`, `-cc`,
`-mb`). They were chosen before this registry existed, not from a
number. The `#`
column is the only place the Validation-NN sequence is actually decided.
Keep it that way: a number derived from initials or creation order breaks
the moment two guests share initials, or a devnote gets rebuilt out of
order.
