# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-757` (dept) · 2026-07-31T22:37:26.925184+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full YouTube transcript for *"The Science of Sleep Optimization"*.
2. Save the transcript as a clean, full-length file (e.g., `.txt` or `.md`) for review.
3. Verify the transcript’s accuracy and completeness against the video.
4. Store the transcript in a designated directory (e.g., `transcripts/`).
5. Tag the transcript with metadata (e.g., video title, date fetched, source URL).
6. Notify the team via GitHub issue or Slack for review.

**What changed:** Transcript retrieval is now automated via the MCP server.
