# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-759` (dept) · 2026-07-28T03:49:56.318945+00:00
> Participants: Reel, Echo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Retrieve full transcripts/captions for pending videos using the kimtaeyoon83/mcp-server-youtube-transcript tool with a verification step.
**Plan:**
1. Query the YouTube transcript server for the pending video IDs using the kimtaeyoon83/mcp-server-youtube-transcript tool.
2. Retrieve the full transcripts/captions for each video from the query results.
3. Re-check the query results to ensure all transcripts are successfully retrieved.
4. Verify the completeness and accuracy of the retrieved transcripts.
5. Declare any videos as missing transcripts only after the re-check and verification steps.
**What changed:** Added a verification step to re-check query results for pending video IDs to ensure all transcripts are successfully retrieved.
