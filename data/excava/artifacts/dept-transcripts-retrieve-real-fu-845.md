# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-845` (dept) · 2026-07-31T04:58:38.708323+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full transcript for *"How to Build a Resilient Team"*.
2. Save the transcript as a `.txt` file in the designated repository.
3. Verify the transcript’s completeness and accuracy by cross-checking against the video.
4. Push the file to the remote repository with a clear commit message (e.g., "Add full transcript for 'How to Build a Resilient Team'").
5. Notify the team via Slack/email that the transcript is ready for review.
6. Archive the tool’s output logs for future reference.

**What changed:** Transcript retrieval is now automated via the MCP server tool.
