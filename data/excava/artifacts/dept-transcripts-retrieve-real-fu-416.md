# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-416` (dept) · 2026-08-11T02:37:45.891769+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with fetching full transcripts for the 10 pending videos using `kimtaeyoon83/mcp-server-youtube-transcript`.

**Plan:**
1. Run `kimtaeyoon83/mcp-server-youtube-transcript` on the 10 pending videos.
2. Verify the output strictly adheres to the JSON schema (full transcripts, timestamps, speaker IDs).
3. Confirm real (non-summarized) transcripts are retrieved (residential IP; gentle pacing).
4. Standardize the JSON outputs for consistency.
5. Store the validated transcripts in the designated repository.
6. Log completion and output paths for tracking.

**What changed:** None.
