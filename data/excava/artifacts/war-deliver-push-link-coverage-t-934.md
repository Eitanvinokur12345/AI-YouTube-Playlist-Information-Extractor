# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-934` (war) · 2026-07-13T18:18:58.454483+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Set a $50 per-link cap with a $500 absolute override—any link under $500 gets fixed if it blocks a critical path, but routine spending is capped at $50 to avoid waste.

**Plan:**
1. Implement a $50 per-link spending cap for routine link fixes.
2. Add a $500 absolute override threshold for critical path links.
3. Automate triage to flag links blocking critical paths for override review.
4. Track daily coverage growth (+5%/day) and override usage.
5. Reassess thresholds weekly based on coverage velocity and bus task impact.
6. Document override decisions for auditability.

**What changed:** Override threshold increased from 1% to $500 absolute.
