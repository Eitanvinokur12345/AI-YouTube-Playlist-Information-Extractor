# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-625` (dept) · 2026-07-27T18:27:20.106888+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` for the first pending video ID.
2. Use residential IP and gentle pacing to fetch the full real transcript.
3. Validate the transcript for completeness and accuracy.
4. Save the transcript to the designated storage location.
5. Mark the video ID as processed in the tracking system.
6. Log the action and timestamp for audit purposes.

**What changed:** Resolved to execute the transcript retrieval using residential IP and gentle pacing.
