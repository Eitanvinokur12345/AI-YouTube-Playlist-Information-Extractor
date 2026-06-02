"""
src/fetch.py  —  YouTube playlist fetch + transcript pull + news classification.
Run with:  python -m src.fetch
"""
from __future__ import annotations

import json
import logging
import os
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import pytz
from dateutil import parser as dateutil_parser
from googleapiclient.discovery import build

# ── logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
log = logging.getLogger(__name__)

# ── paths ─────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
CONFIG_PATH = ROOT / "config.json"
DATA_DIR = ROOT / "data"
PENDING_DIR = DATA_DIR / "_pending"
SKILLS_JSON = DATA_DIR / "skills.json"
STATUS_JSON = DATA_DIR / "status.json"
DAILY_JSON = DATA_DIR / "daily_news.json"
WEEKLY_JSON = DATA_DIR / "weekly_news.json"
MONTHLY_JSON = DATA_DIR / "monthly_news.json"

EASTERN = pytz.timezone("America/New_York")
MAX_TRANSCRIPT_CHARS = 8000


# ── helpers ───────────────────────────────────────────────────────────────────
def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def load_skills() -> dict:
    if SKILLS_JSON.exists():
        with open(SKILLS_JSON, encoding="utf-8") as fh:
            return json.load(fh)
    return {"videos_seen": [], "skills": []}


def load_status() -> dict:
    """Read existing status.json (to preserve cumulative analyze-stage counters)."""
    if STATUS_JSON.exists():
        try:
            with open(STATUS_JSON, encoding="utf-8") as fh:
                return json.load(fh)
        except Exception:
            return {}
    return {}


def save_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


# ── YouTube API ───────────────────────────────────────────────────────────────
def get_youtube_client(api_key: str):
    return build("youtube", "v3", developerKey=api_key, cache_discovery=False)


def fetch_playlist_videos(youtube, playlist_id: str) -> list[dict]:
    """Fetch ALL videos from a playlist; returns list of raw video dicts."""
    videos = []
    page_token = None

    while True:
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=page_token,
        )
        response = request.execute()

        for item in response.get("items", []):
            snippet = item.get("snippet", {})
            video_id = snippet.get("resourceId", {}).get("videoId", "")
            if not video_id:
                continue
            videos.append(
                {
                    "video_id": video_id,
                    "title": snippet.get("title", ""),
                    "description": snippet.get("description", ""),
                    "publishedAt": snippet.get("publishedAt", ""),
                    "channel_name": snippet.get("videoOwnerChannelTitle", ""),
                }
            )

        page_token = response.get("nextPageToken")
        if not page_token:
            break

    log.info("Fetched %d videos from playlist %s", len(videos), playlist_id)
    return videos


# ── transcript ────────────────────────────────────────────────────────────────
def fetch_transcript(
    video_id: str, title: str, description: str, languages: list[str]
) -> tuple[str, str, str]:
    """
    Try a real transcript in each language in `languages` order (e.g. ["en", "he"]),
    preferring manually-created over auto-generated.  Fallbacks: description, then title.

    The text is returned EXACTLY as YouTube provides it — never edited, translated,
    or rephrased — truncated to the first MAX_TRANSCRIPT_CHARS characters.

    Returns (text, lang, source):
      lang   = transcript language code actually used ("en"/"he"/...), "" for a fallback
      source = "transcript" | "description" | "title"
    """
    try:
        from youtube_transcript_api import YouTubeTranscriptApi

        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        for lang in languages:
            transcript = None
            try:
                transcript = transcript_list.find_manually_created_transcript([lang])
            except Exception:
                try:
                    transcript = transcript_list.find_generated_transcript([lang])
                except Exception:
                    transcript = None

            if transcript is not None:
                raw = " ".join(entry["text"] for entry in transcript.fetch())
                if raw.strip():
                    log.info("Using %s transcript for %s", lang, video_id)
                    return raw[:MAX_TRANSCRIPT_CHARS], lang, "transcript"

    except Exception as exc:
        log.warning("Transcript unavailable for %s: %s", video_id, exc)

    # fallback to description
    if description and description.strip():
        log.info("Using description as transcript for %s", video_id)
        return description.strip()[:MAX_TRANSCRIPT_CHARS], "", "description"

    # final fallback: title
    log.info("Using title as transcript for %s", video_id)
    return title.strip()[:MAX_TRANSCRIPT_CHARS], "", "title"


# ── news classification ───────────────────────────────────────────────────────
def classify_news(videos: list[dict], run_time_utc: datetime) -> tuple[list, list, list]:
    """
    Returns (daily, weekly, monthly) lists.
    Each entry: video dict + summary placeholder.
    """
    run_eastern = run_time_utc.astimezone(EASTERN)
    daily, weekly, monthly = [], [], []

    for v in videos:
        pub_str = v.get("publishedAt", "")
        if not pub_str:
            continue
        try:
            pub_dt = dateutil_parser.isoparse(pub_str)
            if pub_dt.tzinfo is None:
                pub_dt = pub_dt.replace(tzinfo=timezone.utc)
            pub_eastern = pub_dt.astimezone(EASTERN)
        except Exception:
            continue

        age_hours = (run_eastern - pub_eastern).total_seconds() / 3600.0

        entry = {
            "video_id": v["video_id"],
            "title": v["title"],
            "channel_name": v.get("channel_name", ""),
            "publishedAt": pub_str,
            "summary": "",  # to be filled by analysis stage
        }

        if age_hours <= 24:
            daily.append((pub_eastern, entry))
        elif age_hours <= 7 * 24:
            weekly.append((pub_eastern, entry))
        elif age_hours <= 30 * 24:
            monthly.append((pub_eastern, entry))
        # else: excluded

    # sort newest → oldest
    daily_sorted = [e for _, e in sorted(daily, key=lambda x: x[0], reverse=True)]
    weekly_sorted = [e for _, e in sorted(weekly, key=lambda x: x[0], reverse=True)]
    monthly_sorted = [e for _, e in sorted(monthly, key=lambda x: x[0], reverse=True)]
    return daily_sorted, weekly_sorted, monthly_sorted


def build_news_file(run_time_utc: datetime, entries: list[dict], window_label: str) -> dict:
    run_eastern = run_time_utc.astimezone(EASTERN)
    if entries:
        oldest = entries[-1]["publishedAt"]
        newest = entries[0]["publishedAt"]
    else:
        oldest = newest = ""
    return {
        "header": {
            "run_time": run_eastern.isoformat(),
            "window": window_label,
            "covered_from": oldest,
            "covered_to": newest,
        },
        "entries": entries,
    }


# ── main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    PENDING_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "processed").mkdir(parents=True, exist_ok=True)

    # load config
    cfg = load_config()
    playlist_id = cfg.get("playlist_id", "")
    rate_limit = float(cfg.get("rate_limit_seconds", 0.5))
    languages = cfg.get("transcript_languages", ["en"])
    run_interval = float(cfg.get("run_interval_hours", 48))

    # read API key from env — never hardcode
    api_key = os.environ.get("YOUTUBE_API_KEY", "")
    if not api_key:
        log.error("YOUTUBE_API_KEY environment variable not set. Aborting.")
        sys.exit(1)

    # load already-seen IDs
    skills_data = load_skills()
    seen_ids: set[str] = set(skills_data.get("videos_seen", []))
    already_seen_count: int = len(seen_ids)
    total_skills: int = len(skills_data.get("skills", []))

    # preserve cumulative analyze-stage counter across runs
    prev_status = load_status()
    total_videos_analyzed: int = int(prev_status.get("total_videos_analyzed", 0))

    run_time_utc = datetime.now(timezone.utc)
    run_eastern = run_time_utc.astimezone(EASTERN)
    next_run_utc = run_time_utc + timedelta(hours=run_interval)
    no_transcript_count = 0
    log.info("Run started at %s", run_time_utc.isoformat())

    # fetch playlist
    youtube = get_youtube_client(api_key)
    all_videos = fetch_playlist_videos(youtube, playlist_id)

    # filter to new videos
    new_videos = [v for v in all_videos if v["video_id"] not in seen_ids]
    log.info("%d new videos (out of %d total)", len(new_videos), len(all_videos))

    if not new_videos:
        log.info("No new videos found — nothing to process.")
        # still update news classification + status
    else:
        for v in new_videos:
            vid = v["video_id"]
            log.info("Processing video %s: %s", vid, v["title"])
            time.sleep(rate_limit)

            transcript, lang, source = fetch_transcript(
                vid, v["title"], v["description"], languages
            )
            if source != "transcript":
                no_transcript_count += 1

            pending_record = {
                "video_id": vid,
                "title": v["title"],
                "description": v["description"],
                "publishedAt": v["publishedAt"],
                "channel_name": v.get("channel_name", ""),
                "transcript": transcript,
                "transcript_lang": lang,
                "transcript_source": source,
                "fetched_at": run_time_utc.isoformat(),
            }
            save_json(PENDING_DIR / f"{vid}.json", pending_record)
            log.info("Wrote pending record for %s (source=%s)", vid, source)

        # update seen IDs
        new_ids = [v["video_id"] for v in new_videos]
        skills_data["videos_seen"] = list(seen_ids | set(new_ids))
        save_json(SKILLS_JSON, skills_data)

    # ── Tab 5: news classification (ALL playlist videos, every run) ───────────
    daily, weekly, monthly = classify_news(all_videos, run_time_utc)

    # preserve existing summaries if any
    def merge_summaries(new_entries: list[dict], existing_path: Path) -> list[dict]:
        if not existing_path.exists():
            return new_entries
        try:
            with open(existing_path, encoding="utf-8") as fh:
                old = json.load(fh)
            old_summaries = {e["video_id"]: e.get("summary", "") for e in old.get("entries", [])}
            for e in new_entries:
                if not e["summary"] and old_summaries.get(e["video_id"]):
                    e["summary"] = old_summaries[e["video_id"]]
        except Exception:
            pass
        return new_entries

    daily = merge_summaries(daily, DAILY_JSON)
    weekly = merge_summaries(weekly, WEEKLY_JSON)
    monthly = merge_summaries(monthly, MONTHLY_JSON)

    save_json(DAILY_JSON, build_news_file(run_time_utc, daily, "last 24 hours"))
    save_json(WEEKLY_JSON, build_news_file(run_time_utc, weekly, "last 7 days"))
    save_json(MONTHLY_JSON, build_news_file(run_time_utc, monthly, "last 30 days"))
    log.info(
        "News: daily=%d  weekly=%d  monthly=%d",
        len(daily), len(weekly), len(monthly),
    )

    # ── status.json ──────────────────────────────────────────────────────────
    pending_count = len(list(PENDING_DIR.glob("*.json")))

    # The fetch stage INITIALIZES the run report.  The analyze stage (driven by
    # CLAUDE.md) updates analyzed_this_run / skipped_not_relevant / errors and
    # increments the cumulative total_videos_analyzed as it works through pending/.
    status = dict(prev_status) if isinstance(prev_status, dict) else {}
    status.update({
        "last_run": run_time_utc.isoformat(),
        "last_fetch": run_time_utc.isoformat(),
        "next_run": next_run_utc.isoformat(),
        "videos_seen": len(skills_data.get("videos_seen", [])),
        "total_skills": total_skills,
        "total_videos_analyzed": total_videos_analyzed,
        "new_videos_this_run": len(new_videos),
        "run_report": {
            "run_time": run_eastern.isoformat(),
            "timezone": "America/New_York",
            "total_in_playlist": len(all_videos),
            "already_seen": already_seen_count,
            "new_found": len(new_videos),
            "no_transcript": no_transcript_count,
            "pending_to_analyze": pending_count,
            "analyzed_this_run": 0,
            "skipped_not_relevant": 0,
            "errors": 0,
        },
        "paths": {
            "pending": str(PENDING_DIR),
            "skills_json": str(SKILLS_JSON),
            "daily_news": str(DAILY_JSON),
            "weekly_news": str(WEEKLY_JSON),
            "monthly_news": str(MONTHLY_JSON),
        },
    })
    save_json(STATUS_JSON, status)
    log.info("Status written to %s", STATUS_JSON)
    log.info("Fetch stage complete.")


if __name__ == "__main__":
    main()
