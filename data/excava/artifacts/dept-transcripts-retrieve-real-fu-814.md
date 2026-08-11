# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-814` (dept) · 2026-08-11T01:47:17.220789+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Scriv re-checks `kimtaeyoon83/mcp-server-youtube-transcript` to confirm it outputs full, unaltered captions (not summaries) for all 10 pending videos.
2. Scriv runs the tool on the 10 videos and validates the transcripts match the expected format and completeness.
3. Scriv documents the output quality in a brief report (e.g., sample checks, transcript length consistency).
4. If outputs are verified, Scriv approves the transcripts as "real, unaltered captions" and marks the task complete.
5. If issues are found, Scriv flags them for Reel to address (e.g., tool configuration, API limits).
6. Reel and Scriv coordinate on any necessary fixes before re-running.

**What changed:** Added validation step to ensure transcripts are full and unaltered before task completion.
