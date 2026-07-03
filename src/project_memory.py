"""
src/project_memory.py — the PROJECT MEMORY MASTER (Phase 0.7, owner-directed 2026-07-03).

The rule (see PROJECT_MEMORY.md at repo root): **no AI tool starts a change from scratch.**
Every change starts from what the project already remembers about every prior change, however
small — recalled, not re-derived. That's the token saving.

Two feeds (owner chose auto + manual WHY):
  AUTO   — every EXCAVA beat calls ingest(): new git commits + new bus-trace events become
           episodes. Zero effort, never forgotten, incremental (state tracks offsets).
  MANUAL — tools log the WHY git can't see:  python -m src.project_memory log
           --what "..." --why "..." --files "a,b"

Store (data/project_memory/): episodes.jsonl (one line per change: when/what/files/topics/why)
+ graph.json (Obsidian/graphify-style bipartite index: file->episodes, topic->episodes — the
brain the recall walks) + state.json (ingest offsets).

Recall:  python -m src.project_memory recall "cockpit mode chip"   -> a compact context pack
(top episodes + the files & hand-off docs they touch), pasteable into ANY AI tool.
Rollup keeps it bounded: episodes older than 90 days compress into monthly digests.
Free, stdlib-only, never raises out of a beat.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
PM = ROOT / "data" / "project_memory"
EPISODES = PM / "episodes.jsonl"
GRAPH = PM / "graph.json"
PSTATE = PM / "state.json"
TRACES = ROOT / "data" / "excava" / "traces"
ROLLUP_DAYS = 90

_STOP = {"the", "a", "an", "and", "or", "for", "to", "of", "in", "on", "with", "into", "from",
         "data", "json", "src", "docs", "md", "py", "js", "html", "update", "updates", "new"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _topics(text: str, files: list[str]) -> list[str]:
    words = re.findall(r"[a-zA-Z][a-zA-Z\-_]{3,}", (text or "").lower())
    parts = []
    for f in files or []:
        parts += re.split(r"[/\\.]", str(f).lower())
    seen, out = set(), []
    for w in words + parts:
        w = w.strip("-_")
        if len(w) > 3 and w not in _STOP and w not in seen:
            seen.add(w); out.append(w)
    return out[:12]


def _state() -> dict:
    try:
        return json.load(open(PSTATE, encoding="utf-8"))
    except Exception:
        return {"last_commit": "", "trace_offsets": {}}


def _save_state(st: dict) -> None:
    PM.mkdir(parents=True, exist_ok=True)
    PSTATE.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")


def _append(episodes: list[dict]) -> None:
    if not episodes:
        return
    PM.mkdir(parents=True, exist_ok=True)
    with open(EPISODES, "a", encoding="utf-8") as fh:
        for e in episodes:
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")
    # keep the graph index current (file -> episode ids, topic -> episode ids)
    try:
        g = json.load(open(GRAPH, encoding="utf-8"))
    except Exception:
        g = {"files": {}, "topics": {}}
    for e in episodes:
        for f in e.get("files", []):
            g["files"].setdefault(f, []).append(e["id"])
        for t in e.get("topics", []):
            g["topics"].setdefault(t, []).append(e["id"])
    GRAPH.write_text(json.dumps(g, ensure_ascii=False, indent=2), encoding="utf-8")


def _read_all() -> list[dict]:
    out = []
    try:
        for line in open(EPISODES, encoding="utf-8"):
            try:
                out.append(json.loads(line))
            except Exception:
                continue
    except FileNotFoundError:
        pass
    return out


def _git(*args) -> str:
    try:
        r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=30)
        return r.stdout or ""
    except Exception:
        return ""


def ingest() -> int:
    """AUTO feed: new git commits + new bus-trace events -> episodes. Incremental + safe."""
    st = _state()
    new: list[dict] = []

    # git commits since the last ingested hash (shallow CI clones just yield fewer entries).
    # Bodies are ingested too — that's where the detailed WHAT/WHY of big commits lives.
    rng = f"{st['last_commit']}..HEAD" if st.get("last_commit") else "-n 30"
    bodies = {}
    for rec in _git("log", *rng.split(), "--pretty=%H%x01%cI%x01%s%x01%b%x02").split("\x02"):
        p = rec.strip().split("\x01")
        if len(p) == 4:
            bodies[p[0]] = (p[1], p[2], re.sub(r"\s+", " ", p[3]).strip())
    log = _git("log", *rng.split(), "--pretty=@@%H", "--name-only")
    head = _git("rev-parse", "HEAD").strip()
    block_hash, files = None, []
    def _flush():
        if block_hash and block_hash in bodies:
            when, subj, body = bodies[block_hash]
            what = subj + (f" — {body[:400]}" if body else "")
            new.append({"id": f"c-{block_hash[:10]}", "at": when, "kind": "commit",
                        "what": what, "why": "", "files": files[:20],
                        "topics": _topics(what, files), "by": "git"})
    for line in log.splitlines():
        if line.startswith("@@"):
            _flush()
            block_hash, files = line[2:].strip(), []
        elif line.strip():
            files.append(line.strip())
    _flush()
    if head:
        st["last_commit"] = head

    # bus traces: routing/hand-off/completion events are project changes too
    offs = st.setdefault("trace_offsets", {})
    if TRACES.exists():
        for tf in sorted(TRACES.glob("*.jsonl")):
            lines = tf.read_text(encoding="utf-8").splitlines()
            start = offs.get(tf.name, 0)
            for i, line in enumerate(lines[start:], start):
                try:
                    ev = json.loads(line)
                except Exception:
                    continue
                if ev.get("kind") in ("handoff", "completed", "escalated", "owner_approved"):
                    what = f"[bus:{ev['kind']}] {tf.stem}: " + (
                        ev.get("doc") or ev.get("result", "") or ev.get("reason", ""))[:200]
                    new.append({"id": f"t-{tf.stem[:20]}-{i}", "at": ev.get("at", _now()),
                                "kind": "trace", "what": what, "why": "",
                                "files": [f"data/excava/traces/{tf.name}"] + (
                                    [ev["doc"]] if ev.get("doc") else []),
                                "topics": _topics(what, []), "by": ev.get("by", "excava")})
            offs[tf.name] = len(lines)

    _append(new)
    _save_state(st)
    return len(new)


def log_manual(what: str, why: str, files: list[str], by: str = "ai-tool") -> str:
    """MANUAL feed: the WHY that git can't see. One line, seconds, saves the next tool minutes."""
    import os as _os
    eid = f"m-{int(datetime.now(timezone.utc).timestamp()) % 10**8}-{_os.urandom(2).hex()}"
    _append([{"id": eid, "at": _now(), "kind": "manual", "what": what, "why": why,
              "files": files[:20], "topics": _topics(f"{what} {why}", files), "by": by}])
    return eid


def recall(query: str, k: int = 10) -> str:
    """The context pack: top-k episodes matching the query by topic/file/word overlap,
    newest-first on ties. Output is compact text any AI tool can consume."""
    q = set(_topics(query, [query]))
    if not q:
        return "(empty query)"
    scored = []
    for e in _read_all():
        hay = set(e.get("topics", [])) | set(e.get("files", []))
        exact = len(q & hay)
        # loose matches (query word inside a longer token) only count for long words,
        # and never carry an episode on their own — 'mode' must not match 'models.json'
        loose = sum(1 for t in q if len(t) >= 6 and any(t in h and t != h for h in hay))
        if exact:
            scored.append((exact * 3 + loose, e.get("at", ""), e))
    scored = sorted(scored, key=lambda x: (-x[0], x[1] or ""))[:k]
    if not scored:
        return f"No episodes match '{query}' yet — this area is genuinely new ground."
    lines = [f"PROJECT MEMORY — context pack for: {query}  ({len(scored)} episodes, newest history below)"]
    for score, _, e in scored:
        why = f"  WHY: {e['why']}" if e.get("why") else ""
        fl = ", ".join(e.get("files", [])[:4])
        lines.append(f"- [{e.get('at', '')[:16]}] ({e.get('kind')}) {e.get('what', '')[:160]}{why}"
                     + (f"\n    files: {fl}" if fl else ""))
    lines.append("Start from this. Do not re-derive what is already here.")
    return "\n".join(lines)


def rollup() -> int:
    """Bounded forever: episodes older than ROLLUP_DAYS compress into one digest per month."""
    cutoff = datetime.now(timezone.utc).timestamp() - ROLLUP_DAYS * 86400
    keep, old = [], {}
    for e in _read_all():
        try:
            ts = datetime.fromisoformat(e["at"]).timestamp()
        except Exception:
            ts = None
        if ts and ts < cutoff and e.get("kind") != "rollup":
            old.setdefault(e["at"][:7], []).append(e)
        else:
            keep.append(e)
    for month, es in old.items():
        tops: dict[str, int] = {}
        for e in es:
            for t in e.get("topics", []):
                tops[t] = tops.get(t, 0) + 1
        top = sorted(tops, key=lambda t: -tops[t])[:15]
        keep.append({"id": f"r-{month}", "at": f"{month}-01T00:00:00+00:00", "kind": "rollup",
                     "what": f"{len(es)} episodes in {month}; dominant topics: {', '.join(top)}",
                     "why": "", "files": [], "topics": top, "by": "rollup"})
    if old:
        PM.mkdir(parents=True, exist_ok=True)
        EPISODES.write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in keep),
                            encoding="utf-8")
        # rebuild the graph from what remains
        try:
            GRAPH.unlink()
        except FileNotFoundError:
            pass
        _append([])
        g = {"files": {}, "topics": {}}
        for e in keep:
            for f in e.get("files", []):
                g["files"].setdefault(f, []).append(e["id"])
            for t in e.get("topics", []):
                g["topics"].setdefault(t, []).append(e["id"])
        GRAPH.write_text(json.dumps(g, ensure_ascii=False, indent=2), encoding="utf-8")
    return sum(len(v) for v in old.values())


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="project memory master — recall before you change")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("ingest")
    sub.add_parser("rollup")
    p = sub.add_parser("recall"); p.add_argument("query"); p.add_argument("-k", type=int, default=10)
    p = sub.add_parser("log")
    p.add_argument("--what", required=True); p.add_argument("--why", required=True)
    p.add_argument("--files", default=""); p.add_argument("--by", default="ai-tool")
    a = ap.parse_args()
    if a.cmd == "ingest":
        print(f"ingested {ingest()} new episodes")
    elif a.cmd == "rollup":
        print(f"rolled up {rollup()} old episodes")
    elif a.cmd == "recall":
        print(recall(a.query, a.k))
    elif a.cmd == "log":
        print(f"logged {log_manual(a.what, a.why, [f for f in a.files.split(',') if f], a.by)}")
    else:
        ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
