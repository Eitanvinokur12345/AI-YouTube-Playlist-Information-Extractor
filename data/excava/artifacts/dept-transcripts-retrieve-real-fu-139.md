# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-139` (dept) · 2026-07-31T14:08:18.189231+00:00
> Participants: Reel · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Retrieve full transcripts for pending videos using the YouTube transcript server.
**Plan:**
1. Identify pending videos with residential IP and gentle pacing.
2. Extract YouTube URLs for the identified pending videos.
3. Query the YouTube transcript server (`kimtaeyoon83/mcp-server-youtube-transcript`) using the extracted YouTube URLs.
4. Retrieve and store the full transcripts/captions for each pending video.
5. Review the retrieved transcripts for quality and accuracy.
**What changed:** The approach to retrieving transcripts shifted to utilizing the YouTube transcript server for efficient and accurate transcript retrieval.
