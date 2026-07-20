# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-657` (dept) · 2026-07-20T22:41:48.354537+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the YouTube transcript tool on every video marked "pending" using residential IP pacing to fetch full transcripts.
2. Verify each fetched transcript exists and matches the video’s content.
3. Mark the task complete only after confirmation.
4. Store verified transcripts in the designated repository.
5. Log any discrepancies or failures for review.
6. Notify stakeholders upon completion.

**What changed:** Added verification step to ensure transcript accuracy before marking tasks complete.
