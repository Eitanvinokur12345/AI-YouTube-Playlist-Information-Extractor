# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-260` (war) · 2026-07-26T01:30:20.415011+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Adopt **pre-approved model thresholds** set jointly by Engineering and Data Protection for all models.
2. Require **joint Engineering and Data Protection approval** for any override, with documented justification.
3. Implement a **rolling daily validation loop** that spot-checks overrides against fresh data.
4. **Immediately review** any model if thresholds are breached during validation.
5. **Log all overrides** and analyze spikes to inform threshold adjustments.
6. **Fast-track high-risk models** via Scriv’s override but enforce Data Protection’s Arcads AI Video validation.

**What changed:** Overrides now require joint approval and daily validation, replacing loose valves with structured oversight.
