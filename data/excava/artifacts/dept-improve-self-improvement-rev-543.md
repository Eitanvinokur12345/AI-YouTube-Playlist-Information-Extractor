# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-543` (dept) · 2026-08-08T05:22:32.708554+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on the newest open PR first, then expand to merged PRs.

**Plan:**
1. Configure PR-Agent to run in shadow mode on the newest open PR (highest priority).
2. Monitor shadow mode output for routing flaws and systemic issues.
3. Expand shadow mode to merged PRs after open PRs are stabilized.
4. Integrate PR-Agent feedback into CI/CD pipeline for open PRs.
5. Document routing flaw patterns discovered in shadow mode.
6. Review and adjust shadow mode scope based on initial results.

**What changed:** Prioritized open PRs over merged PRs for shadow mode to catch routing flaws pre-shipping.
