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

## Why a plain table, not a generated number

The slug and branch names use each guest's initials (`-nk`, `-cc`,
`-mb`). They were chosen before this registry existed, not from a
number. The `#`
column is the only place the Validation-NN sequence is actually decided.
Keep it that way: a number derived from initials or creation order breaks
the moment two guests share initials, or a devnote gets rebuilt out of
order.
