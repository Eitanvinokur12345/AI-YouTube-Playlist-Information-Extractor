# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-464` (war) · 2026-07-16T18:15:07.191545+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Require human-written changelog snippets only for user-facing PRs; machine-generate boilerplate for internal changes.

**Plan:**
1. Update PR templates to include a checkbox: "Does this PR include user-facing changes? (If yes, provide a human-written changelog snippet.)"
2. Add a GitHub Action to auto-generate boilerplate changelog entries for non-user-facing PRs (refactors, tests, internal tooling).
3. Require maintainers to manually approve PRs with missing human-written changelog snippets for user-facing changes.
4. Document the policy in the repo’s CONTRIBUTING.md and link it in PR templates.
5. Monitor changelog quality weekly and adjust exemptions as needed.

**What changed:** Human-written changelogs now required only for user-facing changes; internal changes auto-logged.
