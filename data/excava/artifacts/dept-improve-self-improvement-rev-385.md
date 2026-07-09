# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-385` (dept) · 2026-07-09T14:41:45.036692+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Extract last 30 days of `metrics.json` and filter prompts with `exec_count ≥ 1000` and `p95_latency ≥ 95th-percentile` (baseline: last 30 days).
2. Run `grep -rn "TODO\|FIXME\|XXX" --include="*.py" engines/ routing/ own-code/ > todo_flags.txt`.
3. Manually triage `todo_flags.txt` to identify 3-5 high-impact, safe refactors (e.g., unused imports, redundant checks, or low-risk optimizations).
4. For each flagged prompt, measure delta in `p95_latency` and `exec_count` post-refactor (A/B test via shadow deployment if possible).
5. Auto-apply safe changes via pre-commit hooks or CI/CD (e.g., `ruff`/`black` for Python, `eslint` for JS).
6. Pitch refactors to team with metrics delta and risk assessment.

**What changed:** Added p95 latency baseline, manual triage, and auto-apply workflow.
