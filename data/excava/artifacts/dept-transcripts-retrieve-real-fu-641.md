# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-641` (dept) · 2026-07-18T01:35:05.932767+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Echo authorizes Reel to fetch the transcript for video ID "dQw4w9" using the kimtaeyoon83/mcp-server-youtube-transcript tool.

**Plan:**
1. Reel executes the kimtaeyoon83/mcp-server-youtube-transcript tool with video ID "dQw4w9".
2. Reel verifies the output is a full, real transcript with timestamps.
3. Reel confirms the artifact exists and is valid before proceeding.
4. Reel marks the video as "transcript retrieved" in the pending queue.
5. Reel notifies Echo of completion with the transcript reference.

**What changed:**
Reel is now actively fetching the transcript for "dQw4w9".
