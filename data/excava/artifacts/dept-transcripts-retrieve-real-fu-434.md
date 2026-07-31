# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-434` (dept) · 2026-07-31T18:24:19.663507+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the `kimtaeyoon83/mcp-server-youtube-transcript` tool on the first pending video to fetch its full transcript.
2. Reel verifies the transcript file exists and is readable.
3. Reel marks the task as complete in the tracking system.
4. Echo confirms the action and updates the status log.
5. The transcript file is stored in the designated repository folder for review.

**What changed:** First pending video’s full transcript is now retrieved and verified.
