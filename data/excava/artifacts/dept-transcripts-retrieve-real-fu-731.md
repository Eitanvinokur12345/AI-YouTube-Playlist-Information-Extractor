# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-731` (dept) · 2026-08-09T22:12:14.618694+00:00
> Participants: Reel, Scriv, Echo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement the use of kimtaeyoon83/mcp-server-youtube-transcript to retrieve real full transcripts for pending videos.
**Plan:**
1. Reel runs kimtaeyoon83/mcp-server-youtube-transcript on every pending video.
2. The script retrieves real full transcripts/captions for each video.
3. Reel delivers the retrieved transcripts to Scriv for verification.
4. Scriv verifies the accuracy and completeness of the transcripts.
5. Verified transcripts are then used for further processing or analysis.
**What changed:** The method for retrieving real full transcripts for pending videos was finalized using kimtaeyoon83/mcp-server-youtube-transcript.
