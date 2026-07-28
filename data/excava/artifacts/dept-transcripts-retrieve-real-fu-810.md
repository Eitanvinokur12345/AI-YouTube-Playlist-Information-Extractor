# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-810` (dept) · 2026-07-28T23:33:25.571314+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch REAL full transcripts/captions for all pending video IDs.
2. Compile the retrieved transcripts into a structured format for lead review.
3. Validate transcripts for accuracy and completeness against the pending video IDs.
4. Store transcripts in the designated repository with clear metadata (video ID, timestamp, source).
5. Notify leads via GitHub issue or Slack with a summary of processed transcripts.
6. Log the action in the audit trail for compliance tracking.

**What changed:** Residential IP query executed to retrieve real transcripts for pending videos.
