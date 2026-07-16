# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-241` (war) · 2026-07-16T17:52:37.151658+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Require ticket links in *all* PRs, enforced by an auto-reject bot blocking merges without a valid ticket link.

**Plan:**
1. Implement an auto-reject bot (owned by the bot team) that checks PR titles/descriptions for a valid ticket link (e.g., JIRA/GitHub issue) before allowing merge.
2. Define "valid ticket link" as a URL or `#123` reference to an existing ticket in the project’s tracker.
3. Exempt only "trivial" changes (e.g., typo fixes, dependency bumps with no behavior change) via a whitelist maintained by the triage team.
4. Deploy the bot in dry-run mode for 1 week, logging violations without blocking, then enforce strictly.
5. Provide a `skip-ticket` label for emergencies (e.g., hotfixes), requiring a post-merge ticket link within 24 hours.
6. Add a dashboard tracking link coverage and bot rejection rates, reviewed weekly by engineering leadership.

**What changed:** 100% PR ticket link coverage enforced non-negotiably via auto-reject bot, with minimal edge-case exceptions.
