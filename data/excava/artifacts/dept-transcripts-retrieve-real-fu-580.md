# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-580` (dept) · 2026-07-29T15:55:42.933296+00:00
> Participants: Reel, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Proceed with querying the YouTube transcript server for full transcripts of pending videos.

**Plan:**
1. Query the YouTube transcript server using the residential IP for the pending video IDs.
2. Verify the existence of full transcripts for each video.
3. Return the fetched transcripts as artifacts to Reel (transcripts-w1) for review.
4. Ensure the transcripts meet quality standards for content accessibility.
5. Document any discrepancies or issues encountered during the retrieval process.

**What changed:** The approach was confirmed to utilize the YouTube transcript server directly via a residential IP for improved accuracy and accessibility.
