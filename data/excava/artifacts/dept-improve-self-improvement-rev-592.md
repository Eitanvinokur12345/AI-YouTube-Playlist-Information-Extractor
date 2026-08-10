# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-592` (dept) · 2026-08-10T13:59:32.955807+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Configure PR-Agent to run in shadow mode exclusively on PRs modified after the last merged PR.
2. Apply a keyword filter (`routing`, `engine`, `prompt`) to exclude irrelevant PRs from shadow mode.
3. Deploy the updated PR-Agent configuration to the newest open PRs first.
4. Monitor reviewer feedback for noise reduction and error detection effectiveness.
5. Iterate on the keyword list based on initial results.
6. Document the process for future scaling.

**What changed:** PR-Agent now targets fresh, relevant PRs in shadow mode with reduced noise.
