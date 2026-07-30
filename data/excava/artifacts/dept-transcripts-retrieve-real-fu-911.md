# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-911` (dept) · 2026-07-30T23:51:14.047330+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full verbatim transcript for *"How to Build a Resilient Team"*.
2. Validate the transcript for completeness and accuracy (no summaries, no edits).
3. Save the raw transcript to a dedicated file (e.g., `transcript_how_to_build_a_resilient_team.txt`) in the repository.
4. Cross-check the video ID and title to ensure the correct source is transcribed.
5. Log the action in the project’s activity log with timestamp and tool used.
6. Notify the team via the designated channel (e.g., Slack) with a link to the transcript file.

**What changed:** Transcript retrieval is now automated via the specified tool, replacing manual or partial methods.
