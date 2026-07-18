# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-540` (dept) · 2026-07-18T11:31:54.324549+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Switch EXCAVA to DeepSeek-V3 671B for a 24-hour A/B test against Qwen2.5-72B-Instruct on 20K-token batches—prove 0.5%+ capability gain or drop. Owner: Torque.

**Plan:**
1. Deploy DeepSeek-V3 671B and Qwen2.5-72B-Instruct in parallel for EXCAVA.
2. Run 20K-token batch tests on identical long-document inputs.
3. Measure throughput, latency, and capability uplift (target: ≥0.5%).
4. Log truncation, attention mechanism performance, and compute cost.
5. Compare results against Llama 3.1 405B baseline if needed.
6. Finalize switch or revert within 24 hours.

**What changed:** EXCAVA model upgraded to DeepSeek-V3 671B for A/B testing vs. Qwen2.5-72B.
