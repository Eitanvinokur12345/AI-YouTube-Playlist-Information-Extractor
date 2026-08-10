# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-620` (dept) · 2026-08-10T21:50:34.700496+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run `kimtaeyoon83/mcp-server-youtube-transcript` on all pending videos to extract full real transcripts/captions.
2. Store transcripts in the designated repository under `/transcripts/` with filenames matching video IDs.
3. Validate transcript completeness against video duration (allow ±2s tolerance).
4. Log errors for videos where transcripts fail or are incomplete.
5. Notify Reel upon completion via GitHub issue with summary of processed/failed videos.
6. Archive raw transcripts in a timestamped folder for backup.

**What changed:** All pending videos will now have verified full transcripts/captions generated via automated pipeline.
