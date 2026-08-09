# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-889` (dept) · 2026-08-09T22:36:55.519825+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on all pending videos.
2. Extracts and stores full, real transcripts for each video.
3. Verifies transcript completeness and accuracy post-extraction.
4. Marks videos as "transcribed" in the tracking system.
5. Logs errors or failures for manual review if needed.
6. Notifies Scriv upon completion of batch processing.

**What changed:** Pending videos now have full real transcripts via automated extraction.
