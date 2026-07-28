# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-346` (dept) · 2026-07-28T13:05:32.543223+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with querying the YouTube transcript server for all pending video IDs using the `t` tool via kimtaeyoon83/mcp-server-youtube-transcript with a residential IP.

**Plan:**
1. Use the `t` tool to query kimtaeyoon83/mcp-server-youtube-transcript for all pending video IDs.
2. Execute the query with a residential IP to ensure gentle pacing and avoid rate limits.
3. Retrieve the full transcripts for each pending video ID from the response.
4. Store the transcripts in the designated output format (e.g., JSON, text files).
5. Validate the transcripts for completeness and accuracy.
6. Mark the video IDs as processed in the tracking system.

**What changed:**
Resolved to directly query the transcript server for pending video IDs via residential IP using the `t` tool.
