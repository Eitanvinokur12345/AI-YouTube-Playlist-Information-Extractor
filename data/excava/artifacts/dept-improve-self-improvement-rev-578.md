# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-578` (dept) · 2026-07-09T15:18:37.179315+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Score `/prompts/` and `/engines/` files using: `(tokens / 500) + (TODO/FIXME_count / max(1, tokens/100)) + (days_since_edit / 30)`
2. Flag files with score ≥ 2 for review (adjust threshold via data after 1 week).
3. Whitelist safe lint fixes: trailing whitespace, trailing newlines, Markdown link syntax.
4. Auto-apply whitelisted fixes to flagged files with score ≥ 1.
5. Log all changes to `self_improvement_audit.log` with scores and diffs.
6. Re-run `make lint` post-apply to verify no regressions.

**What changed:** Auto-applied safe lint fixes to high-impact, actionable files.
