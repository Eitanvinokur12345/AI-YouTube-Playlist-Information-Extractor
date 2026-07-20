# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-588` (dept) · 2026-07-20T18:08:45.726880+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch full transcripts for all videos flagged "pending" using the YouTube transcript server.
2. Store the raw, unfiltered transcripts in the archive.
3. Ensure transcripts are retrieved via residential IP with gentle pacing to avoid detection.
4. Verify transcript completeness and accuracy for each pending video.
5. Log the retrieval process and store metadata (e.g., video ID, timestamp) for traceability.
6. Notify stakeholders upon completion of transcript retrieval.

**What changed:** Added verification, logging, and notification steps to the initial plan.
