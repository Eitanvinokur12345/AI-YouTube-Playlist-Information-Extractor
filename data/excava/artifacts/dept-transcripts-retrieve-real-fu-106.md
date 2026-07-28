# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-106` (dept) · 2026-07-28T11:00:24.558559+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to query YouTube transcripts for pending video IDs via residential IP.
2. Verify each result contains a **full transcript** (not truncated or partial).
3. Cross-check transcript completeness against video duration (e.g., ~1500 chars per minute for standard speech).
4. Log failed queries (e.g., missing transcripts) and retry with exponential backoff (max 3 attempts).
5. Store successful transcripts in a structured format (e.g., JSON with video ID + transcript text).
6. Flag videos with missing/partial transcripts for manual review.

**What changed:** Resolved to use residential IP + explicit verification of transcript completeness before success declaration.
