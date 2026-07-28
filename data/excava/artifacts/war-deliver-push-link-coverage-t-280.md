# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-280` (war) · 2026-07-28T23:12:09.255697+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Require every major decision (over $5K or strategic impact) to be documented in a **Markdown file in `/decisions/`** with a one-line link in the PR/issue, owned by the decision-maker.

**Plan:**
1. Create `/decisions/` folder in the repo root with a `README.md` template (decision, reason, trade-off, date, owner).
2. Mandate a one-line link to the decision file in PR/issue descriptions (e.g., `Closes #decision-123`).
3. Require approval from the decision owner before merging PRs with linked decisions.
4. Add a GitHub Action to flag stale decisions (no updates in 90 days).
5. Include `/decisions/` in repo health metrics (e.g., "decision coverage %").
6. Review decision format quarterly to balance structure and readability.

**What changed:** Decisions are now traceable, contextual, and machine-readable without cluttering PRs/issues.
