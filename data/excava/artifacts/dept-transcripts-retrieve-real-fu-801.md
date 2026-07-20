# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-801` (dept) · 2026-07-20T22:26:57.996594+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel fetches full YouTube transcripts for all videos marked "pending."
2. Echo verifies each fetched transcript exists and is complete.
3. If verification passes, mark the video as "done."
4. Log any missing or incomplete transcripts for reprocessing.
5. Repeat steps 1-4 until all pending videos are processed.
6. Notify stakeholders upon completion.

**What changed:** Added verification step to ensure transcript completeness before marking videos as done.
