"""
src/excava_leases.py — M2.2: the LEASE ARBITER. Hard ceilings, zero runaway spend.

Every engine call an agent makes goes through acquire(dept, engine): it checks the
department's DAILY token budget, the per-engine RPM cap, and the special CLAUDE/PRO budget
(so automation never eats the quota Eitan uses in Claude Desktop). Denied = held + traced,
never silently over. Ledger: data/excava/leases.json (per-UTC-day; prunes itself).
Budgets: data/excava/budgets.json (owner-tunable).

Free math: all engines are free tiers — the ceilings protect RATE LIMITS and the Pro quota,
money can't be spent because nothing paid is wired (P1).
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
EXDIR = ROOT / "data" / "excava"
LEDGER = EXDIR / "leases.json"
BUDGETS = EXDIR / "budgets.json"

DEFAULTS = {
    "note": "M2.2 daily budgets — tokens per department per UTC day + per-engine requests/min. Owner-tunable.",
    "dept_daily_tokens": {"default": 120000, "creators": 200000, "analysis": 200000,
                          "improve": 80000, "security": 60000},
    "engine_rpm": {"default": 20, "cerebras": 25, "groq": 25, "gemini": 12,
                   "openrouter": 8, "gh-models": 10},
    "claude_pro": {"runs_per_day": 6,
                   "note": "premium: CI claude-code runs on Eitan's Pro OAuth — highest-value work only"},
}


def _now():
    return datetime.now(timezone.utc)


def _load(p: Path, d):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def budgets() -> dict:
    b = _load(BUDGETS, None)
    if b is None:
        EXDIR.mkdir(parents=True, exist_ok=True)
        BUDGETS.write_text(json.dumps(DEFAULTS, ensure_ascii=False, indent=2), encoding="utf-8")
        return dict(DEFAULTS)
    return b


def _ledger() -> dict:
    day = _now().strftime("%Y-%m-%d")
    led = _load(LEDGER, {})
    if led.get("day") != day:                       # new UTC day -> fresh ledger
        led = {"day": day, "dept_tokens": {}, "engine_calls": [], "claude_runs": 0, "denials": []}
    return led


def _save(led: dict) -> None:
    EXDIR.mkdir(parents=True, exist_ok=True)
    led["engine_calls"] = led.get("engine_calls", [])[-600:]
    LEDGER.write_text(json.dumps(led, ensure_ascii=False, indent=1), encoding="utf-8")


def acquire(dept: str, engine: str, est_tokens: int = 1500) -> tuple[bool, str]:
    """Must be called before an engine call. (ok, reason)."""
    b, led = budgets(), _ledger()
    cap = b["dept_daily_tokens"].get(dept, b["dept_daily_tokens"]["default"])
    used = led["dept_tokens"].get(dept, 0)
    if used + est_tokens > cap:
        led.setdefault("denials", []).append({"at": _now().isoformat(), "dept": dept,
                                              "why": f"daily token budget ({used}/{cap})"})
        _save(led)
        return False, f"{dept} at daily budget ({used}/{cap} tokens) — resumes at UTC midnight"
    rpm = b["engine_rpm"].get(engine, b["engine_rpm"]["default"])
    cutoff = _now().timestamp() - 60
    recent = sum(1 for c in led.get("engine_calls", []) if c["e"] == engine and c["t"] > cutoff)
    if recent >= rpm:
        return False, f"{engine} at {rpm} rpm — retry next beat"
    return True, "ok"


def record(dept: str, engine: str, tokens: int) -> None:
    led = _ledger()
    led["dept_tokens"][dept] = led["dept_tokens"].get(dept, 0) + max(tokens, 1)
    led.setdefault("engine_calls", []).append({"e": engine, "t": _now().timestamp()})
    _save(led)


def claude_allowed() -> tuple[bool, str]:
    """The Pro budget: a few premium runs/day so Desktop always has headroom."""
    b, led = budgets(), _ledger()
    cap = b.get("claude_pro", {}).get("runs_per_day", 6)
    if led.get("claude_runs", 0) >= cap:
        return False, f"Claude/Pro daily cap reached ({cap}) — premium work queues for tomorrow"
    return True, "ok"


def claude_record() -> None:
    led = _ledger()
    led["claude_runs"] = led.get("claude_runs", 0) + 1
    _save(led)


def snapshot() -> dict:
    b, led = budgets(), _ledger()
    return {"day": led.get("day"), "dept_tokens": led.get("dept_tokens", {}),
            "claude_runs": led.get("claude_runs", 0),
            "claude_cap": b.get("claude_pro", {}).get("runs_per_day", 6),
            "denials_today": len(led.get("denials", []))}


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ok, why = acquire("analysis", "groq")
    print("acquire test:", ok, why)
    record("analysis", "groq", 1200)
    print("snapshot:", json.dumps(snapshot()))
