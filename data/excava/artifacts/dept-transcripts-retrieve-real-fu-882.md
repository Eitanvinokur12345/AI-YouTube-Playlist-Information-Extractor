# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-882` (dept) · 2026-07-31T00:27:06.948831+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch the full transcript for *"How to Build a Resilient Team"* via `kimtaeyoon83/mcp-server-youtube-transcript`.
2. Verify the fetched text matches the video’s captions.
3. Return the raw transcript as-is.
4. Fetch the full transcript for *"How AI Will Change Your Job in 2025"* using the YouTube transcript tool.
5. Verify the fetched text matches the video’s captions.
6. Return the raw transcript as-is.

**What changed:** Resolved conflicting video titles by prioritizing both requests sequentially.
