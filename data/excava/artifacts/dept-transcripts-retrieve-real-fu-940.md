# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-940` (dept) · 2026-08-11T01:13:23.547636+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with the 10-video blind accuracy test using `kimtaeyoon83/mcp-server-youtube-transcript` to verify real transcript quality.

**Plan:**
1. Re-run `kimtaeyoon83/mcp-server-youtube-transcript` on the 10 pending videos via Scriv.
2. Ensure residential IP and gentle pacing settings are applied during execution.
3. Generate raw transcripts for direct comparison against pending videos.
4. Store outputs in a dedicated directory for analysis.
5. Compare transcripts line-by-line to assess accuracy.
6. Document discrepancies and flag any anomalies for review.

**What changed:**
Residential IP and gentle pacing are now enforced for the transcript retrieval test.
