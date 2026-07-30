"""
src/dynamic_tabs.py — deterministic tab_candidates -> extra_tabs promotion (EXCAVA v2/M1-M3,
non-brain front, no LLM, no network).

CLAUDE.md's Step 8b (and docs/REFERENCE_SPEC.md Q37-Q39) describe the contract: when material
keeps appearing that fits none of the existing tabs, the analyze stage logs an anecdote to
data/tab_candidates.json; "once a theme recurs across enough distinct videos" the self-improvement
stage is supposed to promote it into a real, announced dashboard tab in data/extra_tabs.json.
The READ side of this was already fully built — docs/dashboard.js renders dynamic tabs with a NEW
badge (injectDynamicTabs/renderDynamicTab/tabIsNew), and mcp_server/server.py already ships
list_dynamic_tabs/dismiss_dynamic_tab — but nothing ever WROTE a promoted tab: extra_tabs.json sat
at {"tabs": []} regardless of how often a theme recurred. This module is the missing WRITE side.

Purely mechanical and deterministic, same spirit as src/github_meta_enrich.py: group candidates by
`theme`, count DISTINCT `video_id`s (repetition from the SAME video must not count twice), and
promote any theme whose distinct-video evidence meets config.json's
self_improvement.dynamic_tabs.min_evidence_videos. Never re-creates a theme that was already
promoted (active OR dismissed — dismissal is permanent, per dismiss_dynamic_tab's own contract).
Respects max_total_active and reserved_tab_ids. Idempotent: safe to run every beat.

Run: python -m src.dynamic_tabs [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _cfg() -> dict:
    cfg = _load(ROOT / "config.json", {})
    return (cfg.get("self_improvement", {}) or {}).get("dynamic_tabs", {}) or {}


def _slugify(theme: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (theme or "").lower()).strip("-")
    return s or "untitled"


def promote(dry_run: bool = False) -> dict:
    cfg = _cfg()
    if not cfg.get("enabled", True):
        return {"skipped": "dynamic_tabs disabled in config.json"}

    min_evidence = int(cfg.get("min_evidence_videos", 5))
    max_active = int(cfg.get("max_total_active", 6))
    badge_days = int(cfg.get("new_badge_days", 7))
    reserved = {str(x).lower() for x in cfg.get("reserved_tab_ids", [])}
    cand_path = ROOT / cfg.get("candidates_file", "data/tab_candidates.json")

    candidates = _load(cand_path, {}).get("candidates", [])
    by_theme = defaultdict(list)
    for c in candidates:
        theme = str(c.get("theme") or "").strip()
        if theme:
            by_theme[theme].append(c)

    tabs_path = DATA / "extra_tabs.json"
    store = _load(tabs_path, {"tabs": []})
    tabs = store.get("tabs", [])
    known_themes = {t.get("theme") or t.get("id") for t in tabs}  # active AND dismissed — never redo
    active_count = sum(1 for t in tabs if (t.get("status") or "active") == "active")

    created = []
    for theme, items in sorted(by_theme.items(), key=lambda kv: -len({c.get("video_id") for c in kv[1]})):
        if theme in known_themes:
            continue
        video_ids = sorted({c.get("video_id") for c in items if c.get("video_id")})
        if len(video_ids) < min_evidence:
            continue
        tab_id = _slugify(theme)
        if tab_id in reserved or tab_id in {t.get("id") for t in tabs}:
            continue
        if active_count >= max_active:
            break  # cap reached; leave the rest queued in tab_candidates for a future run

        label = next((c.get("label") for c in items if c.get("label")), theme.replace("-", " ").title())
        # description: the longest distinct note gives the richest topic summary for the badge card
        notes = sorted({c.get("note") for c in items if c.get("note")}, key=len, reverse=True)
        description = notes[0] if notes else f"Recurring theme spotted across {len(video_ids)} videos."
        created_at = _now()
        seen_pairs = set()
        tab_items = []
        for c in items:
            key = (c.get("video_id"), c.get("note"))
            if key in seen_pairs:
                continue
            seen_pairs.add(key)
            tab_items.append({
                "title": c.get("label") or label,
                "sub": c.get("video_id") or "",
                "body": c.get("note") or "",
                "url": c.get("source_url") or "",
            })

        new_tab = {
            "id": tab_id,
            "theme": theme,
            "title": label,
            "description": description,
            "status": "active",
            "created_at": created_at,
            "badge_until": (datetime.now(timezone.utc) + timedelta(days=badge_days)).isoformat(),
            "evidence_video_ids": video_ids,
            "items": tab_items,
        }
        tabs.append(new_tab)
        known_themes.add(theme)
        active_count += 1
        created.append({"id": tab_id, "title": label, "evidence_videos": len(video_ids)})

    if created and not dry_run:
        tabs_path.write_text(json.dumps({"tabs": tabs}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return {
        "min_evidence_videos": min_evidence,
        "themes_seen": len(by_theme),
        "themes_already_promoted_or_dismissed": len(known_themes) - len(created),
        "themes_promoted_this_run": created,
        "active_tabs_now": active_count,
        "dry_run": dry_run,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    result = promote(dry_run=a.dry_run)
    if result.get("skipped"):
        print(f"dynamic-tabs: {result['skipped']}")
        return 0
    made = result["themes_promoted_this_run"]
    if made:
        names = ", ".join(f"{m['title']} ({m['evidence_videos']} videos)" for m in made)
        print(f"dynamic-tabs: promoted {len(made)} new tab(s): {names} — "
              f"{result['themes_seen']} theme(s) scanned, {result['active_tabs_now']} active total"
              f"{' [dry-run, not written]' if a.dry_run else ''}")
    else:
        top = f" (min_evidence_videos={result['min_evidence_videos']})"
        print(f"dynamic-tabs: nothing crossed the promotion threshold this run{top} — "
              f"{result['themes_seen']} theme(s) scanned, none yet at the evidence bar; "
              f"{result['themes_already_promoted_or_dismissed']} already handled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
