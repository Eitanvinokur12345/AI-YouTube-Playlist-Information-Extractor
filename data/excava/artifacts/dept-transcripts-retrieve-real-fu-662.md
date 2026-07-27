# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-662` (dept) · 2026-07-27T21:02:39.213058+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` for the first pending video ID to fetch its raw transcript.
2. Save the retrieved transcript as a `.txt` file in the designated transcripts directory.
3. Validate the transcript for completeness (no missing segments or errors).
4. If valid, mark the video ID as processed in the tracking system.
5. If invalid, log the error and escalate to manual review.
6. Repeat for the next pending video ID with a 5-second delay between queries.

**What changed:** Automated transcript retrieval is now actionable via the specified tool.
