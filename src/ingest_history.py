"""
src/ingest_history.py — pull the OWNER'S full project history OUT of Claude's local session
transcripts and INTO the repo, so the supervisor (even in CI) can know the entire history:
every desire, every correction, every "this is wrong". (Owner law 2026-07-07: non-negotiable.)

The transcripts live at ~/.claude/projects/<mangled>/*.jsonl (156MB, mostly tool-output noise).
This extracts the SIGNAL — every real owner (user) message — into data/excava/history.jsonl, which
IS committed and travels to CI. Run LOCALLY (it reads the local .claude dir): python -m src.ingest_history
"""
from __future__ import annotations

import glob
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "data" / "excava" / "history.jsonl"
INDEX = ROOT / "data" / "excava" / "history_index.json"
# the local-agent project dir holding the EXCAVA session transcripts
PROJ = os.path.expanduser(
    "~/.claude/projects/C--Users-eitan-AppData-Local-Packages-Claude-pzs8sxrjxfjjc-LocalCache-"
    "Roaming-Claude-local-agent-mode-sessions-814655b9-eca1-42bf-8551-cbda27cc43e2-"
    "40c20b0e-846b-4c64-bf19-3ec352240848-local-057d2ebf--ojyswd")

MAX_CHARS = 4000          # cap each owner message so the corpus stays lean
SKIP = ("tool_result", "<command-name>", "<local-command", "Caveat:", "[Request interrupted")


def _long(p: str) -> str:
    """Windows extended-length path prefix — the transcript paths exceed MAX_PATH (260)."""
    ap = os.path.abspath(p).replace("/", "\\")
    return "\\\\?\\" + ap if os.name == "nt" else p


def _text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(p.get("text", "") for p in content
                        if isinstance(p, dict) and p.get("type") == "text")
    return ""


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    files = glob.glob(PROJ + "/*.jsonl")
    rows, sessions, skipped = [], set(), 0
    for f in files:
        try:
            head = open(_long(f), encoding="utf-8", errors="ignore").read(80000)
        except Exception:
            skipped += 1
            continue
        if "xcavatortron" not in head and "EXCAVA" not in head:
            continue                                     # only EXCAVA sessions
        sess = os.path.basename(f)[:8]
        for ln in open(_long(f), encoding="utf-8", errors="ignore"):
            try:
                d = json.loads(ln)
            except Exception:
                continue
            m = d.get("message")
            if not isinstance(m, dict):
                continue
            ts = d.get("timestamp", "")
            content = m.get("content")
            # 1) OWNER MESSAGES (his desires, corrections, "this is wrong")
            if m.get("role") == "user":
                txt = _text(content).strip()
                if len(txt) >= 40 and not any(s in txt[:40] for s in SKIP):
                    sessions.add(sess)
                    rows.append({"kind": "owner_msg", "at": ts, "session": sess, "text": txt[:MAX_CHARS]})
            # 2) Q&A + tool-use decisions embedded in content parts (the ~300 answered questions)
            if isinstance(content, list):
                for p in content:
                    if not isinstance(p, dict):
                        continue
                    if p.get("type") == "tool_use" and p.get("name") == "AskUserQuestion":
                        qs = (p.get("input") or {}).get("questions", [])
                        for q in qs:
                            opts = " | ".join(o.get("label", "") for o in q.get("options", []))
                            rows.append({"kind": "question", "at": ts, "session": sess,
                                         "text": f"Q[{q.get('header', '')}]: {q.get('question', '')}  options: {opts}"[:MAX_CHARS]})
                    elif p.get("type") == "tool_result":
                        rc = p.get("content", "")
                        rc = rc if isinstance(rc, str) else json.dumps(rc, ensure_ascii=False)
                        if "have been answered" in rc:                # the owner's actual choices
                            sessions.add(sess)
                            rows.append({"kind": "answer", "at": ts, "session": sess, "text": rc[:MAX_CHARS]})
    rows.sort(key=lambda r: r["at"])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    from collections import Counter
    by_kind = Counter(r["kind"] for r in rows)
    idx = {"generated_at": datetime.now(timezone.utc).isoformat(), "records": len(rows),
           "owner_messages": by_kind.get("owner_msg", 0), "questions": by_kind.get("question", 0),
           "answers": by_kind.get("answer", 0), "by_kind": dict(by_kind),
           "sessions": sorted(sessions), "session_count": len(sessions),
           "first": rows[0]["at"] if rows else "", "last": rows[-1]["at"] if rows else "",
           "chars": sum(len(r["text"]) for r in rows)}
    INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"history: {len(rows)} records from {len(sessions)} EXCAVA sessions — "
          f"{by_kind.get('owner_msg', 0)} owner msgs, {by_kind.get('question', 0)} questions, "
          f"{by_kind.get('answer', 0)} answer-sets ({idx['chars'] // 1000}KB) -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
