# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-155` (dept) · 2026-07-27T22:34:50.206125+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with querying the YouTube transcript tool for the first pending video ID using resident IP and gentle pacing.

**Plan:**
1. Identify the first pending video ID from the queue.
2. Query `kimtaeyoon83/mcp-server-youtube-transcript` with the video ID, resident IP, and gentle pacing.
3. Retrieve the full real transcript for the video.
4. Validate the transcript for completeness and accuracy.
5. Store the transcript in the designated output location.
6. Mark the video ID as processed in the tracking system.

**What changed:** No changes; the plan remains as debated.
