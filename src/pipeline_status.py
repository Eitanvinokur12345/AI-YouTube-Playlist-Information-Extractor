"""
src/pipeline_status.py — a LIVE heartbeat readout of the whole retrieval+analysis pipeline.

The dashboard's "is it actually working?" monitor. Every automated lane commits with its own
message prefix, so the git history IS the pipeline's heartbeat. This reads that history, maps each
prefix to a friendly lane, and records when it last ran, how often it ran this week, and whether
it's live or stale. It also snapshots the library totals so the dashboard can show "since the last
refresh: +N tools, +N skills" — concrete proof that analysis is producing, not frozen.

Free, mechanical, no Claude tokens. Writes data/pipeline_status.json. Run it in every workflow's
"keep derived data consistent" step.
"""
from __future__ import annotations

import glob
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "pipeline_status.json"
NOW = datetime.now(timezone.utc)

# (key, label, what it does, [commit-prefixes], cadence_hours) — cadence = how often it SHOULD run.
LANES = [
    ("gemini_video", "Gemini watch (audio+visual)", "Watches videos directly — clears the backlog free",
     ["gemini-video"], 12),
    ("transcribe", "Transcript retrieval", "Pulls captions (Supadata cloud + residential)",
     ["transcribe", "backfill", "fetch:"], 24),
    ("free_pool", "Free analysis pool", "Turns transcripts into skills/tools/connectors (free engines)",
     ["bulk-analyze"], 6),
    ("mine", "External mining", "Mines 80+ web feeds for new tools/skills/MCPs",
     ["mine-feeds", "mine ", "discover:"], 12),
    ("claude_analyze", "Deep analysis (night-gated)", "Claude re-analysis + safety pass",
     ["analyze:"], 24),
    ("news", "AI news refresh", "Refreshes official-site AI news",
     ["news:"], 12),
    ("self_improve", "Self-improvement review", "Weekly usability/quality/bug review",
     ["review:"], 168),
]

DATASETS = [("skills.json", "skills"), ("tools.json", "tools"), ("models.json", "models"),
            ("connectors.json", "connectors"), ("prompts.json", "prompts"), ("commands.json", "commands")]


def _load(p: Path, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def _git_log(n: int = 500):
    try:
        out = subprocess.run(["git", "-C", str(ROOT), "log", "-n", str(n), "--pretty=%cI%x09%s"],
                             capture_output=True, text=True, encoding="utf-8", errors="replace",
                             timeout=30)
        rows = []
        for line in out.stdout.splitlines():
            if "\t" not in line:
                continue
            iso, msg = line.split("\t", 1)
            try:
                dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
                rows.append((dt, msg))
            except Exception:
                continue
        return rows
    except Exception:
        return []


def _counts():
    c = {}
    for fname, key in DATASETS:
        d = _load(DATA / fname, {})
        c[key] = len(d.get(key, [])) if isinstance(d, dict) else (len(d) if isinstance(d, list) else 0)
    # coverage — transcript fetched OR watched by Gemini (both yield real analysis). The
    # "analyzed" number is the honest one: it rises whenever ANY lane processes a video, even
    # when no caption exists, so it climbs as work happens (transcript-only can dip when new
    # videos arrive faster than captions are fetched).
    tot = have = analyzed = 0
    for f in glob.glob(str(DATA / "processed" / "*.json")):
        tot += 1
        r = _load(Path(f), None)
        if not isinstance(r, dict):
            continue
        has_t = r.get("transcript_source") == "transcript"
        if has_t:
            have += 1
        if has_t or r.get("gemini_video_analyzed"):
            analyzed += 1
    c["videos_total"] = tot
    c["videos_with_transcript"] = have
    c["videos_analyzed"] = analyzed
    return c


def main() -> int:
    log = _git_log()
    lanes = []
    for key, label, what, prefixes, cad in LANES:
        matches = [dt for dt, msg in log if any(msg.startswith(p) for p in prefixes)]
        last = max(matches) if matches else None
        age_h = ((NOW - last).total_seconds() / 3600) if last else None
        runs_7d = sum(1 for dt in matches if (NOW - dt).days < 7)
        if age_h is None:
            status = "idle"
        elif age_h <= cad * 1.5:
            status = "live"
        elif age_h <= cad * 3:
            status = "slow"
        else:
            status = "stale"
        lanes.append({"key": key, "label": label, "what": what, "cadence_h": cad,
                      "last_run": last.isoformat() if last else None,
                      "age_hours": round(age_h, 1) if age_h is not None else None,
                      "runs_7d": runs_7d, "status": status})

    cur = _counts()
    prev = _load(OUT, {})
    prev_snap = prev.get("snapshot", {})
    prev_at = prev.get("generated_at")
    deltas = {k: cur.get(k, 0) - prev_snap.get(k, cur.get(k, 0)) for k in cur}

    # Rolling 24h history so the dashboard can show "retrieved in the last 24h" instead of "since the
    # last run a few minutes ago" (which is almost always zero). Keep ~120 snapshots.
    hist = [h for h in (prev.get("history") or []) if isinstance(h, dict)]
    hist.append({"at": NOW.isoformat(), "counts": cur})
    hist = hist[-120:]
    base = None
    for h in hist:                                      # oldest snapshot still within the last 24h
        try:
            if (NOW - datetime.fromisoformat(h["at"])).total_seconds() <= 24 * 3600:
                base = h; break
        except Exception:
            continue
    base_counts = (base or hist[0]).get("counts", cur)
    d24 = {k: cur.get(k, 0) - base_counts.get(k, cur.get(k, 0)) for k in cur}

    live = sum(1 for l in lanes if l["status"] == "live")
    overall = "live" if live >= 3 else ("slow" if live >= 1 else "stale")

    OUT.write_text(json.dumps({
        "generated_at": NOW.isoformat(),
        "overall": overall,
        "lanes": lanes,
        "snapshot": cur,
        "deltas_since_last": deltas,
        "deltas_24h": d24,
        "since": prev_at,
        "history": hist,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    moved = ", ".join(f"+{v} {k}" for k, v in d24.items() if v > 0) or "no change"
    print(f"pipeline_status: overall={overall}, {live}/{len(lanes)} lanes live; last 24h: {moved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
