# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-107` (dept) · 2026-07-14T17:44:20.207769+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the `kimtaeyoon83/mcp-server-youtube-transcript` tool for all pending videos to retrieve their raw, unaltered transcripts.
2. Verify each transcript fetch twice (cross-check content and metadata).
3. Mark each video’s transcript as complete only after successful verification.
4. Store the verified transcripts in the designated output directory.
5. Log any failures or discrepancies for manual review.
6. Notify the user upon completion of all pending transcripts.

**What changed:** Tool execution and verification steps are now explicitly defined and ordered.
