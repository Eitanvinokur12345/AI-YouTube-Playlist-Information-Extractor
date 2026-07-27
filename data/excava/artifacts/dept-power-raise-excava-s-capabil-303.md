# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-303` (dept) · 2026-07-27T17:36:32.159531+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Run a 48-hour blind A/B stress test on EXCAVA’s 8xA100 node comparing Qwen3-235B-A22B-Instruct vs. Llama-3.3-70B-Instruct vs. DeepSeek-R1-671B—latency, throughput, and stability metrics must prove which model delivers the 0.5%+ capability bump without sharding fragility.

**Plan:**
1. Deploy Qwen3-235B-A22B-Instruct, Llama-3.3-70B-Instruct, and DeepSeek-R1-671B on EXCAVA’s 8xA100 cluster with identical sharding configs.
2. Configure a 48-hour blind A/B test: randomize model assignment per query, log latency (P50/P99), throughput (tokens/sec), and stability (context-length failures).
3. Use EXCAVA’s existing benchmark harness to generate synthetic workloads (mix of short/long contexts, batch sizes 1–64).
4. Post-test, compare metrics: prioritize models meeting ≥0.5% capability bump with P99 latency <1.2x baseline and zero context-length failures.
5. If no model meets criteria, iterate with fine-tuned variants or hybrid MoE/dense approaches.
6. Publish results in `/docs/decision-2024-05-EXCAVA-model-selection.md` with raw metrics and sharding analysis.

**What changed:** Decision deferred to empirical stress test; no model selected yet.
