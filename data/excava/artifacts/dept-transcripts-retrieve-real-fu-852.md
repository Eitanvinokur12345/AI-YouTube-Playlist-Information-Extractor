# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-852` (dept) · 2026-07-31T17:27:39.429226+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for *"How to Build a Resilient Team"*.
2. Ensure the request is made from a residential IP with gentle pacing to avoid rate limits or blocking.
3. Validate the retrieved transcript for completeness and accuracy before proceeding.
4. Save the transcript in GitHub markdown format with proper formatting (e.g., headers, timestamps).
5. Cross-check the transcript against the video to confirm no critical sections are missing.
6. Upload the finalized transcript to the designated repository or storage location.

**What changed:** Resolved to use the specified MCP server for direct transcript retrieval.
