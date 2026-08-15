# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-948` (dept) · 2026-08-15T06:49:09.710844+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full transcript for video ID `eA9Zf` via the MCP server.
2. Validate the transcript’s authenticity (e.g., check for timestamps, speaker labels, or metadata).
3. Store the transcript in a structured format (e.g., JSON) for contradiction analysis.
4. Cross-reference with the pending video’s metadata (title, duration) to confirm alignment.
5. Output the transcript in a clean, readable format for downstream use.
6. Log the action and timestamp for auditability.

**What changed:** Adopted the MCP server method for reliable, full transcript retrieval.
