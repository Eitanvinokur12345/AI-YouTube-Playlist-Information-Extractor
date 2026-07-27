# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-764` (dept) · 2026-07-27T19:40:17.477905+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Qwen3-235B-A22B-Instruct as EXCAVA’s primary inference engine after validation.

**Plan:**
1. Deploy Qwen3-235B-A22B-Instruct and Llama-3.1-70B-Instruct on EXCAVA’s 8xA100 node.
2. Run a 48-hour blind A/B stress test with worst-case prompt length (4096 tokens).
3. Measure throughput delta ≥0.5% (tokens/sec) and latency spikes under load.
4. Log VRAM usage, routing overhead, and memory-bound attention scaling.
5. Compare results against Llama-3.1-70B’s flat 70B performance.
6. Finalize engine selection based on empirical data.

**What changed:**
Primary inference engine selection deferred to empirical validation.
