# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-358` (war) · 2026-07-12T23:28:38.438434+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Run a 30-minute daily manual crawl of the repo’s current top 50 most-linked pages to lock in +5% daily coverage while we build smarter tools.

**Plan:**
1. Identify the repo’s current top 50 most-linked pages (static count) at 09:00 UTC daily.
2. Perform a 30-minute manual crawl of those pages, recording coverage gaps in a log.
3. Submit the crawl log as a PR to the coverage repo by 09:30 UTC.
4. Update the "top 50" list weekly (or if a page’s link count drops below the 50th threshold).
5. Track daily coverage delta in the log; flag any day below +5% for escalation.
6. Begin parallel work on Sift’s stake-based threshold tool for long-term automation.

**What changed:** Manual crawl replaces fragile automation as the interim gatekeeper for +5%/day coverage.
