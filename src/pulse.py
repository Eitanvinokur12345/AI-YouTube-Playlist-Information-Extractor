"""src/pulse.py — ONE-GLANCE PULSE of the autonomous program (2026-07-24).

"Is it actually alive and moving while I'm away?" is Eitan's single most-repeated question, and the
honest answer was scattered across six files: the git log, AWAY_LOG.md, QUESTIONS.md,
data/guardrails_status.json, data/excava/movement.json, data/excava/local_worker.json. pulse reads
them all DETERMINISTICALLY (no engine, no key, no network) and writes two things:

  · PULSE.md               — a human one-glance status at the repo ROOT. Open the file, no server
                             needed — this is the answer to "is it working?" without reading git.
  · data/excava/pulse.json — the same snapshot as machine data (for a future cockpit card).

It does not just cheer-lead: it shows the movement DELTA, so a silent decline (done: 1566 -> 1256
over 72h, which no existing view surfaced) shows up as a red ▼ instead of hiding behind a flat
"12 departments moving". Permission-safe: git is read via subprocess INSIDE python, never as a bash
`git` command (the unattended loop stalls on cd+git).

  python -m src.pulse        # regenerate PULSE.md + pulse.json, print the human summary
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
PULSE_MD = ROOT / "PULSE.md"
PULSE_JSON = DATA / "excava" / "pulse.json"


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _age_h(iso: str):
    try:
        return (_now() - datetime.fromisoformat(iso)).total_seconds() / 3600
    except Exception:
        return None


def _rel(iso: str) -> str:
    a = _age_h(iso)
    if a is None:
        return "?"
    if a < 1:
        return f"{int(a * 60)}m ago"
    if a < 48:
        return f"{a:.1f}h ago"
    return f"{a / 24:.1f}d ago"


def _git_log(n: int = 8) -> list[dict]:
    """Last n commits, read through subprocess (permission-safe) — %x1f field sep, %cI ISO date."""
    try:
        out = subprocess.run(
            ["git", "log", f"-{n}", "--format=%h%x1f%cI%x1f%s"],
            cwd=str(ROOT), capture_output=True, text=True, timeout=20,
            encoding="utf-8", errors="replace",  # force UTF-8 — Windows locale would mojibake em-dashes (trips G-D)
        ).stdout
    except Exception:
        return []
    rows = []
    for line in out.splitlines():
        parts = line.split("\x1f")
        if len(parts) == 3:
            rows.append({"hash": parts[0], "at": parts[1], "subject": parts[2][:100]})
    return rows


def _movement() -> dict:
    mv = _load(DATA / "excava" / "movement.json", {})
    hist = mv.get("history", []) or []
    done, depts = mv.get("done"), mv.get("depts_moving")
    delta, span = None, None
    if hist and done is not None:
        latest_age = _age_h(hist[-1].get("at", "")) or 0.0
        base = None  # newest entry that is still >= 24h older than the latest point
        for h in hist:
            a = _age_h(h.get("at", ""))
            if a is not None and a >= latest_age + 24:
                base = h
        base = base or hist[0]
        if "done" in base:
            delta = done - base["done"]
            span = _age_h(base.get("at", ""))
    return {"done": done, "depts_moving": depts, "delta": delta,
            "delta_span_h": round(span, 1) if span else None, "points": len(hist)}


def _throughput() -> dict:
    """The REAL movement number, as opposed to `_movement()`'s bus snapshot.

    `_movement()` reads movement.json's `done`, which is `len([t for t in bus.json.tasks if
    status==done])` at the moment a beat ran. bus.json is a bounded working set — old completed
    tasks age out of it to make room for new ones — so that count churns (and can fall) even
    while the program keeps completing NEW work. This surfaced as a false "regression" (done
    1566 -> 1256 -> 1130) that a prior fire displayed but did not diagnose.

    state.json's `usage[dept]` is different: `beat()` only ever increments `ticks`/`done` there,
    per department, once per completed tick — it never shrinks. Summing it is the honest
    cumulative total. A dept with ticks>0 but done==0 (all handoffs, e.g. links/transcripts) is a
    real stall signal that the bus snapshot's flat 'depts moving' count hides.
    """
    st = _load(DATA / "excava" / "state.json", {})
    usage = st.get("usage", {}) or {}
    if not usage:
        return {}
    completed_total = sum(v.get("done", 0) for v in usage.values())
    stalled = sorted(d for d, v in usage.items() if v.get("ticks", 0) > 0 and v.get("done", 0) == 0)
    top = sorted(((d, v.get("done", 0)) for d, v in usage.items()), key=lambda kv: -kv[1])[:5]
    return {
        "completed_total": completed_total,
        "beats": st.get("beats", 0),
        "n_depts": len(usage),
        "stalled_depts": stalled,
        "top": top,
    }


def _drain() -> dict:
    st = _load(DATA / "excava" / "local_worker.json", {})
    if not st:
        return {"alive": False, "note": "never run"}
    age = _age_h(st.get("at", ""))
    return {"alive": age is not None and age <= 26, "age_h": round(age, 1) if age is not None else None,
            "host": st.get("host", "?"), "model": st.get("model", "?"),
            "enriched": st.get("enriched", 0), "stubs": st.get("stubs", "?")}


def _guardrails() -> dict:
    g = _load(DATA / "guardrails_status.json", {})
    return {"passing": g.get("passing"), "total": g.get("total"),
            "critical": g.get("critical_failures"), "at": g.get("generated_at", "")}


def _count(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text, re.MULTILINE))


def _questions() -> dict:
    p = ROOT / "QUESTIONS.md"
    if not p.exists():
        return {"numbered": 0, "answered": 0, "open": 0, "audit_staged": 0}
    text = p.read_text(encoding="utf-8", errors="replace")
    numbered = [ln for ln in text.splitlines() if re.match(r"^\d+\.", ln)]
    answered = [ln for ln in numbered if ("✅" in ln or "ANSWERED" in ln)]
    return {"numbered": len(numbered), "answered": len(answered),
            "open": len(numbered) - len(answered),
            "audit_staged": _count(r"^- \*\*#\d+", text)}


def _away() -> dict:
    p = ROOT / "AWAY_LOG.md"
    if not p.exists():
        return {"fires": 0, "last": ""}
    lines = [ln for ln in p.read_text(encoding="utf-8", errors="replace").splitlines()
             if re.match(r"^- \*\*", ln)]
    last = re.sub(r"^\s*-\s*", "", lines[0]).replace("**", "").strip()[:150] if lines else ""
    return {"fires": len(lines), "last": last}


def build() -> dict:
    commits = _git_log(8)
    within24 = sum(1 for c in commits if (_age_h(c["at"]) or 1e9) <= 24)
    doc = {
        "generated_at": _now().isoformat(),
        "guardrails": _guardrails(),
        "movement": _movement(),
        "throughput": _throughput(),
        "drain": _drain(),
        "questions": _questions(),
        "away": _away(),
        "commits_24h": within24,
        "recent_commits": commits,
    }
    PULSE_JSON.parent.mkdir(parents=True, exist_ok=True)
    PULSE_JSON.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    PULSE_MD.write_text(_render(doc), encoding="utf-8")
    return doc


def _arrow(delta) -> str:
    if delta is None:
        return ""
    if delta > 0:
        return f" (▲ +{delta})"
    if delta < 0:
        return f" (▼ {delta})"
    return " (→ flat)"


def _render(d: dict) -> str:
    g, mv, tp, dr, q, aw = d["guardrails"], d["movement"], d.get("throughput") or {}, d["drain"], d["questions"], d["away"]
    gl = (f"{g['passing']}/{g['total']} passing, {g['critical']} critical"
          if g.get("total") else "no status")
    drain = ("never run" if not dr.get("age_h") and dr.get("age_h") != 0 else
             f"{dr['age_h']}h ago on {dr['host']} ({dr['model']}): {dr['enriched']} enriched, {dr['stubs']} stubs")
    alive = "✅ ALIVE" if (g.get("critical") == 0 and d["commits_24h"] > 0) else "⚠ CHECK"
    span = f" over ~{mv['delta_span_h']}h" if mv.get("delta_span_h") else ""
    lines = [
        "# PULSE — autonomous program, one glance",
        f"_Auto-generated by `python -m src.pulse` at {d['generated_at'][:16]}Z. "
        "Regenerated each away fire. This is the honest 'is it working?' answer without reading git._",
        "",
        f"## {alive}",
        f"- **guardrails:** {gl}",
        f"- **commits (last 24h):** {d['commits_24h']}",
        f"- **local drain:** {drain}",
        "",
        "## Movement",
    ]
    if tp:
        lines.append(f"- **completed (cumulative, only rises):** {tp['completed_total']} "
                      f"across {tp['n_depts']} depts · {tp['beats']} beats")
        top_str = ", ".join(f"{d} {n}" for d, n in tp["top"])
        lines.append(f"- **in the bus right now:** {mv['done']} done (live snapshot — churns every "
                      f"beat, NOT a trend) · top: {top_str}")
        if tp["stalled_depts"]:
            lines.append(f"- ⚠ **never completed a task (0 cumulative):** "
                          f"{', '.join(tp['stalled_depts'])} — the real stall signal, unlike the churning snapshot above.")
    else:
        lines.append(f"- **tasks done (rolling):** {mv['done']}{_arrow(mv['delta'])}{span}")
        lines.append(f"- **departments moving:** {mv['depts_moving']}")
        if mv.get("delta") is not None and mv["delta"] < 0:
            lines.append("- ⚠ _the done-counter is DECLINING — worth a look; a flat 'depts moving' hides it._")
    lines += [
        "",
        "## Away loop",
        f"- **fires logged:** {aw['fires']}" + (f" · last: {aw['last']}" if aw['last'] else ""),
        f"- **questions open:** {q['open']} of {q['numbered']} numbered "
        f"· **audit decisions staged:** {q['audit_staged']}",
        "",
        "## Last commits",
    ]
    for c in d["recent_commits"]:
        lines.append(f"- `{c['hash']}` {_rel(c['at'])} — {c['subject']}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Regenerate PULSE.md + pulse.json")
    ap.parse_args()
    d = build()
    print(PULSE_MD.read_text(encoding="utf-8"))
    print(f"[wrote {PULSE_MD.name} + {PULSE_JSON.name}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
