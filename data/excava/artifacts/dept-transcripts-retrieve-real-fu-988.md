# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-988` (dept) · 2026-07-27T18:34:17.666546+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` with the first pending video ID to fetch its full transcript.
2. Validate the retrieved transcript for completeness and accuracy (e.g., no missing segments, correct formatting).
3. Store the transcript in the designated repository under `/transcripts/[video_id].txt`.
4. Mark the video ID as "transcribed" in the pending queue log.
5. Log the action in the project's activity tracker with timestamp and video ID.
6. Proceed to the next pending video ID if the queue is not empty.

**What changed:** Initiated transcript retrieval for the first pending video ID via the specified tool.
