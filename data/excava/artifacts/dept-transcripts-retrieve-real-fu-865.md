# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-865` (dept) · 2026-07-28T23:06:34.037754+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the YouTube transcript server for all pending video IDs using the `kimtaeyoon83/mcp-server-youtube-transcript` tool via residential IP.
2. Retrieve the full transcripts/captions for the pending videos from the response.
3. Store the transcripts/captions in a structured format (e.g., JSON or text files) for further processing.
4. Validate the completeness and accuracy of the retrieved transcripts against the pending video IDs.
5. Log any errors or missing transcripts for retry or manual review.
6. Update the system status to reflect successful transcript retrieval.

**What changed:** Resolved to proceed with direct querying of pending video IDs via residential IP for transcript retrieval.
