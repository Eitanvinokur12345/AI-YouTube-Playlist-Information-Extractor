# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-624` (dept) · 2026-08-15T05:00:19.315757+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Install/update the `kimtaeyoon83/mcp-server-youtube-transcript` tool (if not already available).
2. Identify the first pending video in the queue.
3. Execute the tool on the selected video to generate a real, downloadable transcript file.
4. Verify the transcript file contains full captions (not summaries or placeholders).
5. Save the transcript file to the designated review directory.
6. Mark the video as "transcript retrieved" in the tracking system.

**What changed:** Tool execution directly retrieves real transcripts per approved method.
