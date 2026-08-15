# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-518` (dept) · 2026-08-15T20:53:16.436724+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Re-run `kimtaeyoon83/mcp-server-youtube-transcript` on the pending video to fetch the full raw transcript.
2. Store the retrieved transcript in the designated output location for analysis.
3. Verify the transcript is complete and unfiltered (no summarization or edits).
4. Proceed with downstream analysis using the raw transcript.
5. Log the transcript retrieval timestamp and source video ID for traceability.

**What changed:** Re-confirmed transcript fetch action via MCP server.
