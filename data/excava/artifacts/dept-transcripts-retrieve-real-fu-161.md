# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-161` (dept) · 2026-07-27T19:15:21.340489+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` with the first pending video ID to fetch its full transcript.
2. Save the raw transcript file to a local directory for review.
3. Validate the transcript for completeness and accuracy (e.g., timestamps, speaker labels).
4. If incomplete, retry the query with adjusted parameters (e.g., retry-after delay, alternative API).
5. Store the verified transcript in the designated transcripts/captions folder.
6. Mark the video ID as processed in the pending queue.

**What changed:** Initiated transcript retrieval for the first pending video ID via the specified tool.
