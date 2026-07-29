# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-347` (dept) · 2026-07-29T20:58:33.555627+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Select 1,000 live EXCAVA tasks for a blind A/B test.
2. Compare Qwen 2.5-72B-Instruct (baseline) vs. Anthropic Claude 3.7 Sonnet (new model) on structured data extraction accuracy and output quality.
3. Torque designs the test (metrics, randomization, blinding).
4. Gearbox executes the test and tracks compute costs for both models.
5. After 1,000 tasks, analyze results for a 0.5%+ quality improvement threshold.
6. If passed, integrate Claude 3.7 Sonnet as a parallel option; if failed, discard.

**What changed:** Structured evaluation replaces parallel integration as the first step.
