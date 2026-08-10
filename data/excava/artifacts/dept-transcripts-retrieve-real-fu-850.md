# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-850` (dept) · 2026-08-10T21:25:58.859692+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Scriv runs `kimtaeyoon83/mcp-server-youtube-transcript` on every pending video.
2. Extract full real transcripts/captions for each video.
3. Store transcripts in a structured format (e.g., JSON or text files).
4. Verify transcript accuracy against video content.
5. Flag any failures for manual review.
6. Archive completed transcripts in a dedicated repository folder.

**What changed:** Scriv executes the transcript retrieval plan immediately.
