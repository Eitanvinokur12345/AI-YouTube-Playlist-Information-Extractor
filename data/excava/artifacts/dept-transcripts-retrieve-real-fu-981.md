# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-981` (dept) · 2026-08-09T11:29:06.612461+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on all pending videos.
2. Reel retrieves real, full transcripts/captions for each video.
3. Reel stores transcripts in a structured format (e.g., JSON per video).
4. Scriv verifies transcripts for accuracy and completeness.
5. Echo archives the original pending video list post-transcript retrieval.
6. Log all actions in a `transcript_retrieval.log` for audit.

**What changed:** Pending videos now have full, real transcripts via Reel's execution.
