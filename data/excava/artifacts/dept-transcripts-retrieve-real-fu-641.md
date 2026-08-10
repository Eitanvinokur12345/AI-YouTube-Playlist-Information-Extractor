# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-641` (dept) · 2026-08-10T20:48:26.994158+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Scriv will execute the transcript retrieval action as mission-critical.

**Plan:**
1. Scriv runs `kimtaeyoon83/mcp-server-youtube-transcript` on every pending video.
2. Store the full, real transcripts with speaker labels in the designated output directory.
3. Validate transcript completeness and speaker label accuracy for each video.
4. Log errors or missing transcripts for manual review.
5. Update the video metadata to reflect transcript availability.
6. Notify the team upon completion of the batch.

**What changed:** Execution of transcript retrieval is now mandatory for all pending videos.
