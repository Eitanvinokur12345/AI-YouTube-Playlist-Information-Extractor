# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-161` (dept) · 2026-07-27T17:58:33.607317+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Run a 48-hour blind A/B stress test on EXCAVA’s 8xA100 node comparing Qwen3-235B-A22B-Instruct vs DeepSeek-R1-671B, with latency, throughput, and memory fragmentation logged hourly by the ops team; winner becomes primary engine by Friday.

**Plan:**
1. Clone Qwen3-235B-A22B-Instruct and DeepSeek-R1-671B into separate EXCAVA inference branches.
2. Configure identical sharding (8xA100) and BF16 quantization for both models.
3. Deploy blind A/B test: route 50% of EXCAVA’s traffic to each model via weighted load balancer.
4. Log hourly metrics: latency (P99), throughput (tokens/sec), VRAM fragmentation (% per GPU).
5. Freeze non-critical EXCAVA updates during test to isolate model performance.
6. Friday 18:00 UTC: ops team publishes report; promote winning model to `main` branch.

**What changed:** No permanent model switch until Friday’s A/B results.
