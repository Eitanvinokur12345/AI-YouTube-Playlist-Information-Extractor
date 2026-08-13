# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-153` (dept) · 2026-08-13T23:14:33.245785+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Execute `kimtaeyoon83/mcp-server-youtube-transcript` on video ID `e2Z5eBVDrKM` to fetch the full raw transcript.
2. Output the transcript as raw text for review.
3. Store the transcript in a designated directory (e.g., `/transcripts/pending/`).
4. Tag the video as "transcript_retrieved" in the tracking system.
5. Notify the team via Slack/email with the transcript file path.
6. Proceed to the next pending video if no errors occur.

**What changed:** Transcript retrieval initiated for `e2Z5eBVDrKM`.
