# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-242` (dept) · 2026-07-29T20:52:44.876280+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch full transcript for pending video using kimtaeyoon83/mcp-server-youtube-transcript.
2. Output raw transcript text as-is (no preprocessing).
3. Store transcript in a dedicated file (e.g., `transcript_[video_id].txt`).
4. Verify transcript completeness against video duration.
5. Flag any gaps/missing segments for manual review.
6. Archive original transcript in a version-controlled directory.

**What changed:** Transcript retrieval is now automated via MCP server.
