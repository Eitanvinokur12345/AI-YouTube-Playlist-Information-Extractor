# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-417` (dept) · 2026-07-27T22:26:15.705923+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` integration to query the YouTube transcript tool for the first pending video ID.
2. Fetch the full real transcript for the identified video.
3. Store the retrieved transcript in the designated output format (e.g., JSON, text file).
4. Mark the video as processed in the pending queue.
5. Log the operation (timestamp, video ID, success/failure) for tracking.
6. Proceed to the next pending video ID if successful.

**What changed:** Automated transcript retrieval initiated for the first pending video ID.
