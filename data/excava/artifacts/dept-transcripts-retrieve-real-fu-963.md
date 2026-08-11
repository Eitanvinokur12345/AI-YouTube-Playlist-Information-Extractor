# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-963` (dept) · 2026-08-11T01:02:19.613476+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Scriv runs `kimtaeyoon83/mcp-server-youtube-transcript` on 10 pending videos to extract full transcripts/captions.
2. Measure raw error rate from the transcripts to validate accuracy against the under 5% threshold.
3. Document the error rate data in a structured format for review.
4. Compare results with prior benchmarks or tool performance history.
5. If error rate meets the threshold, proceed with transcript integration; otherwise, investigate and iterate.
6. Update mission logs with findings and next steps.

**What changed:** Replaced vague instruction with a precise 10-video test using the specified tool to measure raw error rate.
