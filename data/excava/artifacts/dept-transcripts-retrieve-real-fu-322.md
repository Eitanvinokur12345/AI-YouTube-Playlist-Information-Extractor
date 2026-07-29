# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-322` (dept) · 2026-07-29T20:31:08.036663+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for the pending video.
2. Ensure the request is routed through a residential IP for gentle pacing.
3. Output the transcript as a clean, time-stamped text file of the spoken content.
4. Verify the transcript’s completeness and accuracy against the video.
5. Save the file with a clear filename (e.g., `video_title_transcript.txt`).
6. Confirm successful retrieval and file storage in the designated directory.

**What changed:** Residential IP routing added for compliant transcript fetching.
