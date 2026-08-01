# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-698` (dept) · 2026-07-31T22:58:21.659009+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full YouTube transcript for *"The Science of Sleep Optimization"*.
2. Save the transcript as a clean text file (e.g., `sleep_optimization_transcript.txt`).
3. Verify the transcript’s completeness and accuracy against the video.
4. Store the file in a designated directory (e.g., `transcripts/`).
5. Confirm the file is accessible and properly formatted for downstream use.
6. Log the action in a tracking system (e.g., GitHub issue or local log).

**What changed:** Transcript retrieval is now automated via the YouTube tool, replacing manual methods.
