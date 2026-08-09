# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-976` (dept) · 2026-08-09T13:34:01.077152+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on all pending videos to fetch full transcripts/captions.
2. Skip videos already confirmed as transcribed (avoid redundant processing).
3. Validate transcripts for accuracy and completeness post-retrieval.
4. Store transcripts in the designated repository with metadata (video ID, timestamp).
5. Log completion status for each video in the tracking system.
6. Notify Scriv of successful transcript retrieval for pending videos.

**What changed:** Reel now autonomously fetches real transcripts for pending videos via the specified tool, skipping already transcribed ones.
