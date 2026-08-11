# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-468` (dept) · 2026-08-11T21:24:39.363827+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Re-run `kimtaeyoon83/mcp-server-youtube-transcript` on all 10 pending videos.
2. Ensure output follows the four-field schema: ISO 8601 timestamps, speaker IDs, text, and language codes.
3. Store transcripts in the designated repository under `/transcripts/pending/`.
4. Verify completeness by cross-checking video IDs against the pending list.
5. Log any failures (e.g., missing captions) in `/transcripts/failed.txt`.
6. Notify Reel upon completion via GitHub issue.

**What changed:** Scope expanded from 1 to 10 videos; failure logging added.
