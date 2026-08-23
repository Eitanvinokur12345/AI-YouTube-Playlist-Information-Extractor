# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-531` (war) · 2026-08-23T16:55:21.545855+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Run Kaedim first on the full set, then manually audit only the top 20% highest-confidence links—if error rate exceeds 5%, switch to parallel testing.

**Plan:**
1. Batch-process all unlinked items through Kaedim’s AI to auto-generate video links.
2. Extract the top 20% highest-confidence links based on Kaedim’s confidence scores.
3. Manually verify the top 20% for accuracy; flag any errors.
4. If error rate >5%, halt and switch to parallel testing (both matcher + Kaedim).
5. For verified links, push to production and update coverage metrics.
6. Log all decisions and error rates for audit trail.

**What changed:**
Kaedim-first with targeted manual audit replaced the parallel-testing fallback.
