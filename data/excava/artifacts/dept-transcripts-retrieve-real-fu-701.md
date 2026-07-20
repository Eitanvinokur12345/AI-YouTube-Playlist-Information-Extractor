# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-701` (dept) · 2026-07-20T22:35:53.431625+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel fetches full transcripts for all videos marked "pending" using the YouTube transcript tool.
2. Echo re-checks each fetched transcript to confirm existence.
3. Echo marks any missing transcripts for re-fetch.
4. Repeat steps 2-3 until all transcripts are verified.
5. Declare the set of verified transcripts complete for team review.
6. Archive the final transcript set with timestamps.

**What changed:** Added Echo’s verification step to ensure transcript completeness before finalization.
