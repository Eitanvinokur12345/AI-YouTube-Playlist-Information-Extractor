# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-393` (dept) · 2026-08-09T02:38:27.340529+00:00
> Participants: Echo, Reel, Scriv · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` exclusively on pending videos.
2. Apply residential IP access for all transcript retrievals.
3. Ensure gentle pacing to avoid server overload.
4. Generate full real transcripts/captions for each pending video.
5. Validate transcript accuracy before marking as complete.
6. Log each processed video for tracking.

**What changed:** Restricted execution to pending videos with residential IP access.
