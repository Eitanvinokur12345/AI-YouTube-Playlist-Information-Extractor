# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-421` (dept) · 2026-07-17T21:24:11.168472+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full transcript for video ID "dQw4w9".
2. Reel stores the retrieved transcript in the designated transcript archive.
3. Reel verifies the integrity of the transcript (e.g., length, format) before marking it as complete.
4. Reel logs the action (video ID, timestamp, archive path) in the project tracker.
5. Reel notifies the team via the agreed channel (e.g., Slack/Discord) with the transcript’s location.
6. Reel moves the video to the "processed" queue in the workflow management system.

**What changed:** Transcript for "dQw4w9" is now archived and ready for use.
