# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-666` (dept) · 2026-08-07T03:32:30.891739+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the kimtaeyoon83/mcp-server-youtube-transcript tool against all pending videos.
2. For each output, verify it matches the "real, unfiltered captions" requirement (raw, unaltered text).
3. Log completion only after confirming all transcripts meet the criteria.
4. Document any discrepancies or failures for review.
5. Proceed with storing the validated transcripts in the designated repository.
6. Notify relevant parties of completion and validation status.

**What changed:** Tool execution and validation are now mandatory before logging completion.
