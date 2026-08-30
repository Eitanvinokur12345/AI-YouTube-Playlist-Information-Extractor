# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-590` (dept) · 2026-08-30T02:58:36.755619+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on each pending video.
2. Reel retrieves the full, real transcripts/captions for each video.
3. Reel delivers the transcripts to the archive.
4. Scriv verifies the transcripts match the video content.
5. Echo logs the completed action in the system.
6. Archive marks the videos as "transcripts retrieved."

**What changed:** Transcripts for pending videos are now fully retrieved and archived.
