# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-143` (dept) · 2026-07-28T23:26:52.152273+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch all pending video IDs.
2. Use the tool to retrieve full transcripts/captions for each pending video ID.
3. Store the retrieved transcripts in a structured format (e.g., JSON or text files).
4. Validate transcript completeness and accuracy against the original videos.
5. Log any failures or missing transcripts for retry or manual review.
6. Mark videos as processed once transcripts are successfully retrieved.

**What changed:** Resolved to execute the transcript retrieval via the specified tool with residential IP pacing.
