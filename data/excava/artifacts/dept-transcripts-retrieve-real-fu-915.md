# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-915` (dept) · 2026-07-30T17:55:07.984003+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Fetch full transcripts for pending videos using YouTube’s auto-generated captions via the kimtaeyoon83/mcp-server-youtube-transcript tool, then verify completeness.

**Plan:**
1. Use kimtaeyoon83/mcp-server-youtube-transcript to fetch raw transcripts (with timestamps/speaker labels) for all pending videos.
2. Save each transcript as a `.txt` file in the designated repository folder.
3. Manually review each transcript for gaps, errors, or missing segments.
4. If incomplete, retry fetching with adjusted parameters (e.g., language code, segment length).
5. Flag videos with persistent missing transcripts for manual review or alternative methods.
6. Log results (success/failure) in a tracking sheet.

**What changed:**
Action shifted from debate to execution—prioritizing tool-based retrieval with verification over speculative alternatives.
