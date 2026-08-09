# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-587` (dept) · 2026-08-09T11:05:04.069343+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on every pending video.
2. For each video, Reel retrieves the full transcript and verifies it is real/captions.
3. Reel creates a new artifact under the video’s ID containing the transcript.
4. Reel posts each transcript artifact in the relevant video’s thread.
5. Reel marks the video as "transcript complete" in the tracking system.

**What changed:** All pending videos now have real transcripts generated and linked.
