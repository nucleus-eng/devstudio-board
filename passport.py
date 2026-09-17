#!/usr/bin/env python3
"""The DevStudio passport — one append-only file that travels with a work stream.

The board currently *infers* state: a file mtime stands in for "when was this
touched", and a human gate is invisible because nothing on disk records that a
TA started reading. The passport replaces inference with record. Each skill
appends one event as it acts; the board reads the events instead of guessing.

Lives at `passport.json` in the work stream's directory. Before a DevNote(M)
directory exists the work lives in Drive, so the passport is created there by
devstudio-log-to-devnote-g and travels down with the assets at stage 4.

    python3 passport.py init  <dir> --slug pure-yield-rate --author "R. Okafor"
    python3 passport.py log   <dir> --stage 2 --event drafted \\
        --skill devstudio-log-to-devnote-g --detail "3 Log folders synthesised"
    python3 passport.py set   <dir> --artifact devnote_g=https://docs.google.com/...
    python3 passport.py check <dir> --name constructs --status pass --detail "4/4 verified"
    python3 passport.py block <dir> --stage 3 --reason "which MTHFS construct is canonical?" \\
        --who "L. Vance" --asks TA --ref https://docs.google.com/...?disco=abc
    python3 passport.py unblock <dir> --stage 3 --resolution "use pNUC-114" --who "Jon"
    python3 passport.py show  <dir>

Append-only by contract: `log` and `check` never rewrite history. `set` updates
the derived pointers, and records an event saying it did.
"""
import argparse, json, sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "devstudio-passport/1"
FILENAME = "passport.json"

# What an event means, by stage. Events are the vocabulary skills append.
EVENTS = {
    "created", "drafted", "revised", "review_opened", "review_comment",
    "review_approved", "built", "assets_assembled", "pr_opened", "checks_passed",
    "checks_failed", "merged", "published", "blocked", "unblocked", "note",
}


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def path_for(d):
    return Path(d).expanduser().resolve() / FILENAME


def load(d):
    """Return the passport dict, or None. Never raises on a malformed file."""
    p = path_for(d)
    if not p.is_file():
        return None
    try:
        pp = json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return None
    return pp if pp.get("schema", "").startswith("devstudio-passport/") else None


def save(d, pp):
    path_for(d).write_text(json.dumps(pp, indent=2) + "\n")
    return pp


def init(d, slug=None, author=None, title=None):
    pp = load(d)
    if pp:
        return pp
    root = Path(d).expanduser().resolve()
    pp = {
        "schema": SCHEMA,
        "slug": slug or root.name,
        "title": title or "",
        "author": author or "",
        "created": now(),
        "sources": {},      # log_folders, build_file, platemap — where this came from
        "artifacts": {},    # devnote_g, devnote_m, archive_pr, docs_g, docs_m_pr
        "checks": {},       # name -> {status, ts, detail}
        "events": [],       # append-only
    }
    append(d, pp, stage=0, event="created", actor="human",
           detail=f"passport opened for {pp['slug']}")
    return pp


def append(d, pp=None, stage=0, event="note", actor="claude", skill=None,
           detail="", ref=None, **extra):
    pp = pp or load(d) or init(d)
    if event not in EVENTS:
        print(f"warning: '{event}' is not a known event "
              f"({', '.join(sorted(EVENTS))})", file=sys.stderr)
    pp["events"].append({k: v for k, v in {
        "ts": now(), "stage": stage, "event": event, "actor": actor,
        "skill": skill, "detail": detail, "ref": ref, **extra,
    }.items() if v not in (None, "")})
    return save(d, pp)


def block(d, stage, reason, who=None, asks="TA", ref=None):
    """Raise a hand. `asks` is who is being asked — TA, developer, author.

    A block is a first-class event, not a flag in prose, because the board has to
    be able to say how long it has been open and who it is waiting on."""
    return append(d, stage=stage, event="blocked", actor="human", detail=reason,
                  ref=ref, asks=asks, who=who)


def unblock(d, stage, resolution, who=None):
    return append(d, stage=stage, event="unblocked", actor="human",
                  detail=resolution, who=who)


def blocked_state(pp):
    """The open block, if any. Later unblocks clear earlier blocks."""
    cur = None
    for e in (pp or {}).get("events", []):
        if e.get("event") == "blocked":
            cur = e
        elif e.get("event") == "unblocked":
            cur = None
    return cur


def set_artifact(d, key, value):
    pp = load(d) or init(d)
    pp["artifacts"][key] = value
    return append(d, pp, stage=pp["events"][-1].get("stage", 0) if pp["events"] else 0,
                  event="note", actor="claude", detail=f"artifact {key} = {value}")


def set_check(d, name, status, detail=""):
    pp = load(d) or init(d)
    pp["checks"][name] = {"status": status, "ts": now(), "detail": detail}
    return append(d, pp, event="checks_passed" if status == "pass" else "checks_failed",
                  actor="claude", detail=f"{name}: {status} {detail}".strip())


# ------------------------------------------------------------------ reading

def last_event(pp, stage=None):
    evs = [e for e in pp.get("events", []) if stage is None or e.get("stage") == stage]
    return evs[-1] if evs else None


def stage_reached(pp):
    """Highest stage any event mentions."""
    return max((e.get("stage", 0) for e in pp.get("events", [])), default=0)


def parked_since(pp):
    """Timestamp of the most recent event — what the board should call parked time."""
    e = last_event(pp)
    return e["ts"] if e else pp.get("created")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init"); p.add_argument("dir")
    p.add_argument("--slug"); p.add_argument("--author"); p.add_argument("--title")

    p = sub.add_parser("log"); p.add_argument("dir")
    p.add_argument("--stage", type=int, required=True)
    p.add_argument("--event", required=True)
    p.add_argument("--actor", default="claude")
    p.add_argument("--skill"); p.add_argument("--detail", default=""); p.add_argument("--ref")

    p = sub.add_parser("set"); p.add_argument("dir")
    p.add_argument("--artifact", required=True, metavar="KEY=VALUE")

    p = sub.add_parser("check"); p.add_argument("dir")
    p.add_argument("--name", required=True)
    p.add_argument("--status", required=True, choices=["pass", "fail", "skip"])
    p.add_argument("--detail", default="")

    p = sub.add_parser("block"); p.add_argument("dir")
    p.add_argument("--stage", type=int, required=True)
    p.add_argument("--reason", required=True)
    p.add_argument("--who", help="who raised it")
    p.add_argument("--asks", default="TA", help="who is being asked (TA, developer, author)")
    p.add_argument("--ref", help="link to the Doc comment or thread")

    p = sub.add_parser("unblock"); p.add_argument("dir")
    p.add_argument("--stage", type=int, required=True)
    p.add_argument("--resolution", required=True)
    p.add_argument("--who")

    p = sub.add_parser("show"); p.add_argument("dir")

    a = ap.parse_args()
    if a.cmd == "init":
        pp = init(a.dir, a.slug, a.author, a.title)
    elif a.cmd == "log":
        pp = append(a.dir, stage=a.stage, event=a.event, actor=a.actor,
                    skill=a.skill, detail=a.detail, ref=a.ref)
    elif a.cmd == "set":
        k, _, v = a.artifact.partition("=")
        pp = set_artifact(a.dir, k, v)
    elif a.cmd == "block":
        pp = block(a.dir, a.stage, a.reason, a.who, a.asks, a.ref)
    elif a.cmd == "unblock":
        pp = unblock(a.dir, a.stage, a.resolution, a.who)
    elif a.cmd == "check":
        pp = set_check(a.dir, a.name, a.status, a.detail)
    else:
        pp = load(a.dir)
        if not pp:
            sys.exit(f"no {FILENAME} in {a.dir}")
    print(json.dumps(pp, indent=2))


if __name__ == "__main__":
    main()
