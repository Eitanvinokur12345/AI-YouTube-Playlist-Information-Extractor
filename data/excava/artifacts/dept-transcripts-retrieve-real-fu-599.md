# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-599` (dept) · 2026-07-22T23:10:40.329737+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch the full caption file for the first pending video.
2. Parse the raw transcript text for immediate review (e.g., check completeness, timestamps, and formatting).
3. Validate the transcript against the video’s metadata (title, duration, language) to ensure accuracy.
4. Save the verified transcript as a `.txt` or `.json` file in a structured directory (e.g., `/transcripts/pending/`).
5. Log the action in a tracking file (e.g., `transcript_log.md`) with video ID, timestamp, and status.
6. Proceed to the next pending video only after confirming the current transcript meets quality standards.

**What changed:** Resolved to execute the transcript retrieval via residential IP using the specified tool, with structured validation and logging.
