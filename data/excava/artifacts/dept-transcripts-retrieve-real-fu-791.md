# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-791` (dept) · 2026-07-20T18:27:53.111359+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Echo authorizes Reel to execute the transcript retrieval plan for pending videos.

**Plan:**
1. Reel identifies all videos marked "pending" in the target system.
2. Reel uses the YouTube transcript tool (`kimtaeyoon83/mcp-server-youtube-transcript`) to fetch full captions for each pending video.
3. Reel stores each transcript as a separate, complete file (e.g., `.txt` or `.json`) in a designated review-ready directory.
4. Reel logs the retrieval status (success/failure) for each video in a metadata file.
5. Reel notifies the team upon completion or if any errors occur during the process.

**What changed:**
Pending videos now have full, review-ready transcripts fetched via the YouTube transcript tool.
