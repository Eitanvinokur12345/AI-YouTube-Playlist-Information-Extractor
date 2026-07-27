# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-155` (dept) · 2026-07-27T18:40:56.539606+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` for the first pending video ID.
2. Use resident IP and gentle pacing for the request.
3. Retrieve the full real transcript for the video.
4. Store the transcript in the designated output location.
5. Mark the video ID as processed in the tracking system.
6. Proceed to the next pending video ID if available.

**What changed:** Initiated transcript retrieval for the first pending video ID.
