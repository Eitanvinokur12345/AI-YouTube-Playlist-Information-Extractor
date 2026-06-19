"""
src/resolve_comment_gated.py — recover resources the creator gated behind "comment / link below".

Many videos say "comment 'X' and I'll send it" or "link in the description" WITHOUT a usable link.
We never comment (ToS / no bot). Instead: most creators DESCRIBE the resource precisely, so we ask
the FREE engine pool to identify the specific tool/resource + its official URL from that description,
and add it to the catalogue (attributed, deduped). Skips personal/DM-only lists (unresolvable).

Reuses the free engine pool -> ZERO Claude-Pro tokens. State in data/comment_resolved.json.

Usage:  python -m src.resolve_comment_gated --limit 40
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import time
from pathlib import Path

from src.bulk_analyze import NOW, extract, load, norm, save, slugify
from src.mine_feeds import build_pool, merge

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
PROCESSED = DATA / "processed"
CONFIG = ROOT / "config.json"
STATE = DATA / "comment_resolved.json"

GATE = re.compile(r"(comment\s+['\"]?\w+['\"]?\s+(and|to|for|below)|link in (the )?(description|bio|comments?)"
                  r"|check (the )?description|drop a comment|first comment|pinned comment|i'?ll send (you )?the"
                  r"|dm me|link below|grab the (link|template|prompt)s? (in|below))", re.I)


def prompt(rec: dict) -> str:
    text = (rec.get("transcript") or rec.get("description") or rec.get("title") or "")[:8000]
    return (
        "A YouTube creator gated a resource behind a comment / description link but no usable link is "
        "present. From the content, identify the SPECIFIC named tool/resource the creator is offering "
        "and its OFFICIAL url if you are confident. Return STRICT JSON ONLY:\n"
        '{"resolved":true,"tools":[{"name":"","slug":"","category":"other","description":"","quality_score":1,"url":""}],'
        '"connectors":[{"name":"","what_it_does":"","works_in":"both","free":true,"url":""}]}\n'
        "- Only include something you can NAME from the content. If it's a personal/DM-only or unnamed "
        'list, return {"resolved":false}. Never invent a url you are unsure of (leave it "").\n\n'
        f"TITLE: {rec.get('title','')}\nCONTENT:\n{text}\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--sleep", type=float, default=3.0)
    args = ap.parse_args()

    cfg = load(CONFIG, {})
    pool = build_pool(cfg)
    if not pool:
        print("No engine keys present — comment-resolver skipped (graceful)."); return 0

    seen = set((load(STATE, {}) or {}).get("video_ids", []))
    todo = []
    for f in sorted(glob.glob(str(PROCESSED / "*.json"))):
        r = load(Path(f), None)
        if not isinstance(r, dict):
            continue
        vid = r.get("video_id")
        if not vid or vid in seen:
            continue
        if r.get("transcript_source") != "transcript":
            continue
        if GATE.search((r.get("transcript") or "") + " " + (r.get("description") or "")):
            todo.append(r)
    todo = todo[: max(args.limit, 0)]
    print(f"comment-gated candidates this run: {len(todo)} ({len(seen)} already done)")

    tools = load(DATA / "tools.json", {"tools": []})
    conns = load(DATA / "connectors.json", {"connectors": []})
    nt = nc = done = 0
    errs = {e["name"]: 0 for e in pool}
    idx = 0
    timeout = int(cfg.get("news", {}).get("request_timeout_seconds", 30))
    for r in todo:
        active = [e for e in pool if errs[e["name"]] < 3]
        if not active:
            print("  engines rate-limited — stopping; rest retry next run."); break
        eng = active[idx % len(active)]; idx += 1
        time.sleep(args.sleep)
        try:
            res = extract(eng["provider"], eng["base_url"], eng["key"], eng["model"], prompt(r), timeout)
        except Exception:  # noqa: BLE001
            errs[eng["name"]] += 1
            continue
        seen.add(r.get("video_id")); done += 1
        if not isinstance(res, dict) or not res.get("resolved", True):
            continue
        url = f"https://www.youtube.com/watch?v={r.get('video_id')}"
        nt += merge(tools, "tools", "name", res.get("tools"), url, "comment-resolved")
        nc += merge(conns, "connectors", "name", res.get("connectors"), url, "comment-resolved")

    if nt:
        save(DATA / "tools.json", tools)
    if nc:
        save(DATA / "connectors.json", conns)
    save(STATE, {"updated_at": NOW, "video_ids": sorted(seen)})
    print(f"comment-resolver: scanned {done} -> +{nt} tools, +{nc} connectors. NO Claude-Pro tokens used.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
