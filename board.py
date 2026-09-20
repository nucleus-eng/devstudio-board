#!/usr/bin/env python3
"""devstudio-board — read-only status board for one DevNote in the DevStudio pipeline.

Usage:  python3 board.py /path/to/devnote-dir [--port 8765]

Reads only. Never writes, never invokes a skill. Truth comes from the local
filesystem, the `gh` CLI, and an optional `.devstudio-board.json` sidecar in the
devnote directory:

    {"slug": "emitter-cell",
     "doc_url": "https://docs.google.com/...",       # DevNote(G)
     "docs_g_url": "https://docs.google.com/...",    # Docs(G)
     "pr": 42,                                       # archive PR number
     "docs_pr": 17,                                  # nucleus-docs PR number
     "stages": {"1": "done", "3": "active"}}         # manual override, id -> status
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile, threading, uuid
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import passport

ARCHIVE_REPO = "nucleus-eng/nucleus-devnote-archive-1"
DOCS_REPO = "nucleus-eng/nucleus-docs"

# What an appended event means for the stage it names.
EVENT_STATUS = {
    "created": "done", "drafted": "done", "revised": "done", "built": "done",
    "assets_assembled": "done", "pr_opened": "done", "checks_passed": "done",
    "merged": "done", "published": "done", "review_approved": "done",
    "review_opened": "active", "review_comment": "active",
    "checks_failed": "failed", "blocked": "failed", "unblocked": "active",
    "note": None,
}

# id, label, owner, what produces it
STAGES = [
    (0,  "Build → platemap",      "skill", "devstudio-build-to-assets / -to-composition"),
    (1,  "Log folder ready",      "human", "you mark the folder ready in Drive"),
    (2,  "DevNote(G) draft",      "skill", "devstudio-log-to-devnote-g"),
    (3,  "TA review",             "human", "TA comments in the Google Doc"),
    (4,  "DevNote(M)",            "skill", "devstudio-devnote-g-to-devnote-m"),
    (5,  "Assets assembled",      "skill", "devstudio-assemble-devnote-assets"),
    (6,  "Archive PR",            "skill", "devstudio-submit-to-github"),
    (7,  "Merge → publish",       "ci",    "TA merges; Action submits to Curvenote"),
    (8,  "Docs(G) draft",         "skill", "devstudio-devnote-to-docs-g"),
    (9,  "Developer review",      "human", "developers comment in the Docs(G)"),
    (10, "Docs(M) PR",            "skill", "devstudio-docs-g-to-m"),
]

FIGURE_PATTERNS = [
    re.compile(r"^\s*[:`]{3,}\{(?:figure|image)\}\s*(\S+)", re.M),
    re.compile(r"!\[[^\]]*\]\(([^)]+)\)"),
]
FLAG_PATTERN = re.compile(r"(\[FLAG[^\]]*\]|\bTODO\b|\bTK\b|\bFIXME\b|\bXXX\b)")
# Anyone can type this into the Doc or main.md without touching a terminal.
NEEDS_PATTERN = re.compile(r"\[NEEDS-(TA|DEV|AUTHOR)(?::\s*([^\]]*))?\]", re.I)
ASSET_SUFFIXES = {".ipynb", ".csv", ".tsv", ".xlsx", ".gb", ".gbk", ".fasta", ".dna", ".zip"}
IGNORE_DIRS = {".git", "_build", ".ipynb_checkpoints", "node_modules", ".venv"}


def sh(args, cwd=None, timeout=15):
    """Run a command; return stdout or None. Never raises."""
    try:
        r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def mtime(p: Path):
    try:
        return datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc).isoformat()
    except OSError:
        return None


def days_since(iso):
    if not iso:
        return None
    try:
        t = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return None
    return round((datetime.now(timezone.utc) - t).total_seconds() / 86400, 1)


# ---------------------------------------------------------------- filesystem

def scan_dir(root: Path):
    """Everything the local filesystem knows. No network, no config."""
    main = root / "main.md"
    fs = {
        "root": str(root),
        "slug": root.name,
        "has_main": main.is_file(),
        "has_curvenote": (root / "curvenote.yml").is_file(),
        "has_manifest": (root / "manifest.json").is_file(),
        "main_mtime": mtime(main),
        "figures": [],
        "flags": [],
        "asks": [],
        "assets": [],
        "branch": sh(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=root),
        "remote": sh(["git", "remote", "get-url", "origin"], cwd=root),
        "author": sh(["git", "log", "-1", "--format=%an", "--", "main.md"], cwd=root),
    }
    if fs["has_main"]:
        text = main.read_text(errors="replace")
        refs = []
        for pat in FIGURE_PATTERNS:
            refs += pat.findall(text)
        seen = set()
        for ref in refs:
            ref = ref.strip()
            if ref in seen or ref.startswith(("http://", "https://", "#")):
                continue
            seen.add(ref)
            fs["figures"].append({"ref": ref, "present": (root / ref).is_file()})
        for i, line in enumerate(text.splitlines(), 1):
            n = NEEDS_PATTERN.search(line)
            if n:
                fs["asks"].append({"line": i, "asks": n.group(1).upper(),
                                   "reason": (n.group(2) or "").strip() or line.strip()[:160]})
                continue
            m = FLAG_PATTERN.search(line)
            if m:
                fs["flags"].append({"line": i, "marker": m.group(1), "text": line.strip()[:160]})
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in ASSET_SUFFIXES and not (IGNORE_DIRS & set(p.parts)):
            fs["assets"].append(str(p.relative_to(root)))
    return fs


# ---------------------------------------------------------------- github

def slug_tokens(slug):
    return [t for t in re.split(r"[^a-z0-9]+", slug.lower()) if len(t) > 2]


def pr_mentions_slug(pr, slug):
    """A PR counts as this DevNote's only if the slug shows up in its branch or title.

    `gh pr list --search` is a full-text search over the whole repo and will happily
    return a release PR that merely touched the file. Reporting that as this
    DevNote's PR is worse than reporting nothing, so require a real match."""
    hay = f"{pr.get('headRefName', '')} {pr.get('title', '')}".lower()
    toks = slug_tokens(slug)
    return bool(toks) and all(t in hay for t in toks)


_GH_CACHE = {}
GH_TTL = 180  # seconds


def pr_number(v):
    if v in (None, ""):
        return None
    m = re.search(r"(\d+)\s*$", str(v))
    return int(m.group(1)) if m else None


def gh_pr(repo, number=None, search=None):
    key = (repo, number, search)
    hit = _GH_CACHE.get(key)
    now = datetime.now(timezone.utc).timestamp()
    if hit and now - hit[0] < GH_TTL:
        return hit[1]
    val = _gh_pr_uncached(repo, number, search)
    _GH_CACHE[key] = (now, val)
    return val


def _gh_pr_uncached(repo, number=None, search=None):
    fields = ("number,state,isDraft,url,mergedAt,reviewDecision,statusCheckRollup,"
              "updatedAt,title,headRefName")
    if number:
        out = sh(["gh", "pr", "view", str(number), "--repo", repo, "--json", fields], timeout=25)
        if not out:
            return None
        try:
            pr = json.loads(out)
            pr["_source"] = "sidecar"
            return pr
        except json.JSONDecodeError:
            return None
    if search:
        out = sh(["gh", "pr", "list", "--repo", repo, "--state", "all", "--search", search,
                  "--limit", "5", "--json", fields], timeout=25)
        if not out:
            return None
        try:
            items = json.loads(out)
        except json.JSONDecodeError:
            return None
        for pr in items:
            if pr_mentions_slug(pr, search):
                pr["_source"] = "matched"
                return pr
        return None
    return None


def pr_summary(pr):
    if not pr:
        return None
    rollup = pr.get("statusCheckRollup") or []
    counts = {"pass": 0, "fail": 0, "pending": 0}
    for c in rollup:
        v = (c.get("conclusion") or c.get("state") or "").upper()
        if v in ("SUCCESS", "NEUTRAL", "SKIPPED"):
            counts["pass"] += 1
        elif v in ("FAILURE", "ERROR", "CANCELLED", "TIMED_OUT"):
            counts["fail"] += 1
        else:
            counts["pending"] += 1
    return {
        "number": pr.get("number"), "url": pr.get("url"), "title": pr.get("title"),
        "state": pr.get("state"), "draft": pr.get("isDraft"), "merged_at": pr.get("mergedAt"),
        "review": pr.get("reviewDecision"), "checks": counts,
        "updated_at": pr.get("updatedAt"), "parked_days": days_since(pr.get("updatedAt")),
        "branch": pr.get("headRefName"), "source": pr.get("_source"),
    }


# ---------------------------------------------------------------- stages

def nxt_stage_guess(fs):
    """Roughly where an inline marker sits, when no passport says otherwise."""
    return 5 if fs["has_main"] else 3


def passport_stages(pp):
    """Stage -> status, from the events a skill actually appended.

    This is the whole point of the passport: stages 0-3 and 8-9 live in Drive and
    are invisible from disk, so the board used to call them 'unknown'. An event
    recorded when it happened beats an API read after the fact."""
    out = {}
    for e in pp.get("events", []):
        st = EVENT_STATUS.get(e.get("event"))
        if st:
            out[e.get("stage", 0)] = (st, e)
    return out


def derive(fs, side, archive_pr, docs_pr, pending=False, pstages=None, slug=None):
    """Map facts onto the 11 stages. 'unknown' is a real answer and says why."""
    st = {}
    slug = slug or side.get("slug") or fs["slug"]

    def put(i, status, detail, link=None):
        st[i] = {"status": status, "detail": detail, "link": link}

    put(0, "unknown", "Build files live in Drive — not visible from disk")
    put(1, "unknown", "Drive-only signal (v2)")

    doc = side.get("doc_url")
    if doc:
        put(2, "done", "DevNote(G) recorded in sidecar", doc)
        put(3, "active", "Waiting on TA comments — comment count needs Drive (v2)", doc)
    elif fs["has_manifest"]:
        put(2, "done", "manifest.json present, so a DevNote(G) was drafted")
        put(3, "unknown", "No Doc URL recorded — add doc_url to the sidecar")
    else:
        put(2, "unknown", "No Doc URL or manifest.json on disk")
        put(3, "unknown", "Depends on stage 2")

    if fs["has_main"] and fs["has_curvenote"]:
        put(4, "done", f"main.md + curvenote.yml present ({days_since(fs['main_mtime'])}d since edit)")
    elif fs["has_main"] or fs["has_curvenote"]:
        missing = "curvenote.yml" if fs["has_main"] else "main.md"
        put(4, "failed", f"Incomplete — {missing} is missing")
    else:
        put(4, "todo", "No main.md in this directory")

    figs, miss = fs["figures"], [f for f in fs["figures"] if not f["present"]]
    if not fs["has_main"]:
        put(5, "todo", "Nothing to assemble until DevNote(M) exists")
    elif not figs:
        put(5, "unknown", "No figure references found in main.md")
    elif miss:
        put(5, "failed", f"{len(miss)} of {len(figs)} figure targets missing on disk")
    else:
        put(5, "done", f"All {len(figs)} figure targets resolve; {len(fs['assets'])} asset files present")

    if pending:
        put(6, "unknown", "Checking GitHub…")
        put(7, "unknown", "Checking GitHub…")
    elif archive_pr:
        merged = archive_pr["merged_at"]
        if merged:
            put(6, "done", f"PR #{archive_pr['number']} merged", archive_pr["url"])
            put(7, "done", f"Merged {days_since(merged)}d ago — Action fired", archive_pr["url"])
        else:
            c = archive_pr["checks"]
            if c["fail"]:
                put(6, "failed", f"PR #{archive_pr['number']}: {c['fail']} check(s) failing", archive_pr["url"])
            elif c["pending"]:
                put(6, "active", f"PR #{archive_pr['number']}: {c['pending']} check(s) running", archive_pr["url"])
            else:
                put(6, "done", f"PR #{archive_pr['number']} open, checks green", archive_pr["url"])
            kind = "draft" if archive_pr["draft"] else "ready"
            put(7, "active", f"Waiting on TA merge ({kind}, {archive_pr['parked_days']}d since update)",
                archive_pr["url"])
    else:
        put(6, "todo", f"No PR in {ARCHIVE_REPO} whose branch or title names '{slug}' — "
                       f"record \"pr\" in .devstudio-board.json if one exists")
        put(7, "todo", "Depends on stage 6")

    dg = side.get("docs_g_url")
    if dg:
        put(8, "done", "Docs(G) recorded in sidecar", dg)
        put(9, "active", "Waiting on developer comments (Drive, v2)", dg)
    else:
        put(8, "todo", "No Docs(G) URL recorded")
        put(9, "todo", "Depends on stage 8")

    if pending:
        put(10, "unknown", "Checking GitHub…")
    elif docs_pr:
        if docs_pr["merged_at"]:
            put(10, "done", f"PR #{docs_pr['number']} merged", docs_pr["url"])
        else:
            put(10, "active", f"PR #{docs_pr['number']} open in nucleus-docs", docs_pr["url"])
    else:
        put(10, "todo", f"No PR in {DOCS_REPO} naming '{slug}' — "
                        f"record \"docs_pr\" in the sidecar if one exists")

    # Recorded events outrank anything inferred, but never a live GitHub verdict.
    for i, (status, ev) in (pstages or {}).items():
        if i in st and not (i in (6, 7, 10) and (archive_pr or docs_pr)):
            who = ev.get("skill") or ev.get("actor")
            ago = days_since(ev["ts"])
            st[i] = {"status": status,
                     "detail": f"{ev['event'].replace('_', ' ')} — {ev.get('detail') or who}"
                               + (f" ({ago}d ago)" if ago is not None else ""),
                     "link": st[i].get("link") or ev.get("ref")}

    for k, v in (side.get("stages") or {}).items():
        try:
            st[int(k)]["status"] = v
            st[int(k)]["detail"] += " (manual override)"
        except (ValueError, KeyError):
            pass
    return st


ASK_LABEL = {"TA": "a TA", "DEV": "a developer", "AUTHOR": "the author",
             "DEVELOPER": "a developer"}


def next_action(fs, side, st, archive_pr, pending=False, block=None):
    """The one thing to do next, with the prompt to do it."""
    slug, root = side.get("slug") or fs["slug"], fs["root"]
    doc = side.get("doc_url") or "the reviewed DevNote(G) Doc"

    # Somebody raised a hand. Nothing downstream matters until it is answered.
    if block:
        asks = (block.get("asks") or "TA").upper()
        who = block.get("who")
        return {"title": f"Blocked — {ASK_LABEL.get(asks, asks)} needs to answer",
                "why": block.get("detail") or "no reason recorded",
                "stage": block.get("stage", 0), "prompt": None,
                "link": block.get("ref"), "asks": asks, "raised_by": who}

    if st[4]["status"] in ("todo", "failed"):
        return {"title": "Build the DevNote(M)", "stage": 4,
                "why": st[4]["detail"],
                "prompt": f"Use devstudio-devnote-g-to-devnote-m to turn {doc} into a DevNote(M) at {root}"}

    miss = [f["ref"] for f in fs["figures"] if not f["present"]]
    if miss:
        return {"title": "Assemble the missing assets", "stage": 5,
                "why": f"{len(miss)} figure target(s) referenced by main.md are not on disk: "
                       + ", ".join(miss[:4]) + ("…" if len(miss) > 4 else ""),
                "prompt": f"Use devstudio-assemble-devnote-assets to download the missing figure "
                          f"assets for the DevNote(M) at {root}"}

    if fs["flags"]:
        lines = ", ".join(f"line {f['line']}" for f in fs["flags"][:5])
        return {"title": f"Resolve {len(fs['flags'])} open flag(s)", "stage": 4,
                "why": f"main.md still carries uncertainty markers at {lines}",
                "prompt": f"Review the open flags in {root}/main.md and resolve each one against "
                          f"the source Log material"}

    if pending:
        return {"title": "Checking GitHub…", "stage": 6,
                "why": "Everything on disk is in order; asking gh about the PRs.",
                "prompt": None}

    if not archive_pr:
        return {"title": "Open the archive PR", "stage": 6,
                "why": f"No PR in {ARCHIVE_REPO} names '{slug}' (searched branch and title)",
                "prompt": f"Use devstudio-submit-to-github to open a draft PR for the DevNote(M) at {root}"}

    if archive_pr["checks"]["fail"]:
        return {"title": "Fix failing CI on the archive PR", "stage": 6,
                "why": f"{archive_pr['checks']['fail']} check(s) failing on PR #{archive_pr['number']}",
                "prompt": f"Investigate and fix the failing checks on {archive_pr['url']}"}

    if not archive_pr["merged_at"]:
        return {"title": "Waiting on TA merge — nothing for you to run", "stage": 7,
                "why": f"PR #{archive_pr['number']} has been idle {archive_pr['parked_days']}d",
                "prompt": None, "link": archive_pr["url"]}

    if st[8]["status"] == "todo":
        return {"title": "Draft the Docs(G)", "stage": 8,
                "why": "DevNote is published; no module spec draft exists yet",
                "prompt": f"Use devstudio-devnote-to-docs-g to draft a Docs(G) from the DevNote(M) at {root}"}

    if st[10]["status"] == "todo":
        return {"title": "Convert Docs(G) into the docs PR", "stage": 10,
                "why": "Docs(G) exists but nothing has been committed to nucleus-docs",
                "prompt": f"Use devstudio-docs-g-to-m to convert {side.get('docs_g_url', 'the reviewed Docs(G)')} "
                          f"into a spec page and open a PR"}

    return {"title": "Pipeline complete", "stage": 10,
            "why": "Every stage this board can see is done.", "prompt": None}


def build_state(root: Path, use_gh=True):
    fs = scan_dir(root)
    sidecar = root / ".devstudio-board.json"
    side = {}
    if sidecar.is_file():
        try:
            side = json.loads(sidecar.read_text())
        except json.JSONDecodeError:
            side = {"_error": "sidecar is not valid JSON"}

    pp = passport.load(root)
    if pp:
        art = pp.get("artifacts", {})
        declared = {"doc_url": art.get("devnote_g"), "docs_g_url": art.get("docs_g"),
                    "pr": pr_number(art.get("archive_pr")),
                    "docs_pr": pr_number(art.get("docs_m_pr")),
                    "slug": pp.get("slug")}
        side = {**side, **{k: v for k, v in declared.items() if v}}
    slug = side.get("slug") or fs["slug"]

    if use_gh:
        archive_pr = pr_summary(gh_pr(ARCHIVE_REPO, number=side.get("pr"), search=slug))
        docs_pr = pr_summary(gh_pr(DOCS_REPO, number=side.get("docs_pr"), search=slug))
    else:
        archive_pr = docs_pr = None

    # A recorded block wins; an inline [NEEDS-TA:] marker is the fallback for
    # anyone who raised a hand without touching a terminal.
    block = passport.blocked_state(pp) if pp else None
    if not block and fs["asks"]:
        a = fs["asks"][0]
        block = {"stage": nxt_stage_guess(fs), "asks": a["asks"], "detail": a["reason"],
                 "ts": fs["main_mtime"], "who": fs.get("author"), "inline": True,
                 "ref": f"main.md:{a['line']}"}

    pstages = passport_stages(pp) if pp else {}
    st = derive(fs, side, archive_pr, docs_pr, pending=not use_gh, pstages=pstages, slug=slug)
    nxt = next_action(fs, side, st, archive_pr, pending=not use_gh, block=block)
    if block and block.get("ts"):
        parked = days_since(block["ts"])
    elif pp:
        parked = days_since(passport.parked_since(pp))
    elif archive_pr and nxt["stage"] >= 6:
        parked = archive_pr["parked_days"]
    else:
        parked = days_since(fs["main_mtime"])
    return {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "fs": fs, "sidecar": side, "slug": slug,
        "archive_pr": archive_pr, "docs_pr": docs_pr,
        "stages": [{"id": i, "label": l, "owner": o, "producer": p, **st[i]}
                   for i, l, o, p in STAGES],
        "next": nxt,
        "author": (pp or {}).get("author") or fs.get("author"),
        "passport": pp,
        "block": block,
        "parked_days": parked,
        "demo": False,
        "gh_pending": not use_gh,
    }


# TA gates: the stages where the queue stops until *this* person acts.
TA_GATES = {1, 3, 7}

# The three artifact classes the pipeline actually moves through.
PHASES = [("log", "Log", range(0, 2)),
          ("devnote", "DevNote", range(2, 8)),
          ("docs", "Docs", range(8, 11))]


def phase_of(stage_id):
    for key, _, rng in PHASES:
        if stage_id in rng:
            return key
    return "docs"


def fleet_row(state):
    """One row of the fleet board. Grouped by who the work is actually waiting on."""
    nxt = state["next"]
    stage = next((s for s in state["stages"] if s["id"] == nxt["stage"]), state["stages"][0])

    # Group by whether anything can act *now*, not by who nominally owns the stage.
    # A missing figure is a skill's job even though it reads as a failure; an open
    # docs PR is somebody else's read even though a skill produced it.
    asks = (nxt.get("asks") or "").upper()
    if asks:
        group = "you" if asks == "TA" else "others"
    elif nxt["title"] == "Pipeline complete":
        group = "done"
    elif nxt.get("prompt") or nxt["title"].startswith("Checking"):
        group = "moving"
    elif stage["id"] in TA_GATES:
        group = "you"
    else:
        group = "others"

    return {
        "slug": state["slug"], "author": state.get("author"),
        "group": group, "demo": state.get("demo", False),
        "stage_id": stage["id"], "stage_label": stage["label"],
        "phase": phase_of(stage["id"]),
        "events": len((state.get("passport") or {}).get("events", [])),
        "last_actor": ((state.get("passport") or {}).get("events") or [{}])[-1].get("actor"),
        "status": stage["status"], "owner": stage["owner"], "detail": stage["detail"],
        "parked_days": state.get("parked_days"),
        "next_title": nxt["title"], "next_prompt": nxt.get("prompt"),
        "flags": len(state["fs"]["flags"]),
        "figs_missing": sum(1 for f in state["fs"]["figures"] if not f["present"]),
        "checks_failing": (state["archive_pr"] or {}).get("checks", {}).get("fail", 0),
        "blocked": stage["status"] == "failed" or bool(asks),
        "asks": asks or None,
        "raised_by": nxt.get("raised_by"),
        "dots": [s["status"] for s in state["stages"]],
    }


# ---------------------------------------------------------------- new log

# The board still owns no Drive logic. It invokes the skill, which owns it.
# The deployment Drive root changes per event — pass its name with --drive-root.
# "DevStudio-Event" was the 2026-09-20 deployment; earlier ones used
# "San Francisco Node" with a "log" (singular) child folder and a Node layer that
# this one dropped. Do not hardcode a specific event's name below this line.
DEFAULT_DRIVE_ROOT_NAME = "DevStudio-Event"
DRIVE_ROOT_NAME = DEFAULT_DRIVE_ROOT_NAME
DRIVE_ROOT_ID = "1b1vQ-C-WWDaZEjJ2DJHVX6vJHmtNCiR0"   # DevStudio-Event, 2026-09-20 deployment

# A listing call has, in practice, reported a folder as one of its own children —
# confirmed 2026-09-20: /api/docs returned the docs/ folder itself, id
# 17ajfQQ2Z2p0reE4vUsIRI3TAcddkBssY, as a row inside docs/. Whatever asked for a
# folder's children must never see the folder's own id come back as a result, so
# every listing function drops rows matching a known container id below.
KNOWN_CONTAINER_IDS = {
    "1b1vQ-C-WWDaZEjJ2DJHVX6vJHmtNCiR0",   # DevStudio-Event (root)
    "14sW3RW3rJ3_0orAMf3ltxAOxmRoSE86M",   # logs/
    "11-lc-uNir9twSKUlokluy7vz8_-Jo8sd",   # devnotes/
    "17ajfQQ2Z2p0reE4vUsIRI3TAcddkBssY",   # docs/
}


def drop_self_rows(rows):
    """Filter out any row whose id is a known container's own id."""
    return [r for r in rows if r.get("id") not in KNOWN_CONTAINER_IDS]
DRIVE_READ_TOOLS = [
    "mcp__claude_ai_Google_Drive__search_files",
    "mcp__claude_ai_Google_Drive__get_file_metadata",
]
# Templates live in log/ alongside real work. They are not work streams.
TEMPLATE_RE = re.compile(r"template", re.I)
_LOGS = {"ts": 0.0, "rows": [], "error": None}
LOGS_TTL = 300
LOGS_CACHE_FILE = Path(__file__).with_name(".drive-logs.json")
REFRESH_NOW = -1   # sentinel: bypass the cache and actually go to Drive


def _load_logs_cache():
    try:
        d = json.loads(LOGS_CACHE_FILE.read_text())
        if isinstance(d.get("rows"), list):
            _LOGS.update({"ts": d.get("ts", 0.0), "rows": d["rows"], "error": None})
    except (OSError, ValueError):
        pass


def _save_logs_cache():
    try:
        LOGS_CACHE_FILE.write_text(json.dumps({"ts": _LOGS["ts"], "rows": _LOGS["rows"]}))
    except OSError:
        pass


def drive_logs(repo, max_age=LOGS_TTL):
    """Child folders of the deployment's logs/ folder, via a read-only `claude -p`.

    Cached: each call costs a Claude run and several Drive round trips."""
    now = datetime.now(timezone.utc).timestamp()
    if _LOGS["rows"] and now - _LOGS["ts"] < max_age:
        return _LOGS["rows"], _LOGS["error"]
    if not repo:
        return _LOGS["rows"], "no --repo given, so Drive cannot be read"
    if _LOGS["rows"] and max_age is not REFRESH_NOW:
        # Stale but usable: hand it over now and refresh in the background, so a page
        # load never waits minutes on Drive.
        if not _LOGS.get("refreshing"):
            _LOGS["refreshing"] = True
            threading.Thread(target=lambda: (drive_logs(repo, REFRESH_NOW),
                                             _LOGS.update({"refreshing": False})),
                             daemon=True).start()
        return _LOGS["rows"], _LOGS["error"]
    prompt = (
        f"Find the Google Drive folder '{DRIVE_ROOT_NAME}', then its child folder 'logs'. "
        "List every child FOLDER of that 'logs' folder. "
        "Output ONLY a JSON array and nothing else — no prose, no code fence. Each element: "
        '{"name": <folder title>, "id": <file id>, "url": <viewUrl>, '
        '"createdTime": <RFC3339>, "modifiedTime": <RFC3339>}'
    )
    try:
        r = subprocess.run(["claude", "-p", prompt, "--allowedTools", "ToolSearch",
                            *DRIVE_READ_TOOLS], cwd=repo, capture_output=True,
                           text=True, timeout=300)
        m = re.search(r"\[.*\]", r.stdout or "", re.S)
        rows = json.loads(m.group(0)) if m else None
        if not isinstance(rows, list):
            raise ValueError("no JSON array in the reply")
        rows = drop_self_rows(rows)
        _LOGS.update({"ts": now, "rows": rows, "error": None})
        _save_logs_cache()
    except Exception as e:
        _LOGS.update({"ts": now, "error": f"could not read Drive: {e}"})
    return _LOGS["rows"], _LOGS["error"]


# Docs is manual for now — no skill drafts or converts anything here. The board only
# lists what a human already put in docs/, the same read-only pattern as Log.
_DOCS = {"ts": 0.0, "rows": [], "error": None}
DOCS_CACHE_FILE = Path(__file__).with_name(".drive-docs.json")


def _load_docs_cache():
    try:
        d = json.loads(DOCS_CACHE_FILE.read_text())
        if isinstance(d.get("rows"), list):
            _DOCS.update({"ts": d.get("ts", 0.0), "rows": d["rows"], "error": None})
    except (OSError, ValueError):
        pass


def _save_docs_cache():
    try:
        DOCS_CACHE_FILE.write_text(json.dumps({"ts": _DOCS["ts"], "rows": _DOCS["rows"]}))
    except OSError:
        pass


def drive_docs(repo, max_age=LOGS_TTL):
    """Direct children of the deployment's docs/ folder, folders and files both —
    Docs(M) pages have no settled shape here yet, so this does not assume one."""
    now = datetime.now(timezone.utc).timestamp()
    if _DOCS["rows"] and now - _DOCS["ts"] < max_age:
        return _DOCS["rows"], _DOCS["error"]
    if not repo:
        return _DOCS["rows"], "no --repo given, so Drive cannot be read"
    if _DOCS["rows"] and max_age is not REFRESH_NOW:
        if not _DOCS.get("refreshing"):
            _DOCS["refreshing"] = True
            threading.Thread(target=lambda: (drive_docs(repo, REFRESH_NOW),
                                             _DOCS.update({"refreshing": False})),
                             daemon=True).start()
        return _DOCS["rows"], _DOCS["error"]
    prompt = (
        f"Find the Google Drive folder '{DRIVE_ROOT_NAME}', then its child folder 'docs'. "
        "List every direct child of that 'docs' folder, folders and files both. "
        "Output ONLY a JSON array and nothing else — no prose, no code fence. Each element: "
        '{"name": <title>, "id": <file id>, "url": <viewUrl>, "isFolder": <true/false>, '
        '"mimeType": <mimeType>, "createdTime": <RFC3339>, "modifiedTime": <RFC3339>}'
    )
    try:
        r = subprocess.run(["claude", "-p", prompt, "--allowedTools", "ToolSearch",
                            *DRIVE_READ_TOOLS], cwd=repo, capture_output=True,
                           text=True, timeout=300)
        m = re.search(r"\[.*\]", r.stdout or "", re.S)
        rows = json.loads(m.group(0)) if m else None
        if not isinstance(rows, list):
            raise ValueError("no JSON array in the reply")
        rows = drop_self_rows(rows)
        _DOCS.update({"ts": now, "rows": rows, "error": None})
        _save_docs_cache()
    except Exception as e:
        _DOCS.update({"ts": now, "error": f"could not read docs/: {e}"})
    return _DOCS["rows"], _DOCS["error"]


def drive_doc_row(f):
    """A Drive docs/ entry as a fleet card. No pipeline stage, no action buttons —
    docs are handled by a human outside the board for now."""
    return {
        "slug": f.get("name"), "phase": "docs", "group": "drive", "source": "drive",
        "url": f.get("url"), "doc_url": f.get("url") if not f.get("isFolder") else None,
        "isFolder": bool(f.get("isFolder")),
        "parked_days": days_since(f.get("modifiedTime") or f.get("createdTime")),
        "author": None, "next_title": None, "next_prompt": None,
    }


# A DevNote's source Logs never change once it is drafted, so this map is near-static.
# Deriving it costs minutes; persist it and refresh only when asked.
# The shared map lives in Drive so every TA reads the same one. The local file is
# only a mirror, so a cold start is fast and an offline start still shows something.
MAP_FILENAME = "devnote-log-map.json"
CACHE_FILE = Path(__file__).with_name(".devnote-map.json")
_DEVNOTES = {"ts": 0.0, "rows": [], "error": None}


def _load_devnote_cache():
    try:
        d = json.loads(CACHE_FILE.read_text())
        if isinstance(d.get("rows"), list):
            _DEVNOTES.update({"ts": d.get("ts", 0.0), "rows": d["rows"], "error": None})
    except (OSError, ValueError):
        pass


def _save_devnote_cache():
    try:
        CACHE_FILE.write_text(json.dumps(
            {"ts": _DEVNOTES["ts"], "rows": _DEVNOTES["rows"]}, indent=1))
    except OSError:
        pass


def drive_devnote_index(repo, max_age=LOGS_TTL):
    """DevNote folders in the deployment devnotes/, plus the shared log map stored beside them."""
    now = datetime.now(timezone.utc).timestamp()
    if _DEVNOTES["rows"] and (max_age is not REFRESH_NOW and now - _DEVNOTES["ts"] < max_age):
        return _DEVNOTES["rows"], _DEVNOTES["error"]
    if not repo:
        return _DEVNOTES["rows"], "no --repo given, so Drive cannot be read"
    if _DEVNOTES["rows"] and max_age is not REFRESH_NOW:
        if not _DEVNOTES.get("refreshing"):
            _DEVNOTES["refreshing"] = True
            threading.Thread(
                target=lambda: (drive_devnote_index(repo, REFRESH_NOW),
                                _DEVNOTES.update({"refreshing": False})),
                daemon=True).start()
        return _DEVNOTES["rows"], _DEVNOTES["error"]
    prompt = (
        f"Find the Google Drive folder '{DRIVE_ROOT_NAME}', then its child folder 'devnotes'. "
        "Do two things:\n"
        f"1. Download the file named '{MAP_FILENAME}' in that folder if it exists, and read "
        "its 'devnotes' array.\n"
        "2. List every child FOLDER of 'devnotes', skipping any whose name contains "
        "'template' or is named 'drafts'. For each, note its title, its viewUrl, and the "
        "viewUrl of the Google Doc inside it if there is one.\n\n"
        "Merge the two: every DevNote folder appears once, carrying the 'logs' array from "
        f"{MAP_FILENAME} when the map lists it, or an empty array when it does not.\n\n"
        "Output ONLY a JSON array, no prose and no code fence. Each element: "
        '{"name": <folder title>, "url": <folder viewUrl>, "doc_url": <Doc viewUrl or null>, '
        '"logs": [<Log folder names>], "mapped": <true if the map listed it, else false>}'
    )
    try:
        r = subprocess.run(["claude", "-p", prompt, "--allowedTools", "ToolSearch",
                            *DRIVE_READ_TOOLS,
                            "mcp__claude_ai_Google_Drive__download_file_content"],
                           cwd=repo, capture_output=True, text=True, timeout=900)
        m = re.search(r"\[.*\]", r.stdout or "", re.S)
        rows = json.loads(m.group(0)) if m else None
        if not isinstance(rows, list):
            raise ValueError("no JSON array in the reply")
        rows = drop_self_rows(rows)
        _DEVNOTES.update({"ts": now, "rows": rows, "error": None})
        _save_devnote_cache()
    except Exception as e:
        _DEVNOTES.update({"ts": now, "error": f"could not read devnotes/: {e}"})
    return _DEVNOTES["rows"], _DEVNOTES["error"]


def devnote_row(d):
    """A DevNote folder as a card. Everything shown comes from Drive."""
    return {
        "slug": d.get("name"), "phase": "devnote", "group": "drive", "source": "drive",
        "stage_id": 2, "stage_label": "DevNote(G) draft", "status": "unknown",
        "owner": "human", "detail": "draft in Drive",
        "url": d.get("url"), "doc_url": d.get("doc_url"),
        "logs": d.get("logs") or [], "mapped": bool(d.get("mapped")),
        "author": None, "parked_days": None, "flags": 0, "figs_missing": 0,
        "checks_failing": 0, "blocked": False, "asks": None, "raised_by": None,
        "events": 0, "devnotes": [], "next_title": "Review, then convert to MyST",
        "next_prompt": None, "dots": ["todo"] * 11,
    }


def push_devnote_map(repo, rows):
    """Write the shared map back to Drive.

    Drive has no in-place content update, so this creates a new file and trashes the
    old one — leaving both would give devnotes/ two files with the same name and no
    way to tell which is current."""
    body = json.dumps({"schema": "devstudio-devnote-log-map/1",
                       "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                       "devnotes": rows}, indent=2)
    prompt = (
        f"In the Google Drive folder '{DRIVE_ROOT_NAME}' > 'devnotes':\n"
        f"1. Note the file id of the existing file named '{MAP_FILENAME}', if any.\n"
        f"2. Create a new file named exactly '{MAP_FILENAME}' in that folder with "
        "contentMimeType 'application/json' and disableConversionToGoogleType true, whose "
        "content is exactly the JSON between the markers below.\n"
        "3. Then trash the OLD file from step 1, so only one remains.\n"
        "Print DONE on the last line.\n\n"
        f"---BEGIN JSON---\n{body}\n---END JSON---"
    )
    try:
        r = subprocess.run(["claude", "-p", prompt, "--allowedTools", "ToolSearch",
                            *DRIVE_READ_TOOLS,
                            "mcp__claude_ai_Google_Drive__create_file",
                            "mcp__claude_ai_Google_Drive__trash_file"],
                           cwd=repo, capture_output=True, text=True, timeout=600)
        return "DONE" in (r.stdout or ""), (r.stdout or "")[-2000:]
    except Exception as e:
        return False, str(e)


def drive_devnotes(repo, log_names, max_age=None):
    """Which Log folders each DevNote in devnotes/ was built from.

    Derived from each DevNote's figure-manifest, whose asset paths are prefixed with
    the source Log folder. A Log can appear in several DevNotes — this is a mapping,
    not a flag, so nothing here marks a Log as 'used up'."""
    now = datetime.now(timezone.utc).timestamp()
    # max_age=None means "never expire on its own" — the map only changes when a
    # DevNote is drafted, and this board invalidates it itself when that happens.
    if _DEVNOTES["rows"] and (max_age is None or now - _DEVNOTES["ts"] < max_age):
        return _DEVNOTES["rows"], _DEVNOTES["error"]
    if not repo or not log_names:
        return _DEVNOTES["rows"], None
    listing = ", ".join(sorted(log_names))
    prompt = (
        f"Find the Google Drive folder '{DRIVE_ROOT_NAME}', then its child folder 'devnotes'. "
        "For each child FOLDER of 'devnotes' (skip any whose name contains 'template'): "
        "find the file inside it whose name contains 'manifest' and download its content. "
        "If the manifest has a 'source_logs' array, use it verbatim — that is authoritative. "
        "Otherwise fall back to reporting which of these Log folder names appear anywhere in "
        "the manifest text (asset paths are prefixed with the source Log folder):\n"
        f"{listing}\n\n"
        "Output ONLY a JSON array, no prose and no code fence. Each element: "
        '{"name": <devnote folder title>, "url": <folder viewUrl>, '
        '"doc_url": <viewUrl of the Doc inside it, or null>, '
        '"logs": [<matching Log folder names, exactly as spelled above>]}. '
        "If a DevNote folder has no manifest, still list it with an empty logs array."
    )
    try:
        r = subprocess.run(["claude", "-p", prompt, "--allowedTools", "ToolSearch",
                            *DRIVE_READ_TOOLS,
                            "mcp__claude_ai_Google_Drive__download_file_content"],
                           cwd=repo, capture_output=True, text=True, timeout=1800)
        m = re.search(r"\[.*\]", r.stdout or "", re.S)
        rows = json.loads(m.group(0)) if m else None
        if not isinstance(rows, list):
            raise ValueError("no JSON array in the reply")
        rows = drop_self_rows(rows)
        _DEVNOTES.update({"ts": now, "rows": rows, "error": None})
        _save_devnote_cache()
    except Exception as e:
        _DEVNOTES.update({"ts": now, "error": f"could not map DevNotes: {e}"})
    return _DEVNOTES["rows"], _DEVNOTES["error"]


def devnotes_by_log(devnotes, board_jobs=True):
    """log folder name -> [{name, url, doc_url, source}]"""
    out = {}
    for d in devnotes or []:
        for lg in d.get("logs") or []:
            out.setdefault(lg, []).append({"name": d.get("name"), "url": d.get("url"),
                                           "doc_url": d.get("doc_url"), "source": "manifest"})
    if board_jobs:
        # DevNotes this board drafted: the selection is known exactly, and the
        # manifest may not exist yet when the run has only just finished.
        with JOBS_LOCK:
            jobs = [j for j in JOBS.values()
                    if j.get("kind") == "devnote" and j.get("status") == "done"]
        for j in jobs:
            for lg in j.get("logs") or []:
                have = {d["name"] for d in out.get(lg, [])}
                if j.get("name") not in have:
                    out.setdefault(lg, []).append(
                        {"name": j.get("name"), "url": j.get("url"),
                         "doc_url": j.get("doc_url"), "source": "this board"})
    return out


def drive_log_row(f):
    """A Drive Log folder as a fleet row. Deliberately thin — Drive knows the folder
    exists and when it was touched, and nothing else about where the work stands."""
    dots = ["unknown", "unknown"] + ["todo"] * 9
    return {
        "slug": f.get("name"), "author": None, "group": "unfiled", "demo": False,
        "stage_id": 1, "stage_label": "Log folder", "phase": "log",
        "status": "unknown", "owner": "human",
        "detail": "in Drive — no passport, so readiness is unknown",
        "parked_days": days_since(f.get("modifiedTime") or f.get("createdTime")),
        "next_title": "No passport — open one to track it",
        "next_prompt": None, "link": f.get("url"), "url": f.get("url"),
        "flags": 0, "figs_missing": 0, "checks_failing": 0, "blocked": False,
        "asks": None, "raised_by": None, "events": 0, "last_actor": None,
        "source": "drive", "dots": dots, "devnotes": [],
    }


# Drafting a DevNote reads logs, notebooks and data, then writes a Doc + manifest.
DEVNOTE_TOOLS = [
    "mcp__claude_ai_Google_Drive__search_files",
    "mcp__claude_ai_Google_Drive__get_file_metadata",
    "mcp__claude_ai_Google_Drive__read_file_content",
    "mcp__claude_ai_Google_Drive__download_file_content",
    "mcp__claude_ai_Google_Drive__create_file",
    "mcp__claude_ai_Google_Drive__copy_file",
]
ORCID_RE = re.compile(r"^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
DATE_IN_NAME = re.compile(r"(20\d{6})")


def author_initials(name):
    parts = [w for w in re.split(r"[^A-Za-z]+", name or "") if w]
    return "".join(w[0].lower() for w in parts)[:4]


def devnote_name(author_name, log_names):
    """devnote-<initials>-<first date>-<last date>, matching what is already in devnotes/.

    Dates come from the selected Log folder names, which is what the span actually means:
    the range of experiment days this DevNote pools."""
    dates = sorted({d for n in log_names for d in DATE_IN_NAME.findall(n or "")})
    ini = author_initials(author_name)
    if not ini:
        return None, "an author name is required to derive the DevNote name"
    if not dates:
        return None, "none of the selected Log folders carry a date in their name"
    span = [dates[0]] if dates[0] == dates[-1] else [dates[0], dates[-1]]
    return "-".join(["devnote", ini, *span]), None


# G->M writes a MyST directory on disk, so this run needs local file tools as well
# as Drive reads. Broader than the other buttons — deliberately, and no further.
GM_TOOLS = ["Read", "Write", "Edit", "Glob", "Grep", "Bash"]
UUID_RE = re.compile(r"^\s*id:\s*['\"]?([0-9a-fA-F-]{36})['\"]?\s*$", re.M)
VERSION_RE = re.compile(r"^(?P<base>.+?)(?:-v(?P<n>\d+))?$")


def project_uuid(devnote_dir: Path):
    """The curvenote.yml project id. The first 36-char id in the file is the project's;
    later ones are nested resource ids at deeper indentation."""
    try:
        m = UUID_RE.search((devnote_dir / "curvenote.yml").read_text())
        return m.group(1) if m else None
    except OSError:
        return None


def git_root(path):
    out = sh(["git", "-C", str(path), "rev-parse", "--show-toplevel"])
    return Path(out) if out else None


def git_dirty(repo, target):
    """Paths under `target` with uncommitted changes, including untracked."""
    out = sh(["git", "-C", str(repo), "status", "--porcelain", "--", str(target)])
    if not out:
        return []
    return [ln.strip().split(None, 1)[1] for ln in out.splitlines()
            if ln.strip() and len(ln.strip().split(None, 1)) > 1]


def myst_state(out_root, name, others=()):
    """This DevNote's local build — one directory, no version suffixes."""
    d = Path(out_root or "") / name
    if not d.is_dir():
        return None
    n = 1
    fs = scan_dir(d)
    missing = [f["ref"] for f in fs["figures"] if not f["present"]]
    repo = git_root(d)
    return {"dir": str(d), "version": n, "uuid": project_uuid(d),
            "dirty": git_dirty(repo, d) if repo else None,
            "has_main": (d / "main.md").is_file(),
            "has_config": (d / "curvenote.yml").is_file(),
            "missing_figures": missing,
            "buildable": (d / "main.md").is_file() and (d / "curvenote.yml").is_file()
                          and not missing}


# One local preview server at a time. `curvenote start` renders the DevNote as a
# website without submitting anything — the fastest way to look at a build.
def job_guard(fn):
    """Any unhandled error in a worker marks its job failed rather than leaving it
    spinning forever — a stuck 'running' row is indistinguishable from slow work."""
    def wrapper(job_id, *a, **kw):
        try:
            return fn(job_id, *a, **kw)
        except Exception as e:
            with JOBS_LOCK:
                if job_id in JOBS and JOBS[job_id].get("status") == "running":
                    JOBS[job_id].update({"status": "error",
                                         "error": f"{type(e).__name__}: {e}"})
            raise
    return wrapper


PREVIEW = {"proc": None, "name": None, "url": None, "dir": None, "log": []}
PREVIEW_LOCK = threading.Lock()
URL_RE = re.compile(r"https?://(?:localhost|127\.0\.0\.1):\d+\S*")


def stop_preview():
    with PREVIEW_LOCK:
        proc = PREVIEW.get("proc")
        if proc and proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.kill()
        PREVIEW.update({"proc": None, "name": None, "url": None, "dir": None})


def start_preview(name, devnote_dir):
    """Run `curvenote start` and wait for it to announce a URL."""
    stop_preview()
    try:
        proc = subprocess.Popen(["curvenote", "start"], cwd=devnote_dir,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, bufsize=1)
    except FileNotFoundError:
        return None, "the `curvenote` CLI is not on PATH"
    with PREVIEW_LOCK:
        PREVIEW.update({"proc": proc, "name": name, "dir": str(devnote_dir), "log": []})

    def pump():
        for line in proc.stdout:
            with PREVIEW_LOCK:
                PREVIEW["log"].append(line.rstrip())
                del PREVIEW["log"][:-200]
                if not PREVIEW["url"]:
                    m = URL_RE.search(line)
                    if m:
                        PREVIEW["url"] = m.group(0).rstrip(".,)")
    threading.Thread(target=pump, daemon=True).start()

    # The first build can take a while; wait for a URL rather than guessing a port.
    for _ in range(180):
        with PREVIEW_LOCK:
            if PREVIEW["url"]:
                return PREVIEW["url"], None
            if proc.poll() is not None:
                return None, "curvenote start exited: " + "\n".join(PREVIEW["log"][-12:])
        __import__("time").sleep(1)
    return None, "curvenote start did not report a URL within 3 minutes"


@job_guard
def _run_curvenote(job_id, devnote_dir, venue, run_check=False):
    """curvenote check, then a draft submission. Runs the CLI directly — no model in
    the loop, so this is fast and the output is the CLI's own."""
    d = Path(devnote_dir)
    result = {"dir": str(d), "venue": venue}
    try:
        if run_check:
            chk = subprocess.run(["curvenote", "check", venue, "-y"], cwd=d,
                                 capture_output=True, text=True, timeout=900)
            result["check"] = ((chk.stdout or "") + (chk.stderr or "")).strip()[-4000:]
            result["check_ok"] = chk.returncode == 0

        sub = subprocess.run(["curvenote", "submit", venue, "--draft", "--yes"], cwd=d,
                             capture_output=True, text=True, timeout=1800)
        out = ((sub.stdout or "") + (sub.stderr or "")).strip()
        result["log"] = out[-6000:]
        result["status"] = "done" if sub.returncode == 0 else "error"
        if sub.returncode != 0:
            # A failed run has no submission to link to. Curvenote's own CLI prints
            # unrelated links on failure too (its update banner links x.com/curvenote),
            # and picking one of those up here would show a fake "submitted" URL for
            # a run that never submitted anything.
            result["error"] = "curvenote submit failed — see the log"
        else:
            # The venue link may be on curvenote.com, curve.space, or the venue's own
            # domain, so collect every URL and pick the most submission-shaped one
            # rather than assuming a host.
            found = [u.rstrip(".,)>\"'") for u in re.findall(r"https?://[^\s\"'<>]+", out)]
            seen = set()
            urls = [u for u in found if not (u in seen or seen.add(u))]
            def rank(u):
                return (("submission" in u or "/s/" in u or "draft" in u) * 4
                        + ("curvenote.com" in u or "curve.space" in u) * 2
                        + ("nucleus" in u))
            result["urls"] = urls
            result["url"] = max(urls, key=rank) if urls else None
            if not result["url"]:
                result["status"] = "error"
                result["error"] = "curvenote submit reported success but printed no URL"
    except subprocess.TimeoutExpired:
        result.update({"status": "error", "error": "curvenote timed out"})
    except FileNotFoundError:
        result.update({"status": "error",
                       "error": "the `curvenote` CLI is not on PATH"})
    with JOBS_LOCK:
        JOBS[job_id].update(result)


def plan_g_to_m(out_root, name):
    """Decide where this conversion goes, and which project id it should keep.

    One DevNote, one directory — a re-derivation rebuilds in place and git carries
    the history, which is a better changelog than -v2/-v3 directories and keeps the
    assets already fetched. The guard against losing work is the working tree being
    clean, not a fresh directory name.

    The curvenote project id is carried forward from whatever is already there: a
    fresh id would make the venue treat a rebuild as an unrelated project."""
    root = Path(out_root)
    target = root / name
    repo = git_root(root if root.is_dir() else root.parent)
    if not repo:
        return {"action": "blocked", "target": str(target), "version": 1,
                "carry_uuid": None, "prior": None,
                "why": f"{out_root} is not inside a git repository, so a rebuild could "
                       f"not be undone. Run `git init` there first."}
    if target.is_dir():
        dirty = git_dirty(repo, target)
        uuid_ = project_uuid(target)
        if dirty:
            return {"action": "blocked", "target": str(target), "version": 1,
                    "carry_uuid": uuid_, "prior": str(target), "dirty": dirty[:10],
                    "why": f"{name} has {len(dirty)} uncommitted change(s). Commit or "
                           f"discard them first — a rebuild would overwrite them and git "
                           f"cannot recover what was never committed."}
        return {"action": "rebuild", "target": str(target), "version": 1,
                "carry_uuid": uuid_, "prior": str(target),
                "why": "working tree is clean, so this rebuilds in place and "
                       "`git diff` will show exactly what changed"}
    return {"action": "create", "target": str(target), "version": 1,
            "carry_uuid": None, "prior": None}


# Files a human legitimately edits after generation: MyST directive options, ToC,
# frontmatter. Everything else in a DevNote(M) is fetched or boilerplate.
MERGEABLE = ("main.md", "curvenote.yml")


def completeness(target: Path):
    """What is missing before this DevNote(M) can build."""
    fs = scan_dir(target) if target.is_dir() else {"figures": []}
    missing = [f["ref"] for f in fs["figures"] if not f["present"]]
    empty = sorted(d.name for d in target.iterdir()
                   if d.is_dir() and d.name in ("figures", "general", "plasmids", "experiments")
                   and not any(d.rglob("*.*"))) if target.is_dir() else []
    return {"missing_figures": missing, "empty_dirs": empty,
            "buildable": (target / "main.md").is_file() and not missing}


def run_assemble(target: Path, drive_url, repo, doc_url=None):
    """Fetch phase. Adds files from Drive; never touches markdown or config."""
    prompt = (
        f"Use the devstudio-assemble-devnote-assets skill to download the supporting files "
        f"for the DevNote(M) at:\n  {target}\n\n"
        f"The skill's invocation model wants three inputs — here they are, so nothing has "
        f"to be discovered:\n"
        f"  Target: {target}\n"
        f"  DevNote(G): {doc_url or '(unknown — find it in the DevNote folder below)'}\n"
        f"  Root folder ID (the skill's invocation model calls this the 'SF-Node folder "
        f"ID' — it is the deployment's current root, not literally San Francisco Node): "
        f"{DRIVE_ROOT_ID}\n\n"
        f"The DevNote folder in Drive, which holds the figure manifest, is:\n"
        f"  {drive_url}\n\n"
        f"**Read the manifest first and use the Drive ids it already carries** — the "
        f"figure entries include `notebook_drive_id`, `platemap_drive_id` and "
        f"`data_drive_id`. Call `download_file_content` with those ids directly. Do not "
        f"`search_files` by filename for any asset whose id the manifest already gives "
        f"you; that is a wasted round trip per file.\n\n"
        f"Fetch the notebooks, platemaps, raw instrument data, DNA construct files and any "
        f"static figures that main.md references, into the matching subdirectories "
        f"(experiments/, figures/, general/, plasmids/).\n\n"
        f"Do NOT modify main.md or curvenote.yml — this step only adds files. "
        f"Do not modify anything in Google Drive.\n\n"
        f"When finished print, exactly:\nASSETS: <comma-separated relative paths you wrote>"
    )
    cmd = ["claude", "-p", prompt, "--allowedTools", "Skill", "ToolSearch",
           *GM_TOOLS, *DRIVE_READ_TOOLS,
           "mcp__claude_ai_Google_Drive__download_file_content"]
    try:
        r = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, timeout=2400)
        out = ((r.stdout or "") + (r.stderr or "")).strip()
        return {"ok": r.returncode == 0, "log": out[-4000:]}
    except subprocess.TimeoutExpired:
        return {"ok": False, "log": "assemble timed out"}
    except FileNotFoundError:
        return {"ok": False, "log": "the `claude` CLI is not on PATH"}


@job_guard
def _run_assemble_only(job_id, target, drive_url, repo, doc_url=None):
    res = run_assemble(Path(target), drive_url, repo, doc_url)
    comp = completeness(Path(target))
    with JOBS_LOCK:
        JOBS[job_id].update({
            "status": "done" if comp["buildable"] else "error",
            "out_dir": str(target), "assets_log": res["log"], **comp,
            "error": None if comp["buildable"]
                     else ("assets fetched but "
                           + (f"{len(comp['missing_figures'])} figure(s) still missing"
                              if comp["missing_figures"] else "the build is still incomplete"))})


def snapshot_dir(out_root, slug):
    """Where the last *generated* version is kept, as the merge base.

    Not the last committed version — the base must be what the generator last produced,
    so a 3-way merge can tell a human edit apart from a generator change."""
    repo = git_root(Path(out_root))
    root = repo if repo else Path(out_root).parent
    return Path(root) / ".devstudio" / "generated" / slug


def save_current(target: Path, hold: Path):
    """Copy the human-editable files aside before the generator overwrites them."""
    hold.mkdir(parents=True, exist_ok=True)
    for f in MERGEABLE:
        if (target / f).is_file():
            shutil.copy2(target / f, hold / f)


def merge_generated(target: Path, snap: Path, hold: Path):
    """3-way merge each regenerated file against the edits that were there.

    base = what the generator produced last time; ours = what is on disk now
    (base plus hand edits); theirs = what the generator just produced."""
    out = []
    snap.mkdir(parents=True, exist_ok=True)
    for f in MERGEABLE:
        new, base, ours = target / f, snap / f, hold / f
        if not new.is_file():
            continue
        generated = new.read_text(errors="replace")
        if not ours.is_file():
            out.append({"file": f, "status": "created"})
        elif not base.is_file():
            # Nothing to merge against — keep the new file, but never silently drop
            # whatever was there.
            (target / (f + ".pre-rebuild")).write_text(ours.read_text(errors="replace"))
            out.append({"file": f, "status": "no-base"})
        elif ours.read_text(errors="replace") == base.read_text(errors="replace"):
            out.append({"file": f, "status": "unedited"})
        else:
            r = subprocess.run(
                ["git", "merge-file", "-p", "--marker-size=7",
                 "-L", "your edits", "-L", "last generated", "-L", "newly generated",
                 str(ours), str(base), str(new)],
                capture_output=True, text=True)
            if r.returncode < 0:
                out.append({"file": f, "status": "merge-failed"})
            else:
                new.write_text(r.stdout)
                out.append({"file": f,
                            "status": "merged" if r.returncode == 0 else "conflict",
                            "conflicts": r.returncode})
        # The base for next time is always what the generator produced, not the merge.
        (snap / f).write_text(generated)
    return out


@job_guard
def _run_g_to_m(job_id, payload, repo, out_root):
    target = Path(payload["target"])
    snap = snapshot_dir(out_root, payload["name"])
    hold = Path(tempfile.mkdtemp(prefix="devstudio-pre-"))
    save_current(target, hold)
    prompt = (
        f"Use the devstudio-devnote-g-to-devnote-m skill to convert this reviewed "
        f"DevNote(G) into a DevNote(M).\n\n"
        f"Source Google Doc: {payload['doc_url']}\n"
        f"Source DevNote folder in Drive: {payload['url']}\n"
        f"The figure-provenance manifest, if present, is in that same Drive folder.\n\n"
        f"Write the DevNote(M) directory to exactly this local path:\n  {target}\n"
        f"Create it if it does not exist. Do not write anywhere else on disk, and do not "
        f"modify anything in Google Drive — this conversion is read-only with respect to Drive.\n\n"
        + (f"This is version {payload['version']} of this DevNote. In curvenote.yml use "
           f"EXACTLY this project id:\n  {payload['carry_uuid']}\n"
           f"Do not generate a new UUID. It is carried forward from the previous version on "
           f"purpose — a new id would make the Curvenote venue treat this as an unrelated "
           f"project rather than a new version of the same work.\n\n"
           if payload.get("carry_uuid") else "")
        + f"Do NOT invoke devstudio-submit-to-github and do not open any pull request; stop "
        f"once the directory is written so a human can inspect it first.\n\n"
        f"When finished, print two final lines, exactly:\n"
        f"OUT_DIR: {target}\n"
        f"FILES: <comma-separated list of the files you created at the top level>"
    )
    cmd = ["claude", "-p", prompt, "--allowedTools", "Skill", "ToolSearch",
           *GM_TOOLS, *DRIVE_READ_TOOLS,
           "mcp__claude_ai_Google_Drive__download_file_content"]
    try:
        r = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, timeout=2400)
        out = (r.stdout or "") + (("\n" + r.stderr) if r.stderr else "")
        wrote = (target / "main.md").is_file()
        files = sorted(x.name for x in target.iterdir()) if target.is_dir() else []
        fs = scan_dir(target) if target.is_dir() else {"figures": [], "flags": []}
        missing = [f["ref"] for f in fs["figures"] if not f["present"]]
        empty_dirs = sorted(
            d.name for d in target.iterdir()
            if d.is_dir() and d.name in ("figures", "general", "plasmids", "experiments")
            and not any(d.rglob("*.*"))) if target.is_dir() else []
        update = {"status": "done" if wrote else "error",
                  "out_dir": str(target), "files": files,
                  "version": payload.get("version"),
                  "uuid": payload.get("carry_uuid") or project_uuid(target),
                  "missing_figures": missing, "empty_dirs": empty_dirs,
                  "log": out.strip()[-6000:]}
        if not wrote:
            update["error"] = f"no main.md was written to {target} — check the log"
        update["transform_ok"] = wrote
        if wrote:
            merges = merge_generated(target, snap, hold)
            update["merges"] = merges
            conflicted = [m["file"] for m in merges if m["status"] == "conflict"]
            kept = [m["file"] for m in merges if m["status"] == "merged"]
            if conflicted:
                update["merge_warning"] = (
                    "Your edits and the regenerated content touched the same lines in "
                    + ", ".join(conflicted) + " — conflict markers are in the file.")
            elif kept:
                update["merge_note"] = ("Your edits to " + ", ".join(kept)
                                        + " were merged into the regenerated content.")
        shutil.rmtree(hold, ignore_errors=True)
    except subprocess.TimeoutExpired:
        update = {"status": "error", "error": "timed out after 40 minutes", "log": ""}
    except FileNotFoundError:
        update = {"status": "error", "error": "the `claude` CLI is not on PATH", "log": ""}
    with JOBS_LOCK:
        JOBS[job_id].update({**update, "phase": "assets"})

    # Phase 2 — fetch. A fresh version always needs its own assets, so this is the
    # default rather than a second click.
    if update.get("transform_ok"):
        res = run_assemble(target, payload.get("url"), repo, payload.get("doc_url"))
        comp = completeness(target)
        update.update({"assets_log": res["log"], **comp, "phase": "done"})
        update["status"] = "done" if comp["buildable"] else "error"
        if not comp["buildable"]:
            bits = []
            if comp["missing_figures"]:
                bits.append(f"{len(comp['missing_figures'])} figure reference(s) still do not "
                            f"resolve: " + ", ".join(comp["missing_figures"][:4]))
            if comp["empty_dirs"]:
                bits.append("still no assets in " + ", ".join(comp["empty_dirs"]) + "/")
            update["warning"] = ("Structure written and assets attempted, but it will not "
                                 "build as-is — " + "; ".join(bits))
        with JOBS_LOCK:
            JOBS[job_id].update(update)

    if update.get("status") == "done":
        for row in _DEVNOTES["rows"]:
            if row.get("name") == payload["name"]:
                row["myst"] = {"dir": str(target), "version": payload.get("version"),
                               "uuid": update.get("uuid"), "current": True}
        _save_devnote_cache()
        push_devnote_map(repo, _DEVNOTES["rows"])


@job_guard
def _run_devnote(job_id, payload, repo):
    logs = "\n".join(f"  - {n}" for n in payload["logs"])
    a = payload
    prompt = (
        f"Use the devstudio-log-to-devnote-g skill to draft ONE DevNote(G) by pooling these "
        f"Log folders from '{DRIVE_ROOT_NAME}/logs':\n{logs}\n\n"
        f"This set is the human's authoritative selection — do not add or drop folders, and "
        f"do not go looking for others.\n\n"
        f"Write the result into '{DRIVE_ROOT_NAME}/devnotes', inside a NEW folder named "
        f"exactly '{payload['name']}'. Name the draft Google Doc 'main' and write the figure "
        f"manifest alongside it, following the existing devnotes/ layout.\n\n"
        f"Fill the Authors table with exactly one row and no others:\n"
        f"  Name: {a['author']}\n  ORCID: {a['orcid'] or '[PLEASE FILL IN]'}\n"
        f"  Email: {a['email'] or '[PLEASE FILL IN]'}\n"
        f"  Institution: {a['institution'] or '[PLEASE FILL IN]'}\n"
        f"Do not invent or infer any other author, and do not fabricate a Title — the skill's "
        f"rules on blank placeholders still apply.\n\n"
        f"If a folder named '{payload['name']}' already exists in devnotes/, stop and create "
        f"nothing.\n\n"
        f"When finished, print two final lines, exactly:\n"
        f"FOLDER_URL: <url of the new DevNote folder>\n"
        f"DOC_URL: <url of the draft Doc>"
    )
    cmd = ["claude", "-p", prompt, "--allowedTools", "Skill", "ToolSearch", *DEVNOTE_TOOLS]
    try:
        r = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, timeout=2400)
        out = (r.stdout or "") + (("\n" + r.stderr) if r.stderr else "")
        folder = re.search(r"FOLDER_URL:\s*(\S+)", out)
        doc = re.search(r"DOC_URL:\s*(\S+)", out)
        ok = r.returncode == 0 and (folder or doc)
        update = {"status": "done" if ok else "error",
                  "url": (folder or doc).group(1) if ok else None,
                  "doc_url": doc.group(1) if doc else None,
                  "log": out.strip()[-6000:]}
        if not ok and r.returncode == 0:
            update["error"] = "the run finished but reported no DevNote URL — check the log"
    except subprocess.TimeoutExpired:
        update = {"status": "error", "error": "timed out after 40 minutes", "log": ""}
    except FileNotFoundError:
        update = {"status": "error", "error": "the `claude` CLI is not on PATH", "log": ""}
    with JOBS_LOCK:
        JOBS[job_id].update(update)
    if update.get("status") == "done":
        entry = {"name": payload["name"], "url": update.get("url"),
                 "doc_url": update.get("doc_url"), "logs": payload["logs"],
                 "via": "drafted by the board", "mapped": True}
        _DEVNOTES["rows"] = [r for r in _DEVNOTES["rows"]
                             if r.get("name") != payload["name"]] + [entry]
        _save_devnote_cache()
        push_devnote_map(repo, _DEVNOTES["rows"])


DRIVE_TOOLS = [
    "mcp__claude_ai_Google_Drive__search_files",
    "mcp__claude_ai_Google_Drive__get_file_metadata",
    "mcp__claude_ai_Google_Drive__create_file",
    "mcp__claude_ai_Google_Drive__copy_file",
]
# The folder name is interpolated into a prompt, so it is validated, not trusted.
NAME_RE = re.compile(r"^\d{8}-[a-z]{1,4}(?:-[a-z0-9]+)+$")
JOBS = {}
JOBS_LOCK = threading.Lock()


def valid_log_name(date, initials, slug):
    """Rebuild the name from parts server-side. The form is a convenience, not a source."""
    date = re.sub(r"[^0-9]", "", str(date or ""))
    initials = re.sub(r"[^a-z]", "", str(initials or "").lower())[:4]
    slug = re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", str(slug or "").lower())).strip("-")
    if len(date) != 8 or not initials or not slug:
        return None, "date, initials and experiment are all required"
    try:
        datetime.strptime(date, "%Y%m%d")
    except ValueError:
        return None, f"{date} is not a real date"
    name = f"{date}-{initials}-{slug}"
    if not NAME_RE.match(name):
        return None, f"{name} is not a valid Log folder name"
    return name, None


def _run_new_log(job_id, name, repo):
    prompt = (
        f"Use the devstudio-new-log skill to create a new Log folder named exactly "
        f"'{name}' inside the '{DRIVE_ROOT_NAME}/logs' Google Drive folder, seeded from "
        f"'00-TEMPLATE-LOG'. The folder name is already decided — do not ask for or change "
        f"any part of it. Do not create anything outside {DRIVE_ROOT_NAME}/logs. "
        f"If a folder with that exact name already exists, stop and do not create a second one. "
        f"When you are finished, print the new folder's URL on the final line, "
        f"prefixed exactly with 'FOLDER_URL: '."
    )
    cmd = ["claude", "-p", prompt, "--allowedTools", "Skill", "ToolSearch", *DRIVE_TOOLS]
    try:
        r = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, timeout=600)
        out = (r.stdout or "") + (("\n" + r.stderr) if r.stderr else "")
        m = re.search(r"FOLDER_URL:\s*(\S+)", out)
        status = "done" if (r.returncode == 0 and m) else "error"
        update = {"status": status, "url": m.group(1) if m else None, "log": out.strip()[-4000:]}
        if status == "error" and r.returncode == 0:
            update["error"] = "the run finished but reported no folder URL — check the log"
    except subprocess.TimeoutExpired:
        update = {"status": "error", "error": "timed out after 10 minutes", "log": ""}
    except FileNotFoundError:
        update = {"status": "error", "error": "the `claude` CLI is not on PATH", "log": ""}
    with JOBS_LOCK:
        JOBS[job_id].update(update)


class Handler(BaseHTTPRequestHandler):
    targets = []      # list of Path (real) or dict (demo state)
    repo = None       # working dir for `claude -p`, where the skills are loadable
    out_root = None   # where DevNote(M) directories are written
    venue = "bnext-devnotes"
    here = Path(__file__).parent

    def _send(self, code, body, ctype):
        data = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _index(self):
        m = re.search(r"[?&]i=(\d+)", self.path)
        i = int(m.group(1)) if m else 0
        return max(0, min(i, len(self.targets) - 1))

    def _state(self, i, use_gh=True):
        t = self.targets[i]
        return t if isinstance(t, dict) else build_state(t, use_gh)

    def do_POST(self):
        path = self.path.split("?")[0]
        if path not in ("/api/new-log", "/api/new-devnote", "/api/devnote-to-myst",
                        "/api/curvenote-draft", "/api/assemble-assets", "/api/preview"):
            return self._send(404, "not found", "text/plain")
        try:
            n = int(self.headers.get("Content-Length") or 0)
            body = json.loads(self.rfile.read(n) or b"{}")
        except (ValueError, json.JSONDecodeError):
            return self._send(400, json.dumps({"error": "bad JSON"}), "application/json")

        if path == "/api/new-devnote":
            return self._new_devnote(body)
        if path == "/api/devnote-to-myst":
            return self._g_to_m(body)
        if path == "/api/curvenote-draft":
            return self._curvenote(body)
        if path == "/api/assemble-assets":
            return self._assemble(body)
        if path == "/api/preview":
            name = (body.get("name") or "").strip()
            if str(body.get("stop", "")).lower() in ("1", "true", "yes"):
                stop_preview()
                return self._send(200, json.dumps({"stopped": True}), "application/json")
            st = myst_state(self.out_root, name)
            if not st:
                return self._send(400, json.dumps(
                    {"error": f"no local DevNote(M) for {name} — run → MyST first"}),
                    "application/json")
            url, err = start_preview(name, st["dir"])
            if err:
                return self._send(502, json.dumps({"error": err}), "application/json")
            return self._send(200, json.dumps({"url": url, "name": name, "dir": st["dir"]}),
                              "application/json")

        name, err = valid_log_name(body.get("date"), body.get("initials"), body.get("slug"))
        if err:
            return self._send(400, json.dumps({"error": err}), "application/json")
        if str(body.get("dryRun", "")).lower() in ("1", "true", "yes"):
            return self._send(200, json.dumps({"name": name, "dryRun": True}),
                              "application/json")
        if not self.repo:
            return self._send(400, json.dumps(
                {"error": "no --repo given, so the skill cannot be found"}), "application/json")

        # Drive allows duplicate folder titles silently, so check before creating.
        # 60s rather than the read cache's 5 min: a stale yes here creates a twin.
        existing, err = drive_logs(self.repo, max_age=60)
        if err and not existing:
            return self._send(502, json.dumps(
                {"error": f"could not check for an existing folder, so nothing was created "
                          f"({err})"}), "application/json")
        hit = next((f for f in existing if (f.get("name") or "").strip() == name), None)
        if hit:
            return self._send(409, json.dumps(
                {"error": f"A Log folder named {name} already exists in {DRIVE_ROOT_NAME}/logs.",
                 "existing": hit.get("url"), "name": name}), "application/json")

        job_id = uuid.uuid4().hex[:12]
        with JOBS_LOCK:
            JOBS[job_id] = {"status": "running", "name": name, "kind": "log",
                            "started": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        threading.Thread(target=_run_new_log, args=(job_id, name, self.repo),
                         daemon=True).start()
        self._send(202, json.dumps({"job": job_id, "name": name}), "application/json")

    def _assemble(self, body):
        name = (body.get("name") or "").strip()
        st = myst_state(self.out_root, name, [r.get("name") for r in _DEVNOTES["rows"]])
        if not st:
            return self._send(400, json.dumps(
                {"error": f"no local DevNote(M) for {name} — run → MyST first"}),
                "application/json")
        d = next((x for x in _DEVNOTES["rows"] if x.get("name") == name), {})
        job_id = uuid.uuid4().hex[:12]
        with JOBS_LOCK:
            JOBS[job_id] = {"status": "running", "name": name, "kind": "assets",
                            "phase": "assets", "target": st["dir"],
                            "started": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        threading.Thread(target=_run_assemble_only,
                         args=(job_id, st["dir"], d.get("url"), self.repo,
                               d.get("doc_url")),
                         daemon=True).start()
        self._send(202, json.dumps({"job": job_id, "name": name, **st}), "application/json")

    def _curvenote(self, body):
        name = (body.get("name") or "").strip()
        st = myst_state(self.out_root, name, [r.get("name") for r in _DEVNOTES["rows"]])
        if not st:
            return self._send(400, json.dumps(
                {"error": f"no local DevNote(M) for {name} — run → MyST first"}),
                "application/json")
        if not st["has_main"] or not st["has_config"]:
            return self._send(400, json.dumps(
                {"error": f"{st['dir']} is missing "
                          + ("main.md" if not st["has_main"] else "curvenote.yml")}),
                "application/json")
        if st["missing_figures"]:
            # Submitting something that cannot build wastes a venue submission and
            # produces a draft nobody can read.
            return self._send(409, json.dumps(
                {"error": f"{len(st['missing_figures'])} figure reference(s) do not resolve, "
                          f"so this will not build: "
                          + ", ".join(st["missing_figures"][:4]),
                 "hint": "Run devstudio-assemble-devnote-assets first.",
                 "dir": st["dir"]}), "application/json")
        if str(body.get("dryRun", "")).lower() in ("1", "true", "yes"):
            return self._send(200, json.dumps({"dryRun": True, "venue": self.venue, **st}),
                              "application/json")

        job_id = uuid.uuid4().hex[:12]
        with JOBS_LOCK:
            JOBS[job_id] = {"status": "running", "name": name, "kind": "curvenote",
                            "dir": st["dir"], "version": st["version"],
                            "venue": self.venue,
                            "started": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        threading.Thread(target=_run_curvenote,
                         args=(job_id, st["dir"], self.venue), daemon=True).start()
        self._send(202, json.dumps({"job": job_id, "name": name, "venue": self.venue,
                                    **st}), "application/json")

    def _g_to_m(self, body):
        name = (body.get("name") or "").strip()
        known = {d.get("name") for d in _DEVNOTES["rows"]}
        if name not in known:
            return self._send(400, json.dumps(
                {"error": f"{name or '(blank)'} is not a DevNote in devnotes/"}),
                "application/json")
        d = next(x for x in _DEVNOTES["rows"] if x.get("name") == name)
        if not d.get("doc_url"):
            return self._send(400, json.dumps(
                {"error": f"{name} has no draft Doc recorded, so there is nothing to convert"}),
                "application/json")
        if not self.out_root:
            return self._send(400, json.dumps(
                {"error": "no output directory — start the board with --out <dir>"}),
                "application/json")
        plan = plan_g_to_m(self.out_root, name)
        if plan["action"] == "blocked" and not str(
                body.get("dryRun", "")).lower() in ("1", "true", "yes"):
            return self._send(409, json.dumps({"error": plan["why"], **plan}),
                              "application/json")
        if str(body.get("dryRun", "")).lower() in ("1", "true", "yes"):
            return self._send(200, json.dumps(
                {"name": name, "doc_url": d.get("doc_url"), "dryRun": True, **plan}),
                "application/json")

        payload = {"name": name, "doc_url": d.get("doc_url"), "url": d.get("url"),
                   "target": plan["target"], "version": plan["version"],
                   "carry_uuid": plan["carry_uuid"]}
        job_id = uuid.uuid4().hex[:12]
        with JOBS_LOCK:
            JOBS[job_id] = {"status": "running", "name": name, "kind": "g2m",
                            "target": plan["target"], "version": plan["version"],
                            "action": plan["action"],
                            "started": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        threading.Thread(target=_run_g_to_m,
                         args=(job_id, payload, self.repo, self.out_root),
                         daemon=True).start()
        self._send(202, json.dumps({"job": job_id, "name": name, **plan}),
                   "application/json")

    def _new_devnote(self, body):
        author = (body.get("author") or "").strip()
        email = (body.get("email") or "").strip()
        orcid = (body.get("orcid") or "").strip()
        institution = (body.get("institution") or "").strip()
        logs = [str(x).strip() for x in (body.get("logs") or []) if str(x).strip()]

        if not author:
            return self._send(400, json.dumps({"error": "an author name is required"}),
                              "application/json")
        if not logs:
            return self._send(400, json.dumps(
                {"error": "select at least one Log folder to pool"}), "application/json")
        if email and not EMAIL_RE.match(email):
            return self._send(400, json.dumps({"error": f"{email} is not an email address"}),
                              "application/json")
        if orcid and not ORCID_RE.match(orcid):
            return self._send(400, json.dumps(
                {"error": "ORCID must look like 0000-0002-1825-0097"}), "application/json")

        # The selection must be real folders, not names the page invented.
        known, err = drive_logs(self.repo, max_age=300)
        names = {f.get("name") for f in known}
        unknown = [n for n in logs if n not in names]
        if unknown and known:
            return self._send(400, json.dumps(
                {"error": f"not Log folders in logs/: {', '.join(unknown)}"}),
                "application/json")

        name, err = devnote_name(author, logs)
        if err:
            return self._send(400, json.dumps({"error": err}), "application/json")
        if str(body.get("dryRun", "")).lower() in ("1", "true", "yes"):
            return self._send(200, json.dumps({"name": name, "logs": logs, "dryRun": True}),
                              "application/json")
        if not self.repo:
            return self._send(400, json.dumps(
                {"error": "no --repo given, so the skill cannot be found"}), "application/json")

        payload = {"name": name, "author": author, "email": email, "orcid": orcid,
                   "institution": institution, "logs": logs}
        job_id = uuid.uuid4().hex[:12]
        with JOBS_LOCK:
            JOBS[job_id] = {"status": "running", "name": name, "kind": "devnote",
                            "logs": logs,
                            "started": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        threading.Thread(target=_run_devnote, args=(job_id, payload, self.repo),
                         daemon=True).start()
        self._send(202, json.dumps({"job": job_id, "name": name}), "application/json")

    def do_GET(self):
        path = self.path.split("?")[0]
        try:
            if path == "/api/state":
                use_gh = "gh=0" not in self.path
                st = self._state(self._index(), use_gh)
                st["index"] = self._index()
                st["fleet_size"] = len(self.targets)
                self._send(200, json.dumps(st, indent=1), "application/json")
            elif path == "/api/fleet":
                use_gh = "gh=0" not in self.path
                n = len(self.targets)
                # gh is ~30s per DevNote; serial would make a 12-note fleet unusable.
                with ThreadPoolExecutor(max_workers=8) as pool:
                    states = list(pool.map(lambda i: self._state(i, use_gh), range(n)))
                rows = []
                for i, st in enumerate(states):
                    r = fleet_row(st)
                    r["index"] = i
                    r["gh_pending"] = st.get("gh_pending", False)
                    rows.append(r)
                self._send(200, json.dumps({"rows": rows, "gh_pending": not use_gh}, indent=1),
                           "application/json")
            elif path in ("/", "/index.html"):
                page = "board.html" if (len(self.targets) == 1 and not self.repo) \
                    else "fleet.html"
                self._send(200, (self.here / page).read_text(), "text/html; charset=utf-8")
            elif path == "/api/logs":
                force = "force=1" in self.path
                rows, err = drive_logs(self.repo, REFRESH_NOW if force else LOGS_TTL)
                out = [drive_log_row(f) for f in rows
                       if f.get("name") and not TEMPLATE_RE.search(f["name"])]
                # Cache only: never rebuild here. Rebuilding is opt-in via
                # /api/devnotes/refresh, because it costs minutes.
                by_log = devnotes_by_log(_DEVNOTES["rows"])
                for r in out:
                    r["devnotes"] = by_log.get(r["slug"], [])
                self._send(200, json.dumps({"rows": out, "error": err,
                                            "skipped_templates": len(rows) - len(out)}),
                           "application/json")
            elif path == "/api/docs":
                force = "force=1" in self.path
                rows, err = drive_docs(self.repo, REFRESH_NOW if force else LOGS_TTL)
                self._send(200, json.dumps(
                    {"rows": [drive_doc_row(f) for f in rows], "error": err}),
                    "application/json")
            elif path == "/api/devnotes/push":
                ok, log = push_devnote_map(self.repo, _DEVNOTES["rows"])
                self._send(200 if ok else 502,
                           json.dumps({"pushed": ok, "log": log}), "application/json")
            elif path == "/api/devnotes/refresh":
                _DEVNOTES["rows"] = []          # force a rebuild from manifests
                logs, _ = drive_logs(self.repo)
                names = [f["name"] for f in logs
                         if f.get("name") and not TEMPLATE_RE.search(f["name"])]
                dn, err = drive_devnotes(self.repo, names)
                self._send(200, json.dumps({"devnotes": dn, "error": err}), "application/json")
            elif path == "/api/devnotes":
                force = "force=1" in self.path
                rows, err = drive_devnote_index(self.repo, REFRESH_NOW if force else LOGS_TTL)
                out = []
                for d in rows:
                    row = devnote_row(d)
                    row["myst"] = myst_state(self.out_root, row["slug"],
                                             [r.get("name") for r in rows])
                    out.append(row)
                self._send(200, json.dumps(
                    {"rows": out, "raw": rows, "error": err, "venue": self.venue,
                     "out_root": self.out_root, "built": _DEVNOTES["ts"]}),
                    "application/json")
            elif path == "/api/preview":
                with PREVIEW_LOCK:
                    self._send(200, json.dumps(
                        {"name": PREVIEW["name"], "url": PREVIEW["url"],
                         "dir": PREVIEW["dir"],
                         "running": bool(PREVIEW["proc"] and PREVIEW["proc"].poll() is None),
                         "log": PREVIEW["log"][-30:]}), "application/json")
            elif path == "/api/jobs":
                with JOBS_LOCK:
                    out = [{**j, "id": k} for k, j in JOBS.items()]
                out.sort(key=lambda j: j.get("started") or "", reverse=True)
                self._send(200, json.dumps({"jobs": out[:20]}), "application/json")
            elif path == "/api/job":
                m = re.search(r"[?&]id=([0-9a-f]+)", self.path)
                with JOBS_LOCK:
                    job = JOBS.get(m.group(1)) if m else None
                self._send(200 if job else 404,
                           json.dumps(job or {"error": "no such job"}), "application/json")
            elif path == "/note":
                self._send(200, (self.here / "board.html").read_text(), "text/html; charset=utf-8")
            else:
                self._send(404, "not found", "text/plain")
        except Exception as e:
            self._send(500, json.dumps({"error": str(e)}), "application/json")

    def log_message(self, *a):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("devnote_dir", nargs="*", help="one or more DevNote directories")
    ap.add_argument("--roots", nargs="*", default=[],
                    help="parent dirs to scan for DevNotes (any dir with curvenote.yml)")
    ap.add_argument("--demo", action="store_true", help="synthetic TA queue, touches no disk")
    ap.add_argument("--repo", help="directory to run `claude -p` in; the skills must load "
                                   "there (e.g. your nucleus-skills checkout)")
    ap.add_argument("--out", help="directory to write DevNote(M) output into "
                                  "(default ~/Documents/code/devnote-out)")
    ap.add_argument("--venue", default="bnext-devnotes", help="Curvenote venue")
    ap.add_argument("--drive-root", help="Deployment Drive root folder name "
                                         f"(default: {DEFAULT_DRIVE_ROOT_NAME!r})")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--json", action="store_true", help="print state and exit")
    a = ap.parse_args()

    targets = []
    if a.demo:
        import demo
        demo.STAGES = STAGES
        targets = demo.demo_states()
    else:
        for d in a.devnote_dir:
            root = Path(d).expanduser().resolve()
            if not root.is_dir():
                sys.exit(f"not a directory: {root}")
            targets.append(root)
        for r in a.roots:
            for cn in sorted(Path(r).expanduser().resolve().glob("*/curvenote.yml")):
                if cn.parent not in targets:
                    targets.append(cn.parent)
    if not targets and not a.repo:
        sys.exit("give --repo (Drive-backed board), or a DevNote directory / --roots / --demo")

    if a.json:
        if not targets:
            sys.exit("--json needs a local DevNote directory")
        t = targets[0]
        print(json.dumps(t if isinstance(t, dict) else build_state(t), indent=2))
        return

    if not a.demo:
        # Demo mode must never leak real Drive state onto screen — that is the
        # one thing it promises. These caches hold whatever the last real run
        # against a real deployment Drive saw.
        _load_devnote_cache()
        _load_logs_cache()
        _load_docs_cache()
    Handler.targets = targets
    Handler.repo = str(Path(a.repo).expanduser().resolve()) if a.repo else None
    global DRIVE_ROOT_NAME
    if a.drive_root:
        DRIVE_ROOT_NAME = a.drive_root
    Handler.venue = a.venue
    Handler.out_root = str(Path(a.out).expanduser().resolve()) if a.out \
        else str(Path("~/Documents/code/devnote-out").expanduser())
    label = "demo fleet" if a.demo else f"{len(targets)} DevNote(s)"
    print(f"devstudio-board  {label}\n  http://localhost:{a.port}")
    ThreadingHTTPServer(("127.0.0.1", a.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
