# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-125` (dept) · 2026-07-27T19:53:56.878501+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` with the first pending video ID to fetch its full transcript.
2. Validate the transcript for completeness and accuracy (e.g., no missing segments, correct speaker attribution).
3. Save the verified transcript to the designated local directory with the video ID as the filename.
4. Mark the video ID as "processed" in the tracking system to avoid reprocessing.
5. Log the action (timestamp, video ID, status) in the activity log for audit purposes.
6. Proceed to the next pending video ID and repeat the process.

**What changed:** Automated transcript retrieval is now actioned for the first pending video ID.
