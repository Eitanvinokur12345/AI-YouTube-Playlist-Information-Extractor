"""
src/token_diet.py — the TOKEN DIET, made visible (owner 2026-07-12: "you say it's happening,
but I can't verify it — add it to one of the tabs so I can see it").

Computes REAL numbers from the room transcripts — average turn length per day, turns per day —
so the diet is a measurable line, not a claim. Writes data/excava/token_diet.json, which the
Effectiveness tab renders alongside the standing laws and hard caps.
Free, stdlib-only. Run: python -m src.token_diet
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
CHATS = ROOT / "data" / "excava" / "chats"
OUT = ROOT / "data" / "excava" / "token_diet.json"


def measure() -> dict:
    days = []
    for day_dir in sorted(CHATS.glob("2026-*"))[-7:]:
        turns, chars = 0, 0
        for f in day_dir.glob("*.jsonl"):
            for ln in f.read_text(encoding="utf-8").splitlines():
                try:
                    m = json.loads(ln)
                except Exception:
                    continue
                if m.get("agent") == "system":
                    continue
                turns += 1
                chars += len(m.get("text", ""))
        if turns:
            days.append({"day": day_dir.name, "turns": turns,
                         "avg_chars_per_turn": round(chars / turns),
                         "approx_tokens_per_turn": round(chars / turns / 4)})
    report = {"generated_at": datetime.now(timezone.utc).isoformat(),
              "laws": [
                  "Ponytail (hub, quality 8): reuse before build, minimal diffs — adopted as a "
                  "standing law 2026-07-10.",
                  "Caveman (github.com/JuliusBrussee/caveman): no filler in AGENT prompts — wired "
                  "into the room style law; owner reports stay full sentences.",
              ],
              "hard_caps": {
                  "agent_turn_max_tokens": 260,
                  "room_fallthrough_attempts": 3,
                  "benchmark_canary_max_tokens": 12,
                  "canary_cadence": "hourly (never per-beat — protects the quota it measures)",
                  "turn_pacing_seconds": 2,
              },
              "per_day": days,
              "note": "approx tokens = chars/4. Falling avg-per-turn with steady turn counts = "
                      "the diet working; rising = investigate."}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return report


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    r = measure()
    for d in r["per_day"]:
        print(f"  {d['day']}: {d['turns']} turns, ~{d['approx_tokens_per_turn']} tokens/turn")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
