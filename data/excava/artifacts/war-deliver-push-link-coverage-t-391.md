# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-391` (war) · 2026-07-16T17:29:57.457443+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Require every PR to include a live ticket link in the title or description *before review*, enforced strictly at merge time by verifying the link resolves to an active issue.

**Plan:**
1. Update PR templates to include a required "Ticket Link" field in the title/description.
2. Add a GitHub Action to validate ticket links *before review* (blocking if invalid).
3. Implement a merge gate that re-checks the ticket link resolves to an active issue.
4. Train engineers on ticket link requirements and active issue validation.
5. Monitor link coverage daily and flag PRs missing valid links.
6. Review enforcement metrics weekly and adjust validation rules as needed.

**What changed:**
Mandatory live ticket links enforced pre-review and at merge, replacing placeholder enforcement.
