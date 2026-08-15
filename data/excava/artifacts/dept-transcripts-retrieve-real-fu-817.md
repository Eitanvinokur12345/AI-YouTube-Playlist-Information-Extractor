# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-817` (dept) · 2026-08-15T16:54:35.459640+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch the full transcript for the pending video using the `kimtaeyoon83/mcp-server-youtube-transcript` tool.
2. Verify the transcript is complete and real (no summaries or AI-generated paraphrasing).
3. Save the transcript as a `.txt` or `.md` file in the designated repository.
4. Cross-check the transcript against the video’s captions (if available) for accuracy.
5. Upload the verified transcript to the pending video’s metadata or description.
6. Log the action in the project’s tracking system (e.g., GitHub issue or changelog).

**What changed:** Transcripts will now be fetched directly from the source tool instead of relying on summaries.
