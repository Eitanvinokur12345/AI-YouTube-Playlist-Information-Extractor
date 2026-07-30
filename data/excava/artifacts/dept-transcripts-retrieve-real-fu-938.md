# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-938` (dept) · 2026-07-30T20:16:26.770257+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with fetching the full transcript for *"How to Build a Resilient Team"* using the specified tool.

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full transcript for video ID `dQw4w9WgXcQ`.
2. Verify the transcript is complete (no missing segments) and matches the video’s spoken content.
3. If complete, save the transcript to a local file (e.g., `resilient_team_transcript.txt`).
4. Cross-check with YouTube’s auto-generated captions for discrepancies (if needed).
5. Confirm success by logging the transcript’s length and timestamp.
6. Notify the user of completion with a direct link to the saved file.

**What changed:** Tool selection and verification steps were formalized to ensure transcript accuracy.
