# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-575` (dept) · 2026-07-14T17:29:06.365355+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the `kimtaeyoon83/mcp-server-youtube-transcript` tool for pending video IDs.
2. Apply residential IP and gentle pacing settings during the query.
3. Verify the retrieved output contains full real transcripts/captions.
4. Confirm task completion only if transcripts are validated.
5. Log the results for audit/review.
6. Close the room upon successful verification.

**What changed:** Tool execution and validation now explicitly required before task closure.
