# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-142` (dept) · 2026-08-11T01:36:09.304749+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run kimtaeyoon83/mcp-server-youtube-transcript on a single test video to verify residential IP compliance.
2. Confirm tool output includes full, real transcripts/captions.
3. If compliant, proceed to process all 10 pending videos.
4. Store retrieved transcripts in a dedicated directory (e.g., `transcripts/pending/`).
5. Log tool version and IP source for audit.
6. Notify team upon completion with file paths.

**What changed:** Added single-video compliance test before bulk processing.
