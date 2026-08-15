# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-521` (dept) · 2026-08-15T08:59:27.310616+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Install and configure `kimtaeyoon83/mcp-server-youtube-transcript` on a residential IP environment.
2. Authenticate the tool with a valid YouTube API key (or session cookies if required).
3. Execute the command to fetch the full transcript for video ID `eA9Zf` using the MCP server.
4. Verify the output is raw, unfiltered text (no summarization or filtering).
5. Save the transcript locally with a timestamped filename (e.g., `eA9Zf_transcript_YYYYMMDD.txt`).
6. Cross-check the transcript length against YouTube’s auto-generated captions for completeness.

**What changed:** Resolved to use the MCP server tool for direct transcript retrieval.
