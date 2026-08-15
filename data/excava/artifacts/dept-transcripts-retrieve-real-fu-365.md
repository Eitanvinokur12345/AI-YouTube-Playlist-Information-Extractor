# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-365` (dept) · 2026-08-15T10:52:01.713810+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full transcript for the pending video with ID "UCX6OQ3Dk1IWZT_X8Zz5Y4Zg".
2. Save the retrieved transcript as a complete, real transcript file (e.g., `.txt` or `.json`).
3. Verify the transcript contains no placeholders or partial data (e.g., "[Music]" or "[Applause]").
4. Upload the transcript to the designated repository or storage location.
5. Mark the video as "transcript retrieved" in the tracking system.
6. Notify the team of completion via the agreed-upon channel.

**What changed:** Transcript retrieval is now automated via the MCP server, replacing manual or partial methods.
