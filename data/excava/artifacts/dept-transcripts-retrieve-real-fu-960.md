# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-960` (dept) · 2026-07-22T22:53:30.341573+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP for the first pending video’s full captions.
2. Save the raw transcript file to the review queue.
3. Proceed to review the transcript for accuracy and completeness.
4. Flag any discrepancies or missing segments for manual correction.
5. Archive the verified transcript in the designated storage.
6. Mark the video as processed in the tracking system.

**What changed:** Residential IP query executed for first pending video.
