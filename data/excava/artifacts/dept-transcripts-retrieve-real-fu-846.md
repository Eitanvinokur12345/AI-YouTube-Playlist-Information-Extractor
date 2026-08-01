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
> Decision artifact · room `dept-transcripts-retrieve-real-fu-846` (dept) · 2026-07-31T01:25:22.996423+00:00
> Participants: Reel, Echo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full transcript for *"How to Build a Resilient Team"*.
**Plan:**
1. Reel will utilize the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the transcript.
2. The fetched transcript will be verified for completeness and accuracy.
3. The output will be checked to ensure it contains the real, full transcript of the video.
4. Once verified, the transcript will be marked as retrieved and complete.
5. The process will be repeated for any remaining pending videos.
**What changed:** The approach to fetching transcripts now includes a verification step to ensure accuracy and completeness.
