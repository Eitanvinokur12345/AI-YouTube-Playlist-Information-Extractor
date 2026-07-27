# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-688` (dept) · 2026-07-27T18:13:30.198259+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` for the first pending video ID to fetch its full real transcript.
2. Validate the transcript for completeness and accuracy (e.g., no missing segments, correct speaker attribution).
3. Store the verified transcript in the designated repository under `/transcripts/[video_id].txt`.
4. Log the action in the progress tracker with timestamp and video ID.
5. Proceed to the next pending video ID if the current transcript is valid.
6. Notify the team via Slack/email upon completion of the batch.

**What changed:** Actionable plan adopted to systematically retrieve and store transcripts.
