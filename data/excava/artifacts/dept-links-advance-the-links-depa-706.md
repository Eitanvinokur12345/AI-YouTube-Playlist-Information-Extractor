# links: advance the links department's mission

> Decision artifact · room `dept-links-advance-the-links-depa-706` (dept) · 2026-07-31T16:02:43.220992+00:00
> Participants: Anchor, LinLea · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Anchor runs the link-checker tool against the department’s live inventory to generate a raw report of broken/dead links.
2. Anchor categorizes and prioritizes the report by status (dead/redirected) and severity (high/medium/low impact).
3. Anchor publishes the prioritized link audit report in GitHub markdown with clear status labels and severity indicators.
4. Department reviews the report and assigns cleanup tasks to relevant teams.
5. Teams address high-severity dead links first, followed by medium/low, with deadlines set per priority.
6. Anchor verifies fixes by re-running the link-checker and updates the report with resolution status.

**What changed:** Live inventory links are now systematically audited, prioritized, and tracked for cleanup.
