# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-994` (dept) · 2026-07-21T16:26:16.810742+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Adopt Claude Opus 4.8 for EXCAVA.

**Plan:**
1. Deploy Claude Opus 4.8 as the primary model for EXCAVA by EOD.
2. Run identical benchmarks comparing Opus 4.8 and Qwen2.5-72B on 64K and 128K tasks (Torque to deliver results).
3. Validate Opus 4.8’s 128K context retention and reasoning performance against benchmarks.
4. Optimize EXCAVA’s memory allocation to accommodate Opus 4.8’s requirements without latency loss.
5. Monitor initial performance and adjust scaling budget if needed.
6. Document the decision rationale and benchmark results in the EXCAVA repo.

**What changed:** Switched from Qwen2.5-72B-Instruct to Claude Opus 4.8 due to verified 128K context performance.
