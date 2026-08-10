# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-440` (dept) · 2026-08-10T21:13:32.917487+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run `kimtaeyoon83/mcp-server-youtube-transcript` on every pending video.
2. Extract and store full real transcripts/captions for each video.
3. Verify transcript accuracy against video content.
4. Organize transcripts in a structured directory (e.g., by video ID).
5. Log completion status for each video.
6. Notify stakeholders upon finalization.

**What changed:** Execution of transcript retrieval initiated for all pending videos.
