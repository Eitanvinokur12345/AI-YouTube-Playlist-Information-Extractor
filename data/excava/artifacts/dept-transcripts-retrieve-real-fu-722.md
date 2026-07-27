# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-722` (dept) · 2026-07-27T22:33:01.526685+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` for the first pending video ID.
2. Use residential IP and gentle pacing to retrieve the full transcript.
3. Validate the transcript for completeness and accuracy.
4. Save the transcript in the designated output directory.
5. Mark the video ID as processed in the tracking system.
6. Log the action and timestamp for audit purposes.

**What changed:** Resolved to execute the transcript retrieval with residential IP and gentle pacing.
