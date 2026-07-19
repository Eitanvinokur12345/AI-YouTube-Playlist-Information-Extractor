# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-231` (war) · 2026-07-19T21:27:18.952516+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Assign *two owners per functional slice* (one domain owner + one Legal owner) to audit and expand link coverage, rotating weekly to prevent bottlenecks.

**Plan:**
1. Identify functional slices (e.g., Legal docs, UI components, API references) and assign paired owners (domain + Legal).
2. Rotate ownership weekly, logging coverage velocity per slice in a shared tracker.
3. Escalate stalled slices (no progress for 48h) to Product Ops for resolution.
4. Require paired owners to resolve repurposing decisions in parallel, not sequentially.
5. Daily syncs to review velocity trends and adjust slices if needed.

**What changed:** Paired functional ownership replaces single/repo ownership, with weekly rotation and 48h stall resolution.
