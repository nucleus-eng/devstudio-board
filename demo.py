"""Synthetic DevStudio fleet — a busy TA queue, for judging the layout.

Emits the same state schema build_state() produces, so the fleet view and the
drill-in run one code path whether the data is real or demo.
"""
from datetime import datetime, timedelta, timezone

STAGES = None  # injected by board.py to avoid a circular import


# A plausible history for each stage, so the demo timeline reads like a real one.
STAGE_EVENTS = {
    0: ("built", "devstudio-build-to-composition", "claude", "build.xlsx → 12 conditions"),
    1: ("created", None, "human", "Log folder marked ready"),
    2: ("drafted", "devstudio-log-to-devnote-g", "claude", "Log folders synthesised"),
    3: ("review_opened", None, "human", "sent to TA for review"),
    4: ("built", "devstudio-devnote-g-to-devnote-m", "claude", "main.md + curvenote.yml written"),
    5: ("assets_assembled", "devstudio-assemble-devnote-assets", "claude", "figures and notebooks downloaded"),
    6: ("pr_opened", "devstudio-submit-to-github", "claude", "draft PR opened on the archive"),
    7: ("merged", None, "human", "merged; Action submitted to Curvenote"),
    8: ("drafted", "devstudio-devnote-to-docs-g", "claude", "module spec drafted"),
    9: ("review_opened", None, "human", "sent to developers for comment"),
    10: ("pr_opened", "devstudio-docs-g-to-m", "claude", "spec page PR opened on nucleus-docs"),
}


def _passport(slug, author, reached, parked):
    """Backdate one event per completed stage, ending `parked` days ago."""
    events, n = [], reached + 1
    for k, i in enumerate(range(n)):
        ev, skill, actor, detail = STAGE_EVENTS[i]
        age = parked + (n - 1 - k) * 2.4          # ~2.4 days between stages
        ts = (datetime.now(timezone.utc) - timedelta(days=age)).isoformat(timespec="seconds")
        e = {"ts": ts, "stage": i, "event": ev, "actor": actor, "detail": detail}
        if skill:
            e["skill"] = skill
        events.append(e)
    return {"schema": "devstudio-passport/1", "slug": slug, "author": author,
            "created": events[0]["ts"], "sources": {}, "artifacts": {}, "checks": {},
            "events": events}


def _state(slug, author, reached, current_status, next_title, next_why,
           next_prompt, parked, flags=0, figs=(0, 0), pr=None, detail=None,
           asks=None, raised_by=None, ref=None):
    """reached = id of the stage the work is sitting at; everything below is done."""
    stages = []
    for i, label, owner, producer in STAGES:
        if i < reached:
            status, d = "done", "complete"
        elif i == reached:
            status, d = current_status, detail or "current"
        else:
            status, d = "todo", "not started"
        stages.append({"id": i, "label": label, "owner": owner, "producer": producer,
                       "status": status, "detail": d, "link": None})
    return {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "slug": slug, "author": author, "demo": True,
        "fs": {"root": f"~/code/nucleus-content/{slug}", "slug": slug,
               "figures": [{"ref": f"./figures/fig{n}.png", "present": n > figs[0]}
                           for n in range(1, figs[1] + 1)],
               "flags": [{"line": 40 + n * 7, "marker": "[FLAG]",
                          "text": f"[FLAG] value in the {n}th condition not found in the Log"}
                         for n in range(1, flags + 1)],
               "assets": [], "has_main": reached > 4},
        "sidecar": {}, "archive_pr": pr, "docs_pr": None,
        "stages": stages, "parked_days": parked,
        "passport": _passport(slug, author, reached, parked),
        "next": {k: v for k, v in {
            "title": next_title, "why": next_why, "prompt": next_prompt, "stage": reached,
            "asks": asks, "raised_by": raised_by, "link": ref}.items() if v is not None},
        "block": {"stage": reached, "asks": asks, "detail": next_why, "who": raised_by,
                  "ref": ref} if asks else None,
        "gh_pending": False,
    }


def demo_states():
    return [
        _state("pure-yield-rate", "R. Okafor", 3, "active",
               "Waiting on your review", "Draft has sat at the TA review gate for 9 days, "
               "carrying 6 unresolved flags", None, 9.2, flags=6,
               detail="TA review — 6 open flags, 3 unresolved comments"),

        _state("mthfs-kinetics", "R. Okafor", 7, "active",
               "Merge the archive PR", "PR #58 is green and has been idle 4 days", None, 4.1,
               pr={"number": 58, "url": "#", "state": "OPEN", "draft": False, "merged_at": None,
                   "review": "APPROVED", "checks": {"pass": 28, "fail": 0, "pending": 0},
                   "parked_days": 4.1, "branch": "devnote/mthfs-kinetics"},
               detail="PR #58 green, approved, awaiting your merge"),

        _state("emitter-cell-v2", "L. Vance", 6, "failed",
               "Fix failing CI on the archive PR", "3 checks failing on PR #61 — MyST strict build",
               "Investigate and fix the failing checks on PR #61 in nucleus-devnote-archive-1", 2.0,
               pr={"number": 61, "url": "#", "state": "OPEN", "draft": True, "merged_at": None,
                   "review": "", "checks": {"pass": 25, "fail": 3, "pending": 0},
                   "parked_days": 2.0, "branch": "devnote/emitter-cell-v2"},
               detail="PR #61: 3 check(s) failing"),

        _state("cytosol-lifetime", "L. Vance", 5, "failed",
               "Assemble the missing assets", "2 of 5 figure targets referenced by main.md are "
               "not on disk", "Use devstudio-assemble-devnote-assets to download the missing "
               "figure assets for the DevNote(M) at ~/code/nucleus-content/cytosol-lifetime",
               1.3, figs=(2, 5), detail="2 of 5 figure targets missing on disk"),

        _state("reporter-degfp", "A. Iwu", 9, "active",
               "Waiting on developer review", "Docs(G) has been open for developer comment "
               "for 12 days with no activity", None, 12.4,
               detail="Developer review — no comments in 12 days"),

        _state("base-cell-11", "A. Iwu", 10, "active",
               "Waiting on docs review", "PR #249 open in nucleus-docs, awaiting review", None, 3.0,
               detail="PR #249 open in nucleus-docs"),

        _state("txtl-mg-titration", "R. Okafor", 4, "todo",
               "Build the DevNote(M)", "DevNote(G) was approved 1 day ago; no main.md yet",
               "Use devstudio-devnote-g-to-devnote-m to turn the approved DevNote(G) into a "
               "DevNote(M) at ~/code/nucleus-content/txtl-mg-titration", 1.1,
               detail="No main.md in this directory"),

        _state("plasmid-qc-batch3", "L. Vance", 2, "active",
               "Draft the DevNote(G)", "Log folder marked ready 2 days ago",
               "Use devstudio-log-to-devnote-g to draft a DevNote(G) from the plasmid-qc-batch3 "
               "Log folder", 2.2, detail="Log folder ready — drafting not started"),

        _state("ribosome-recycling", "A. Iwu", 6, "active",
               "Open the archive PR", "DevNote(M) is complete and assets resolve; no PR yet",
               "Use devstudio-submit-to-github to open a draft PR for the DevNote(M) at "
               "~/code/nucleus-content/ribosome-recycling", 0.4,
               detail="No PR in the archive names this DevNote"),

        _state("fluor-calibration", "R. Okafor", 3, "active",
               "Waiting on your review", "Draft entered the review gate 2 days ago, 1 open flag",
               None, 2.0, flags=1, detail="TA review — 1 open flag"),

        _state("cell-free-atp", "L. Vance", 8, "todo",
               "Draft the Docs(G)", "DevNote published 5 days ago; no module spec drafted",
               "Use devstudio-devnote-to-docs-g to draft a Docs(G) from the DevNote(M) at "
               "~/code/nucleus-content/cell-free-atp", 5.0,
               detail="Published — no Docs(G) yet"),

        _state("sfgfp-maturation", "L. Vance", 3, "failed",
               "Blocked — a TA needs to answer",
               "the 30C and 37C runs disagree by 3x — do we report both or drop the 30C set?",
               None, 5.4, flags=2, asks="TA", raised_by="L. Vance",
               ref="https://docs.google.com/document/d/sfgfp?disco=c1",
               detail="[NEEDS-TA] raised in the DevNote(G) 5 days ago"),

        _state("cyto-ph-probe", "A. Iwu", 8, "failed",
               "Blocked — a developer needs to answer",
               "does this module supersede reporter-degfp or sit alongside it?",
               None, 2.1, asks="DEV", raised_by="A. Iwu",
               ref="https://docs.google.com/document/d/cytoph?disco=c7",
               detail="[NEEDS-DEV] raised in the Docs(G) 2 days ago"),

        _state("mg-atp-matrix", "L. Vance", 0, "active",
               "Generate the platemap", "build.xlsx uploaded 3 days ago; no platemap CSV yet",
               "Use devstudio-build-to-assets to turn the mg-atp-matrix build file into a "
               "Nucleus-compatible platemap CSV", 3.1,
               detail="build.xlsx present — no platemap generated"),

        _state("t7-promoter-panel", "R. Okafor", 1, "active",
               "Mark the Log folder ready", "Experiment ran 6 days ago; the Log folder has not "
               "been marked ready to draft", None, 6.2,
               detail="Log folder not yet marked ready"),

        _state("kinetic-analysis", "A. Iwu", 10, "done",
               "Pipeline complete", "Every stage this board can see is done.", None, 0.0,
               detail="PR #241 merged"),
    ]
