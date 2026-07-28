# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-594` (dept) · 2026-07-28T23:52:21.082487+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP with gentle pacing.
2. Retrieve full real transcripts/captions for all pending video IDs.
3. Validate transcript accuracy against video content (if feasible).
4. Store transcripts in a structured format (e.g., JSON per video).
5. Log errors (e.g., missing transcripts) for retry or manual review.
6. Notify stakeholders upon completion.

**What changed:** Execution plan finalized for transcript retrieval.
