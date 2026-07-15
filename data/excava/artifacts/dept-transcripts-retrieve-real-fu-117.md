# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-117` (dept) · 2026-07-15T03:47:05.290835+00:00
> Participants: Reel, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Retrieve real full transcripts for pending videos using the kimtaeyoon83/mcp-server-youtube-transcript tool.

**Plan:**  
1. Query the kimtaeyoon83/mcp-server-youtube-transcript tool for the pending video IDs with visibility checks.  
2. Implement a 5-minute rolling cache to track "last modified" timestamps for each video.  
3. Retrieve the full transcript/captions for video ID "UC-9bX9X8".  
4. Verify the output to ensure it contains real text and not placeholders.  
5. Repeat the process for the next pending videos based on the results of the previous queries.  

**What changed:** The focus shifted towards a systematic approach for retrieving complete transcripts, including verification steps.
