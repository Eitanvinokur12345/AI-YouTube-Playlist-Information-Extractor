# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-823` (dept) · 2026-08-10T21:39:06.525377+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Scriv runs `kimtaeyoon83/mcp-server-youtube-transcript` on every pending video.
2. For each video, Scriv verifies the transcript is full and real before proceeding.
3. Scriv stores the verified transcripts securely (residential IP; gentle pacing).
4. Scriv marks each video as processed upon successful transcript retrieval.
5. Scriv logs completion status for all pending videos in a summary report.

**What changed:** Scriv now executes the transcript retrieval process with verification.
