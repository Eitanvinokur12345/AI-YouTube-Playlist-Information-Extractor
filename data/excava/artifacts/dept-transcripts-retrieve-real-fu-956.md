# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-956` (dept) · 2026-08-10T20:10:31.054639+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Scriv runs kimtaeyoon83/mcp-server-youtube-transcript on every pending video to retrieve real full transcripts/captions.

**Plan:**
1. Identify all pending videos requiring transcripts.
2. Execute kimtaeyoon83/mcp-server-youtube-transcript on each pending video.
3. Verify the output for completeness and accuracy.
4. Store transcripts/captions in the designated repository.
5. Mark videos as "transcribed" in the tracking system.
6. Log completion and any discrepancies for review.

**What changed:**
Pending videos now have real full transcripts/captions via kimtaeyoon83/mcp-server-youtube-transcript.
