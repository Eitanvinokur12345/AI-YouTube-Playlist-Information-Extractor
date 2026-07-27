# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-797` (dept) · 2026-07-27T22:12:27.340727+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` for the first pending video ID to retrieve its full real transcript.
2. Store the retrieved transcript in the designated output directory with the video ID as the filename.
3. Log the successful retrieval in the transcript tracking system.
4. Mark the video ID as processed in the pending queue.
5. Proceed to the next pending video ID and repeat the process.
6. Verify transcript integrity (e.g., non-empty, valid format) before finalizing.

**What changed:** Actionable plan adopted; transcript retrieval initiated.
