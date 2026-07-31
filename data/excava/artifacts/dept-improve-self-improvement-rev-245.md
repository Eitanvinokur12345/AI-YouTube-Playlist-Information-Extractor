# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-245` (dept) · 2026-07-31T11:12:44.675648+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Reject auto-applying whitespace patches to third-party dependencies via Pret.
**Plan:**
1. Implement a pre-commit hook to check third-party dependency formatting for consistency.
2. Flag deviations in formatting without altering upstream code, ensuring awareness of inconsistencies.
3. Manually review and address flagged formatting issues to maintain code cleanliness.
4. Consider forking dependencies for critical updates or bug fixes, applying formatting changes manually.
5. Submit patches upstream to contribute to the cleanliness and consistency of third-party dependencies.
**What changed:** Enforced formatting consistency through a pre-commit hook instead of auto-applying patches.
