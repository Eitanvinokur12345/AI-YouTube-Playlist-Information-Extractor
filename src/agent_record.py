"""
src/agent_record.py — AGENT-PLATFORM LAYER 2 (owner build order 2026-07-12): the VISIBLE
per-agent TRACK RECORD. "Each agent has an in-app record — what it argued, what shipped from
its decisions — so YOU can judge which agents earn trust" (study §6: accountability).

v1, honest scope: activity + memory + participation per agent, from data that already exists —
  turns_7d        — how much it actually spoke (chat transcripts, last 7 days)
  rooms_7d        — how many distinct rooms it worked in
  engines_used    — which brains it borrowed (diversity = realness)
  positions_held  — its remembered stances (agent_memory/<id>.jsonl, layer 1)
  last_position   — the freshest thing it committed to
Hit-rate ("did what it argued SHIP?") honestly needs the initiative layer's decision→outcome
links — labeled 'next layer', not faked here.

Output: data/excava/agent_records.json → rendered in the app (Rooms tab, 👥 Agents card).
Free, stdlib-only. Run: python -m src.agent_record
"""
from __future__ import annotations

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "excava" / "agent_records.json"


def build() -> dict:
    reg = json.load(open(DATA / "excava" / "agents.json", encoding="utf-8"))
    agents = {a["id"]: a for a in reg.get("agents", [])}
    rec = {aid: {"id": aid, "name": a.get("name", aid), "dept": a.get("department", ""),
                 "role": a.get("role", ""), "turns_7d": 0, "rooms_7d": set(),
                 "engines_used": set(), "positions_held": 0, "last_position": ""}
           for aid, a in agents.items()}
    # activity from the last 7 days of transcripts
    cutoff = (datetime.now(timezone.utc) - timedelta(days=7)).date()
    for day_dir in (DATA / "excava" / "chats").glob("2026-*"):
        try:
            if datetime.fromisoformat(day_dir.name).date() < cutoff:
                continue
        except Exception:
            continue
        for f in day_dir.glob("*.jsonl"):
            for ln in f.read_text(encoding="utf-8").splitlines():
                try:
                    m = json.loads(ln)
                except Exception:
                    continue
                aid = m.get("agent", "")
                if aid in rec:
                    rec[aid]["turns_7d"] += 1
                    rec[aid]["rooms_7d"].add(f.stem)
                    rec[aid]["engines_used"].add((m.get("engine") or "?").split("/")[0])
    # layer-3 initiative: proposals + outcomes = the REAL hit-rate (owner asked 'what shipped
    # from its decisions'; deferred at layer 2, honest from birth here)
    try:
        for t in json.load(open(DATA / "excava" / "bus.json", encoding="utf-8")).get("tasks", []):
            src = str(t.get("source", ""))
            if src.startswith("agent:"):
                aid = src.split(":", 1)[1]
                if aid in rec:
                    r = rec[aid]
                    r["proposed"] = r.get("proposed", 0) + 1
                    if t.get("status") == "done":
                        r["shipped"] = r.get("shipped", 0) + 1
    except Exception:
        pass
    # remembered positions (layer-1 memory)
    for p in (DATA / "excava" / "agent_memory").glob("*.jsonl"):
        aid = p.stem
        if aid in rec:
            rows = p.read_text(encoding="utf-8").splitlines()
            rec[aid]["positions_held"] = len(rows)
            try:
                rec[aid]["last_position"] = json.loads(rows[-1]).get("said", "")[:120]
            except Exception:
                pass
    records = sorted(({**r, "rooms_7d": len(r["rooms_7d"]),
                       "engines_used": sorted(r["engines_used"])}
                      for r in rec.values()),
                     key=lambda r: -r["turns_7d"])
    report = {"generated_at": datetime.now(timezone.utc).isoformat(),
              "window": "last 7 days",
              "note": ("Layer-2 accountability: activity + memory + participation per agent. "
                       "Hit-rate (did what it argued SHIP?) arrives with the initiative layer's "
                       "decision-to-outcome links — not faked here."),
              "agents": records}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return report


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    r = build()
    act = [a for a in r["agents"] if a["turns_7d"]]
    print(f"agent-record: {len(r['agents'])} agents, {len(act)} active in 7d; top:")
    for a in act[:6]:
        print(f"  {a['name']:<10} ({a['dept']}/{a['role']}) turns={a['turns_7d']} rooms={a['rooms_7d']} "
              f"engines={','.join(a['engines_used'])} positions={a['positions_held']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
