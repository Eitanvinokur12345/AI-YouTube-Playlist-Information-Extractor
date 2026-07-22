# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-940` (dept) · 2026-07-22T23:32:07.003470+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch the full caption file for the first pending video.
2. Validate the retrieved transcript for completeness and accuracy.
3. Save the verified transcript to the designated repository or storage.
4. Mark the video as processed in the pending queue.
5. Log the action and timestamp for audit purposes.
6. Proceed to the next pending video if no errors are detected.

**What changed:** Initiated real transcript retrieval for the first pending video via residential IP.
