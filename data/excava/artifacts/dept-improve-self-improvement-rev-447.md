# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-447` (dept) · 2026-08-16T14:53:26.744633+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode only on open PRs flagged high-risk by a lightweight classifier for one week, then switch to Overhaul.

**Plan:**
1. Implement a lightweight risk classifier (e.g., dependency updates, major refactors) to flag high-risk open PRs.
2. Configure PR-Agent to run in shadow mode exclusively on flagged high-risk PRs for one week.
3. Log all unsafe changes detected by PR-Agent during the shadow mode period.
4. After one week, Overhaul takes ownership of the classifier and the switch to full PR-Agent integration.
5. Review logs to assess false positives/negatives and refine the classifier if needed.
6. Transition PR-Agent from shadow mode to active mode on high-risk PRs post-review.

**What changed:**
PR-Agent now runs in shadow mode only on high-risk PRs, reducing compute waste while maintaining early detection of unsafe changes.
