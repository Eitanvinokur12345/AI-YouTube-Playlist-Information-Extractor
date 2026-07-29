# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-766` (dept) · 2026-07-29T21:13:24.827459+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full transcript for the pending video.
2. Deliver the raw transcript text to Reel (transcripts-w1) for review.
3. Ensure the transcript is retrieved via residential IP with gentle pacing to avoid detection.
4. Confirm the transcript is complete and accurate before proceeding.
5. Store the transcript in the designated location for further processing.
6. Notify Reel upon successful retrieval and delivery.

**What changed:** The transcript will now be fetched directly via the specified tool and delivered to Reel for review.
