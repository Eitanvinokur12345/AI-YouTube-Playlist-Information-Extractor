# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-189` (dept) · 2026-08-07T01:15:03.628051+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the `kimtaeyoon83/mcp-server-youtube-transcript` tool against the pending video list.
2. Extract verified, real captions for each video.
3. Ensure transcripts are fetched under residential IP with gentle pacing.
4. Validate transcript accuracy post-extraction.
5. Store transcripts in the designated repository.
6. Mark videos as processed in the pending list.

**What changed:** Tool execution initiated for transcript retrieval.
