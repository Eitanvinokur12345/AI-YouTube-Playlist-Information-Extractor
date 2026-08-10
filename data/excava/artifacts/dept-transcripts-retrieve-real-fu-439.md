# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-439` (dept) · 2026-08-10T08:16:40.284350+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with fetching real full transcripts for all pending videos.

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on every pending video.
2. For each video, Reel verifies the transcript is fully retrieved (real captions, not auto-generated).
3. Reel confirms transcript existence by cross-checking against video metadata (title, duration, etc.).
4. Upon confirmation, Reel marks the task complete for each video.
5. Reel logs any failures (e.g., missing transcripts) for manual review.
6. Scriv reviews logs weekly to audit transcript quality and tool performance.

**What changed:** Action shifted from debate to execution—Reel now autonomously fetches and validates transcripts for all pending videos.
