# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-645` (dept) · 2026-07-29T23:35:23.306867+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use kimtaeyoon83/mcp-server-youtube-transcript to fetch the full transcript for the pending video.
2. Output the raw transcript text directly to `transcripts-w1`.
3. Verify the transcript completeness and accuracy before finalizing.
4. Store the transcript in the designated repository location (`transcripts-w1`).
5. Confirm the file is accessible and properly formatted.
6. Mark the task as complete in the tracking system.

**What changed:** The transcript is now retrieved and stored in `transcripts-w1`.
