# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-998` (dept) · 2026-07-12T12:17:04.511340+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply only *mechanical* fixes (typos, formatting, missing imports) before human review, with full change logs for audit—reject deeper "fixes" that risk masking logic flaws.

**Plan:**
1. Implement a pre-review lint pass that flags but does not auto-fix logic-related issues (e.g., potential dependency breaks, subtle typos masking flaws).
2. Auto-apply mechanical fixes (typos, formatting, missing imports) *only* if they pass a strict whitelist of safe transformations.
3. Log every auto-applied change in a machine-readable format (e.g., JSON diffs) with human-readable summaries for audit.
4. Add a human override mechanism (e.g., `/revert` command) to undo auto-applied changes within 24 hours.
5. Deploy to a 10% canary cohort for 2 weeks, measuring false positives/negatives before full rollout.
6. Require explicit owner approval for any auto-applied change that modifies >3 lines or touches critical paths.

**What changed:**
Pre-review auto-fixes limited to mechanical changes with full audit logs.
