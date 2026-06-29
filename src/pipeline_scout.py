"""
src/pipeline_scout.py — find catalogue items that could improve OUR OWN pipeline, comprehensively.

The owner rightly pushed back: with ~4000 tools/skills/MCPs we should find far more than 2 helpers.
The old version used 5 narrow keyword lists over tools+connectors only. This version scans EVERY
type (tools, connectors, skills, models) across the system's real PROCESSES, ranks by quality, and
feeds the strongest into self-improvement (queued as "evaluate integrating X") — so the scout is an
improvement TO the system, not a separate panel. Free, mechanical.

Run:  python -m src.pipeline_scout
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "pipeline_scout.json"
TASKS = DATA / "improvement_tasks.json"
NOW = datetime.now(timezone.utc).isoformat()

# Every real PROCESS in the pipeline + the signals of a tool that could improve it. Goal it serves.
PROCESSES = [
    ("Retrieval: web search/scrape", "G1", ["firecrawl", "tavily", " exa ", "serpapi", "brave search",
     "bright data", "scrape", "crawl", "web search", "apify", "scrapingbee", "jina"]),
    ("Retrieval: transcripts/audio", "G1", ["transcript", "whisper", "deepgram", "assemblyai", "yt-dlp",
     "caption", "subtitle", "speech to text", " stt ", "diariz"]),
    ("Retrieval: browser automation", "G1", ["playwright", "puppeteer", "selenium", "browser use",
     "computer use", "stagehand", "browserbase", "browser automation"]),
    ("Analysis: structured extraction", "G1", ["structured output", "json mode", "extraction",
     "instructor", "function calling", "schema", "parse", "ocr"]),
    ("Activator: embeddings/RAG/search", "G2", ["embedding", "vector", "semantic search", " rag",
     "retrieval augmented", "reranker", "pinecone", "weaviate", "qdrant", "chroma", "hybrid search"]),
    ("Dedup/entity resolution", "G2", ["dedup", "deduplicat", "entity resolution", "fuzzy match",
     "canonical", "record linkage", "normaliz"]),
    ("Validation / QA / guardrails", "G3", ["guardrail", "validation", "pydantic", "json schema",
     "link checker", "url valid", "lint", "data quality"]),
    ("Agents / orchestration (the OS)", "G6", ["agent framework", "orchestrat", "langgraph", "crewai",
     "autogen", "workflow", "multi-agent", "n8n", "flowise", "dspy", "smolagents", "controlflow"]),
    ("Storage: vector / graph DB", "G6", ["vector database", "graph database", "neo4j", "duckdb",
     "sqlite", "knowledge graph", "graphrag"]),
    ("Observability / eval", "G2", ["observability", "tracing", "langsmith", "langfuse", " eval",
     "evaluation", "monitoring", "benchmark"]),
    ("Token / cost optimization", "G4", ["prompt cach", "router", "semantic cache", "cost optim",
     "litellm", "token", "context compress", "prompt optim"]),
    ("Brain / graph visualization", "G6", ["graph viz", "gephi", "obsidian", "cytoscape", "d3",
     "sigma.js", "force graph", "graphify"]),
]


def _items(name, key, kind):
    try:
        d = json.load(open(DATA / name, encoding="utf-8"))
        return [(kind, x) for x in (d.get(key, []) if isinstance(d, dict) else [])]
    except Exception:
        return []


def main() -> int:
    pool = (_items("tools.json", "tools", "tool") + _items("connectors.json", "connectors", "connector")
            + _items("skills.json", "skills", "skill") + _items("models.json", "models", "model"))
    blobs = [(k, x, f" {x.get('name','') or x.get('skill_name','')} "
              f"{x.get('description','') or x.get('what_it_does','') or ''} {x.get('category','')} ".lower())
             for k, x in pool]

    roles, total = [], 0
    for proc, goal, kws in PROCESSES:
        finds = []
        for kind, x, blob in blobs:
            if any(k in blob for k in kws):
                finds.append({"name": x.get("name") or x.get("skill_name"), "kind": kind,
                              "quality": x.get("quality_score") or 0,
                              "link": x.get("homepage") or x.get("github") or x.get("url") or "",
                              "desc": (str(x.get("description") or x.get("what_it_does") or ""))[:110]})
        seen, uniq = set(), []
        for f in sorted(finds, key=lambda f: f["quality"], reverse=True):
            n = (f["name"] or "").lower()
            if n and n not in seen:
                seen.add(n); uniq.append(f)
        total += len(uniq)
        roles.append({"process": proc, "goal": goal, "count": len(uniq),
                      "recommended": uniq[0]["name"] if uniq else None, "finds": uniq[:8]})

    OUT.write_text(json.dumps({"generated_at": NOW, "status": "proposals — approve to integrate",
                               "total_candidates": total, "processes": roles},
                              ensure_ascii=False, indent=2), encoding="utf-8")

    # FEED self-improvement: queue the top candidate per process as an "evaluate integrating" task.
    tj = json.load(open(TASKS, encoding="utf-8")) if TASKS.exists() else {"tasks": []}
    tasks = tj.get("tasks", []); have = {t.get("scout_key") for t in tasks}; added = 0
    for r in roles:
        if r["recommended"]:
            k = f"scout:{r['process']}"
            if k not in have:
                tasks.append({"scout_key": k, "kind": "scout", "goal": r["goal"],
                              "question": f"[pipeline] evaluate '{r['recommended']}' to improve: {r['process']}",
                              "fix": f"{r['count']} candidates found for '{r['process']}'. Pick the best free one and wire it in as a sub-job.",
                              "status": "open", "created_at": NOW}); added += 1
    if added:
        TASKS.write_text(json.dumps({"updated_at": NOW, "tasks": tasks}, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"pipeline_scout: {total} candidates across {len(PROCESSES)} processes; queued {added} into self-improvement.")
    for r in roles:
        print(f"  {r['count']:3}  {r['process']:34}  top: {r['recommended']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
