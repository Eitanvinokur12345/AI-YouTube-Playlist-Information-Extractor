# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-952` (dept) · 2026-07-31T18:09:02.941258+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Enforce only high-confidence mechanical checks** via PR-Agent:
   - Linting (ESLint, Pylint, etc.)
   - Dependency hygiene (outdated/unsafe packages)
   - Hard-fail test coverage (below configured threshold)
2. **Block merges** if any enforced check fails.
3. **Human review remains mandatory** for all other aspects (design, edge cases, trade-offs).
4. **Document the policy** in the repo’s CONTRIBUTING.md.
5. **Review and adjust** enforced checks quarterly based on false-positive rates.
6. **Train teams** to treat PR-Agent as a safety net, not a substitute for judgment.

**What changed:** PR-Agent now gates only mechanical checks; humans own all subjective reviews.
