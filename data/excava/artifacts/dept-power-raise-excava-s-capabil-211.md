# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-211` (dept) · 2026-07-18T17:32:26.849025+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Llama3.2-3B-Instruct for EXCAVA’s long-document pipeline after 24-hour A/B testing.

**Plan:**
1. Run a 24-hour A/B test comparing Llama3.2-3B-Instruct (50K-token sample first) and Mistral-7B-Instruct-v0.3 on EXCAVA’s long-document pipeline.
2. Measure capability gain (≥0.5%) and compute cost (≤8x lower than Qwen2.5-72B) for both models.
3. If Llama3.2-3B fails (hallucination/coherence loss), switch to Mistral-7B for production.
4. If both pass, deploy Llama3.2-3B by default due to lower compute cost.
5. Log truncation rates, token usage, and output quality metrics for post-test analysis.
6. Freeze model selection for 30 days post-deployment to stabilize performance.

**What changed:**
Switched from Qwen2.5-72B to Llama3.2-3B (or Mistral-7B if needed) to balance capability and compute cost.
