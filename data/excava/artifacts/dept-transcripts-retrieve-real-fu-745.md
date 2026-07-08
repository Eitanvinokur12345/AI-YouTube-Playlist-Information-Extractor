# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-745` (dept) · 2026-07-08T17:42:19.473413+00:00
> Participants: Reel, Scriv, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Exhaustively scan all indexed video directories for recent uploads and verify against ingest logs.

**Plan:**
1. Execute a unified `find` command across `/videos/pending/`, `/videos/drafts/`, `/videos/qa/`, and `/videos/incoming/` to locate all `.mp4` and `.mov` files modified in the last 7 days.
2. Include checks for user-uploaded temporary paths such as `/tmp/video_ingest_*` to ensure comprehensive coverage of potential pending video sources.
3. Count the number of files returned from the search to assess the volume of pending videos needing transcripts.
4. Generate a list of found files and cross-verify with ingest logs to identify any missing or straggling videos not in the indexed directories.
5. Retrieve full transcripts for each identified pending video, ensuring gentle pacing for accurate sentiment capture.

**What changed:** The decision now includes a broader search strategy accounting for multiple directories and paths to ensure no pending videos are overlooked.
