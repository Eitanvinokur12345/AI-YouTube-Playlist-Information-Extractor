# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-136` (dept) · 2026-08-11T11:23:30.153809+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Re-run `kimtaeyoon83/mcp-server-youtube-transcript` on all 10 pending videos.
2. Validate that the JSON output includes full content (timestamp, speaker ID, and text) for each video.
3. Confirm transcripts exist for all videos before marking completion.
4. If transcripts are incomplete, switch to a dedicated transcript-fetching tool per Scriv’s suggestion.
5. Log discrepancies in a `transcript-issues.md` file for review.

**What changed:** Reaffirmed tool usage but added validation steps to ensure full transcript extraction.
