# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-709` (dept) · 2026-07-20T11:24:37.591203+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
**Plan:**
1. Deploy Qwen2.5-72B-Instruct and Llama-3.2-370B in parallel for EXCAVA.
2. Run 7-day live A/B tests at 50K, 64K, and 100K prompt lengths.
3. Measure truncation loss, cost per token, and output quality for both models.
4. Torque designs test metrics and validation criteria; Gearbox handles model deployment.
5. Collect data on failure modes (e.g., token-heap pressure) for post-test analysis.
6. Final model selection based on 0.5%+ capability lift or cost-adjusted parity.

**What changed:** Added 100K prompt test to validate Qwen2.5-72B’s 128K claim under EXCAVA’s pipeline constraints.
