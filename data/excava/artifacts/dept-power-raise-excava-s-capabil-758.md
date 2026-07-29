# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-758` (dept) · 2026-07-29T20:37:55.559461+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add the newest Anthropic Claude 3.7 Sonnet model to EXCAVA’s toolkit after validating its performance against Qwen 2.5-72B-Instruct in a controlled A/B test.

**Plan:**
1. Torque designs the A/B test, defining EXCAVA’s power setup analysis cases and evaluation metrics (reasoning quality, latency, cost).
2. Run parallel inference on 100+ representative power cases, logging per-query outputs and compute costs for both models.
3. Measure delta in capability (≥0.5% threshold) and cost impact; if neither model meets the threshold, iterate with next-best alternatives.
4. If Claude 3.7 Sonnet meets or exceeds the threshold, integrate it into EXCAVA’s toolkit with fallback to Qwen 2.5-72B-Instruct if latency spikes >20%.
5. Document test results and integration steps in EXCAVA’s model registry.

**What changed:**
Claude 3.7 Sonnet will be adopted only if proven superior in controlled testing, mitigating Torque’s regression risk while targeting Gearbox’s efficiency goals.
