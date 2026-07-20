# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-747` (dept) · 2026-07-20T18:02:41.953057+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch full transcripts for all videos flagged "pending" using the YouTube transcript tool.
2. Verify each transcript exists and is complete before proceeding.
3. Store transcripts in a structured format (e.g., JSON or CSV) for easy retrieval.
4. Mark each video as "transcript retrieved" in the tracking system.
5. Log any failures (e.g., missing transcripts) for manual review.
6. Notify the team upon completion of all pending videos.

**What changed:** Added verification and structured storage steps to ensure reliability.
