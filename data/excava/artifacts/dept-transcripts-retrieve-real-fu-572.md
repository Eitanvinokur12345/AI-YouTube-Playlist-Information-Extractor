# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-572` (dept) · 2026-07-28T12:36:50.253600+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the YouTube transcript server for all pending video IDs using the `kimtaeyoon83/mcp-server-youtube-transcript` tool.
2. Retrieve the full real transcripts/captions for each video from the response.
3. Store the transcripts/captions in a structured format (e.g., JSON or markdown) for further processing.
4. Validate the transcripts for completeness and accuracy against the original videos.
5. Mark the videos as processed in the tracking system to avoid reprocessing.
6. Log any errors or missing transcripts for manual review.

**What changed:** Automated transcript retrieval is now prioritized over manual or partial methods.
