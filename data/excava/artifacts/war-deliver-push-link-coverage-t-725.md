# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-725` (war) · 2026-07-12T12:10:27.827093+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Audit the access gate first, but run a 5-minute smoke test to confirm its links are missing before committing—if stable, pivot immediately to auditing the *least-covered* pages to maximize coverage gains.

**Plan:**
1. Run a 5-minute smoke test on the access gate to verify if its links are missing or incomplete.
2. If links are missing, prioritize auditing and fixing the access gate’s coverage immediately.
3. If links are stable, pivot to auditing the *least-covered* pages first to maximize coverage gains.
4. For high-traffic pages, allocate 20% of audit time to quick fixes (e.g., adding missing links).
5. Track daily progress toward +5% coverage, adjusting focus based on real-time data.
6. Reassess blocker status of the access gate after 48 hours or if coverage stalls.

**What changed:** Added a 5-minute smoke test to validate the access gate’s link status before committing resources, ensuring no time is wasted on stable pages.
