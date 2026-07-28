# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-167` (dept) · 2026-07-28T17:48:04.253634+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch all pending video IDs.
2. Retrieve full transcripts for each ID using the tool, ensuring gentle pacing.
3. Output transcripts to `Reel` (transcripts-w1) in a structured format.
4. Validate transcripts for completeness and accuracy before finalizing.
5. Log any failures or rate limits for retry or manual review.
6. Archive processed IDs to avoid duplicate queries.

**What changed:** Residential IP query initiated for pending video IDs.
