# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-276` (war) · 2026-08-19T00:56:37.286937+00:00
> Participants: Echo, Reel, Scriv, Chisel, Sift, Scope · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a **pre-commit gate** requiring contributors to fix and sign off on their own links tied to the next artifact stage before a **48-hour auto-apply checkpoint**.
2. Enforce the gate via an **artifact-locked checkpoint**: if links aren’t fixed within 48 hours, the stage fails and rolls back.
3. Publish a **public leaderboard** tracking daily link-coverage progress (5%/day target) to drive urgency and visibility.
4. Restrict counted links to those **directly unlocking the next artifact stage**, verified by contributor sign-off (no neutral review).
5. Auto-apply fixes after the 48-hour window to prevent retroactive gaming or blame-shifting.
6. Include a **retrospective trigger**: if coverage stalls below 90% for 3 consecutive days, escalate to a neutral review for critical gaps.

**What changed:** Switched from neutral review to pre-commit contributor sign-off with 48-hour auto-apply to balance speed and accountability.
