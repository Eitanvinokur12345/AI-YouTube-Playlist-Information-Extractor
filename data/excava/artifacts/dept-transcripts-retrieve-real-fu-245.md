# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-245` (dept) · 2026-07-30T17:41:11.612804+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full auto-generated captions for the pending video.
2. Store the raw transcript output as a text artifact (e.g., `.txt` file) in the designated repository for lead review.
3. Verify the transcript’s completeness and accuracy against the video’s content.
4. If gaps or errors are found, manually supplement with additional caption sources (e.g., third-party tools or manual transcription).
5. Flag any discrepancies for lead review before finalizing the transcript.
6. Archive the raw transcript and any supplementary files in the project’s documentation.

**What changed:** Tool-based auto-captions will be prioritized, with manual review for quality assurance.
