"""
src/horse.py — M4.2 HORSE: ten agents each FULLY execute a goal, then the best of
their RESULTS is merged into one deliverable, weighted to your WORK-taste (M3.11b / E5).

Not a plan-and-pick: every runner produces the actual deliverable via a real engine
(varied across the free families), the results are scored against your work-taste dials,
and the top few are synthesised into one superior artifact. Offline (no engines wired,
e.g. a local run) it degrades honestly — the same contract M2's rooms use — and the ten
real executions run on the CI beat.

CLI:  python -m src.horse "<goal>"
Saves: data/horse/<day>-<hash>.json (full run) + data/horse_runs.json (dashboard index).
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
HORSE_DIR = DATA / "horse"
TASTE_FILE = DATA / "excava" / "taste.json"

WORK_DIMS = ["thoroughness", "detail", "boldness", "novelty", "scope", "polish"]
STYLES = ["thorough", "fast", "bold", "careful", "creative", "minimal",
          "polished", "novel", "proven", "balanced"]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def work_taste() -> dict:
    """The owner's work-taste dials (0-100 each). Defaults to balanced (50).
    Written server-side by the 'EXCAVA: set taste' channel (M3.11b Save-to-EXCAVA)."""
    w = {}
    try:
        w = (json.loads(TASTE_FILE.read_text(encoding="utf-8")) or {}).get("work", {})
    except Exception:
        pass
    return {k: int(w.get(k, 50)) for k in WORK_DIMS}


def _engines(n: int) -> list:
    """Vary engines across the n runners (cycle the available free families)."""
    try:
        from src.excava_engines import available
        av = available()
    except Exception:
        av = []
    return [av[i % len(av)] if av else None for i in range(n)]


def _execute(goal: str, engine, idx: int) -> dict:
    """One runner fully executes the goal via its engine and returns its candidate."""
    style = STYLES[idx % len(STYLES)]
    if engine is None:
        return {"idx": idx, "style": style, "engine": "offline", "ok": False, "ms": 0,
                "text": f"[engine offline locally — runner {idx + 1} ({style}) executes on the CI beat]"}
    from src.excava_engines import complete
    prompt = (f"You are runner {idx + 1} of 10 with a {style} working style. "
              f"FULLY complete this goal — produce the actual deliverable, not a plan or an outline:\n\n"
              f"{goal}\n\nOutput only the finished deliverable.")
    r = complete(prompt, engine=engine, difficulty="normal", max_tokens=900)
    return {"idx": idx, "style": style, "engine": r.get("engine"), "ok": bool(r.get("ok")),
            "text": r.get("text", ""), "ms": r.get("ms", 0)}


def _proxies(text: str) -> dict:
    """Cheap, deterministic proxies for each work dimension (0-100), refined by the merge
    engine when it's up. Length/structure stand in for thoroughness/detail/scope; lexical
    cues for boldness/novelty; formatting for polish."""
    t = text or ""
    words = len(t.split())
    low = t.lower()
    return {
        "thoroughness": min(100, words / 6),
        "detail": min(100, t.count("\n") * 8 + words / 8),
        "boldness": 50 + (12 if any(w in low for w in ("recommend", "should", "best", "must", "avoid")) else -12),
        "novelty": 50 + (12 if any(w in low for w in ("novel", "new ", "instead", "alternativ", "rethink")) else 0),
        "scope": min(100, words / 5),
        "polish": 50 + (14 if (t.count("```") >= 2 or t.count("#") >= 1 or t.count("- ") >= 3) else -6),
    }


def _score(candidate: dict, taste: dict) -> float:
    """Closeness of a candidate to the desired work-taste (higher = closer)."""
    p = _proxies(candidate.get("text", ""))
    return round(sum(100 - abs(p[d] - taste[d]) for d in WORK_DIMS) / len(WORK_DIMS), 1)


def _merge(goal: str, top: list, taste: dict) -> dict:
    """Synthesise the top candidates into one superior deliverable, matching work-taste."""
    from src.excava_engines import complete
    profile = ", ".join(f"{d} {taste[d]}" for d in WORK_DIMS)
    blob = "\n\n".join(f"--- Candidate {c['idx'] + 1} ({c['style']}, score {c['score']}):\n{c['text'][:1500]}"
                       for c in top)
    prompt = (f"Merge the best of these {len(top)} independent executions into ONE superior deliverable, "
              f"matching this work-taste (each 0-100): {profile}.\n\nGoal: {goal}\n\n{blob}\n\n"
              f"Output only the merged deliverable.")
    r = complete(prompt, difficulty="hard", max_tokens=1200)
    return {"text": r.get("text", ""), "engine": r.get("engine"), "ok": bool(r.get("ok")), "ms": r.get("ms", 0)}


def run_horse(goal: str, n: int = 10) -> dict:
    taste = work_taste()
    engines = _engines(n)
    cands = [_execute(goal, engines[i], i) for i in range(n)]
    for c in cands:
        c["score"] = _score(c, taste)
    ranked = sorted(cands, key=lambda c: c["score"], reverse=True)
    top = [c for c in ranked if c.get("ok") and c.get("text")][:3]
    merged = _merge(goal, top, taste) if top else {
        "text": "[all 10 runners offline locally — HORSE merges the real executions on the CI beat]",
        "engine": "offline", "ok": False, "ms": 0}
    result = {"goal": goal, "at": _now(), "runners": n, "work_taste": taste,
              "candidates": cands, "winner_idx": (ranked[0]["idx"] if ranked else None),
              "merged": merged}
    _save(result)
    return result


def _save(result: dict) -> None:
    HORSE_DIR.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha1(result["goal"].encode("utf-8")).hexdigest()[:8]
    path = HORSE_DIR / f"{result['at'][:10]}-{h}.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    idx_file = DATA / "horse_runs.json"
    try:
        runs = json.loads(idx_file.read_text(encoding="utf-8"))
    except Exception:
        runs = {"note": "M4.2 HORSE runs — 10 executions merged best-of to work-taste.", "runs": []}
    runs.setdefault("runs", []).insert(0, {
        "goal": result["goal"], "at": result["at"], "winner_idx": result["winner_idx"],
        "runners": result["runners"], "engine": result["merged"].get("engine"),
        "ok": result["merged"].get("ok"), "file": str(path.relative_to(ROOT)).replace("\\", "/")})
    runs["runs"] = runs["runs"][:50]
    idx_file.write_text(json.dumps(runs, ensure_ascii=False, indent=1), encoding="utf-8")


def main() -> int:
    goal = " ".join(sys.argv[1:]).strip()
    if not goal:
        print('usage: python -m src.horse "<goal>"')
        return 1
    res = run_horse(goal)
    w = res["winner_idx"]
    print(f"HORSE: {res['runners']} runners · winner #{(w or 0) + 1 if w is not None else '?'} · "
          f"merged via {res['merged'].get('engine')} · ok={res['merged'].get('ok')}")
    print(res["merged"]["text"][:600])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
