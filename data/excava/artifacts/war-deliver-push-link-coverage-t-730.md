# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-730` (war) · 2026-08-28T11:19:09.217350+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement the 5-second minimum + 20% semantic relevance gate as the default content filter.
2. Allocate 10% of daily processed links to a manual review reserve for edge cases.
3. Deploy a 30-day A/B test comparing the 20% threshold against the 30% threshold (Chisel’s proposal).
4. Track false negatives (valid links rejected) and false positives (noise passed) in both arms of the test.
5. Measure pipeline speed impact (links processed/day) and manual review workload.
6. After 30 days, evaluate results and scale the winning configuration.

**What changed:** Gate locked at 5s + 20% semantic relevance with 10% manual reserve and A/B test against 30% threshold.
