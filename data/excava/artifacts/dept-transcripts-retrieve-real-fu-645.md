# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-645` (dept) · 2026-08-07T00:38:10.519140+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel runs the `kimtaeyoon83/mcp-server-youtube-transcript` tool against the pending video list.
2. The tool fetches verified, real full transcripts for each video.
3. Echo spot-checks a 30-second sample from each transcript to confirm completeness.
4. If samples are complete, Echo marks the videos as ready.
5. If samples are incomplete, Reel re-runs the tool for the affected videos.

**What changed:** Added Echo’s spot-check verification step.
