"""
src/build_hub_index.py — the PUBLIC HUB INDEX (the north-star "hub for future systems").

Excavatortron's goal is to be a huge, machine-readable hub of all AI knowledge — for Eitan AND
for OTHER/future systems. External systems shouldn't have to scrape the dashboard or guess file
names: this writes ONE versioned manifest, data/hub.json, that maps the whole library — every
dataset, its public URL, item count, and field list — so any program can discover and fetch it.

GitHub Pages serves this repo from the ROOT, and Pages sends `Access-Control-Allow-Origin: *`,
so every data file is fetchable cross-origin at:
    https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data/<file>

This is the concrete fix for the effectiveness scoreboard's recurring weak dimension `ease_external`.
Stdlib only; regenerated every analysis cycle. Companion human doc: HUB_API.md (repo root).

Usage:  python -m src.build_hub_index
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
BASE_URL = ("https://eitanvinokur12345.github.io/"
            "AI-YouTube-Playlist-Information-Extractor/data/")

# (id, file, root_key, one-line description). root_key = the array key inside the JSON.
DATASETS = [
    ("skills", "skills.json", "skills", "Techniques / skills — things you DO with AI."),
    ("tools", "tools.json", "tools", "Products / tools — things that EXIST."),
    ("models", "models.json", "models", "AI models (a ranked subset of tools)."),
    ("connectors", "connectors.json", "connectors", "MCP servers / connectors."),
    ("prompts", "prompts.json", "prompts", "Reusable prompts."),
    ("commands", "commands.json", "commands", "Slash commands / CLI commands."),
    ("daily_news", "daily_web_news.json", "entries", "AI news (50 web sources) — daily window."),
    ("weekly_news", "weekly_web_news.json", "entries", "AI news (50 web sources) — weekly window."),
    ("monthly_news", "monthly_web_news.json", "entries", "AI news (50 web sources) — monthly window."),
    ("effectiveness", "effectiveness.json", "lanes", "Per-lane effectiveness/rigidity scoreboard."),
    ("health", "health.json", None, "Live counts: transcripts X/Y + library totals."),
]


def _load(path):
    try:
        return json.load(open(path, encoding="utf-8"))
    except Exception:
        return None


def _fields(items):
    """Union of keys across a small sample (stable, order-preserving)."""
    seen = {}
    for it in items[:25]:
        if isinstance(it, dict):
            for k in it:
                seen[k] = True
    return list(seen.keys())


def main() -> int:
    health = _load(DATA / "health.json") or {}
    eff = _load(DATA / "effectiveness.json") or {}

    datasets = []
    for ds_id, fname, root_key, desc in DATASETS:
        d = _load(DATA / fname)
        if d is None:
            continue
        if root_key is None:                      # whole-object datasets (e.g. health)
            count, fields = None, list(d.keys()) if isinstance(d, dict) else []
        else:
            items = d.get(root_key, []) if isinstance(d, dict) else (d if isinstance(d, list) else [])
            count, fields = len(items), _fields(items)
        datasets.append({
            "id": ds_id, "file": fname, "url": BASE_URL + fname,
            "root_key": root_key, "count": count, "fields": fields, "description": desc,
        })

    hv = health.get("videos", {}) if isinstance(health, dict) else {}
    out = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project": "Excavatortron — AI knowledge hub",
        "north_star": "A huge, machine-readable hub of ALL AI knowledge for humans AND future "
                      "systems; the data is also used to improve existing skills, integrate new "
                      "parts, and test better versions.",
        "source": "A curated YouTube AI playlist + 50 web news sources, extracted by a free cloud pipeline.",
        "license": "Derived from PUBLIC content; transcripts are quoted verbatim. No personal data.",
        "base_url": BASE_URL,
        "cors": "open (GitHub Pages sends Access-Control-Allow-Origin: *)",
        "totals": {
            "videos_total": hv.get("total"),
            "videos_with_transcript": hv.get("with_transcript"),
            "transcript_pct": hv.get("transcript_pct"),
            **{ds["id"]: ds["count"] for ds in datasets if ds["count"] is not None},
        },
        "library_quality": eff.get("library_quality") if isinstance(eff, dict) else None,
        "datasets": datasets,
        "how_to_consume": (
            "GET base_url + <dataset.file>. Each content file is a JSON object {root_key: [items]} "
            "(see each dataset's root_key/fields). All files are CORS-open. Poll hub.json's "
            "generated_at (or any file) to detect updates — the pipeline refreshes every ~3h. "
            "Stable IDs: items carry a 'slug' (skills/tools/connectors) you can use as a key."
        ),
    }
    with open(DATA / "hub.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
    print(f"hub index: {len(datasets)} datasets | "
          + ", ".join(f"{ds['id']}={ds['count']}" for ds in datasets if ds["count"] is not None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
