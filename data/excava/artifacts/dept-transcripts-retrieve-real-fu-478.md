# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-478` (dept) · 2026-07-30T19:18:23.186387+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for *"How to Build a Resilient Team"*.
2. Verify the transcript contains real, complete content (no placeholders or partial data).
3. If valid, store the transcript in a structured format (e.g., JSON or plain text).
4. Cross-check the transcript against the video’s metadata (title, duration) for consistency.
5. If discrepancies are found, flag the transcript for manual review.
6. Report back with the final transcript and validation status.

**What changed:** Resolved to proceed with direct transcript retrieval via the specified tool.
