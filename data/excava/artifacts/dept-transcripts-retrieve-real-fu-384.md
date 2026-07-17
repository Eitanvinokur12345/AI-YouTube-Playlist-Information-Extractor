# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-384` (dept) · 2026-07-17T11:56:08.272030+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Execute the kimtaeyoon83/mcp-server-youtube-transcript tool on the first pending video in the queue.
2. Verify the output is a full, real transcript/captions (not AI-generated or summarized).
3. Save the transcript to the designated repository with the video’s metadata (title, ID, timestamp).
4. Mark the video as "transcribed" in the tracking system.
5. Proceed to the next pending video in the queue.
6. Log errors or missing captions for manual review if the tool fails.

**What changed:** Tool execution initiated for the first pending video.
