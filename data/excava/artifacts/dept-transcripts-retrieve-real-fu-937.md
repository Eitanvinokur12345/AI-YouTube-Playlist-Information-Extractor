# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-937` (dept) · 2026-07-22T23:22:58.544127+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch the full transcript of the first pending video.
2. Return the raw, unfiltered transcript text for immediate use.
3. Store the transcript in the designated repository or system for pending videos.
4. Verify the transcript’s completeness and accuracy against the video.
5. Proceed to the next pending video only after confirming the current transcript’s integrity.
6. Log the action and timestamp for audit purposes.

**What changed:** Execution of transcript retrieval via residential IP initiated.
