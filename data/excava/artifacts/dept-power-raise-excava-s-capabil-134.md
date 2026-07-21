# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-134` (dept) · 2026-07-21T17:15:03.267274+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Adopt Llama-3.1-405B-Instruct for EXCAVA with a controlled 64K benchmark as the artifact.

**Plan:**
1. Deploy Llama-3.1-405B-Instruct in EXCAVA’s stack with 64K context length enabled.
2. Conduct a controlled benchmark comparing its long-context accuracy against Qwen2.5-72B and DeepSeek-v3-671B at 64K.
3. Verify context stability via side-by-side tests (no loss past 32K or 64K thresholds).
4. Measure net accuracy gain (target: ≥0.5%) and token/compute cost trade-offs.
5. Document results in a GitHub artifact (side-by-side metrics, stability logs).
6. Gearbox owns execution; Torque reviews and signs off on benchmark validity.

**What changed:** Replaced Qwen2.5-72B and DeepSeek-v3-671B with Llama-3.1-405B-Instruct pending 64K verification.
