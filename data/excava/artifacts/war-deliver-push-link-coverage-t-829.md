# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-829` (war) · 2026-07-26T02:37:38.533049+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Create a public-facing changelog (`CHANGELOG.md`) listing only user-facing changes with exact URLs fixed.
2. Create an internal changelog (`INTERNAL_CHANGELOG.md`) listing *all* link fixes (internal + user-facing) with exact URLs fixed.
3. Enforce a weekly audit: every Friday, the team reviews `INTERNAL_CHANGELOG.md` to ensure 100% link coverage.
4. Auto-generate changelog entries from link-fix commits (e.g., via GitHub Actions) to reduce manual overhead.
5. Add a `changelog` label to link-fix PRs to auto-populate entries in `INTERNAL_CHANGELOG.md`.
6. Document the process in `CONTRIBUTING.md` with clear rules for changelog entry formatting.

**What changed:** Split changelogs to balance user clarity and internal link enforcement.
