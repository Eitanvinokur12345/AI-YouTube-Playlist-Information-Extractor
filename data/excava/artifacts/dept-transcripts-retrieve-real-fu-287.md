# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-287` (dept) · 2026-07-28T22:58:27.558729+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the kimtaeyoon83/mcp-server-youtube-transcript tool via residential IP to fetch full transcripts/captions for all pending video IDs.
2. Validate the completeness and accuracy of retrieved transcripts against YouTube’s captions.
3. Store transcripts in a structured format (e.g., JSON/CSV) with metadata (video ID, timestamp, language).
4. Log failures (missing/partial transcripts) for retry or manual review.
5. Notify the user upon completion or if errors exceed a threshold.
6. Archive raw transcripts and processed data in a designated directory.

**What changed:** Resolved to execute the transcript retrieval via residential IP with gentle pacing.
