"""
src/excava_proof.py — PROOF (owner law 2026-07-07: "I can't rely on anything — I need to SEE it").
For every department: its ACTUAL latest output + a clickable link to the RAW committed file and the
GitHub Actions log — GitHub's evidence, NOT a number I generated — so the owner verifies himself.
Plus before/after deltas of the real data. Writes PROOF.md at the repo root, regenerated every beat.
Run: python -m src.excava_proof
"""
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
GH = "https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor"
STATE = DATA / "excava" / "proof_state.json"

# dept -> the RAW data file its real work writes (the un-fakeable evidence to click)
EVIDENCE = {
    "security": "data/security.json", "visual": "data/designs.json",
    "news": "data/weekly_web_news.json", "memory": "data/brain_graph.json",
    "mining": "data/connectors.json", "analysis": "data/elements_index.json",
    "links": "data/elements_index.json", "creators": "data/created_by_excava.json",
    "improve": "data/self_check.json", "watch": "data/_pending", "transcripts": "data/processed",
}


def _load(p, d=None):
    try:
        return json.loads((DATA / p).read_text(encoding="utf-8"))
    except Exception:
        return d if d is not None else {}


def _counts() -> dict:
    """Real, independently-recomputable metrics (the owner can verify each against the raw files)."""
    ix = _load("elements_index.json", {}).get("elements", [])
    designs = _load("designs.json", {})
    designs = designs.get("designs", designs) if isinstance(designs, dict) else designs
    return {
        "elements": len(ix),
        "verified": sum(1 for e in ix if e.get("verified", {}).get("status") == "verified"),
        "with_link": sum(1 for e in ix if (e.get("links") or {}).get("website") or (e.get("links") or {}).get("github")),
        "designs": len(designs) if hasattr(designs, "__len__") else 0,
        "creations": len(_load("created_by_excava.json", {}).get("creations", [])),
    }


def _delta(cur: dict, prev: dict) -> dict:
    return {k: cur[k] - prev.get(k, cur[k]) for k in cur}


def _run_id() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=str(ROOT),
                              capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:
        return ""


def build() -> str:
    sup = _load("excava/supervisor.json")
    bus = _load("excava/bus.json")
    mv = _load("excava/movement.json")
    cur = _counts()
    prev = _load("excava/proof_state.json", {}).get("counts", {})
    d = _delta(cur, prev)
    sha = _run_id()

    # latest real output per department (from the bus)
    latest = {}
    for t in sorted(bus.get("tasks", []), key=lambda z: z.get("updated_at", "")):
        if t.get("status") == "done" and (t.get("department") or "core") != "core":
            latest[t["department"]] = t
    verdict = {v["dept"]: v for v in sup.get("verdicts", []) if v.get("dept")}

    def link(path):
        return f"[`{path}`]({GH}/blob/main/{path})"

    rows = []
    for dept in sorted(latest):
        t = latest[dept]
        res = str(t.get("result", ""))[:150]
        ev = EVIDENCE.get(dept, "")
        evlink = f"[`{ev}`]({GH}/{'tree' if '.' not in ev.split('/')[-1] else 'blob'}/main/{ev})" if ev else "—"
        v = (verdict.get(dept, {}) or {}).get("verdict", "?")
        rows.append(f"| **{dept}** | {v} | {res} | {evlink} |")

    dsum = " · ".join(f"{k} {'+' if d[k] >= 0 else ''}{d[k]}" for k in ("elements", "verified", "with_link", "designs", "creations") if d.get(k))
    trend = [h.get("done", 0) for h in mv.get("history", [])[-6:]]

    out = f"""# PROOF — what EXCAVA actually did (auto-generated every beat)

> **Do not trust these words — click the links.** Every link below goes to the RAW committed file or
> the GitHub Actions log. Those are GitHub's records, not numbers I generated. Verify anything yourself.
> Generated {datetime.now(timezone.utc).isoformat()} · commit `{sha}`

## Independently-checkable reality
- **Supervisor real_pct:** {sup.get('real_pct', '?')}%  ({sup.get('counts', {})}) — [raw supervisor.json]({GH}/blob/main/data/excava/supervisor.json)
- **Movement (done trend):** {trend or 'n/a'} — [raw movement.json]({GH}/blob/main/data/excava/movement.json)
- **Change since last beat:** {dsum or 'no measurable change this beat'}
- **Live totals (recompute yourself):** {cur['elements']} elements · {cur['verified']} verified · {cur['with_link']} with a real link · {cur['designs']} designs · {cur['creations']} creations

## SEE the agents talk (the real conversations)
- [Room transcripts by day]({GH}/tree/main/data/excava/chats) — open a `.jsonl`, read what the agents actually said.
- [Decision artifacts they produced]({GH}/tree/main/data/excava/artifacts)
- [Every CI beat + its full log]({GH}/actions/workflows/excava_beat.yml) — GitHub's log of every run.

## What each department produced (latest) — click the evidence file to verify
| department | verdict | actual output | raw evidence (click) |
|---|---|---|---|
{chr(10).join(rows) if rows else '| (none yet) | | | |'}

_Verdicts: **real** = ran a real tool / real assessment · **noop** = ran but produced nothing · **planned** = wrote a plan, did not execute · **failed**. The supervisor grades these against your intent charter + your 5-session history._
"""
    (ROOT / "PROOF.md").write_text(out, encoding="utf-8")
    STATE.write_text(json.dumps({"at": datetime.now(timezone.utc).isoformat(), "counts": cur},
                                ensure_ascii=False, indent=1), encoding="utf-8")
    return f"proof: PROOF.md written — {len(rows)} depts, real_pct {sup.get('real_pct','?')}%, delta [{dsum or 'none'}]"


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
