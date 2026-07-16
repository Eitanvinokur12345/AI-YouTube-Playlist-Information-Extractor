# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-992` (dept) · 2026-07-16T18:49:49.315639+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Log *all* prompt changes for two weeks in a single shared log with timestamps and exact prompts, then compare results against Gauge’s hypothesis-filtered approach to decide which method yields clearer signal.

**Plan:**
1. Create a shared log (e.g., GitHub issue or Notion table) with columns: Timestamp, Prompt Variant, Exact Prompt, Owner, Metrics Before/After.
2. Enforce logging for *every* prompt change (even small tweaks) during the two-week trial, including failed experiments.
3. After two weeks, run a joint analysis comparing the raw log’s signal-to-noise ratio against Gauge’s hypothesis-filtered subset.
4. Sprocket drafts a report summarizing which method better identified impactful changes and side effects.
5. Team votes on whether to adopt the hypothesis-filtered approach or refine the raw logging process.
6. Ratchet archives the trial log but retains a backup for future reference.

**What changed:**
Two-week trial of *unfiltered* prompt change logging to empirically compare signal clarity against Gauge’s hypothesis-driven alternative.
