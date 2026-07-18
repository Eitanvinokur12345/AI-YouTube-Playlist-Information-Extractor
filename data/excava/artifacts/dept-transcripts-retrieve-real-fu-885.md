# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-885` (dept) · 2026-07-18T01:23:12.302254+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full transcript for video ID "dQw4w9".
2. Reel verifies the transcript artifact exists (e.g., checks file size, content length, or metadata).
3. Reel marks the video as "transcript retrieved" in the pending queue.
4. Reel proceeds to the next pending video in the queue.
5. If the transcript fails to generate, Reel logs the error and flags the video for manual review.
6. Repeat steps 1–5 until all pending videos have transcripts.

**What changed:** Transcript retrieval for "dQw4w9" is now automated and verified before proceeding.
