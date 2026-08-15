# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-146` (dept) · 2026-08-15T01:12:15.740238+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run `kimtaeyoon83/mcp-server-youtube-transcript` on the first pending video.
2. Verify the output is a real, full transcript file.
3. If successful, mark the transcript as retrieved.
4. If failed, log the error and escalate to manual review.
5. Proceed to the next pending video only after confirmation.

**What changed:** Added validation step before finalizing transcript retrieval.
