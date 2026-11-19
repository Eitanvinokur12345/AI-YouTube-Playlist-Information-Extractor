"""
src/power_scan.py — the POWER department's real executor (owner 2026-07-11: "the Power
department should find ways to add tools in addition to me manually adding an API KEY").

What it DOES each run (mechanical, free, honest):
  1. CAPACITY AUDIT — which engine families in the catalog have no live key here, and the
     exact free way to get one (so any 'add capacity' ask is one concrete step, never vague).
  2. HUB SELF-USE — search EXCAVA's own element hub for free engines / gateways / capacity
     tools it could adopt (the owner's law: the project must use its own information).
  3. FILE THE BEST MOVE — the single highest-value opportunity becomes a v2 pitch (who/need/
     importance/missing) in the owner's in-app decide queue, deduped.

Output: data/excava/power_scan.json + at most one new pitch per run.
Free, stdlib-only. Run: python -m src.power_scan
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "excava" / "power_scan.json"

# The exact free path to each engine family's key — capacity is one step away, never a mystery.
FREE_KEY_HOWTO = {
    "groq": "console.groq.com → API Keys (free tier, fastest llama-70b)",
    "sambanova": "cloud.sambanova.ai → free API key (llama-70b)",
    "mistral": "console.mistral.ai → La Plateforme free tier",
    "gh-models": "already free with a GitHub token (models:read) — no signup at all",
    "cerebras": "cloud.cerebras.ai → free API key (very fast llama)",
    "gemini": "aistudio.google.com → free API key (also unlocks video watch)",
    "openrouter": "openrouter.ai → free key; unlocks many :free models incl. DeepSeek R1",
    "nvidia": "build.nvidia.com → free API key (llama/nemotron)",
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def scan() -> dict:
    from src import excava_engines as engines
    live = {e["name"] for e in engines.available()}
    # 1) capacity audit: families with NO live key + the concrete free path to one
    missing = [{"kind": "free-engine-key", "engine": name, "how": FREE_KEY_HOWTO.get(name, ""),
                "value": "one more parallel brain for rooms + analysis"}
               for name, *_ in [(s[0],) for s in engines.CATALOG]
               if name not in live and name in FREE_KEY_HOWTO]
    # 2) hub self-use: free engines/gateways/capacity tools EXCAVA already knows about
    hub_hits = []
    try:
        els = json.load(open(DATA / "elements_index.json", encoding="utf-8")).get("elements", [])
        for e in els:
            hay = (str(e.get("name", "")) + " " + str(e.get("what", ""))).lower()
            if e.get("type") in ("tool", "model", "connector") and "free" in hay and any(
                    k in hay for k in ("api", "inference", "llm", "model", "gateway", "router")):
                hub_hits.append({"kind": "hub-tool", "id": e.get("id"), "name": e.get("name"),
                                 "quality": e.get("quality_score") or 0,
                                 "why": str(e.get("what", ""))[:110]})
        hub_hits.sort(key=lambda x: -x["quality"])
        hub_hits = hub_hits[:8]
    except Exception:
        pass
    report = {"generated_at": _now(),
              "note": "POWER: capacity EXCAVA can gain WITHOUT waiting for a manual key — "
                      "each item is one concrete step (owner ask 2026-07-11).",
              "engines_live_here": sorted(live),
              "opportunities": missing + hub_hits}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")

    # 3) pitch the single best move (deduped by 'what' inside _gen-style store)
    try:
        best = (hub_hits or [None])[0]
        if best and best["quality"] >= 7:
            pit_p = DATA / "excava" / "pitches.json"
            pitched = json.load(open(pit_p, encoding="utf-8")) if pit_p.exists() else {"pitches": []}
            what = f"adopt from the hub: {best['name']} (free capacity)"
            if what not in {p.get("what") for p in pitched.get("pitches", [])}:
                pitched.setdefault("pitches", []).append({
                    "id": f"pitch-{abs(hash(what)) % 100000}", "what": what,
                    "why": best["why"], "class": "new tool (tier-3 → owner pitch)",
                    "owner_what": f"Approve to let EXCAVA wire '{best['name']}' as extra free capacity.",
                    "requested_by": "Power department (capacity scan of EXCAVA's own hub)",
                    "need": "More parallel engine capacity so rooms and analysis never stall on one "
                            "surviving model.",
                    "importance": f"High — capacity is the proven bottleneck; this is free (hub quality {best['quality']}/10).",
                    "missing": "The owner's yes (new tools from scratch are tier-3 by the autonomy contract).",
                    "plan": [f"Pull '{best['name']}' from the hub and read its interface (it's already "
                             "indexed, quality " + str(best["quality"]) + "/10).",
                             "Wire it into the engine/canary pool behind the autonomy gate so the "
                             "rooms can draw on it as extra free capacity.",
                             "Run the golden-task regression, then report the new healthy-engine count "
                             "in-app so you see capacity actually went up."],
                    "effort": "Small: it's a hub adoption, not a build — roughly one beat to wire and test.",
                    "reversible": "Fully reversible — remove it from the pool and capacity returns to "
                                  "today's; no existing engine or data is touched.",
                    "hub_candidates": [{"id": best["id"], "name": best["name"]}],
                    "at": _now(), "status": "pending"})
                pit_p.write_text(json.dumps(pitched, ensure_ascii=False, indent=1), encoding="utf-8")
    except Exception:
        pass
    return report


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    r = scan()
    print(f"power-scan: {len(r['opportunities'])} opportunities "
          f"({sum(1 for o in r['opportunities'] if o['kind'] == 'free-engine-key')} missing free keys, "
          f"{sum(1 for o in r['opportunities'] if o['kind'] == 'hub-tool')} hub tools)")
    for o in r["opportunities"][:6]:
        print("  -", o.get("engine") or o.get("name"), "|", (o.get("how") or o.get("why", ""))[:70])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
