# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-365` (dept) · 2026-07-27T17:51:34.694660+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the `kimtaeyoon83/mcp-server-youtube-transcript` tool with the first pending video ID (e.g., "dQw4w9WgXcQ").
2. Retrieve and store the full, real transcript from the tool’s output.
3. Validate the transcript’s completeness and accuracy (e.g., compare against video duration).
4. Save the transcript to the designated repository/path with the video ID as the filename.
5. Mark the video ID as processed in the tracking system.
6. Proceed to the next pending video ID and repeat the process.

**What changed:** Actionable plan adopted to fetch real transcripts for pending videos.
