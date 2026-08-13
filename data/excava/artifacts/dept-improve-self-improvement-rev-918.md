# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-918` (dept) · 2026-08-13T14:01:34.019584+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent live on open PRs with non-blocking comments only for one week, then expand to merged PRs for baseline validation if noise is acceptable.

**Plan:**
1. Deploy PR-Agent on all open PRs with non-blocking comment mode enabled.
2. Monitor noise levels (irrelevant/low-value comments) and review turnaround time for one week.
3. If noise is acceptable (<10% irrelevant comments), expand PR-Agent to merged PRs for baseline accuracy validation.
4. Collect metrics on review quality improvements and false positives/negatives.
5. After two weeks, review data and adjust PR-Agent’s prompt/engine/routing as needed.
6. Finalize auto-apply rules for safe changes based on validated baseline.

**What changed:**
PR-Agent now runs live on open PRs with non-blocking comments, deferring merged PR validation until noise assessment.
