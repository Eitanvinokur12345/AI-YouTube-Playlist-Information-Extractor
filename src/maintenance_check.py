"""
src/maintenance_check.py — the MAINTENANCE protocol (part of self-improvement).

A self-running integrity sweep over the whole system, so quality doesn't silently rot as the
library grows. It catches the failure modes that turn the Obsidian brain into "huge white lines"
(empty notes, duplicate titles that collide, oversized category hubs that render as hairballs,
phantom wikilinks) AND the broader data-health problems (missing fields, version-less vendor names,
orphan connectors, stale lanes). It writes data/maintenance.json (a graded report) and queues the
worst issues into improvement_tasks.json. Free, mechanical, no Claude tokens.

Usage:  python -m src.maintenance_check
"""
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "maintenance.json"
TASKS = DATA / "improvement_tasks.json"
NOW = datetime.now(timezone.utc)

VENDOR_BARE = {"claude", "chatgpt", "gpt", "gemini", "grok", "llama", "sora", "veo", "copilot"}


def load(name, default):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return default


def _items(name, key):
    d = load(name, {})
    return d.get(key, []) if isinstance(d, dict) else (d if isinstance(d, list) else [])


def _title(s: str) -> str:
    t = re.sub(r'[\\/:*?"<>|#^\[\]]+', " ", str(s or "")).strip()
    return re.sub(r"\s+", " ", t)[:90]


def main() -> int:
    skills = _items("skills.json", "skills")
    tools = _items("tools.json", "tools")
    conns = _items("connectors.json", "connectors")
    prompts = _items("prompts.json", "prompts")

    issues = []

    def add(sev, area, what, count, fix, sample=None):
        issues.append({"severity": sev, "area": area, "issue": what, "count": count,
                       "fix": fix, "sample": (sample or [])[:5]})

    # ── Brain-breaking problems (the "white lines") ───────────────────────────────
    # 1) Empty notes: items whose body would be blank (no description/use/what) -> blank graph dots.
    def empty(items, fields, nk):
        return [str(x.get(nk) or x.get("slug") or "?") for x in items
                if not any(str(x.get(f, "")).strip() for f in fields)]
    e_sk = empty(skills, ["description", "use_case", "tips"], "skill_name")
    e_to = empty(tools, ["description"], "name")
    e_co = empty(conns, ["what_it_does", "description"], "name")
    if e_sk or e_to or e_co:
        # build_graph.py (fire 10, 2026-07-26) now skips these from the dashboard graph AND
        # build_brain.py already skipped them from the Obsidian export — so this is no longer a
        # RENDER bug, just the underlying data-completeness gap (same pool deep_retrieve drains).
        add("medium", "data", "Items with no description (excluded from both brain renders, still hollow records)",
            len(e_sk) + len(e_to) + len(e_co),
            "Backfill via deep_retrieve/analysis; these no longer break the graph but stay useless "
            "in search/detail views until they have real content.", e_sk + e_to + e_co)

    # 2) Title collisions: many items map to the SAME Obsidian note filename -> they overwrite each
    #    other and the hub links all point at one node (a giant white star).
    def collisions(items, nk):
        c = Counter(_title(x.get(nk) or x.get("slug") or "") for x in items)
        return {k: n for k, n in c.items() if n > 1 and k}
    col = {}
    for items, nk in [(skills, "skill_name"), (tools, "name"), (conns, "name"), (prompts, "title")]:
        col.update(collisions(items, nk))
    if col:
        add("high", "brain", "Title collisions: distinct items share one note name and overwrite each other",
            sum(col.values()), "De-duplicate or suffix colliding titles so each item is its own note.",
            list(col.keys()))

    # 3) Oversized hubs: a category with hundreds of members renders as an unreadable hairball.
    cat_counts = Counter(str(x.get("category") or "other") for x in (tools + skills))
    big = {c: n for c, n in cat_counts.items() if n > 120}
    if big:
        add("medium", "brain", "Oversized category hubs become hairballs in the graph view",
            sum(big.values()), "Sub-bucket big categories (cap members per hub, add sub-hubs) so the "
            "graph stays readable.", [f"{c} ({n})" for c, n in big.items()])

    # ── Broader data-health problems ──────────────────────────────────────────────
    bare = [t.get("name") for t in tools
            if (t.get("name", "").strip().lower() in VENDOR_BARE) and not t.get("model_version")]
    if bare:
        add("medium", "data", "Version-less bare vendor names kept as tools",
            len(bare), "Re-derive an exact version for each, or fold into the proper product record.", bare)

    orphan_conn = [c.get("name") for c in conns if not (c.get("url") or c.get("install_or_source"))]
    if orphan_conn:
        add("low", "data", "Connectors with no URL/source can't be installed or verified",
            len(orphan_conn), "Resolve each connector's repo/package URL (or drop it).", orphan_conn)

    noq = [t.get("name") for t in tools if not t.get("quality_score")]
    if noq:
        add("low", "data", "Tools with no quality score can't be ranked",
            len(noq), "Score them in the next analysis pass.", noq)

    # ── Stale lanes (from pipeline_status) ────────────────────────────────────────
    ps = load("pipeline_status.json", {})
    stale = [l["label"] for l in (ps.get("lanes") or []) if l.get("status") in ("slow", "stale", "idle")]
    if stale:
        add("high", "pipeline", "Pipeline lanes overdue — retrieval/analysis may have stalled",
            len(stale), "Check the workflow logs for these lanes; re-dispatch if blocked.", stale)

    sev_rank = {"high": 3, "medium": 2, "low": 1}
    issues.sort(key=lambda i: (sev_rank.get(i["severity"], 0), i["count"]), reverse=True)
    score = max(0, 100 - sum(sev_rank[i["severity"]] * min(i["count"], 30) for i in issues) // 4)
    grade = "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 60 else "D"

    OUT.write_text(json.dumps({
        "generated_at": NOW.isoformat(), "health_score": score, "grade": grade,
        "issue_count": len(issues), "issues": issues,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    # queue HIGH-severity issues into self-improvement (dedup by a stable key).
    queued = 0
    tj = load("improvement_tasks.json", {"tasks": []}) or {"tasks": []}
    tasks = tj.get("tasks", [])
    have = {t.get("maint_key") for t in tasks}
    for i in issues:
        key = f"{i['area']}:{i['issue'][:40]}"
        if i["severity"] == "high" and key not in have:
            tasks.append({"maint_key": key, "kind": "maintenance",
                          "question": f"[maintenance/{i['area']}] {i['issue']} ({i['count']})",
                          "fix": i["fix"], "status": "open", "created_at": NOW.isoformat()})
            queued += 1
    if queued:
        TASKS.write_text(json.dumps({"updated_at": NOW.isoformat(), "tasks": tasks},
                                    ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"maintenance_check: grade {grade} ({score}/100), {len(issues)} issue types; queued {queued} high-sev.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
