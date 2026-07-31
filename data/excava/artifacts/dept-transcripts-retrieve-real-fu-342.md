# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-342` (dept) · 2026-07-31T11:36:49.558921+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full YouTube transcript for *"How to Build a Resilient Team"*.
2. Validate the transcript exists and is complete (e.g., check length, no missing segments).
3. Save the transcript locally with a timestamped filename (e.g., `resilient_team_transcript_YYYYMMDD.txt`).
4. Verify the file is readable and matches the video’s content (e.g., compare key timestamps).
5. Upload the transcript to the designated repository or system for pending videos.
6. Confirm completion via GitHub issue/PR or direct message to stakeholders.

**What changed:** Transcript retrieval is now automated via MCP server, replacing manual methods.
