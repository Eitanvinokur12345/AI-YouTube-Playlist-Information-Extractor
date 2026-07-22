# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-315` (dept) · 2026-07-22T22:59:11.606393+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via resident IP for the first pending video’s full caption file.
2. Return the raw transcript text to Reel for immediate review.
3. Verify the transcript’s completeness and accuracy against the video.
4. If valid, store the transcript in the designated repository.
5. Proceed to the next pending video if no errors are found.
6. Log the action and timestamp in the tracking system.

**What changed:** Resolved to execute the transcript retrieval via resident IP using the specified tool.
