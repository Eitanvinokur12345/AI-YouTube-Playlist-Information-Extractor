"""
src/trend_watch.py — the TREND-IDENTIFICATION protocol (part of self-improvement).

The system shouldn't just collect data — it should NOTICE what's surging and reshape itself
around it. This watches the growing library for (a) emerging topics that don't yet have a tab /
category / filter, and (b) categories gaining momentum, then proposes concrete dashboard features
(new tab, new filter, new category) — each scored by how well it serves the 5 MAIN GOALS and by
hard evidence (counts + momentum). Strong proposals are queued into improvement_tasks.json so the
self-improvement stage acts on them.

Momentum needs history, so each run appends a small snapshot to data/trends.json (kept ~30 deep)
and measures growth against the oldest snapshot in the window. Free, mechanical, no Claude tokens.

Usage:  python -m src.trend_watch
"""
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "trends.json"
TASKS = DATA / "improvement_tasks.json"
NOW = datetime.now(timezone.utc)

# The 5 MAIN GOALS this project exists to serve. Trends are scored by which goal they advance.
GOALS = {
    "G1": "Retrieve & analyze ALL AI info into a huge machine-readable hub",
    "G2": "Self-improve the system's own skills, protocols & data quality",
    "G3": "Integrate skills/tools/MCPs/commands into working combinations",
    "G4": "Evaluate & test tool/model versions — surface what actually works",
    "G5": "Activate — put the info to use inside ANY tool (the activator)",
}

# Emerging-tech buckets to watch. A bucket with a big footprint but NO matching category/tab is a
# candidate for a new tab/filter. keyword -> bucket label.
TOPICS = {
    "voice": ["voice", "speech", "tts", "text-to-speech", "audio", "podcast", "transcription", "stt"],
    "video": ["video", "veo", "sora", "runway", "kling", "clip", "footage", "b-roll"],
    "image": ["image", "diffusion", "midjourney", "flux", "photo", "logo", "thumbnail"],
    "3d": ["3d", "mesh", "blender", "gaussian", "nerf", "cad", "scene"],
    "music": ["music", "song", "suno", "udio", "soundtrack", "melody"],
    "agents": ["agent", "agentic", "autonomous", "multi-agent", "orchestrat", "swarm"],
    "memory_rag": ["memory", "rag", "retrieval", "vector", "embedding", "knowledge base", "recall"],
    "browser_cua": ["browser", "computer use", "computer-use", "scrape", "automation", "playwright", "puppeteer"],
    "coding": ["code", "ide", "copilot", "cursor", "refactor", "debug", "pull request"],
    "robotics": ["robot", "embodied", "drone", "hardware", "device", "wearable"],
    "realtime": ["realtime", "real-time", "streaming", "live", "low latency"],
    "data": ["data", "analytics", "sql", "dashboard", "spreadsheet", "bi "],
    "security": ["security", "prompt injection", "jailbreak", "guardrail", "safety", "red team"],
    "local_models": ["local", "on-device", "offline", "gguf", "ollama", "quantize", "edge"],
}

# Existing dashboard categories/tabs, so we only propose NEW ones.
EXISTING_CATEGORIES = {
    "code", "productivity", "agents", "research", "integration", "other", "video creation",
    "automation", "image creation", "design", "marketing", "writing", "music", "social",
}
TOPIC_TO_GOAL = {
    "agents": "G3", "memory_rag": "G1", "browser_cua": "G3", "coding": "G5", "security": "G2",
    "data": "G1", "realtime": "G4", "local_models": "G4",
}


def load(name, default):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return default


def _items(name, key):
    d = load(name, {})
    return d.get(key, []) if isinstance(d, dict) else (d if isinstance(d, list) else [])


def _blob(x: dict) -> str:
    return " ".join(str(x.get(k, "")) for k in ("name", "skill_name", "title", "description",
                                                 "what_it_does", "category", "use_case")).lower()


def snapshot() -> dict:
    tools = _items("tools.json", "tools")
    skills = _items("skills.json", "skills")
    conns = _items("connectors.json", "connectors")
    items = tools + skills + conns
    blobs = [_blob(x) for x in items]
    cats = Counter((str(x.get("category") or "other").lower()) for x in (tools + skills))
    topics = Counter()
    for b in blobs:
        for topic, kws in TOPICS.items():
            if any(k in b for k in kws):
                topics[topic] += 1
    return {"at": NOW.isoformat(), "total": len(items),
            "categories": dict(cats), "topics": dict(topics)}


def main() -> int:
    prev = load("trends.json", {}) or {}
    history = prev.get("history", [])
    cur = snapshot()
    base = history[0] if history else None          # oldest snapshot in the rolling window
    base_topics = (base or {}).get("topics", {}) if base else {}
    base_cats = (base or {}).get("categories", {}) if base else {}

    proposals = []

    # 1) EMERGING TOPIC with no tab/category yet — propose a new tab/filter.
    for topic, count in sorted(cur["topics"].items(), key=lambda kv: kv[1], reverse=True):
        label = topic.replace("_", "/")
        is_category = any(topic.split("_")[0] in c for c in EXISTING_CATEGORIES)
        momentum = count - base_topics.get(topic, count)
        if count >= 25 and not is_category:
            goal = TOPIC_TO_GOAL.get(topic, "G1")
            score = min(10, round(count / 12) + max(0, momentum))
            proposals.append({
                "key": f"tab:{topic}", "kind": "new_tab",
                "trend": f"'{label}' is a large, distinct cluster ({count} items) with no dedicated tab",
                "evidence": {"items": count, "momentum_window": momentum},
                "proposed_feature": f"Add a '{label.title()}' tab/filter so this cluster is browsable on its own",
                "goal": goal, "goal_text": GOALS[goal], "score": score})

    # 2) RISING category — momentum worth surfacing.
    for cat, count in cur["categories"].items():
        mom = count - base_cats.get(cat, count)
        if mom >= 8:
            proposals.append({
                "key": f"rising:{cat}", "kind": "rising_category",
                "trend": f"Category '{cat}' is rising fast (+{mom} since the window start, now {count})",
                "evidence": {"items": count, "momentum_window": mom},
                "proposed_feature": f"Feature '{cat}' on the home overview / pin its newest items",
                "goal": "G1", "goal_text": GOALS["G1"], "score": min(10, 4 + mom // 4)})

    proposals.sort(key=lambda p: p["score"], reverse=True)

    # roll history forward (keep ~30, which at the pipeline cadence is several days of momentum)
    history = (history + [cur])[-30:]
    OUT.write_text(json.dumps({
        "generated_at": NOW.isoformat(),
        "goals": GOALS,
        "window_from": (base or cur)["at"],
        "proposals": proposals,
        "current": {"topics": cur["topics"], "categories": cur["categories"]},
        "history": history,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    # queue the strongest NEW proposals into the self-improvement task list (dedup by key).
    queued = 0
    tj = load("improvement_tasks.json", {"tasks": []}) or {"tasks": []}
    tasks = tj.get("tasks", [])
    have = {t.get("trend_key") for t in tasks}
    for p in proposals[:5]:
        if p["score"] >= 6 and p["key"] not in have:
            tasks.append({
                "trend_key": p["key"], "kind": "trend",
                "question": f"[trend] {p['trend']}",
                "fix": p["proposed_feature"] + f"  (serves {p['goal']}: {p['goal_text']})",
                "goal": p["goal"], "status": "open", "created_at": NOW.isoformat(),
            })
            queued += 1
    if queued:
        TASKS.write_text(json.dumps({"updated_at": NOW.isoformat(), "tasks": tasks},
                                    ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"trend_watch: {len(proposals)} proposals (top score "
          f"{proposals[0]['score'] if proposals else 0}); queued {queued} into self-improvement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
