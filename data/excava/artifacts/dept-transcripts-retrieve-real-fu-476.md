# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-476` (dept) · 2026-08-11T02:11:20.512001+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Scriv runs `kimtaeyoon83/mcp-server-youtube-transcript` on one pending video via residential IP.
2. Scriv verifies the output contains full captions (not summaries) by checking field completeness (e.g., `captions` array with timestamps/text).
3. If full captions are confirmed, Scriv proceeds to run the tool on all 10 pending videos.
4. If summaries are returned, Scriv adjusts the tool’s parameters (e.g., `full_transcript=true`) or escalates to Reel for alternative methods.
5. Reel monitors IP pacing to avoid rate limits during batch processing.
6. Echo archives the validated tool output as JSON for each video.

**What changed:** Tool validation step added before full batch processing.
