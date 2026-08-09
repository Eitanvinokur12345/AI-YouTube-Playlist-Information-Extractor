# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-893` (dept) · 2026-08-09T21:05:51.240970+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on every pending video to fetch full, real transcripts.
2. Scriv verifies each transcript exists before marking the video as processed.
3. Reel logs each transcript retrieval for audit.
4. Scriv updates the status of each video to "completed" upon transcript confirmation.
5. Both parties review the final transcript list for discrepancies.
6. Archive the execution logs for future reference.

**What changed:** Automated transcript retrieval and verification workflow is now enforced for pending videos.
