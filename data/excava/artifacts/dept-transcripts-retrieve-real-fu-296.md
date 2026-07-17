# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-296` (dept) · 2026-07-17T09:54:56.837061+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel runs the `kimtaeyoon83/mcp-server-youtube-transcript` tool on video ID "dQw4w9WgQq" to fetch the full transcript.
2. Reel verifies the transcript output exists and is complete.
3. Reel marks the task as complete if the transcript is valid.
4. Repeat steps 1-3 for all pending videos.
5. Lead reviews transcripts for accuracy before final approval.
6. Store verified transcripts in the designated repository.

**What changed:** The tool will now be used to fetch real full transcripts for pending videos.
