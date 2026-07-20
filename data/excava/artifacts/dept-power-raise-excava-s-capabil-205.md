# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-205` (dept) · 2026-07-20T17:13:38.278221+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Secure access to DeepSeek-v3-671B and Llama-3.3-70B for a 7-day live A/B test.
2. Deploy EXCAVA with each model in parallel, logging 128K-context throughput and stability metrics.
3. If access to Llama-3.3-70B fails, proceed with DeepSeek-v3-671B alone.
4. If both models fail stability tests, default to Mistral Large 2.1 (48B) as the fallback.
5. Measure capability lift (≥0.5%) via EXCAVA’s performance benchmarks.
6. Finalize model selection based on A/B test results and stability data.

**What changed:** Decision deferred to live A/B test between DeepSeek-v3-671B and Llama-3.3-70B, with Mistral Large 2.1 as fallback.
