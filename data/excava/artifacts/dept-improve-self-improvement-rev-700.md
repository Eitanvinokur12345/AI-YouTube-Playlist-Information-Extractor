# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-700` (dept) · 2026-07-16T18:33:09.925711+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Log *all* prompt changes for two weeks in a single shared log with timestamps and exact variants; after, analyze the log to identify which changes moved metrics by >5% and which were noise.

**Plan:**
1. Create a shared log (Google Sheet/Notion) with columns: Timestamp, Prompt Variant, Change Description, Owner.
2. Mandate logging *all* prompt changes (even minor tweaks) within 1 hour of deployment.
3. After two weeks, Sprocket exports the full log and shares it with Gauge.
4. Gauge analyzes the log to flag changes with >5% metric deltas (success criteria).
5. Gauge drafts a post-audit report identifying signal vs. noise, with recommendations.
6. Team reviews report in a 30-min retro to adjust future prompt-change processes.

**What changed:**
Moved from sampling debate to *full* logging for two weeks to ensure no edge cases are missed.
