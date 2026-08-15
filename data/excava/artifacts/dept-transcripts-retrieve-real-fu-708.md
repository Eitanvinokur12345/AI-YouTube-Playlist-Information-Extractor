# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-708` (dept) · 2026-08-15T13:12:06.804741+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch the full transcript for the pending video using the kimtaeyoon83/mcp-server-youtube-transcript MCP server via mseep.ai/app/kimtaeyoon83-mcp-server-youtube-trans.
2. Verify the transcript is complete and matches the video’s content.
3. Save the transcript in a structured format (e.g., `.txt` or `.md`) for review.
4. Cross-check the transcript against the video’s captions for accuracy.
5. If discrepancies are found, re-run the fetch with adjusted parameters (e.g., slower pacing, residential IP).
6. Archive the final transcript in a designated repository for pending videos.

**What changed:** Decision to proceed with the MCP server method for transcript retrieval.
