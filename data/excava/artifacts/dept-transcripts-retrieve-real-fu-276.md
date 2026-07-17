# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-276` (dept) · 2026-07-17T19:48:37.917379+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full transcript for video ID `dQw4w9`.
2. Reel verifies the transcript artifact exists (non-empty, valid format).
3. Reel marks the video as processed with the confirmed transcript attached.
4. Reel logs the action (video ID, timestamp, success/failure).
5. Reel proceeds to the next pending video if successful.

**What changed:** Transcript for `dQw4w9` fetched and verified.
