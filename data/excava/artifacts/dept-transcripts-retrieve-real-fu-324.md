# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-324` (dept) · 2026-07-12T12:36:18.262886+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` as the primary tool to fetch transcripts directly from YouTube’s captions API for all pending videos.
2. For each video, immediately cross-verify the transcript using `yt-dlp` with auto-subtitles as a secondary source.
3. If the primary transcript is missing, incomplete, or older than a year, default to the `yt-dlp` auto-subtitles as the authoritative source.
4. Log discrepancies between sources (e.g., missing lines, timestamps) and flag videos for manual review if needed.
5. Store only the verified, complete transcript in the final output, ensuring no data loss from API limitations.
6. Process videos in batches to monitor YouTube’s API throttling and adjust pacing if required.

**What changed:** Added mandatory secondary verification to ensure transcripts are real and complete, mitigating risks of missing captions.
