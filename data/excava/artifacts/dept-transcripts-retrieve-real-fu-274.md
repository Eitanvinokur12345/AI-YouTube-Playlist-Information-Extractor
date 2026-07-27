# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-274` (dept) · 2026-07-27T19:08:37.761027+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` for the first pending video ID to retrieve its full transcript.
2. Store the raw transcript text in a structured format (e.g., JSON or text file) for the video.
3. Validate the transcript for completeness and accuracy against the video content.
4. Save the verified transcript to the designated repository for pending videos.
5. Mark the video ID as processed in the tracking system.
6. Log the action and timestamp for audit purposes.

**What changed:** Initiated transcript retrieval for the first pending video ID via the YouTube transcript tool.
