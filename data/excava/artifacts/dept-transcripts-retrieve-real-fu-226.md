# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-226` (dept) · 2026-07-28T12:21:30.668018+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the YouTube transcript server for pending video IDs using the transcript tool to retrieve full, real transcripts.
2. Store the retrieved transcripts in a structured format (e.g., JSON or Markdown) for each video.
3. Verify transcript accuracy by cross-referencing with video content (e.g., timestamps, speaker labels).
4. Organize transcripts into a GitHub repository with clear file naming (e.g., `videoID_transcript.md`).
5. Implement a lightweight validation script to flag missing or corrupted transcripts for reprocessing.
6. Log all actions (success/failure) in a `transcript_log.md` for auditability.

**What changed:** Decision to proceed with direct transcript API queries instead of manual scraping.
