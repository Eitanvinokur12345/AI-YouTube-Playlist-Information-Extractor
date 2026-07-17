# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-342` (dept) · 2026-07-17T09:32:49.315370+00:00
> Participants: Reel, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Utilize the kimtaeyoon83/mcp-server-youtube-transcript tool to retrieve full transcripts for pending videos.  

**Plan:**  
1. Reel runs the kimtaeyoon83/mcp-server-youtube-transcript tool on each pending video ID.  
2. Save the returned full transcript as a .txt file in the /transcripts directory.  
3. Post a one-line confirmation in the room with the video ID and file path for the lead to verify.  

**What changed:** Agreement on the method and execution of retrieving transcripts.
