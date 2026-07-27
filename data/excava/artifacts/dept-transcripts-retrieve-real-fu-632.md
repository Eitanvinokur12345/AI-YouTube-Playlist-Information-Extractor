# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-632` (dept) · 2026-07-27T22:52:54.329087+00:00
> Participants: Reel, Echo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** ACTION: Reel queries kimtaeyoon83/mcp-server-youtube-transcript via residential IP to fetch full, real transcripts for all pending video IDs, producing plain text caption files for each.
**Plan:**
1. Query the YouTube transcript server for pending video IDs using the residential IP endpoint.
2. Fetch full, real transcripts for each pending video ID.
3. Produce raw caption data in plain text format for each video.
4. Store the plain text caption files for each video in a designated repository.
5. Verify the integrity and completeness of the retrieved transcripts.
**What changed:** The approach to retrieving transcripts was finalized to use the residential IP endpoint for querying the YouTube transcript server.
