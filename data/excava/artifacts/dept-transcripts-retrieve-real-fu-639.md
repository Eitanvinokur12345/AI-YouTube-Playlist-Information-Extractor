# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-639` (dept) · 2026-08-10T20:35:36.940735+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Scriv runs `kimtaeyoon83/mcp-server-youtube-transcript` on every pending video.
2. Scriv verifies real transcripts exist for each video.
3. Scriv logs confirmation for each transcript.
4. Scriv updates the transcript status for all processed videos.
5. Scriv notifies Reel upon completion.

**What changed:** Scriv executes the transcript retrieval action.
