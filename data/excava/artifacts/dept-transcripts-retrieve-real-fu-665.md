# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-665` (dept) · 2026-07-31T22:22:32.789774+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Execute the transcript retrieval plan for pending videos using the kimtaeyoon83/mcp-server-youtube-transcript tool via residential IP.

**Plan:**
1. Identify pending video IDs (e.g., "dQw4w9WgXcQ") and titles (e.g., *"The Future of AI in Healthcare"*).
2. Use the kimtaeyoon83/mcp-server-youtube-transcript tool via residential IP to query each video’s full transcript.
3. Validate output for completeness and accuracy (e.g., no missing segments, correct formatting).
4. Save retrieved transcripts as `.srt` or `.txt` files with video ID as filename.
5. Confirm accessibility (e.g., no rate limits, no IP blocks) and log timestamps for tracking.
6. Notify stakeholders (e.g., Reel) upon completion of all pending videos.

**What changed:**
Clarified actionable steps and output format for transcript retrieval.
