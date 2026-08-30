# Deliver: Keep the Designs tab pure: designs only, live previews, taste-ranked

> Decision artifact · room `war-deliver-keep-the-designs-tab-108` (war) · 2026-08-30T03:22:12.025283+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Cache all 200k clips’ Deepgram transcripts offline, then run the 14-day A/B test on cached transcripts only—no live stitching, no holdout risk.

**Plan:**
1. Pre-process all 200k clips’ transcripts offline using Deepgram (one-time cost).
2. Cache the transcripts in a high-performance key-value store (e.g., Redis) for O(1) lookup.
3. Serve live previews exclusively from the cache—no real-time Deepgram calls during the test.
4. Run the 14-day A/B test using only cached transcripts, ensuring zero latency or stitching risk.
5. Validate the A/B test results post-hoc against the holdout window’s freshness requirement.
6. Monitor cache hit rate and preemptively re-cache any missed clips to maintain purity.

**What changed:**
Pre-processing and caching replace live Deepgram stitching, eliminating real-time costs and latency while preserving Designs tab purity.
