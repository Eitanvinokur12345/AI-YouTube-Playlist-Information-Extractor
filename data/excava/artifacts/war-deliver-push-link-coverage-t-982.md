# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-982` (war) · 2026-07-26T02:14:51.664140+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Publish a *public, rolling log* of every conversation—raw, unfiltered, timestamped, and searchable—on a dedicated subdomain (e.g., logs.reel.works), with daily automated live-checks and email alerts for newly broken links.

**Plan:**
1. Deploy a public subdomain (`logs.reel.works`) hosting a searchable, timestamped log of all conversations.
2. Implement a daily automated live-check system that fetches all links in the log and records their HTTP status codes.
3. Generate and send email notifications to maintainers for links that transition from `200 OK` to any non-200 status since the last check.
4. Require joint Engineering and Data Protection approval for any link that fails validation (non-200 status) before it’s published in the log.
5. Log the last-known status of every link, regardless of validation outcome, to expose drift over time.
6. Publish the log with a disclaimer that links are provided as-is and may change or break.

**What changed:**
Added daily live-checks, real-time failure alerts, and approval gates for broken links to the public log.
