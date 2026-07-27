# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-512` (dept) · 2026-07-27T19:02:06.671360+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` with the first pending video ID to fetch its raw transcript.
2. Save the retrieved transcript as a `.txt` file in the designated transcripts directory.
3. Verify the transcript’s completeness (no missing segments) and readability.
4. If valid, mark the video ID as "transcribed" in the tracking system.
5. Proceed to the next pending video ID and repeat the process.
6. Log any errors (e.g., API failures, missing captions) for manual review.

**What changed:** Automated transcript retrieval is now the primary method for pending videos.
