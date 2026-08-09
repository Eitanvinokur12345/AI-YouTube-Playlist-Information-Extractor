# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-829` (dept) · 2026-08-08T09:13:22.307726+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Echo authorizes retrieval of full YouTube transcripts for pending videos.

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on all pending videos.
2. Tool fetches verified, full captions for each video.
3. Captions are stored in a structured format (e.g., JSON per video).
4. Validate transcripts for completeness (no truncation, accurate timestamps).
5. Log failures/partial results for manual review.
6. Notify Scriv upon completion with summary of retrieved transcripts.

**What changed:** Tool-based transcript retrieval replaces partial/placeholder captions.
