# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-331` (dept) · 2026-07-27T19:21:41.225649+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` for the first pending video ID to fetch its raw transcript.
2. Save the retrieved transcript to a local file (e.g., `transcripts/video_id.txt`).
3. Validate the transcript for completeness (e.g., check for missing segments or errors).
4. If valid, mark the video as processed in the pending queue.
5. If invalid, log the error and flag the video for manual review.
6. Repeat for the next pending video ID until all are processed.

**What changed:** Automated transcript retrieval replaces manual review for pending videos.
