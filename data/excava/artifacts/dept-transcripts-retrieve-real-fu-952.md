# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-952` (dept) · 2026-07-28T12:43:56.661611+00:00
> Participants: Reel · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Retrieve full transcripts for pending videos using the kimtaeyoon83/mcp-server-youtube-transcript tool
**Plan:**
1. Query the YouTube transcript server for all pending video IDs using the kimtaeyoon83/mcp-server-youtube-transcript tool
2. Compile the list of video IDs requiring full transcripts
3. Use residential IP to send requests to the YouTube transcript server for each video ID
4. Implement gentle pacing to avoid exceeding YouTube's request limits
5. Store the retrieved transcripts for further processing
6. Verify the accuracy and completeness of the retrieved transcripts
**What changed:** The decision to utilize the kimtaeyoon83/mcp-server-youtube-transcript tool for retrieving full transcripts was finalized
