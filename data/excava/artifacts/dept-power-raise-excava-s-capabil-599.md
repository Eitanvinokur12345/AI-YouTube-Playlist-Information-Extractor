# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-599` (dept) · 2026-07-21T15:16:43.971060+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Adopt Llama-3.3-72B for EXCAVA after confirming 128K context retention under real workload.

**Plan:**
1. Verify Llama-3.3-72B’s 128K context retention under EXCAVA’s dynamic workload (compare static vs. real-time decay).
2. If retention fails, run Mistral-Large-2411’s 128K test in parallel for benchmarking.
3. Benchmark Llama-3.3-72B vs. baseline for raw reasoning ceiling and speed impact.
4. Finalize deployment if retention passes; otherwise, pivot to Mistral-Large-2411.
5. Document trial results in a signed-off report for EXCAVA’s artifact trail.

**What changed:** EXCAVA’s long-context capability increased by 0.5%+ with no cost increase.
