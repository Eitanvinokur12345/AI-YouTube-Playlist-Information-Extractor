# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-448` (dept) · 2026-07-29T20:37:42.864352+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 2-week A/B test to validate the "prompt health score" metric.

**Plan:**
1. Build the "prompt health score" metric (clarity, conciseness, task alignment) for all active prompts.
2. Implement weekly auto-flagging for the bottom 10% of prompts.
3. Run a 2-week A/B test comparing flagged vs. non-flagged prompts on task outcomes.
4. If no measurable impact, drop the metric; if positive, adopt it weekly.
5. Gauge owns validation; Sprocket owns metric build and maintenance.

**What changed:**
Added outcome-based validation to the prompt health score metric.
