# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-449` (dept) · 2026-08-02T17:49:33.281493+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Route all "safe" auto-apply changes to a dedicated `staging` branch instead of main.
2. Auto-apply changes to `staging` with full static analysis + regression checks.
3. Log all applied changes in a `staging-changes.md` file with timestamps and diffs.
4. Block merges from `staging` to `main` for 7 days (production observation period).
5. After 7 days, require a human lead to review `staging-changes.md` and approve the merge.
6. If approved, fast-forward merge `staging` into `main`; otherwise, revert and log the rejection.

**What changed:** Shadow mode replaces immediate auto-apply; production-proven safety replaces static-only trust.
