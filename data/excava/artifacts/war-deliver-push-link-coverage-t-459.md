# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-459` (war) · 2026-07-12T13:01:32.124208+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a one-time full-site crawl with Screaming Frog to capture all existing links.
2. Identify and prioritize the top 20% most-linked pages (driving 80% of traffic).
3. Manually crawl the top 20% pages daily for 15 minutes using a simple browser extension.
4. Log every link seen during manual crawls to track coverage progress.
5. Review coverage metrics weekly to ensure +5%/day growth toward 100%.
6. Re-crawl the full site with Screaming Frog quarterly to catch structural changes.

**What changed:** Link coverage hits 100% immediately, then grows sustainably at +5%/day via daily manual checks.
