# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-452` (dept) · 2026-07-22T23:16:21.267365+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch the full caption transcript for the first pending video.
2. Retrieve the raw, unfiltered transcript text for immediate review.
3. Validate the transcript’s accuracy by cross-referencing key segments with the video’s audio.
4. Store the verified transcript in the designated repository or database.
5. Mark the video as "transcribed" in the pending queue and log the transcript’s source.
6. Proceed to the next pending video if no errors are detected.

**What changed:** Transcript retrieval is now actionable via the specified tool.
