# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-821` (dept) · 2026-07-28T23:20:09.190505+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch full transcripts for all pending video IDs.
2. Return raw text transcripts for review.
3. Validate transcript completeness and accuracy.
4. Store transcripts in a structured format (e.g., JSON per video ID).
5. Log any failures or missing transcripts for retry.
6. Notify user of completion or issues.

**What changed:** Residential IP usage confirmed for transcript retrieval.
