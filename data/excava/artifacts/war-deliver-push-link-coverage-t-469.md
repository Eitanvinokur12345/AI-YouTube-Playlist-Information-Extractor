# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-469` (war) · 2026-07-16T10:29:30.695631+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement a live link check at PR merge time with retry mechanism and daily review to ensure accurate link coverage
**Plan:**
1. Enforce a live link check at PR merge time, verifying that all links in the PR description or ticket resolve to a 200 status
2. Implement a 30-second retry window for transient failures to minimize unnecessary delays
3. Log all link check failures for daily review by Product Ops to identify and address recurring issues
4. Require engineers to include a link to the ticket in every PR to maintain a connection between code changes and business value
5. Conduct daily reviews of logged failures to identify areas for improvement and optimize the link check process
**What changed:** Link coverage measurement now relies on live link checks at PR merge time with a retry mechanism and daily review, rather than solely on ticket-link inclusion or automated health checks.
