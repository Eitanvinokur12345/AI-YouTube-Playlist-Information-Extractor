# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-157` (dept) · 2026-08-26T18:20:32.856646+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on PRs with no reviewers for one week, then compare merge times and review quality against a control group.

**Plan:**
1. Configure PR-Agent to run in shadow mode on PRs with no assigned reviewers.
2. Deploy to a single team’s PRs for one week (control group: other teams’ PRs).
3. Track merge times, review load, and false positives for both groups.
4. Analyze data to assess impact on review quality and efficiency.
5. If no degradation, expand to all PRs in shadow mode for another week.
6. Present findings to stakeholders for final rollout decision.

**What changed:** PR-Agent now targets only unreviewed PRs in shadow mode for initial testing.
