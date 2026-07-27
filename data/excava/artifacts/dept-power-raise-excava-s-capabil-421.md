# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-421` (dept) · 2026-07-27T18:40:03.569642+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Qwen3-235B-A22B as EXCAVA’s primary inference engine pending stress test results.

**Plan:**
1. Deploy Qwen3-235B-A22B and DeepSeek-R1-671B on EXCAVA’s 8xA100 node in a blind A/B setup.
2. Run a 48-hour stress test measuring throughput, latency, and cost per token for both models.
3. Log raw metrics (tokens/sec, p99 latency, GPU utilization, cost per 1K tokens) without human bias.
4. Publish all raw data in a public GitHub repo within 48 hours of test completion.
5. If Qwen3’s throughput drops >0.5% or costs exceed DeepSeek’s by >0.5%, switch to DeepSeek-R1-671B.
6. Document final model choice and reasoning in a `DECISION.md` file.

**What changed:**
Blind A/B test replaces debate with empirical validation.
