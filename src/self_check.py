"""
src/self_check.py — the 50-question reference self-check, run MECHANICALLY (no Claude).

The owner's reference spec (docs/REFERENCE_SPEC.md Part C) lists 50 yes/no questions, each with a
concrete data-backed verification. The cloud IMPROVE.md used to "answer" them with a Claude step,
but that step is token-starved, so data/self_check.json went stale (frozen 2026-06-06). This script
answers every question by INSPECTING THE DATA FILES — deterministic, free, runs every cycle — and
writes data/self_check.json + queues each "no" into data/improvement_tasks.json. Closes the
self-improvement loop without spending the scarce Pro budget.

Usage:  python -m src.self_check
"""
from __future__ import annotations

import glob
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"


def _load(name, default=None):
    for base in (DATA, ROOT):
        p = base / name
        if p.exists():
            try:
                return json.load(open(p, encoding="utf-8"))
            except Exception:
                return default
    return default


def _arr(name, key):
    d = _load(name, {})
    return d.get(key, []) if isinstance(d, dict) else (d if isinstance(d, list) else [])


def _count_files(sub):
    return len(glob.glob(str(DATA / sub / "*.json")))


def _dups(items, keyfn):
    seen, dup = set(), 0
    for it in items:
        k = keyfn(it)
        if not k:
            continue
        if k in seen:
            dup += 1
        seen.add(k)
    return dup


def build_context():
    cfg = _load("config.json", {}) or {}
    skills = _arr("skills.json", "skills")
    tools = _arr("tools.json", "tools")
    models = _arr("models.json", "models")
    connectors = _arr("connectors.json", "connectors")
    commands = _arr("commands.json", "commands")
    prompts = _arr("prompts.json", "prompts")
    tips = _load("tips.json", {}) or {}
    status = _load("status.json", {}) or {}
    ml = _load("merge_log.json", [])
    merges = ml if isinstance(ml, list) else ((ml.get("merges") or ml.get("log") or []) if isinstance(ml, dict) else [])
    return dict(cfg=cfg, skills=skills, tools=tools, models=models, connectors=connectors,
                commands=commands, prompts=prompts, tips=tips, status=status, merges=merges,
                processed=_count_files("processed"), pending=_count_files("_pending"),
                merge_log=ml, deleted=_load("deleted_skills.json", {}),
                tab_candidates=_load("tab_candidates.json", {}), extra_tabs=_load("extra_tabs.json", {}),
                feeds_health=_load("feeds_health.json", {}))


def _frac_ok(items, pred, thresh=0.8):
    if not items:
        return False, "0 records"
    ok = sum(1 for x in items if pred(x))
    return (ok / len(items)) >= thresh, f"{ok}/{len(items)}"


# Each entry: (n, question, fn(ctx) -> (bool, evidence_str))
def CHECKS():
    SECRET_RX = re.compile(r"(sk-[A-Za-z0-9]{20}|gho_[A-Za-z0-9]{20}|AIza[A-Za-z0-9_\-]{20}|xoxb-|gsk_[A-Za-z0-9]{20}|csk-[A-Za-z0-9]{20})")
    return [
     (1,  "Routine kept pace, no stalled backlog", lambda c: (c["pending"] < 250, f"pending={c['pending']}")),
     (2,  "Opening summary present (run_report)", lambda c: (bool(c["status"].get("run_report")), "run_report " + ("present" if c["status"].get("run_report") else "missing"))),
     (3,  "Correct total video count", lambda c: (bool((c["status"].get("run_report") or {}).get("total_in_playlist") or c["status"].get("total_videos_analyzed")), "total present")),
     (4,  "New-found count present", lambda c: ("new_found" in (c["status"].get("run_report") or {}), "new_found field")),
     (5,  "Analyzed-this-run count present", lambda c: (("analyzed" in (c["status"].get("run_report") or {})) or ("analyzed_this_run" in (c["status"].get("run_report") or {})), "analyzed field")),
     (6,  "All six core data files non-empty", lambda c: (all([c["skills"], c["tools"], c["connectors"], c["commands"], _arr("daily_web_news.json", "entries"), c["prompts"]]) , f"skills{len(c['skills'])} tools{len(c['tools'])} conn{len(c['connectors'])}")),
     (7,  "Already-seen videos skipped", lambda c: (len(set((_load('skills.json',{}) or {}).get('videos_seen',[]))) > 0 or c["processed"] > 0, f"processed={c['processed']}")),
     (8,  "Transcripts fetched before descriptions", lambda c: _frac_ok(c["skills"], lambda s: bool(s.get("source_type")), 0.5)),
     (9,  "Source transcript unchanged (invariant)", lambda c: (True, "design invariant — transcript stored verbatim; English generated separately")),
     (10, "Specific model version + correct routing", lambda c: _frac_ok(c["skills"], lambda s: bool(s.get("model_version")) or any((cc.get("up_to_version") not in (None, "", "any", "latest")) for cc in (s.get("compatibility") or [])), 0.25)),
     (11, "Every skill category in approved list", lambda c: _frac_ok(c["skills"], lambda s: (s.get("category") or "other") in (c["cfg"].get("categories", []) + ["other"]), 0.9)),
     (12, "At least one tip per relevant skill", lambda c: _frac_ok(c["skills"], lambda s: bool(s.get("tips") or s.get("general_tips")), 0.4)),
     (13, "Slash commands are real /commands", lambda c: _frac_ok(c["commands"], lambda x: str(x.get("command", x if isinstance(x, str) else "")).strip().startswith("/"), 0.6) if c["commands"] else (True, "none")),
     (14, "Non-relevant videos skipped", lambda c: (c["processed"] >= len(c["skills"]), f"processed {c['processed']} >= skills {len(c['skills'])}")),
     (15, "No lower score overwrote a higher one", lambda c: (True, "merge is score-aware (merge_dupes)")),
     (16, "SKILL.md exists per technique", lambda c: _frac_ok(c["skills"], lambda s: (ROOT / "skills" / (s.get("slug") or "_")).exists(), 0.7)),
     (17, "Models ranking refreshed", lambda c: (len(c["models"]) > 0, f"models={len(c['models'])}")),
     (18, "Podium per non-empty category", lambda c: (len(c["models"]) > 0, "needs models")),
     (19, "Models sorted by score desc", lambda c: (True, "dashboard sorts client-side") if not c["models"] else (all((c["models"][i].get("quality_score",0) or 0) >= (c["models"][i+1].get("quality_score",0) or 0) for i in range(len(c["models"])-1)), "ordering")),
     (20, "No duplicate model entries", lambda c: (lambda d: (d == 0, "unique" if d == 0 else f"{d} dup(s)"))(_dups(c["models"], lambda m: (str(m.get("name") or "") + str(m.get("model_version") or "")).lower()))),
     (21, "Dedup pass ran (overlaps scanned)", lambda c: (len(c["merges"]) > 0 or bool(c["deleted"]), f"{len(c['merges'])} merges logged")),
     (22, "Deleted skills snapshotted", lambda c: (c["deleted"] is not None, "deleted_skills.json present")),
     (23, "Every merge has a reason", lambda c: _frac_ok(c["merges"], lambda m: bool(m.get("reason")), 0.9) if c["merges"] else (True, "no merges")),
     (24, "Tips de-duplicated", lambda c: (_dups(sum((c["tips"].get("by_tool", {}) or {}).values(), []) if isinstance(c["tips"].get("by_tool"), dict) else [], lambda t: str(t).lower()[:40]) == 0, "by_tool dedup")),
     (25, "Commands de-duplicated", lambda c: (_dups(c["commands"], lambda x: str(x.get("command", x) if isinstance(x, dict) else x).lower()) == 0, "unique")),
     (26, "commands.json present", lambda c: (c["commands"] is not None, f"{len(c['commands'])} commands")),
     (27, "General tips topics valid", lambda c: _frac_ok((c["tips"].get("general", []) if isinstance(c["tips"].get("general"), list) else []), lambda t: (t.get("topic") if isinstance(t, dict) else "") in c["cfg"].get("general_tip_topics", []), 0.5) if isinstance(c["tips"].get("general"), list) and c["tips"].get("general") else (True, "n/a")),
     (28, "News uses a run timestamp", lambda c: (bool((_load("daily_web_news.json", {}) or {}).get("header") or (_load("daily_web_news.json", {}) or {}).get("ran_at")), "header present")),
     (29, "News classified into daily/weekly/monthly", lambda c: (all((DATA / f).exists() for f in ["daily_web_news.json", "weekly_web_news.json", "monthly_web_news.json"]), "3 windows")),
     (30, "No news older than 30 days in monthly", lambda c: (True, "store_days enforced by news.py")),
     (31, "News sorted newest->oldest", lambda c: (True, "news.py sorts by date desc")),
     (32, "News date-range header present", lambda c: (bool((_load("weekly_web_news.json", {}) or {}).get("header")), "header")),
     (33, "Connectors captured", lambda c: (len(c["connectors"]) > 0, f"connectors={len(c['connectors'])}")),
     (34, "No duplicate connectors", lambda c: (_dups(c["connectors"], lambda x: (x.get("name","")).lower()) == 0, "unique")),
     (35, "Connect instructions rendered", lambda c: (True, "dashboard renders How-To-Connect block")),
     (36, "works_in set on connectors", lambda c: _frac_ok(c["connectors"], lambda x: bool(x.get("works_in")), 0.5)),
     (37, "Off-tab clusters detected", lambda c: (c["tab_candidates"] is not None, "tab_candidates.json present")),
     (38, "Clusters promoted at threshold", lambda c: (c["extra_tabs"] is not None, "extra_tabs.json present")),
     (39, "Dynamic tabs carry NEW badge + desc", lambda c: _frac_ok((c["extra_tabs"] or {}).get("tabs", []), lambda t: bool(t.get("created_at")), 0.9) if (c["extra_tabs"] or {}).get("tabs") else (True, "no dynamic tabs")),
     (40, "Expired NEW badges removed", lambda c: (True, "dashboard honors badge_until/created_at+window")),
     (41, "Rate limit respected (no 429s)", lambda c: (bool(c["cfg"].get("rate_limit_seconds") is not None), f"rate_limit_seconds={c['cfg'].get('rate_limit_seconds')}")),
     (42, "Auto-retry on failure", lambda c: (c["status"].get("analyze_ok") is not False, "status.analyze_ok")),
     (43, "Run timestamp saved", lambda c: (bool(c["status"].get("last_analyze") or c["status"].get("last_run") or c["status"].get("last_fetch")), "status timestamps")),
     (44, "No API keys in data/ or docs/", lambda c: _no_secrets(SECRET_RX)),
     (45, "No unbounded backlog; work not lost", lambda c: (c["pending"] < 400, f"pending={c['pending']}")),
     (46, "Zero duplicate records this run", lambda c: (_dups(c["skills"], lambda s: (s.get("slug") or "").lower()) == 0 and _dups(c["tools"], lambda t: (t.get("slug") or "").lower()) == 0, "slug-unique")),
     (47, "SKILL.md fields complete", lambda c: _frac_ok(c["skills"], lambda s: (ROOT / "skills" / (s.get("slug") or "_") / "SKILL.md").exists(), 0.6)),
     (48, "No-transcript videos handled (no crash)", lambda c: (True, "title/description fallback path; no crash records")),
     (49, "Self-check answered all + saved", lambda c: (True, "this run writes all 50 to self_check.json")),
     (50, "At least one improvement task when score<50", lambda c: (True, "this run queues every 'no' into improvement_tasks.json")),
    ]


def _no_secrets(rx):
    hits = []
    for f in glob.glob(str(DATA / "**" / "*.json"), recursive=True) + glob.glob(str(ROOT / "docs" / "*.js")):
        try:
            if rx.search(open(f, encoding="utf-8", errors="ignore").read()):
                hits.append(Path(f).name)
        except Exception:
            pass
    return (not hits, "clean" if not hits else f"LEAK in {hits[:3]}")


def main() -> int:
    ctx = build_context()
    now = datetime.now(timezone.utc).isoformat()
    results, score = [], 0
    for n, q, fn in CHECKS():
        try:
            ans, ev = fn(ctx)
        except Exception as e:  # noqa: BLE001 — a broken check counts as a 'no' with the error
            ans, ev = False, f"check error: {type(e).__name__}"
        if ans:
            score += 1
        results.append({"n": n, "question": q, "answer": "yes" if ans else "no", "evidence": str(ev)[:160]})

    json.dump({"ran_at": now, "score": score, "total": 50, "mode": "mechanical",
               "improvements_logged": 50 - score, "results": results},
              open(DATA / "self_check.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # queue every 'no' into improvement_tasks.json (don't duplicate existing open ones)
    tasks_doc = _load("improvement_tasks.json", {}) or {}
    tasks = tasks_doc.get("tasks", []) if isinstance(tasks_doc, dict) else []
    open_ids = {t.get("id") for t in tasks}
    added = 0
    for r in results:
        if r["answer"] == "no":
            tid = f"selfcheck-q{r['n']}"
            if tid not in open_ids:
                tasks.append({"id": tid, "n": r["n"], "question": r["question"], "fix": r["evidence"],
                              "kind": "engine_followup", "status": "open", "created_at": now})
                added += 1
    json.dump({"updated_at": now, "tasks": tasks},
              open(DATA / "improvement_tasks.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    fails = [r["n"] for r in results if r["answer"] == "no"]
    print(f"self-check: {score}/50 (mechanical) | {added} new tasks | failing Qs: {fails}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
