# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-343` (dept) · 2026-07-30T21:47:17.374132+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to query YouTube’s transcript server.
2. Specify the video title *"Orchestrated AI"* and enforce residential IP routing.
3. Retrieve the full, raw transcript file (no summarization or filtering).
4. Deliver the raw transcript directly to the lead for review.
5. Confirm completion with a status update (e.g., file size, integrity check).
6. Archive the transcript in the designated repository for audit.

**What changed:** Resolved to execute the query via residential IP with no intermediate processing.
