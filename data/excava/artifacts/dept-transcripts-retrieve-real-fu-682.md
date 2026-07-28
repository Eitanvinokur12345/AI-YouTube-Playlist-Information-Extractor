# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-682` (dept) · 2026-07-28T17:55:46.245064+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch all pending video IDs requiring full transcripts.
2. For each pending video ID, request real full transcripts/captions from the YouTube transcript server.
3. Validate transcripts for completeness and accuracy before marking as processed.
4. Store retrieved transcripts in a structured format (e.g., JSON/CSV) with video ID references.
5. Log errors or missing transcripts for retry or manual review.
6. Update the pending video list to reflect completed transcript retrievals.

**What changed:** Resolved to execute the transcript retrieval plan using the specified tool and residential IP.
