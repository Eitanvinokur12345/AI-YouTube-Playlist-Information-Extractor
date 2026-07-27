# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-434` (dept) · 2026-07-27T19:20:57.850441+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Llama-3.1-70B-Instruct as EXCAVA’s primary inference engine after stress test validation.

**Plan:**
1. Spin up an 8xA100 node cluster with identical software stacks for Qwen3-235B-A22B-Instruct and Llama-3.1-70B-Instruct.
2. Run a 48-hour blind A/B stress test on 128K-token prompts with a strict 5-second latency cap.
3. Log throughput (tokens/sec), latency (P99), and memory usage for both models.
4. Benchmark long-context reasoning (e.g., retrieval accuracy) on EXCAVA’s worst-case prompt.
5. Compare raw capability vs. efficiency trade-offs using Torque’s metrics.
6. Finalize model selection based on stress test results.

**What changed:**
Primary inference engine selection deferred to stress test outcome.
