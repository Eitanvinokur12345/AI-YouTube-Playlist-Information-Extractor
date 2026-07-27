# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-724` (dept) · 2026-07-27T22:19:13.315206+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` for the first pending video ID using a residential IP.
2. Retrieve the full real transcript for the specified video.
3. Validate the transcript for accuracy and completeness.
4. Store the transcript in the designated output location.
5. Mark the video ID as processed in the pending queue.
6. Log the action and result for audit tracking.

**What changed:** Initiated transcript retrieval for the first pending video ID via residential IP.
