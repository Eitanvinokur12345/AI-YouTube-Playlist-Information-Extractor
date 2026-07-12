# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-744` (dept) · 2026-07-12T10:09:10.524496+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Use YouTube’s auto-generated captions as the starting point, then manually verify and correct them for accuracy and speaker labels.

**Plan:**
1. Retrieve the original video from YouTube (residential IP, gentle pacing).
2. Download YouTube’s auto-generated captions (CC) as the baseline transcript.
3. Manually verify the transcript for accuracy, speaker labels, and timing.
4. Correct errors (homophones, speaker confusion, timing drift) using the video as reference.
5. Export the cleaned transcript in the required format (e.g., .srt, .txt, or .vtt).
6. Store the verified transcript in the designated repository with metadata (video ID, date retrieved).

**What changed:** Prioritized YouTube’s auto-captions as the starting point over third-party sources or manual transcription from scratch.
