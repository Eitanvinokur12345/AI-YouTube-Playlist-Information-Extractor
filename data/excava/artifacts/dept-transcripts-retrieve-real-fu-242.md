# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-242` (dept) · 2026-07-10T03:11:12.972610+00:00
> Participants: Reel, Scriv, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Fetch real transcripts via `yt-dlp --write-auto-sub --sub-lang en` only for videos with `transcript_status: "verified"`.

**Plan:**
1. Pull the pending video list from `pending_videos.json` and filter for entries with `transcript_status: "verified"`.
2. Queue a batch of 20 videos that qualify for fetching verified transcripts.
3. Use `yt-dlp --write-auto-sub --sub-lang en --skip-download` specifically on these videos to retrieve subtitles.
4. Log the results in a JSON format including `video_id`, `transcript_path`, and `source_type: "youtube_verified"`.

**What changed:** The approach now relies solely on videos with verified transcripts to ensure accuracy, addressing concerns about the reliability of auto-generated captions.
