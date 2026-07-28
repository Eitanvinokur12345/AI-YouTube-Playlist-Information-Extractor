# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-474` (dept) · 2026-07-28T12:58:23.594276+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP for each pending video ID.
2. Apply gentle pacing to retrieve full transcripts/captions.
3. Verify transcript completeness before marking as done.
4. Store raw captions in the transcript tracker.
5. Repeat for all pending video IDs.

**What changed:** No changes; plan aligns with debate.
