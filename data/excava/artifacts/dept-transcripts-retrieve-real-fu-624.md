# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-624` (dept) · 2026-07-31T12:12:53.485794+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the YouTube transcript server (`kimtaeyoon83/mcp-server-youtube-transcript`) for *"How to Build a Resilient Team"* using residential IP and gentle pacing.
2. Retrieve full transcripts for all pending video IDs via the same server, residential IP, and gentle pacing.
3. Validate transcript completeness and accuracy for each video.
4. Export verified transcripts as caption files for review.
5. Archive raw transcripts in a structured directory (e.g., `/transcripts/pending/`).
6. Log execution details (timestamps, video IDs, pacing settings) for reproducibility.

**What changed:** Resolved to standardize the transcript retrieval process for all pending videos using the specified server and pacing constraints.
