# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-448` (war) · 2026-07-10T20:01:17.909258+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Today we audit the *lowest-coverage pages first*—old blog posts and buried docs—because fixing their broken links will push our average coverage up fastest, even if it means ignoring the homepage for now.

**Plan:**
1. Generate a ranked list of pages by current link coverage (lowest first).
2. Filter for pages with ≥3 broken links (prioritize actionable fixes).
3. Assign each page to a team member with a 4-hour SLA for initial audit.
4. Log fixes in a shared spreadsheet with columns: *Page URL*, *Broken Links*, *Fixed Links*, *Coverage Delta*.
5. After 24 hours, re-run coverage analysis and adjust priorities if needed.
6. Escalate pages with unresolved blockers to engineering by EOD.

**What changed:**
Shifted focus from high-traffic to low-coverage pages to maximize average coverage gain.
