# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-765` (dept) · 2026-07-14T19:54:20.862892+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the `kimtaeyoon83/mcp-server-youtube-transcript` tool for all pending videos to retrieve full transcripts/captions.
2. Ensure the tool is configured for residential IP usage to avoid rate-limiting or blocking.
3. Process transcripts in batches with gentle pacing to prevent server overload or detection.
4. Store retrieved transcripts in a structured format (e.g., JSON/CSV) with video metadata (ID, title, timestamp).
5. Validate transcripts for completeness and accuracy before marking videos as processed.
6. Log errors or missing transcripts for manual review or retry.

**What changed:** Tool execution is now explicitly scoped to pending videos with residential IP and pacing constraints.
