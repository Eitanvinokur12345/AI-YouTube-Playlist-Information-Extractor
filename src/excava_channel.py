"""
src/excava_channel.py — the GitHub-issue channel into EXCAVA (Phase 1: multi-channel task send).

The dashboard is a static page, so its cockpit form can't write to the repo — instead it opens
a PREFILLED GitHub issue titled "EXCAVA: <text>". The excava_inbox workflow runs this module,
which parses the title and applies it, then the workflow comments the receipt and closes the
issue. Three channels, one inbox: tell Claude / edit the file / GitHub issue (works on phone).

Commands (title after the "EXCAVA:" prefix):
    kill | safe | run            -> set data/excava_config.json mode (kill switch / safe-mode)
    approve <task-id>            -> add to data/excava_approvals.json granted (applied next beat)
    weight <area> <0-100>        -> set a priority-weights dial value (e.g. weight access 95)
    anything else                -> a TASK: appended to data/excava_inbox.json (owner rank, G-8)

Env: ISSUE_TITLE, ISSUE_BODY, ISSUE_NUMBER. Prints the receipt (the workflow comments it back).
Free, mechanical, no tokens.
"""
from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
MODES = ("run", "safe", "kill")


def _rw(name: str, mutate) -> dict:
    p = DATA / name
    try:
        obj = json.load(open(p, encoding="utf-8"))
    except Exception:
        obj = {}
    mutate(obj)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    return obj


def apply(title: str, body: str, number: str) -> str:
    text = re.sub(r"^\s*EXCAVA\s*:\s*", "", title or "", flags=re.I).strip()
    if not text:
        return "Nothing after the EXCAVA: prefix — closed with no action."
    low = text.lower()

    if low in MODES:
        _rw("excava_config.json", lambda c: c.__setitem__("mode", low))
        return {"kill": "🔴 KILL SWITCH ON — EXCAVA won't touch the bus until you send 'EXCAVA: run'.",
                "safe": "🟡 SAFE MODE — EXCAVA syncs + routes but no worker acts until 'EXCAVA: run'.",
                "run": "🟢 RUN MODE — EXCAVA operating normally."}[low]

    m = re.match(r"direction\s+(.+)$", text, re.I | re.S)
    if m:
        stmt = m.group(1).strip()[:600]
        def _dir(d):
            ds = d.setdefault("directions", [])
            ds.append({"id": f"dir-{len(ds) + 1}", "text": stmt,
                       "at": datetime.now(timezone.utc).isoformat(),
                       "via": f"github-issue #{number}", "status": "active", "excava_reading": ""})
        _rw("excava_direction.json", _dir)
        return ("🧭 Direction recorded (Phase 6 loop). EXCAVA acknowledges it next beat — its reading "
                "appears on the cockpit's Direction card, and major changes preview against it first. "
                "Overrule any reading with another 'EXCAVA: direction …'.")

    m = re.match(r"approve\s+(\S+)$", low)
    if m:
        tid = m.group(1)
        def _grant(a):
            g = set(a.get("granted", [])); g.add(tid); a["granted"] = sorted(g)
        _rw("excava_approvals.json", _grant)
        return f"✅ Approval granted for `{tid}` — applied and re-queued on the next beat (hourly)."

    m = re.match(r"weight\s+([a-z\-]+)\s+(\d{1,3})$", low)
    if m:
        area, val = m.group(1), min(100, int(m.group(2)))
        def _w(c):
            c.setdefault("priority_weights", {})[area] = val
        _rw("excava_config.json", _w)
        return f"🎚 Priority weight set: **{area} = {val}** — auto-priorities re-order next beat."

    task_id = f"gh{number or datetime.now(timezone.utc).strftime('%m%d%H%M')}"
    def _add(inbox):
        tasks = inbox.setdefault("tasks", [])
        if any(t.get("task") == text and t.get("status") in ("queued", "working") for t in tasks):
            return
        tasks.append({"id": task_id, "task": text, "status": "queued",
                      "added_at": datetime.now(timezone.utc).isoformat(),
                      "via": "github-issue", "detail": (body or "").strip()[:500]})
    _rw("excava_inbox.json", _add)
    return (f"📥 Queued as **{task_id}** at owner rank (outranks all auto-priorities). "
            "EXCAVA picks it up on the next beat (hourly); outward work still waits for the gate. "
            "Track it on the cockpit → https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/docs/")


def main() -> int:
    import sys
    try:                                   # Windows console defaults to cp1252 -> emoji crash
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    receipt = apply(os.environ.get("ISSUE_TITLE", ""), os.environ.get("ISSUE_BODY", ""),
                    os.environ.get("ISSUE_NUMBER", ""))
    print(receipt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
