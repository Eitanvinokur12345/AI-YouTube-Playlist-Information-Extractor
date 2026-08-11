# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-875` (dept) · 2026-08-11T00:49:39.571304+00:00
> Participants: Echo, Reel, Scriv · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run `kimtaeyoon83/mcp-server-youtube-transcript` on every pending video via Scriv.
2. Verify transcripts/captions are full and real for each video.
3. Store transcripts in the designated output directory.
4. Log completion status for each video (success/failure).
5. Notify team upon completion of all pending videos.
6. Archive raw transcripts for future reference.

**What changed:** Scriv now executes the transcript generation action.
