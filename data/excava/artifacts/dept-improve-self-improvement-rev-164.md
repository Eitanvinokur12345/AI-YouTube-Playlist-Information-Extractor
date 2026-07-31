# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-164` (dept) · 2026-07-31T15:17:50.317424+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent on every PR before human review, with a lightweight pre-filter and weekly metrics.

**Plan:**
1. **Pre-filter PRs:** Add a 30-second human triage step to block clearly irrelevant PRs (e.g., WIP, trivial typo fixes).
2. **Auto-apply safe changes:** For PRs passing the filter, auto-apply PR-Agent suggestions with ≥80% confidence.
3. **Surface remaining feedback:** For lower-confidence suggestions, add PR-Agent comments for human review.
4. **Measure impact:** Track false positive rate and suggestion survival rate weekly.
5. **Iterate:** Adjust confidence thresholds or pre-filter rules based on weekly metrics.
6. **Document:** Update contributor guidelines to explain PR-Agent’s role and how to override its feedback.

**What changed:** PR-Agent now runs on all PRs post-filter, with auto-apply for high-confidence fixes and human review for the rest.
