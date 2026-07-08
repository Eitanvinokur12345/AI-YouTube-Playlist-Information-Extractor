# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-573` (dept) · 2026-07-08T20:07:54.742699+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Audit self-improvement flows end-to-end to identify actionable gaps, not grep noise.

**Plan:**
1. Map self-improvement data paths: trace prompt → engine → routing → output in `./src/prompts/self_improve/`, `./src/improve/engine.py`, and `./src/improve/routing.py`.
2. Validate guards/safety: check for missing input validation, edge-case handling, or unsound assumptions in mapped paths.
3. Identify *real* flaws: document missing guards, unsafe defaults, or unhandled edge cases with reproducible examples.
4. Propose minimal fixes: prioritize safe, low-risk changes (e.g., adding guards, clarifying docs) with rollback plans.
5. Auto-apply safe changes: implement via a controlled script (e.g., `./scripts/apply_safe_fixes.sh`) with pre/post checks.
6. Pitch improvements: summarize findings and proposed changes in `./docs/self_improve_audit.md` for team review.

**What changed:** Focus shifted from grep-based noise to end-to-end flow validation and evidence-based flaws.
