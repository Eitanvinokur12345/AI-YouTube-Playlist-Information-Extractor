"""
src/add_to_playlist.py — insert APPROVED suggested videos into the real YouTube playlist (OAuth).

Reads data/channel_suggestions.json; for every suggestion whose status is "approved", inserts
its videos into config.source_growth.playlist_id, then flips the status to "added". After that
the normal pipeline (fetch -> transcribe -> analyze) picks them up like any other playlist video.

Needs the one-time OAuth secrets (set up via src/oauth_setup.py):
  YOUTUBE_OAUTH_CLIENT_ID, YOUTUBE_OAUTH_CLIENT_SECRET, YOUTUBE_OAUTH_REFRESH_TOKEN
Graceful no-op if they're absent or nothing is approved — so it never breaks the workflow.

Run:  python -m src.add_to_playlist
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"


def get_service():
    cid = os.environ.get("YOUTUBE_OAUTH_CLIENT_ID")
    csec = os.environ.get("YOUTUBE_OAUTH_CLIENT_SECRET")
    rt = os.environ.get("YOUTUBE_OAUTH_REFRESH_TOKEN")
    if not (cid and csec and rt):
        return None
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    creds = Credentials(
        None, refresh_token=rt, client_id=cid, client_secret=csec,
        token_uri="https://oauth2.googleapis.com/token",
        scopes=["https://www.googleapis.com/auth/youtube"],
    )
    return build("youtube", "v3", credentials=creds, cache_discovery=False)


def main() -> None:
    cfg = json.load(open(ROOT / "config.json", encoding="utf-8"))
    sg = cfg.get("source_growth", {}) or {}
    playlist_id = sg.get("playlist_id")
    sf = ROOT / sg.get("suggestions_file", "data/channel_suggestions.json")
    if not playlist_id or not sf.exists():
        print("no playlist id or no suggestions file.")
        return
    data = json.load(open(sf, encoding="utf-8"))
    approved = [s for s in data.get("suggestions", []) if s.get("status") == "approved"]
    if not approved:
        print("nothing approved to add.")
        return
    yt = get_service()
    if yt is None:
        print("OAuth secrets not set — can't write to the playlist yet. "
              "Run `python -m src.oauth_setup client_secret.json` once and add the 3 secrets.")
        return

    now = datetime.now(timezone.utc).isoformat()
    for s in approved:
        added = 0
        for v in s.get("videos", []):
            try:
                yt.playlistItems().insert(
                    part="snippet",
                    body={"snippet": {"playlistId": playlist_id,
                                      "resourceId": {"kind": "youtube#video", "videoId": v["id"]}}},
                ).execute()
                added += 1
            except Exception as e:  # noqa: BLE001
                print(f"  insert {v.get('id')} failed: {type(e).__name__}: {str(e)[:90]}")
        s.update(status="added", added_at=now, added_count=added)
        print(f"added {added}/{len(s.get('videos', []))} videos from {s.get('channel')} to the playlist.")
    with open(sf, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    sys.exit(main())
