"""
src/excava_experiments.py — SI step 2 (owner 2026-07-10): PROFESSIONAL EXPERIMENTS the
self-improvement department runs ON EXCAVA ITSELF. First experiment: ENGINE BENCHMARK.

Why this first: the proven bottleneck is engine quota (rooms stalled 5.5h on 2026-07-10 with
every free engine 429'd). A benchmark turns "engines feel dead" into data — and the chat layer
uses the ranking to prefer healthy engines, so the experiment IMPROVES the system, not just
measures it (owner law: captured != built != used).

Method (golden-task canary, the professional standard for API health):
  one tiny fixed prompt per engine, every ~hour (not per-beat — that would eat the very quota
  it measures). Records latency, validity (did it follow the instruction), and the error class
  (429 quota / 404 bad-model / auth). Engines without a key here are recorded honestly as
  "no-key" (keys live in CI secrets).

Output: data/excava/engine_health.json — {results per engine, ranking} — read by
excava_engines (prefer healthy) and the dashboard (honest engine panel).
Free, stdlib-only. Run: python -m src.excava_experiments [--force]
"""
from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path

from src import excava_engines as engines

ROOT = Path(__file__).parent.parent
OUT = ROOT / "data" / "excava" / "engine_health.json"
GOLDEN = "Reply with exactly these two words and nothing else: benchmark ok"
FRESH_S = 55 * 60          # re-run at most hourly; the beat calls this every cycle


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _stale() -> bool:
    try:
        prev = json.load(open(OUT, encoding="utf-8"))
        age = (datetime.now(timezone.utc)
               - datetime.fromisoformat(prev["generated_at"])).total_seconds()
        return age > FRESH_S
    except Exception:
        return True


def benchmark_engines(force: bool = False) -> dict | None:
    """One golden-task pass over every catalog engine. Returns the report (or None if fresh)."""
    if not force and not _stale():
        return None
    results = []
    for spec in engines.CATALOG:
        name, kind = spec[0], spec[5] if len(spec) > 5 else ""
        eng = next((e for e in engines.available() if e["name"] == name), None)
        if not eng:
            results.append({"engine": name, "status": "no-key",
                            "note": "no API key in this environment (keys live in CI secrets)"})
            continue
        t0 = time.time()
        try:
            r = engines.complete(GOLDEN, engine=eng, max_tokens=12)
            ms = int((time.time() - t0) * 1000)
            if r.get("ok"):
                valid = "benchmark ok" in (r.get("text") or "").lower()
                results.append({"engine": name, "status": "healthy" if valid else "answering-but-sloppy",
                                "valid": valid, "ms": ms, "model": r.get("model", "")})
            else:
                results.append({"engine": name, "status": "failing", "ms": ms,
                                "note": str(r.get("text") or r.get("error") or "no answer")[:120]})
        except Exception as ex:
            err = str(ex)[:120]
            klass = ("quota-429" if "429" in err else "bad-model-404" if "404" in err
                     else "auth" if "401" in err or "403" in err else "error")
            results.append({"engine": name, "status": klass, "ms": int((time.time() - t0) * 1000),
                            "note": err})
    order = {"healthy": 0, "answering-but-sloppy": 1, "error": 2, "quota-429": 3,
             "failing": 3, "auth": 4, "bad-model-404": 4, "no-key": 5}
    ranking = [r["engine"] for r in sorted(
        results, key=lambda r: (order.get(r["status"], 9), r.get("ms", 99999)))]
    report = {"generated_at": _now(), "experiment": "engine-benchmark (golden-task canary)",
              "golden_prompt": GOLDEN, "results": results, "ranking": ranking,
              "note": "Hourly canary. The chat layer prefers engines by this ranking; "
                      "'no-key' here is normal on a PC — real numbers come from the CI beat."}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return report


def main() -> int:
    import argparse, sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    r = benchmark_engines(force=ap.parse_args().force)
    if not r:
        print("engine benchmark: fresh (<55min) — skipped")
    else:
        for x in r["results"]:
            print(f"  {x['engine']:<12} {x['status']:<20} {x.get('ms','')}ms  {x.get('note','')[:60]}")
        print("ranking:", ", ".join(r["ranking"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
