# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

<<<<<<< HEAD
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
=======
> Decision artifact · room `dept-improve-self-improvement-rev-952` (dept) · 2026-07-31T18:06:47.288306+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Gate PR-Agent on *only* high-confidence mechanical checks (linting, dependency hygiene, basic test coverage) and require human review for all subjective or contextual judgments.

**Plan:**
1. Configure PR-Agent to enforce only:
   - Linting violations (ESLint, Pylint, etc.)
   - Dependency hygiene (outdated/unsafe packages)
   - Basic test coverage thresholds (e.g., 80% line coverage)
2. Disable PR-Agent flags for:
   - Style violations (e.g., "prefer-arrow-functions")
   - Design/architecture critiques
   - Edge-case trade-offs
3. Add a GitHub Action step to run PR-Agent *before* human review, blocking merges if mechanical checks fail.
4. Require a human reviewer to approve *all* subjective or contextual aspects (design, edge cases, trade-offs).
5. Document the rule in the team’s `CONTRIBUTING.md` under "Automated Checks."
6. Monitor PR-Agent’s false-positive rate for mechanical checks and adjust thresholds quarterly.

**What changed:** PR-Agent now only gates mechanical checks; humans own all subjective judgments.
>>>>>>> 733479ce89d6b2d71cfa2a9ccfbc71af84161603
