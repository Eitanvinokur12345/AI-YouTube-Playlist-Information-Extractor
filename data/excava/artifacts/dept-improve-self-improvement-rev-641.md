# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-641` (dept) · 2026-07-13T09:31:39.889446+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Merge-time scanning wins—fail fast, auto-clean, accept small merge delay to cut production risk.

**Plan:**
1. Implement a merge-time duplicate/near-duplicate scanner for all prompts.
2. Block merges if duplicates are detected (fail fast).
3. Auto-apply safe cleanups (e.g., deduplication, formatting) at merge time.
4. Log all scan results and auto-clean actions for audit.
5. Add a 1-minute merge delay tolerance for urgent changes (manual override if needed).
6. Owner (Gauge) to document and enforce the new process in the team’s workflow.

**What changed:**
All prompts now scanned at merge; duplicates blocked immediately; safe cleanups applied automatically.
