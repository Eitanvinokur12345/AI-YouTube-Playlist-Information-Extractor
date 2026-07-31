# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-311` (dept) · 2026-07-31T13:40:42.399755+00:00
> Participants: Reel · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Retrieve full transcripts/captions for pending videos using the YouTube transcript server.
**Plan:**
1. Identify the video ID of the pending video.
2. Query the YouTube transcript server (`kimtaeyoon83/mcp-server-youtube-transcript`) using the video ID.
3. Retrieve the full transcript/captions from the server response.
4. Review the retrieved transcript/captions for accuracy and completeness.
5. Store the retrieved transcript/captions for further processing or reference.
**What changed:** The approach to retrieving transcripts/captions shifted to utilizing the YouTube transcript server for more accurate and complete results.
