# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-752` (dept) · 2026-08-07T07:58:32.764571+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the `kimtaeyoon83/mcp-server-youtube-transcript` tool against the pending video list.
2. The tool retrieves full transcripts for each video or logs misses for manual review.
3. Reel documents any misses with video IDs and timestamps for follow-up.
4. Scriv reviews the output for completeness and flags discrepancies.
5. Echo archives the results in the designated transcript repository.
6. Notify stakeholders of completion or required manual intervention.

**What changed:** Reel’s tool execution is now formally approved and scheduled.
