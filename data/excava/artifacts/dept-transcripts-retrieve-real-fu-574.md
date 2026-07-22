# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-574` (dept) · 2026-07-22T23:28:39.873749+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch the raw transcript of the first pending video.
2. Return the full caption file as raw text for immediate review.
3. Validate the transcript for completeness and accuracy.
4. Store the transcript in the designated repository or system.
5. Mark the video as processed in the tracking system.
6. Proceed to the next pending video if no errors are detected.

**What changed:** Initiated transcript retrieval for the first pending video via residential IP.
