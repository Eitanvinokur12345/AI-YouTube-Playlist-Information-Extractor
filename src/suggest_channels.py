"""
src/suggest_channels.py — grow the playlist when it stalls.

When fewer than config.source_growth.min_new_per_week videos were added to the playlist in the
last period_days, this proposes ONE high-value channel (ranked by the quality of the skills/
tools its videos produced) plus N of its recent uploads that aren't in the playlist yet, and
writes them to data/channel_suggestions.json for the owner to approve (yes/no) in the
dashboard's "Grow Sources" tab. On approval, src/add_to_playlist.py inserts them for real.

Read-only here (needs YOUTUBE_API_KEY). The owner adds nothing by hand at this stage.
Run:  python -m src.suggest_channels
"""
from __future__ import annotations

import glob
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"


def _load(p, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def _save(p, obj):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def _days_since(iso, now):
    try:
        return (now - datetime.fromisoformat(iso.replace("Z", "+00:00"))).days
    except Exception:
        return 9999


def main() -> None:
    cfg = _load(ROOT / "config.json", {})
    sg = cfg.get("source_growth", {}) or {}
    if not sg.get("enabled", True):
        print("source_growth disabled.")
        return
    threshold = int(sg.get("min_new_per_week", 25))
    period_days = int(sg.get("period_days", 7))
    n_suggest = int(sg.get("videos_per_suggestion", 20))
    cooldown = int(sg.get("channel_cooldown_days", 30))
    growth_file = ROOT / sg.get("growth_file", "data/source_growth.json")
    sug_file = ROOT / sg.get("suggestions_file", "data/channel_suggestions.json")

    skills_data = _load(DATA / "skills.json", {"videos_seen": [], "skills": []})
    seen = set(skills_data.get("videos_seen", []))
    total_seen = len(seen)
    now = datetime.now(timezone.utc)

    # ── 1) track growth, compute additions over the period ───────────────────────
    growth = _load(growth_file, {"history": []})
    hist = growth.get("history", [])
    hist.append({"ts": now.isoformat(), "total_seen": total_seen})
    hist = hist[-400:]
    cutoff = now - timedelta(days=period_days)
    past = [h for h in hist if datetime.fromisoformat(h["ts"]) <= cutoff]
    base = past[-1]["total_seen"] if past else (hist[0]["total_seen"] if hist else total_seen)
    weekly_additions = max(0, total_seen - base)
    growth.update(history=hist, weekly_additions=weekly_additions, threshold=threshold,
                  checked_at=now.isoformat())
    _save(growth_file, growth)
    print(f"additions in last {period_days}d: {weekly_additions} (threshold {threshold})")

    sugdata = _load(sug_file, {"suggestions": []})
    sugdata.update(weekly_additions=weekly_additions, threshold=threshold, updated_at=now.isoformat())

    if weekly_additions >= threshold:
        print("playlist growing enough — no suggestion needed.")
        _save(sug_file, sugdata)
        return

    api_key = os.environ.get("YOUTUBE_API_KEY", "")
    if not api_key:
        print("YOUTUBE_API_KEY not set — recorded the gap but cannot fetch a channel. Skipping.")
        _save(sug_file, sugdata)
        return

    # ── 2) rank channels by the quality of what they produced ────────────────────
    vid_channel, chan_sample = {}, {}
    for f in glob.glob(str(DATA / "processed" / "*.json")):
        r = _load(f, {})
        vid, ch = r.get("video_id"), r.get("channel_name")
        if vid and ch:
            vid_channel[vid] = ch
            chan_sample.setdefault(ch, vid)
    score = defaultdict(lambda: [0, 0.0])  # channel -> [count, sum_quality]
    for items in (skills_data.get("skills", []), _load(DATA / "tools.json", {}).get("tools", [])):
        for it in items:
            ch = vid_channel.get(it.get("source_video_id"))
            if ch:
                score[ch][0] += 1
                score[ch][1] += float(it.get("quality_score") or 0)
    ranked = sorted(score.items(), key=lambda kv: (kv[1][1], kv[1][0]), reverse=True)
    if not ranked:
        print("no channel value data yet.")
        _save(sug_file, sugdata)
        return

    # cooldown: skip channels already pending, or dismissed/added within the cooldown
    recent = {s.get("channel"): (s.get("status"), s.get("generated_at", "")) for s in sugdata.get("suggestions", [])}
    pick = None
    for ch, (cnt, sq) in ranked:
        st = recent.get(ch)
        if st:
            status, gen = st
            if status == "pending":
                continue
            if status in ("dismissed", "added") and _days_since(gen, now) < cooldown:
                continue
        pick = (ch, cnt, sq)
        break
    if not pick:
        print("all top channels are pending or in cooldown.")
        _save(sug_file, sugdata)
        return
    channel, cnt, sq = pick

    # ── 3) resolve the channel + pull recent uploads not already seen ────────────
    try:
        from googleapiclient.discovery import build
        yt = build("youtube", "v3", developerKey=api_key, cache_discovery=False)
        vresp = yt.videos().list(part="snippet", id=chan_sample[channel]).execute()
        items = vresp.get("items", [])
        channel_id = items[0]["snippet"]["channelId"] if items else None
        if not channel_id:
            print("couldn't resolve channel id.")
            _save(sug_file, sugdata)
            return
        cresp = yt.channels().list(part="contentDetails,snippet", id=channel_id).execute()
        cit = cresp.get("items", [])
        if not cit:
            print("channel not found.")
            _save(sug_file, sugdata)
            return
        uploads = cit[0]["contentDetails"]["relatedPlaylists"]["uploads"]
        channel_title = cit[0]["snippet"]["title"]
        candidates, page = [], None
        while len(candidates) < n_suggest * 3:
            resp = yt.playlistItems().list(part="snippet,contentDetails", playlistId=uploads,
                                           maxResults=50, pageToken=page).execute()
            for it in resp.get("items", []):
                vid = it["contentDetails"]["videoId"]
                if vid in seen:
                    continue
                candidates.append({
                    "id": vid, "title": it["snippet"]["title"],
                    "published": it["contentDetails"].get("videoPublishedAt", ""),
                    "url": f"https://www.youtube.com/watch?v={vid}",
                })
            page = resp.get("nextPageToken")
            if not page:
                break
        candidates = candidates[:n_suggest]
    except Exception as e:  # noqa: BLE001
        print(f"YouTube API error: {type(e).__name__}: {str(e)[:120]}")
        _save(sug_file, sugdata)
        return

    if not candidates:
        print(f"{channel}: no new uploads outside the playlist.")
        _save(sug_file, sugdata)
        return

    suggestion = {
        "channel": channel, "channel_id": channel_id, "channel_title": channel_title,
        "reason": (f"{cnt} skills/tools in your library came from {channel} "
                   f"(total quality {sq:.0f}) — one of your highest-value sources. "
                   f"These {len(candidates)} recent uploads aren't in your playlist yet."),
        "status": "pending", "generated_at": now.isoformat(), "videos": candidates,
    }
    kept = [s for s in sugdata.get("suggestions", []) if s.get("status") != "pending"]
    sugdata["suggestions"] = ([suggestion] + kept)[:50]
    _save(sug_file, sugdata)
    print(f"suggested channel '{channel}' with {len(candidates)} videos -> {sug_file.name}")


if __name__ == "__main__":
    sys.exit(main())
