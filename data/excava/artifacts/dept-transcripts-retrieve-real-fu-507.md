# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-507` (dept) · 2026-07-17T15:58:39.158946+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Execute the kimtaeyoon83/mcp-server-youtube-transcript tool on the first pending video to fetch its full transcript.
2. Store the timestamped, module-level transcript in a designated repository folder (e.g., `transcripts/pending/`).
3. Notify Product Ops via GitHub issue or Slack for mandatory review.
4. Log the action in the project tracker (e.g., Jira/Notion) with the video ID and timestamp.
5. Archive the transcript in a structured format (e.g., JSON) for future reference.
6. Proceed to the next pending video upon completion.

**What changed:** Automated transcript retrieval initiated for the first pending video.
