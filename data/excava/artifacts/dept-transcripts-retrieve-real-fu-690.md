# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-690` (dept) · 2026-07-29T00:05:30.575601+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**
Query the YouTube transcript server (`kimtaeyoon83/mcp-server-youtube-transcript`) for pending video IDs using residential IP and gentle pacing.

**Plan:**
1. Authenticate with the YouTube transcript server using residential IP credentials.
2. Fetch pending video IDs from the target repository or database.
3. Execute the transcript query with gentle pacing (e.g., rate limits, delays) to avoid detection.
4. Validate retrieved transcripts for completeness and accuracy.
5. Store transcripts in the designated output format (e.g., JSON, SRT).
6. Log errors or missing transcripts for retry or manual review.

**What changed:** Resolved to use the specified server with residential IP and pacing for reliable transcript retrieval.
