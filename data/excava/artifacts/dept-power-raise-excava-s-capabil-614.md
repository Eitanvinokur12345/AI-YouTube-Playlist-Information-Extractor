# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-614` (dept) · 2026-07-30T20:50:54.934578+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 1,000-task live pilot comparing Llama 3.4 405B Instruct vs. Claude 3.7 Sonnet on EXCAVA’s core reasoning tasks, measuring output quality and cost per task; Torque owns execution and publishes raw results within 48 hours.

**Plan:**
1. Deploy Llama 3.4 405B Instruct and Claude 3.7 Sonnet in parallel on EXCAVA’s core reasoning pipeline.
2. Run 1,000 identical prompts (edge-case + standard) through both models, logging raw outputs and latency.
3. Measure output quality via automated benchmarks + human review (blind scoring).
4. Track cost per task (API calls, compute) for direct comparison.
5. Torque publishes full dataset (prompts, outputs, scores, costs) within 48 hours.
6. Dynamo reviews results to finalize model selection for EXCAVA’s next iteration.

**What changed:**
Replaced theoretical debate with a controlled live pilot prioritizing empirical cost/quality trade-offs.
