# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-846` (dept) · 2026-07-31T04:08:22.113364+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full transcript for *"How to Build a Resilient Team"*.
2. Verify the output contains the complete, unedited text (no truncation or omissions).
3. Save the transcript as a `.txt` file with the naming convention: `How_to_Build_a_Resilient_Team_Transcript_[YYYYMMDD].txt`.
4. Cross-check the transcript against the video duration to ensure no gaps.
5. Upload the verified transcript to the designated repository (e.g., GitHub/GitLab) under `/transcripts/pending/`.
6. Notify the team via Slack/email with the file path and verification status.

**What changed:** Decision formalized with a structured, executable plan.
