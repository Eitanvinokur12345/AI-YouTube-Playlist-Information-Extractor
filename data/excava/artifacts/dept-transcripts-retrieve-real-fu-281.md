# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-281` (dept) · 2026-09-02T16:25:11.211873+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the real, unaltered transcript for the pending video.
2. Scriv verifies the transcript exists as the unaltered source.
3. Reel confirms the transcript is retrieved and matches the video’s captions.
4. Store the transcript in the designated repository under `/transcripts/[video_id].txt`.
5. Log the action in `transcript_log.md` with timestamp and video ID.
6. Notify the team via Slack/email that the transcript is ready for review.

**What changed:** Transcript retrieval is now automated and verified as the real source.
