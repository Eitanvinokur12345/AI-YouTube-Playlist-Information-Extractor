# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-113` (dept) · 2026-07-27T17:59:31.320636+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the `kimtaeyoon83/mcp-server-youtube-transcript` tool with the first pending video ID.
2. Use residential IP and gentle pacing settings for the query.
3. Retrieve the full transcript/captions for the video.
4. Store the transcript in the designated output format.
5. Mark the video ID as processed in the pending queue.
6. Proceed to the next pending video ID if transcripts are successfully retrieved.

**What changed:** Initiated transcript retrieval for the first pending video ID.
