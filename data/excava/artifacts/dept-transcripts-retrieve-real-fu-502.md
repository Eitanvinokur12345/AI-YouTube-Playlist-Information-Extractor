# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-502` (dept) · 2026-07-12T12:17:13.883286+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Pull the first transcript using kimtaeyoon83/mcp-server-youtube-transcript on a single test video to confirm real captions exist, then decide next steps based on the outcome.

**Plan:**
1. Select a pending video with confirmed captions (e.g., ID `dQw4w9WgXcQ`).
2. Use `kimtaeyoon83/mcp-server-youtube-transcript` to fetch its full transcript via YouTube’s captions API.
3. Verify the transcript is clean, complete, and matches YouTube’s displayed captions.
4. If successful, log the transcript locally with a timestamp and video ID for caching.
5. If throttled/blocked, retry once with a 30-second delay; if persistent, switch to metadata check first.
6. Document the outcome (success/failure) and adjust the pipeline accordingly.

**What changed:** Prioritized immediate API test over local caching to validate caption authenticity before scaling.
