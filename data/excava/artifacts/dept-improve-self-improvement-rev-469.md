# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-469` (dept) · 2026-08-10T20:41:52.441685+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on the newest merged PR first to calibrate rules safely, then apply refined rules to the newest open PR.

**Plan:**
1. Deploy PR-Agent in shadow mode on the newest merged PR to gather feedback data.
2. Analyze feedback from merged PRs to identify and reduce false positives.
3. Tighten PR-Agent rules based on merged PR insights.
4. Apply refined rules to the newest open PR in shadow mode.
5. Review shadow mode results on the open PR to confirm false positive reduction.
6. Gradually roll out refined rules to all open PRs if successful.

**What changed:** PR-Agent rules tuned for lower false positives.
