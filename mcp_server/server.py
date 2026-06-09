"""
YouTube Skills Tracker — local MCP server.

Self-contained: standard library + the official MCP SDK ONLY.
NO Playwright, no browser, no external connector — so every query works fully OFFLINE
from the locally synced data folder.

It exposes query tools over the tracker's JSON files (all OFFLINE), plus a few tools that
need the internet and degrade gracefully when offline / without a token:
  * three "force run" tools that trigger the cloud GitHub Actions workflows, and
  * curation write tools (star/unstar a skill, approve/dismiss an improvement suggestion)
    that commit a tiny state file (data/stars.json, data/approvals.json) back to the repo
    via the GitHub contents API, so the daily self-improvement stage can act on them.

Configuration (environment variables):
  SKILLS_DATA_DIR  Absolute path to the synced data folder
                   (e.g. C:\\Users\\eitan\\OneDrive\\Desktop\\AI Skills Data).
                   Falls back to the repo's ./data if unset.
  GITHUB_REPO      "owner/repo" for the cloud actions. Default: the project repo.
  GITHUB_PAT       Fine-grained GitHub token, optional. For force-run it needs
                   "Actions: Read and write"; for star/approve writes it also needs
                   "Contents: Read and write" on this repo.

Run:  python -m mcp_server.server      (or:  python mcp_server/server.py)
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

# ── data location ──────────────────────────────────────────────────────────────
_REPO_ROOT = Path(__file__).resolve().parent.parent
_DEFAULT_DATA = _REPO_ROOT / "data"
DATA_DIR = Path(os.environ.get("SKILLS_DATA_DIR", str(_DEFAULT_DATA)))

GITHUB_REPO = os.environ.get(
    "GITHUB_REPO", "Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor"
)

mcp = FastMCP("youtube-skills-tracker")


# ── json helpers (all offline-safe) ─────────────────────────────────────────────
def _load(name: str, default: Any) -> Any:
    """Load data/<name>; return `default` if missing or unreadable."""
    path = DATA_DIR / name
    if not path.exists():
        return default
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return default


def _config() -> dict:
    """Read config.json (for caps like stars.max_total). Repo root, then data dir."""
    for p in (_REPO_ROOT / "config.json", DATA_DIR / "config.json"):
        try:
            if p.exists():
                with open(p, encoding="utf-8") as fh:
                    return json.load(fh)
        except Exception:
            pass
    return {}


def _parse_iso(s: str):
    """Parse an ISO-8601 timestamp to an aware datetime (stdlib only); min on failure."""
    from datetime import datetime, timezone

    if not s:
        return datetime.min.replace(tzinfo=timezone.utc)
    try:
        dt = datetime.fromisoformat(s.strip().replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        return datetime.min.replace(tzinfo=timezone.utc)


def _skills() -> list[dict]:
    return _load("skills.json", {"skills": []}).get("skills", [])


def _fmt_skill(s: dict) -> str:
    name = s.get("skill_name", s.get("slug", "?"))
    score = s.get("quality_score", "?")
    cat = s.get("category", "?")
    tool = s.get("target_tool", "claude")
    desc = s.get("description", "")
    line = f"- [{score}/10] {name}  ({cat}, {tool})\n    {desc}"
    compat = s.get("compatibility") or []
    if compat:
        parts = []
        for c in compat:
            ver = c.get("up_to_version")
            t = c.get("tool", "?")
            parts.append(f"{t} (up to {ver})" if ver and ver not in ("any", "latest") else str(t))
        tag = " [multi-tool]" if (s.get("multi_tool") or len(compat) > 1) else ""
        line += f"\n    Works with{tag}: " + ", ".join(parts)
    return line


def _no_data(thing: str) -> str:
    return (
        f"No {thing} found yet. The data folder is:\n  {DATA_DIR}\n"
        "If this looks wrong, set SKILLS_DATA_DIR to your synced 'AI Skills Data' folder. "
        "If the pipeline has not produced results yet, run a sync or a force run first."
    )


# ── read-time ASCII rendering (token-saver B2) ──────────────────────────────────
# Claude no longer writes pre-rendered ASCII into the data files (it wastes output
# tokens). The dashboard draws an HTML podium/table; here, for the text-only MCP
# client, we render the same things as ASCII at READ time from the structured data.
def _ascii_podium(pod: list[dict], category: str = "") -> str:
    """Render a top-3 model podium as ASCII from the structured `podium` list."""
    items = [p for p in (pod or []) if p][:3]
    if not items:
        return ""
    by_rank: dict[int, dict] = {}
    for p in items:
        try:
            by_rank[int(p.get("rank", 0) or 0)] = p
        except Exception:
            pass
    first, second, third = by_rank.get(1), by_rank.get(2), by_rank.get(3)
    if first and second and third:
        ordered = [(2, second), (1, first), (3, third)]   # visual: silver, gold, bronze
    else:
        ordered = []
        for i, p in enumerate(items):
            try:
                r = int(p.get("rank", i + 1) or (i + 1))
            except Exception:
                r = i + 1
            ordered.append((r, p))

    def label(p: dict) -> str:
        nm = str(p.get("name", "?"))
        ver = p.get("version")
        if ver and ver not in ("any", "latest"):
            nm += " " + str(ver)
        return nm

    if not ordered:
        return ""
    inner = min(26, max(10, max(len(label(p)) for _, p in ordered) + 2))
    risers = {1: 3, 2: 1, 3: 0}   # gold stands tallest

    def box(rank: int, p: dict) -> list[str]:
        nm = label(p)
        if len(nm) > inner:
            nm = nm[: inner - 3] + "..."
        score = f"{p.get('score', '?')}/10"
        lines = [
            "+" + "-" * inner + "+",
            "|" + f"#{rank}".center(inner) + "|",
            "|" + nm.center(inner) + "|",
            "|" + score.center(inner) + "|",
        ]
        for _ in range(risers.get(rank, 0)):
            lines.append("|" + " " * inner + "|")
        lines.append("+" + "-" * inner + "+")
        return lines

    cols = [box(rank, p) for rank, p in ordered]
    h = max(len(c) for c in cols)
    blank = " " * (inner + 2)
    cols = [[blank] * (h - len(c)) + c for c in cols]   # bottom-align so gold rises
    body = "\n".join("  ".join(col[i] for col in cols) for i in range(h))
    return (f"{category} - top 3\n" if category else "") + body


def _ascii_run_report(st: dict) -> str:
    """Render the latest run report as an ASCII box from status.run_report."""
    rr = st.get("run_report", {}) or {}
    rows = [
        ("Run time (ET)", rr.get("run_time", "?")),
        ("Total in playlist", rr.get("total_in_playlist", "?")),
        ("Already seen", rr.get("already_seen", "?")),
        ("New found", rr.get("new_found", "?")),
        ("Analyzed this run", rr.get("analyzed_this_run", "?")),
        ("Skipped (not relevant)", rr.get("skipped_not_relevant", "?")),
        ("No transcript", rr.get("no_transcript", "?")),
        ("Errors", rr.get("errors", "?")),
        ("Pending remaining", rr.get("pending_to_analyze", "?")),
        ("Total analyzed (all time)", st.get("total_videos_analyzed", "?")),
    ]
    lk = max(len(k) for k, _ in rows)
    lv = max(len(str(v)) for _, v in rows)
    title = "LATEST RUN REPORT"
    inner = max(lk + lv + 3, len(title))
    out = ["+" + "-" * (inner + 2) + "+", "| " + title.ljust(inner) + " |",
           "+" + "-" * (inner + 2) + "+"]
    for k, v in rows:
        out.append("| " + f"{k.ljust(lk)} : {str(v).rjust(lv)}".ljust(inner) + " |")
    out.append("+" + "-" * (inner + 2) + "+")
    return "\n".join(out)


# ── reliability warnings (A1 analyze-failure / A2 stalled pipeline) ──────────────
def _stale_message(st: dict) -> str:
    """Return a 'pipeline stalled' message if the last fetch is far older than expected."""
    from datetime import datetime, timezone

    floor = datetime.min.replace(tzinfo=timezone.utc)
    last_dt = _parse_iso(st.get("last_fetch") or st.get("last_run") or "")
    if last_dt <= floor:
        return ""
    now = datetime.now(timezone.utc)
    next_dt = _parse_iso(st.get("next_run", ""))
    interval = (next_dt - last_dt).total_seconds() if next_dt > last_dt else 0.0
    if interval <= 0:
        interval = float(_config().get("run_interval_hours", 48) or 48) * 3600.0
    age = (now - last_dt).total_seconds()
    if age > interval * 2:
        days = max(1, round(age / 86400))
        hrs = round(interval / 3600)
        return (
            f"PIPELINE STALLED? No new fetch for ~{days} day(s) (expected about every "
            f"{hrs}h). GitHub disables scheduled runs after ~60 days of repo inactivity - "
            "check the Actions tab, or trigger a Fetch run (run_pipeline)."
        )
    return ""


def _pipeline_warnings(st: dict) -> str:
    """A1+A2 banner text for the MCP client: analyze failure (token) and/or staleness."""
    out = []
    if st.get("analyze_ok") is False:
        hint = st.get("token_hint") or (
            "The last analyze run failed. Check the GitHub Actions log; the most common "
            "cause is an expired Claude subscription token (renew it once a year with "
            "`claude setup-token` and update the CLAUDE_CODE_OAUTH_TOKEN_REAL secret)."
        )
        out.append("[!] PIPELINE ERROR: " + hint)
    stale = _stale_message(st)
    if stale:
        out.append("[~] " + stale)
    return ("\n".join(out) + "\n") if out else ""


# ── Tab 1: Skills Library ────────────────────────────────────────────────────────
@mcp.tool()
def list_categories() -> str:
    """List every skill category that currently has skills, with counts."""
    counts: dict[str, int] = {}
    for s in _skills():
        counts[s.get("category", "other")] = counts.get(s.get("category", "other"), 0) + 1
    if not counts:
        return _no_data("categories")
    lines = [f"{c:<18} {n}" for c, n in sorted(counts.items(), key=lambda x: -x[1])]
    return "Categories (skill count):\n" + "\n".join(lines)


@mcp.tool()
def get_skills_in_category(category: str) -> str:
    """Get all skills in a given category, best quality score first."""
    hits = [s for s in _skills() if s.get("category", "").lower() == category.lower()]
    if not hits:
        return f"No skills found in category '{category}'. Try list_categories."
    hits.sort(key=lambda s: s.get("quality_score", 0), reverse=True)
    return f"Skills in '{category}' ({len(hits)}):\n" + "\n".join(_fmt_skill(s) for s in hits)


@mcp.tool()
def search_skills(query: str) -> str:
    """Search skills by name, slug, description, or tips (case-insensitive substring)."""
    q = query.lower().strip()
    hits = []
    for s in _skills():
        blob = " ".join(
            [
                str(s.get("skill_name", "")),
                str(s.get("slug", "")),
                str(s.get("description", "")),
                str(s.get("use_case", "")),
                " ".join(s.get("tips", []) or []),
            ]
        ).lower()
        if q in blob:
            hits.append(s)
    if not hits:
        return f"No skills matched '{query}'."
    hits.sort(key=lambda s: s.get("quality_score", 0), reverse=True)
    return f"{len(hits)} skill(s) matched '{query}':\n" + "\n".join(_fmt_skill(s) for s in hits)


@mcp.tool()
def get_skill(slug: str) -> str:
    """Show the full record for one skill by its slug."""
    for s in _skills():
        if s.get("slug", "").lower() == slug.lower():
            return json.dumps(s, ensure_ascii=False, indent=2)
    return f"No skill with slug '{slug}'. Try search_skills."


# ── Tab 2: Models Ranking ────────────────────────────────────────────────────────
@mcp.tool()
def get_ranking_table(category: str = "") -> str:
    """Get the full model ranking table for a category. Omit category to list all."""
    models = _load("models.json", {})
    if not models:
        return _no_data("model rankings")
    if not category:
        out = []
        for cat, blk in models.items():
            n = len(blk.get("full_ranking", []))
            out.append(f"{cat:<18} {n} model(s)")
        return "Ranked categories (use get_ranking_table('<category>')):\n" + "\n".join(out)
    blk = models.get(category) or models.get(category.lower())
    if not blk:
        return f"No ranking for category '{category}'."
    rows = blk.get("full_ranking", [])
    lines = [f"{'#':>3}  {'score':>5}  model (company)"]
    for r in rows:
        nm = r.get("name", "?")
        ver = (" " + r["version"]) if r.get("version") else ""
        comp = f" ({r['company']})" if r.get("company") else ""
        lines.append(f"{r.get('rank','?'):>3}  {r.get('score','?'):>5}  {nm}{ver}{comp}")
    return f"Full ranking — {category} ({len(rows)} models):\n" + "\n".join(lines)


@mcp.tool()
def show_podium(category: str) -> str:
    """Show the top-3 model podium for a category as ASCII, rendered at read time from the
    structured podium data (Claude no longer stores pre-rendered ASCII — a token saver)."""
    models = _load("models.json", {})
    blk = models.get(category) or models.get(category.lower())
    if not blk:
        return f"No podium for category '{category}'."
    legacy = blk.get("ascii_podium")   # honour any old pre-rendered art still in the data
    if legacy:
        return legacy
    pod = blk.get("podium", []) or (blk.get("full_ranking", []) or [])[:3]
    if not pod:
        return f"No podium data for '{category}'."
    art = _ascii_podium(pod, category)
    if art:
        return art
    return "\n".join(
        f"#{p.get('rank')}  {p.get('name','?')} {p.get('version','')}  "
        f"{p.get('score','?')}/10  ({p.get('company','')})"
        for p in pod
    )


# ── Tab 3: Skills Improvement (audit trail) ─────────────────────────────────────
@mcp.tool()
def show_merge_log() -> str:
    """Show the log of merged/overlapping skills."""
    log = _load("merge_log.json", [])
    if isinstance(log, dict):
        log = log.get("merges", log.get("entries", []))
    if not log:
        return "Merge log is empty — no skills have been merged yet."
    return "Merge log:\n" + "\n".join(
        f"- {e.get('timestamp','?')}: {e.get('merged_from','?')} -> "
        f"{e.get('merged_into','?')} ({e.get('reason','')})"
        for e in log
    )


@mcp.tool()
def show_deleted_log() -> str:
    """Show skills that were discarded/superseded (the deleted-skills backup)."""
    log = _load("deleted_skills.json", [])
    if isinstance(log, dict):
        log = log.get("deleted", log.get("entries", []))
    if not log:
        return "Deleted-skills log is empty."
    return "Deleted / superseded skills:\n" + "\n".join(
        f"- {e.get('slug', e.get('skill_name','?'))}: {e.get('reason','')}"
        for e in log
    )


# ── Tab 4: Tips & Commands ──────────────────────────────────────────────────────
@mcp.tool()
def get_tips(topic_or_tool: str = "") -> str:
    """Get tips for a tool or general topic. Omit the argument to list all keys."""
    tips = _load("tips.json", {})
    by_tool = tips.get("by_tool", {})
    general = tips.get("general", {})
    if not topic_or_tool:
        keys = sorted(set(by_tool) | set(general))
        if not keys:
            return _no_data("tips")
        return "Tip keys (tools + topics):\n" + ", ".join(keys)
    key = topic_or_tool
    items = by_tool.get(key) or general.get(key)
    if items is None:  # case-insensitive retry
        for src in (by_tool, general):
            for k, v in src.items():
                if k.lower() == key.lower():
                    items = v
                    break
    if not items:
        return f"No tips for '{topic_or_tool}'. Use get_tips() to list keys."
    return f"Tips — {topic_or_tool}:\n" + "\n".join(f"- {t}" for t in items)


@mcp.tool()
def list_commands() -> str:
    """List the master list of slash commands collected from videos."""
    cmds = _load("commands.json", {"commands": []}).get("commands", [])
    if not cmds:
        return _no_data("slash commands")
    cmds.sort(key=lambda c: c.get("command", ""))
    return f"Slash commands ({len(cmds)}):\n" + "\n".join(
        f"- {c.get('command','?'):<20} {c.get('description','')}"
        f"{('  ['+c['tool']+']') if c.get('tool') else ''}"
        for c in cmds
    )


# ── Tab 5: News Feed (videos + official sites, merged) ──────────────────────────
def _fmt_news_entry(e: dict) -> str:
    title = e.get("title", "?")
    summary = e.get("summary", "") or "(summary pending)"
    flag = "  [!] low-quality source" if e.get("low_quality_source") else ""
    if e.get("source_type") == "web" or (e.get("url") and not e.get("video_id")):
        src = e.get("source_name", "web")
        return f"- {title}  [{src}] (web){flag}\n    {summary}\n    {e.get('url','')}"
    src = e.get("channel_name", "")
    return (
        f"- {title}  [{src}] (video){flag}\n    {summary}\n"
        f"    https://www.youtube.com/watch?v={e.get('video_id','')}"
    )


def _news(video_name: str, web_name: str, label: str) -> str:
    """Merge the video news file with the official-site web news file for a window."""
    vdata = _load(video_name, {})
    wdata = _load(web_name, {})
    ventries = vdata.get("entries", []) or []
    wentries = wdata.get("entries", []) or []
    entries = list(ventries) + list(wentries)
    if not entries:
        return f"No {label} news entries."
    entries.sort(key=lambda e: _parse_iso(e.get("publishedAt", "")), reverse=True)
    hdr = vdata.get("header", {}) or wdata.get("header", {})
    head = (
        f"{label.upper()} NEWS  (window: {hdr.get('window','')})  "
        f"— {len(ventries)} from videos + {len(wentries)} from official sites\n"
    )
    return head + "\n" + "\n".join(_fmt_news_entry(e) for e in entries)


@mcp.tool()
def daily_news() -> str:
    """AI news from the last 24 hours — merges video news + official-site headlines (newest first)."""
    return _news("daily_news.json", "daily_web_news.json", "daily")


@mcp.tool()
def weekly_news() -> str:
    """AI news from the last 7 days — merges video news + official-site headlines (newest first)."""
    return _news("weekly_news.json", "weekly_web_news.json", "weekly")


@mcp.tool()
def monthly_news() -> str:
    """AI news from the last 30 days — merges video news + official-site headlines (newest first)."""
    return _news("monthly_news.json", "monthly_web_news.json", "monthly")


# ── Tab 6: Connectors ───────────────────────────────────────────────────────────
def _connectors() -> list[dict]:
    return _load("connectors.json", {"connectors": []}).get("connectors", [])


@mcp.tool()
def show_connectors() -> str:
    """List all tracked Claude connectors and MCP servers."""
    items = _connectors()
    if not items:
        return _no_data("connectors")
    items.sort(key=lambda c: c.get("quality_score", 0), reverse=True)
    return f"Connectors / MCP servers ({len(items)}):\n" + "\n".join(
        f"- [{c.get('quality_score','?')}/10] {c.get('name','?')} "
        f"({c.get('type','?')}, {c.get('provider','?')})"
        f"{' [official]' if c.get('official') else ''}\n    {c.get('what_it_does','')}"
        for c in items
    )


@mcp.tool()
def find_connector(query: str) -> str:
    """Find a connector / MCP server by name or description."""
    q = query.lower().strip()
    hits = [
        c
        for c in _connectors()
        if q in (str(c.get("name", "")) + " " + str(c.get("what_it_does", ""))).lower()
    ]
    if not hits:
        return f"No connector matched '{query}'."
    return f"{len(hits)} match(es):\n" + "\n".join(
        json.dumps(c, ensure_ascii=False, indent=2) for c in hits
    )


# ── status / stats ──────────────────────────────────────────────────────────────
@mcp.tool()
def pipeline_status() -> str:
    """Show pipeline status + the run report (last run, next run, counters). Surfaces a clear
    warning if the last analyze run failed (e.g. an expired token, A1) or the pipeline looks
    stalled (A2). The run report is rendered as ASCII at read time (token saver B2)."""
    st = _load("status.json", {})
    if not st:
        return _no_data("status")
    rr = st.get("run_report", {})
    head = (
        f"Last fetch:   {st.get('last_fetch', st.get('last_run','?'))}\n"
        f"Last analyze: {st.get('last_analyze','?')}\n"
        f"Next run:     {st.get('next_run','?')}\n"
        f"Total skills: {st.get('total_skills','?')}\n"
        f"Videos seen:  {st.get('videos_seen','?')}\n"
        f"Analyzed this run: {rr.get('analyzed_this_run','?')}\n"
        f"Total analyzed (all time): {st.get('total_videos_analyzed','?')}\n"
    )
    box = rr.get("ascii") or _ascii_run_report(st)   # legacy art if present, else render now
    parts = []
    warn = _pipeline_warnings(st)
    if warn:
        parts.append(warn)
    parts.append(head)
    if box:
        parts.append(box)
    return "\n".join(parts)


@mcp.tool()
def stats() -> str:
    """Quick counts: analyzed this run vs. total analyzed ever, skills, pending."""
    st = _load("status.json", {})
    rr = st.get("run_report", {})
    return (
        f"Analyzed this run ......... {rr.get('analyzed_this_run', 0)}\n"
        f"Total analyzed (all time) . {st.get('total_videos_analyzed', 0)}\n"
        f"Total skills .............. {st.get('total_skills', len(_skills()))}\n"
        f"Videos seen ............... {st.get('videos_seen', 0)}\n"
        f"Pending to analyze ........ {rr.get('pending_to_analyze', 0)}\n"
        f"New found (last fetch) .... {rr.get('new_found', 0)}"
    )


# ── force run (the only online tools; graceful offline fallback) ─────────────────
def _dispatch(workflow_file: str) -> str:
    pat = os.environ.get("GITHUB_PAT", "")
    manual = (
        f"https://github.com/{GITHUB_REPO}/actions/workflows/{workflow_file}"
        "  (open it and click 'Run workflow')"
    )
    if not pat:
        return (
            "No GITHUB_PAT configured, so I can't trigger the cloud run directly.\n"
            f"Run it manually here:\n  {manual}\n"
            "To enable one-click force-run, create a fine-grained GitHub token with "
            "'Actions: Read and write' on this repo and set it as the GITHUB_PAT env var."
        )
    url = f"https://api.github.com/repos/{GITHUB_REPO}/actions/workflows/{workflow_file}/dispatches"
    body = json.dumps({"ref": "main"}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {pat}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "youtube-skills-tracker-mcp",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            if resp.status in (201, 204):
                return f"Triggered {workflow_file} on the cloud. Results sync after it finishes."
            return f"Unexpected status {resp.status} triggering {workflow_file}."
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:300]
        return f"GitHub refused the request ({exc.code}). Manual link:\n  {manual}\n{detail}"
    except Exception as exc:  # offline / DNS / timeout
        return (
            f"Couldn't reach GitHub (offline?): {exc}\n"
            f"When you're back online, run it manually:\n  {manual}"
        )


@mcp.tool()
def run_pipeline() -> str:
    """Force a full cloud run now: fetch the playlist, then analysis picks it up."""
    return _dispatch("fetch.yml")


@mcp.tool()
def run_analysis() -> str:
    """Force the cloud analysis stage now (process whatever is already pending)."""
    return _dispatch("analyze.yml")


@mcp.tool()
def run_improve() -> str:
    """Force the cloud self-improvement stage now (dedup, calibrate, star, health report)."""
    return _dispatch("improve.yml")


# ── curation writes: stars + suggestion approvals (need PAT + internet) ──────────
# These write a tiny state file back to the repo via the GitHub contents API so the
# daily self-improvement stage can act on them. On success the local copy is updated
# too, so an immediate read-back works without waiting for a sync. They degrade
# gracefully (no PAT / offline) with a clear message and change nothing.
_GH_API = "https://api.github.com"


def _save_local(name: str, obj: Any) -> None:
    """Mirror a state write into the local data folder for immediate read-back."""
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        with open(DATA_DIR / name, "w", encoding="utf-8") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=2)
    except Exception:
        pass  # local mirror is best-effort; the repo is the source of truth


def _gh_request(url: str, method: str, pat: str, payload: dict | None = None):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {pat}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "youtube-skills-tracker-mcp",
        },
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        body = resp.read().decode("utf-8", "replace")
        return resp.status, (json.loads(body) if body else {})


def _write_state(name: str, obj: Any, message: str) -> str | None:
    """Commit data/<name> to the repo via the contents API. Return None on success,
    or an explanatory message string on failure (so nothing is silently lost)."""
    import base64

    pat = os.environ.get("GITHUB_PAT", "")
    if not pat:
        return (
            "This action writes a small file to your repo, which needs a GitHub token.\n"
            "Set GITHUB_PAT (fine-grained, with 'Contents: Read and write' on "
            f"{GITHUB_REPO}) in the MCP env, then try again. Nothing was changed."
        )
    path = f"data/{name}"
    url = f"{_GH_API}/repos/{GITHUB_REPO}/contents/{path}"
    try:
        sha = None
        try:
            status, cur = _gh_request(f"{url}?ref=main", "GET", pat)
            if status == 200 and isinstance(cur, dict):
                sha = cur.get("sha")
        except urllib.error.HTTPError as exc:
            if exc.code != 404:
                raise  # 404 = file does not exist yet → create it
        content = base64.b64encode(
            json.dumps(obj, ensure_ascii=False, indent=2).encode("utf-8")
        ).decode("ascii")
        payload = {"message": message, "content": content, "branch": "main"}
        if sha:
            payload["sha"] = sha
        st, _ = _gh_request(url, "PUT", pat, payload)
        if st in (200, 201):
            _save_local(name, obj)  # immediate local read-back; matches the repo now
            return None
        return f"GitHub returned status {st} writing {path}; nothing changed."
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:200]
        return f"GitHub refused the write ({exc.code}): {detail}\nNothing changed."
    except Exception as exc:  # offline / DNS / timeout
        return f"Couldn't reach GitHub (offline?): {exc}\nNothing changed."


def _stars() -> list[dict]:
    return _load("stars.json", {"starred": []}).get("starred", [])


def _find_skill(slug: str) -> dict | None:
    for s in _skills():
        if str(s.get("slug", "")).lower() == slug.lower():
            return s
    return None


@mcp.tool()
def list_starred() -> str:
    """List skills frozen with a star (kept in original form, never auto-changed)."""
    stars = _stars()
    if not stars:
        return (
            "No starred skills yet. Star a proven best-in-class skill with "
            "star_skill('<slug>', '<why>') to freeze it from any future change."
        )
    lines = []
    for e in stars:
        slug = e.get("slug", "?")
        sk = _find_skill(slug)
        nm = sk.get("skill_name", slug) if sk else slug
        score = f" [{sk.get('quality_score')}/10]" if sk else ""
        lines.append(f"- ★ {nm}{score}  ({slug})\n    reason: {e.get('reason','')}")
    return f"Starred / frozen skills ({len(stars)}):\n" + "\n".join(lines)


@mcp.tool()
def star_skill(slug: str, reason: str = "") -> str:
    """Freeze a skill: mark it starred so no stage ever changes, merges, or deletes it.
    Writes data/stars.json in the repo (needs GITHUB_PAT with Contents: write)."""
    slug = slug.strip().lower()
    sk = _find_skill(slug)
    if not sk:
        return (
            f"No skill with slug '{slug}'. Use search_skills to find the exact slug, "
            "then star that. (Nothing changed.)"
        )
    stars = _stars()
    if any(e.get("slug", "").lower() == slug for e in stars):
        return f"'{slug}' is already starred. Nothing to do."
    max_total = int(
        _config().get("self_improvement", {}).get("stars", {}).get("max_total", 10)
    )
    if len(stars) >= max_total:
        return (
            f"The star quota is full ({len(stars)}/{max_total}). Stars are reserved for a "
            "tiny set of proven best-in-class skills (top score + cited popularity + "
            "multi-video endorsement). Unstar one with unstar_skill('<slug>') first, or "
            "raise self_improvement.stars.max_total in config.json. (Nothing changed.)"
        )
    from datetime import datetime, timezone

    stars.append(
        {
            "slug": slug,
            "reason": reason or "Marked best-in-class; keep in original form.",
            "starred_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    err = _write_state("stars.json", {"starred": stars}, f"star: freeze {slug}")
    if err:
        return err
    return (
        f"★ Starred '{sk.get('skill_name', slug)}'. It is now frozen — no stage will "
        "change, merge, rescore, or delete it. It will show first on the dashboard."
    )


@mcp.tool()
def unstar_skill(slug: str) -> str:
    """Remove a skill's star (un-freeze it, so normal curation can touch it again)."""
    slug = slug.strip().lower()
    stars = _stars()
    kept = [e for e in stars if e.get("slug", "").lower() != slug]
    if len(kept) == len(stars):
        return f"'{slug}' was not starred. Nothing to do."
    err = _write_state("stars.json", {"starred": kept}, f"unstar: unfreeze {slug}")
    if err:
        return err
    return f"Unstarred '{slug}'. It is no longer frozen."


def _suggestions() -> list[dict]:
    return _load("improvement_suggestions.json", {"suggestions": []}).get("suggestions", [])


def _approvals() -> dict:
    a = _load("approvals.json", {"approved_ids": [], "dismissed_ids": []})
    a.setdefault("approved_ids", [])
    a.setdefault("dismissed_ids", [])
    return a


def _effective_status(sug: dict, appr: dict) -> str:
    sid = sug.get("id")
    if sid in appr["approved_ids"]:
        return "approved"
    if sid in appr["dismissed_ids"]:
        return "dismissed"
    return sug.get("status", "pending")


@mcp.tool()
def list_suggestions(status: str = "pending") -> str:
    """List self-improvement suggestions awaiting your decision. status: pending (default),
    approved, dismissed, applied, or all."""
    sugs = _suggestions()
    if not sugs:
        return (
            "No improvement suggestions yet. The daily self-improvement stage writes "
            "risky proposals (fuzzy merges, rescores, recategorize, UI changes, star "
            "suggestions) here for you to approve_suggestion / dismiss_suggestion."
        )
    appr = _approvals()
    want = status.lower().strip()
    out = []
    for s in sugs:
        eff = _effective_status(s, appr)
        if want not in ("", "all") and eff != want:
            continue
        out.append(
            f"- [{eff}] {s.get('id','?')}  ({s.get('type','?')})\n"
            f"    {s.get('detail','')}"
        )
    if not out:
        return f"No suggestions with status '{status}'. Try list_suggestions('all')."
    return f"Suggestions ({status}):\n" + "\n".join(out)


@mcp.tool()
def approve_suggestion(suggestion_id: str) -> str:
    """Approve a suggestion by id. It is applied on the next self-improvement run
    (use run_improve to trigger one now). Writes data/approvals.json."""
    sid = suggestion_id.strip()
    if not any(s.get("id") == sid for s in _suggestions()):
        return f"No suggestion with id '{sid}'. Use list_suggestions to see ids."
    appr = _approvals()
    appr["dismissed_ids"] = [x for x in appr["dismissed_ids"] if x != sid]
    if sid not in appr["approved_ids"]:
        appr["approved_ids"].append(sid)
    err = _write_state("approvals.json", appr, f"approve: {sid}")
    if err:
        return err
    return (
        f"Approved '{sid}'. It will be applied on the next daily self-improvement run "
        "(or run_improve to do it now). Frozen records are still never touched."
    )


@mcp.tool()
def dismiss_suggestion(suggestion_id: str) -> str:
    """Dismiss/reject a suggestion by id so it is not applied. Writes data/approvals.json."""
    sid = suggestion_id.strip()
    if not any(s.get("id") == sid for s in _suggestions()):
        return f"No suggestion with id '{sid}'. Use list_suggestions to see ids."
    appr = _approvals()
    appr["approved_ids"] = [x for x in appr["approved_ids"] if x != sid]
    if sid not in appr["dismissed_ids"]:
        appr["dismissed_ids"].append(sid)
    err = _write_state("approvals.json", appr, f"dismiss: {sid}")
    if err:
        return err
    return f"Dismissed '{sid}'. It will not be applied."


def _find_channel(data: dict, channel: str):
    name = channel.strip().lower()
    for s in data.get("suggestions", []):
        if str(s.get("channel", "")).lower() == name or str(s.get("channel_title", "")).lower() == name:
            return s
    return None


@mcp.tool()
def approve_channel(channel: str) -> str:
    """Approve a suggested channel by name (from the Grow Sources tab). Its videos get added to
    your YouTube playlist on the next add-to-playlist run. Writes data/channel_suggestions.json."""
    data = _load("channel_suggestions.json", {"suggestions": []})
    hit = _find_channel(data, channel)
    if not hit:
        pend = [s.get("channel") for s in data.get("suggestions", []) if s.get("status", "pending") == "pending"]
        return f"No suggested channel matching '{channel}'. Pending: {', '.join(pend) or '(none)'}."
    hit["status"] = "approved"
    err = _write_state("channel_suggestions.json", data, f"approve channel: {hit.get('channel')}")
    if err:
        return err
    n = len(hit.get("videos", []))
    return (f"Approved channel '{hit.get('channel')}'. Its {n} videos will be added to the playlist "
            "on the next add-to-playlist run (needs the one-time Google sign-in — sync/oauth_setup.py).")


@mcp.tool()
def dismiss_channel(channel: str) -> str:
    """Skip a suggested channel by name so its videos are NOT added. Writes channel_suggestions.json."""
    data = _load("channel_suggestions.json", {"suggestions": []})
    hit = _find_channel(data, channel)
    if not hit:
        return f"No suggested channel matching '{channel}'."
    hit["status"] = "dismissed"
    err = _write_state("channel_suggestions.json", data, f"dismiss channel: {hit.get('channel')}")
    return err or f"Dismissed channel '{hit.get('channel')}'. It won't be added."


# ── dynamic trend tabs (auto-created by the self-improvement stage) ──────────────
def _extra_tabs() -> list[dict]:
    return _load("extra_tabs.json", {"tabs": []}).get("tabs", [])


@mcp.tool()
def list_dynamic_tabs() -> str:
    """List auto-created trend tabs (status active/dismissed). The self-improvement stage
    may add one when it spots a recurring theme across videos that fits no existing tab."""
    tabs = _extra_tabs()
    if not tabs:
        return (
            "No dynamic trend tabs yet. When the daily self-improvement stage detects a "
            "recurring, important theme across several videos that fits no existing tab, it "
            "auto-creates a tab here and announces it on the dashboard."
        )
    lines = []
    for t in tabs:
        lines.append(
            f"- [{t.get('status','active')}] {t.get('title','?')}  (id: {t.get('id','?')})\n"
            f"    {t.get('description','')}  — {len(t.get('items',[]))} item(s), "
            f"{len(t.get('evidence_video_ids',[]))} source video(s)"
        )
    return f"Dynamic trend tabs ({len(tabs)}):\n" + "\n".join(lines)


@mcp.tool()
def dismiss_dynamic_tab(tab_id: str) -> str:
    """Dismiss an auto-created trend tab by id: it is hidden on the dashboard and the
    self-improvement stage will never recreate that trend. Writes data/extra_tabs.json."""
    tid = tab_id.strip().lower()
    tabs = _extra_tabs()
    found = False
    for t in tabs:
        if str(t.get("id", "")).lower() == tid:
            t["status"] = "dismissed"
            found = True
    if not found:
        return f"No dynamic tab with id '{tab_id}'. Use list_dynamic_tabs to see ids."
    err = _write_state("extra_tabs.json", {"tabs": tabs}, f"dismiss tab: {tid}")
    if err:
        return err
    return (
        f"Dismissed tab '{tid}'. It is hidden on the dashboard, and the self-improvement "
        "stage will never recreate that trend."
    )


@mcp.tool()
def catch_up_status() -> str:
    """Show the massive-addition 'catch-up' status: whether the analyze stage is sprinting
    through a big backlog, how many videos remain, and why it turned on."""
    cu = _load("catch_up.json", {"active": False, "mode": "auto"})
    st = _load("status.json", {})
    pending = cu.get("last_pending")
    if pending is None:
        pending = st.get("pending_count", st.get("run_report", {}).get("pending_to_analyze", 0))
    mode = cu.get("mode", "auto")
    mode_h = {"auto": "automatic", "forced_on": "forced ON (manual)",
              "forced_off": "forced OFF (manual)"}.get(mode, mode)
    if cu.get("active"):
        return (
            "CATCH-UP: ON — sprinting through a big backlog, newest videos first.\n"
            f"  Remaining to analyze: {pending}\n"
            f"  Mode: {mode_h}\n"
            f"  Reason: {cu.get('reason','')}\n"
            f"  Surge threshold: {cu.get('surge_threshold','?')} new videos in one fetch.\n"
            "It auto-returns to normal speed once the backlog is cleared. "
            "Use set_catch_up('off') to stop early, or set_catch_up('on') to force it."
        )
    return (
        "CATCH-UP: OFF — running at the normal pace (50 videos / few hours).\n"
        f"  Pending to analyze: {pending}\n"
        f"  Mode: {mode_h}\n"
        f"  It turns on automatically when one fetch finds "
        f"{cu.get('surge_threshold', _config().get('catch_up', {}).get('surge_threshold', 100))}+ "
        "new videos (e.g. you merge another playlist). "
        "Use set_catch_up('on') to force a sprint now."
    )


@mcp.tool()
def set_catch_up(mode: str) -> str:
    """Manually control catch-up mode. mode = 'on' (force a sprint now), 'off' (stop and
    return to normal pace), or 'auto' (default: let it switch on automatically at a surge).
    Writes data/catch_up.json (needs GITHUB_PAT, like star/approve)."""
    from datetime import datetime, timezone

    m = mode.strip().lower()
    alias = {"on": "forced_on", "force_on": "forced_on", "forced_on": "forced_on",
             "off": "forced_off", "force_off": "forced_off", "forced_off": "forced_off",
             "auto": "auto"}
    if m not in alias:
        return "mode must be 'on', 'off', or 'auto'."
    new_mode = alias[m]
    raw = _load("catch_up.json", {})
    # Preserve known-good fields even if the file was somehow malformed; fall back to config.
    cu = raw if isinstance(raw, dict) else {}
    if not cu:
        cu = {k: v for k, v in _config().get("catch_up", {}).items()
              if k in ("surge_threshold", "batch_size", "order")}

    cu["mode"] = new_mode
    if new_mode == "forced_on":
        cu["active"] = True
        cu["reason"] = "manual: forced on"
    elif new_mode == "forced_off":
        cu["active"] = False
        cu["reason"] = "manual: forced off"
    else:  # auto — let the cloud recompute active on the next fetch/analyze
        cu["reason"] = "manual: set to auto"
    cu["updated_at"] = datetime.now(timezone.utc).isoformat()
    err = _write_state("catch_up.json", cu, f"catch-up: set mode {new_mode}")
    if err:
        return err
    human = {"forced_on": "ON (forced sprint)", "forced_off": "OFF (normal pace)",
             "auto": "AUTO (turns on by itself at a surge)"}[new_mode]
    return (
        f"Catch-up mode set to {human}. The cloud picks this up on the next analyze run "
        "(within ~30 min while sprinting, or the next scheduled run otherwise)."
    )


@mcp.tool()
def health() -> str:
    """Show the latest data-health report (score, metrics, token + cadence advice)."""
    h = _load("health.json", {})
    if not h:
        return (
            "No health report yet. The daily self-improvement stage writes data/health.json "
            "(run_improve to generate one now)."
        )
    m = h.get("metrics", {})
    lines = [
        f"Health score: {h.get('score','?')}/100   (generated {h.get('generated_at','?')})",
        "Metrics:",
    ]
    for k, v in m.items():
        lines.append(f"  {k:<22} {v}")
    tok = h.get("token_optimization", {})
    if tok.get("advice"):
        lines.append(f"Token advice: {tok['advice']}")
    if h.get("cadence_advice"):
        lines.append(f"Cadence: {h['cadence_advice']}")
    for a in h.get("advice", []) or []:
        lines.append(f"• {a}")
    return "\n".join(lines)


@mcp.tool()
def news_feed_health() -> str:
    """Show per-source news-feed health: consecutive-failure streaks, last-OK time, and the
    last error. The news fetch stage writes data/feeds_health.json; once a feed's streak
    crosses self_improvement.feed_health.fail_streak_threshold, the self-improvement stage
    proposes dropping it (suggest-only — you approve with approve_suggestion)."""
    h = _load("feeds_health.json", {})
    feeds = h.get("feeds", {}) if isinstance(h, dict) else {}
    if not feeds:
        return (
            "No feed-health data yet. It is written by the news fetch stage "
            "(data/feeds_health.json) after the web-news step has run at least once."
        )
    threshold = int(
        _config().get("self_improvement", {}).get("feed_health", {}).get("fail_streak_threshold", 5)
    )
    rows = sorted(feeds.items(), key=lambda kv: (kv[1] or {}).get("fail_streak", 0), reverse=True)
    healthy = sum(1 for _, info in rows if (info or {}).get("fail_streak", 0) == 0)
    lines = [
        f"News-feed health ({len(rows)} feeds; {healthy} healthy)  generated "
        f"{h.get('generated_at','?')}  — drop-suggest threshold = {threshold} consecutive fails:"
    ]
    for name, info in rows:
        info = info or {}
        streak = info.get("fail_streak", 0)
        flag = "  <-- will be suggested for removal" if streak >= threshold else ""
        last_ok = info.get("last_ok") or "never"
        err = info.get("last_error") or ""
        line = f"- {name}: fail_streak={streak}, last_ok={last_ok}"
        if err:
            line += f", last_error={err}"
        lines.append(line + flag)
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
