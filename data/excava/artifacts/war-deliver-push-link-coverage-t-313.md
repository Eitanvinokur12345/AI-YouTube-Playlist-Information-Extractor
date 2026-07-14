# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-313` (war) · 2026-07-14T01:23:30.738506+00:00
> Participants: Echo, Reel, Scriv, Chisel, Sift, Scope · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Adopt the $50/$3% threshold for link coverage with the override rule to prioritize high-impact links by cost and confidence without manual effort.
**Plan:**
1. Implement the $50/$3% threshold to auto-prioritize high-impact links by cost and confidence.
2. Introduce an override rule to ensure links with confidence just above the threshold are not overlooked.
3. Set a $50 per-link cap with a $500 absolute override to control costs.
4. Monitor the link coverage progress to ensure the +5%/day gate is met.
5. Accept and mitigate the trade-off of potential false positives under the $50/$3% threshold.
**What changed:** The decision to prioritize high-impact links using the $50/$3% threshold with an override rule, abandoning stake-weighted confidence drop thresholds and tiered systems.
