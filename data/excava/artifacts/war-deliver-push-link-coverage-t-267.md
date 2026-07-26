# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-267` (war) · 2026-07-26T01:53:08.465433+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Require *three* sign-offs for Data Protection overrides—CEO, DPO, and one rotating non-executive reviewer—to neutralize override loops.

**Plan:**
1. Define the rotating non-executive reviewer role (e.g., board member or independent advisor) with a 30-day rotation cycle.
2. Implement a mandatory 24-hour cooldown period between override requests and approvals to prevent rushed decisions.
3. Require all override rationale to be documented in a shared log with timestamped entries.
4. Assign Engineering + Data Protection joint task force to draft the override workflow and review criteria by [date].
5. Deploy the new process in staging, test with mock overrides, and iterate for 2 weeks before full rollout.
6. Publish the policy to all teams and conduct a training session on override risks and the new process.

**What changed:** Added a rotating non-executive reviewer to the two-sign-off rule to eliminate single-point override risks.
