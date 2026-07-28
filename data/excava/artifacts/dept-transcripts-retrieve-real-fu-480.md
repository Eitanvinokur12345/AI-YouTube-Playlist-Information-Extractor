# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-480` (dept) · 2026-07-28T23:40:04.733954+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch pending video IDs and their transcripts/captions.
2. Output results directly to `Reel` (file: `transcripts-w1`).
3. Validate transcripts for completeness (full vs. partial captions).
4. Store verified transcripts in the designated repository with metadata (video ID, timestamp, source).
5. Flag videos with missing/partial transcripts for manual review or retry.
6. Log execution details (IP, query time, success/failure rates) for audit.

**What changed:** Resolved to use the specified tool for direct transcript retrieval via residential IP.
