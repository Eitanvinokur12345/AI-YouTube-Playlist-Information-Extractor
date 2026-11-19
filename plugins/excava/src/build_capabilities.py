"""
src/build_capabilities.py — the CAPABILITY CATALOG (owner 2026-07-06: "30 = capabilities EXCAVA
can DO, not tasks"). Draft-by-Fable, owner-tweakable. Every capability is tagged HONESTLY per the
2026-07-06 audit: live (proven working) · planned (designed, not real yet) · gated-M5 (external,
needs the gate/tools) · pitch (needs the owner). Writes data/excava/capabilities.json for the
dashboard 'Capabilities' view. A few statuses are computed from real evidence so the catalog can't
lie about itself. Run: python -m src.build_capabilities
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "excava" / "capabilities.json"

# (id, name, what, department, status, evidence)  — status hand-tagged to the audit truth.
CAT = [
    # ── LIVE: proven working (M1 pipeline + this session's real vertical) ──
    ("analyze-video", "Analyze a video from full transcript", "extract tools/skills/prompts from the whole source", "analysis", "live", "6929 elements indexed"),
    ("verify-element", "Verify an element (2 sources + live test)", "cross-check + live link/install before 'real'", "analysis", "live", "verified/niche statuses in the index"),
    ("resolve-links", "Resolve real links for elements", "website/github/codespaces, verified", "links", "live", "links lane commits"),
    ("prune-dead", "Prune only truly-dead links (P3)", "hide dead, keep niche", "links", "live", "P3 in code"),
    ("recall-meaning", "Recall tools/skills by meaning", "vector recall over the hub", "memory", "live", "1400+ vectors"),
    ("relate-graph", "Relate elements / brain graph", "topic + co-occurrence graph", "memory", "live", "brain_graph.json"),
    ("cluster-package", "Turn a graph cluster into a package", "click a cluster → a kit", "memory", "live", "M3.9 shipped"),
    ("assemble-package", "Assemble a reusable package", "bundle elements into a kit", "creators", "live", "packages.json"),
    ("real-backlog", "Value-ranked real-gap backlog", "tasks from real deficits, no make-work", "core", "live", "excava_backlog.py, beat #45"),
    ("size-judgment", "Judge task size (cost+steps+risk)", "big→war room, small→parallel", "core", "live", "plan_beat()"),
    ("room-decision", "Run a room: debate → decision.md", "doer/checker converge to a committed artifact", "core", "live", "data/excava/artifacts/*.md"),
    ("engine-routing", "Multi-engine routing + fallback", "proven pool leads, dead engines parked", "core", "live", "selftest 28817002526"),
    ("lease-budget", "Lease + budget arbiter", "per-dept token budgets, RPM caps", "core", "live", "excava_leases.py"),
    ("guardrails", "12 information-loss guardrails", "quarantine-not-delete, verified push", "core", "live", "GUARDRAILS.md"),
    ("goals-score", "Score the North-Star goals honestly", "self-lifting caps on real evidence", "improve", "live", "goals_check.py"),
    ("discovery", "Discover new tools/repos", "GitHub/HN/PH/releases, quality bar", "mining", "live", "discovery_agent.py"),
    ("news-digest", "Freshness / AI-news digest", "the system's own summary", "news", "live", "news lane"),
    ("prewarm-open", "Pre-warm repos / <10s open", "warm=instant, cold<10s", "links", "live", "prewarm.py"),
    ("taste-learn", "Learn your design taste (Arena)", "picks tune future designs", "visual", "live", "arenaVote"),
    ("verify-connectors", "Sandbox-verify connectors", "run + liveness check", "security", "live", "verify_connectors"),
    # ── PLANNED: designed, not real yet (this session's next parts) ──
    ("war-room", "Open cross-department war rooms", "auto on a real 2+ dept need → shared decision", "core", "planned", "§N spec"),
    ("group-chat", "Open cross-agent group chat", "any agent↔any agent, join/leave by relevance", "core", "planned", "§N spec"),
    ("dept-focus", "Per-department rotating focus", "auto-picked from the biggest gap", "improve", "planned", "§N spec"),
    ("daily-selfimprove", "Daily self-improvement + digest", "auto safe changes, pitch the 5 conditions", "improve", "planned", "§N spec"),
    ("power-meter", "Measure + raise EXCAVA's Power %", "chase every +0.5%, can exceed 100%", "power", "planned", "new dept §J"),
    ("visualization", "Keep the whole UI alive", "liveliness, access, enjoyment, clarity, speed, a11y", "visualization", "planned", "new dept §J"),
    ("console-inapp", "In-app console dispatch", "type a task → runs in-app, no GitHub", "core", "planned", "decision 3"),
    ("monster-cast", "Monster + animation cast (real tool)", "legs + body via image/video gen", "visualization", "planned", "decision 2"),
    ("pitch-monster", "Pitch monster styled to the group", "signals a waiting pitch by who's asking", "visualization", "planned", "§K spec"),
    ("horse", "HORSE: 10 executions merged to taste", "best-of-results to your work-taste", "core", "planned", "horse.py partial"),
    ("activator", "Portable activator skill", "run a hub task in any tool, offline", "core", "planned", "activator/SKILL.md partial"),
    # NOTE: "activator" is upgraded to live by _computed() below when find.py proves itself
    # against the real hub data — this row's own "partial" tag is the pre-verification default.
    # ── GATED-M5: external world actions (hybrid gate: low-risk auto, risky/money pitch) ──
    ("m5-project-tasks", "Manage your projects' tasks", "read/update Budoaris/FreeDup task lists", "core", "gated-M5", "deferred"),
    ("m5-channels", "Post to / monitor your channels", "via OpenClaw + agent-reach", "news", "gated-M5", "needs external tools"),
    ("m5-deploy", "Build + deploy sites/tools", "ship a real tool", "creators", "gated-M5", "deferred"),
    ("m5-money", "Find ways to make you money", "monetization research → pitch", "core", "gated-M5", "deferred"),
    ("m5-spinup", "Spin up whole projects independently", "new project end-to-end", "core", "gated-M5", "deferred"),
    # ── PITCH: needs the owner (P5d owner-only-high-leverage) ──
    ("add-capacity", "Add engine capacity", "more free keys / OmniRoute to go faster", "power", "pitch", "P5d — only Eitan can add keys"),
]


def _recent_room_turns(prefix: str, days: int = 7) -> tuple[int, str]:
    """Count real (>1 line, i.e. more than just the 'room opened' system line) chat logs whose
    filename starts with `prefix` and whose DAY-folder falls in the last `days` days. Returns
    (count, latest_filename) — evidence a war-room/group-chat actually ran recently, not once
    long ago and never since."""
    chats = DATA / "excava" / "chats"
    if not chats.exists():
        return 0, ""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    n, latest, latest_day = 0, "", ""
    for day_dir in sorted(chats.iterdir()):
        try:
            day = datetime.strptime(day_dir.name, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if day < cutoff:
            continue
        for f in sorted(day_dir.glob(f"{prefix}*.jsonl")):
            try:
                lines = [ln for ln in f.read_text(encoding="utf-8").splitlines() if ln.strip()]
            except Exception:
                continue
            if len(lines) > 1:            # more than just the system "room opened" line
                n += 1
                latest, latest_day = f.name, day_dir.name
    return n, f"{latest} ({latest_day})" if latest else ""


def _computed(cid: str, status: str, evidence: str) -> tuple[str, str]:
    """A few statuses are checked against REAL evidence (files on disk) so the hand-typed
    table above can't overstate — or, just as importantly, UNDERSTATE — the truth. Returns
    (status, evidence); evidence is replaced with the concrete proof when computed."""
    if cid == "room-decision":
        arts = list((DATA / "excava" / "artifacts").glob("*.md")) if (DATA / "excava" / "artifacts").exists() else []
        return ("live" if arts else "planned"), evidence
    if cid in ("war-room", "group-chat"):
        prefix = "war-" if cid == "war-room" else "group-"
        n, latest = _recent_room_turns(prefix)
        if n:
            return "live", f"{n} real multi-turn {cid.replace('-', ' ')} log(s) in the last 7d, latest {latest}"
        return "planned", evidence
    if cid == "daily-selfimprove":
        log = DATA / "excava" / "improvements.jsonl"
        if log.exists():
            lines = [ln for ln in log.read_text(encoding="utf-8").splitlines() if ln.strip()]
            recent = lines[-25:]
            try:
                recs = [json.loads(ln) for ln in recent]
                last_at = datetime.fromisoformat(recs[-1]["at"]) if recs else None
                kinds = {r.get("kind", "") for r in recs}
                has_safe = any(k.startswith("safe-") or k == "add-agent" for k in kinds)
                has_pitch = "pitch" in kinds
                fresh = last_at and (datetime.now(timezone.utc) - last_at) < timedelta(days=3)
                if fresh and has_safe and has_pitch:
                    return "live", (f"improvements.jsonl: {len(lines)} logged events, last "
                                     f"{recs[-1]['at'][:10]} — both safe auto-fixes and pitches present")
            except Exception:
                pass
        return "planned", evidence
    if cid == "activator":
        # Live self-test (P9: independent test re-runs before "real" is claimed), not just a
        # files-exist check — actually invoke find.py against the real hub data, same as a
        # user session would, and require at least one real match back.
        script = ROOT / "skills" / "excavatortron-activator" / "find.py"
        if script.exists():
            try:
                import subprocess
                out = subprocess.run(
                    ["python3", str(script), "summarize a youtube video transcript"],
                    capture_output=True, text=True, timeout=15, cwd=str(ROOT),
                )
                res = json.loads(out.stdout)
                total = sum(len(res.get(k, [])) for k in ("skills", "tools", "connectors", "prompts", "commands"))
                if out.returncode == 0 and total > 0:
                    return "live", (f"find.py self-test: {total} real hub match(es) returned "
                                     f"(e.g. \"{res.get('skills', res.get('tools', [{}]))[0].get('name', '')}\")")
            except Exception:
                pass
        return "planned", evidence
    return status, evidence


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    caps = []
    for c in CAT:
        st, ev = _computed(c[0], c[4], c[5])
        caps.append({"id": c[0], "name": c[1], "what": c[2], "department": c[3],
                      "status": st, "evidence": ev})
    from collections import Counter
    by = Counter(c["status"] for c in caps)
    doc = {"generated_at": datetime.now(timezone.utc).isoformat(),
           "total": len(caps), "live": by["live"], "planned": by["planned"],
           "gated_M5": by["gated-M5"], "pitch": by["pitch"], "capabilities": caps}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"capabilities: {len(caps)} total — {by['live']} live · {by['planned']} planned · "
          f"{by['gated-M5']} gated-M5 · {by['pitch']} pitch  -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
