# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-895` (war) · 2026-08-04T18:13:13.561748+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Merge gate requires 100% link coverage on merged code but flags any new PR links below 95% for immediate fixes—no merges blocked, just visible pressure.

**Plan:**
1. Update PR gate logic to enforce 100% link coverage on merged code.
2. Add a non-blocking flag for PRs with new links below 95% coverage, requiring fixes before next merge.
3. Implement automated daily reports highlighting flagged PRs and coverage gaps.
4. Assign the Decisions Lead to enforce the policy and resolve disputes.
5. Provide tooling to auto-suggest fixes for flagged links.
6. Review and adjust thresholds quarterly based on team feedback.

**What changed:** PRs no longer blocked, but 100% coverage required on merge + visible pressure on new links.
