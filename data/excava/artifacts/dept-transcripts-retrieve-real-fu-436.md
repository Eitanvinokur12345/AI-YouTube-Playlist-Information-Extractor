# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-436` (dept) · 2026-07-14T21:33:49.585842+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to query transcripts for all pending videos.
2. Apply residential IP routing for the requests.
3. Set gentle pacing (e.g., rate limits) to avoid detection or throttling.
4. Extract and store the full transcripts/captions in a structured format (e.g., JSON or text files).
5. Verify the completeness and accuracy of the retrieved transcripts.
6. Log the results (success/failure) for each video for tracking.

**What changed:** Resolved to execute the transcript retrieval with residential IP and gentle pacing via the specified tool.
