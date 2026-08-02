"""
src/maintenance_check.py — the MAINTENANCE protocol (part of self-improvement).

A self-running integrity sweep over the whole system, so quality doesn't silently rot as the
library grows. It catches the failure modes that turn the Obsidian brain into "huge white lines"
(empty notes, duplicate titles that collide, oversized category hubs that render as hairballs,
phantom wikilinks) AND the broader data-health problems (missing fields, version-less vendor names,
orphan connectors, stale lanes, elements that miss their own per-type quality bar — see
src/quality_bar.py). It writes data/maintenance.json (a graded report) and queues the
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
    # 1) Empty notes: items whose body would be blank (no description/use/what) -> blank graph dots
    #    -- UNLESS they carry a real link, in which case build_graph.py/build_brain.py already
    #    skip them from both the in-app graph and the Obsidian vault (verified fire 117: both
    #    builders' own `has_body()` gate does exactly this), so they never render as a blank node
    #    anywhere. Treating those the same as a true dead-end (no body AND no link) mislabeled a
    #    187-item mining-enrichment backlog as a "high severity, brain-breaking" defect it isn't
    #    -- it's a real gap, just a different and lower-urgency one. Skills stay strict: a bare
    #    product-name skill with a real link but zero captured technique is still boilerplate
    #    (the exact anti-boilerplate pattern fire 11 fixed at the point of creation), so a link
    #    does NOT excuse a skill the way it excuses a tool/connector stub awaiting enrichment.
    def _has_link(x):
        return any(str(x.get(k, "")).strip()
                   for k in ("github", "homepage", "website", "url", "source_url"))

    def split_empty(items, fields, nk, link_excuses=False):
        blank, stub = [], []
        for x in items:
            if any(str(x.get(f, "")).strip() for f in fields):
                continue
            label = str(x.get(nk) or x.get("slug") or "?")
            (stub if (link_excuses and _has_link(x)) else blank).append(label)
        return blank, stub

    e_sk_blank, _ = split_empty(skills, ["description", "use_case", "tips"], "skill_name")
    e_to_blank, e_to_stub = split_empty(tools, ["description"], "name", link_excuses=True)
    e_co_blank, e_co_stub = split_empty(conns, ["what_it_does", "description"], "name", link_excuses=True)
    blank = e_sk_blank + e_to_blank + e_co_blank
    if blank:
        add("high", "brain", "Empty-body items with no link either render as blank 'white' nodes in the brain graph",
            len(blank),
            "Skip empty-body, linkless items from the brain (or backfill a one-line description) "
            "so they stop appearing as contentless dots.", blank)
    stub = e_to_stub + e_co_stub
    if stub:
        add("medium", "data", "Discovered items have a real link but no description yet (already hidden "
            "from the brain graph/vault, not a display bug -- just waiting on enrichment)",
            len(stub),
            "Backfill a one-line description (deep_retrieve / github_meta_enrich) so these become "
            "real graph nodes instead of staying invisible.", stub)

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

    # 4) Per-type quality bar (OR-1's deliverable, src/quality_bar.py) — the visible
    #    self-improvement number (§4): what fraction of each element type actually meets its
    #    own GOOD-element bar, not just "has any quality_score at all" (check 3, above).
    from src.quality_bar import evaluate_all as _qb_evaluate_all
    qb = _qb_evaluate_all()
    weak_types = {t: s for t, s in qb["types"].items() if s["rate"] is not None and s["rate"] < 0.5}
    if weak_types:
        add("medium", "quality",
            "Element types where under half of items meet their own type-specific quality bar",
            sum(s["total"] - s["meets_bar"] for s in weak_types.values()),
            "See data/quality_bar.json sample_failing per type; re-run deep_retrieve/enrichment "
            "on the missed signals (link, concrete description, provenance).",
            [f"{t} ({s['meets_bar']}/{s['total']}, {s['rate']*100:.0f}%)" for t, s in weak_types.items()])

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
