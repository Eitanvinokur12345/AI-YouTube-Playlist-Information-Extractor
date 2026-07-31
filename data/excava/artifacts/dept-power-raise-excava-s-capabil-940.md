# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-940` (dept) · 2026-07-31T13:09:00.698540+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Torque runs a 1000-sample benchmark comparing distilled 32B vs. fine-tuned 70B on EXCAVA’s real-time task (latency ≤30ms, quality ≥0.5% gain).
2. Benchmark includes live drift risk: test both models against a 5000-sample rolling window of real-world data to validate stability.
3. If 32B meets ≥0.5% quality at ≤30ms, Torque switches EXCAVA to it immediately.
4. If 32B fails, Torque switches to the fine-tuned 70B (targeting ~50ms latency).
5. Gearbox validates compute cost and pipeline integration for the winning model.
6. Dynamo monitors post-switch performance for 24 hours to confirm no regression.

**What changed:** EXCAVA’s model selection now hinges on a controlled benchmark with real-time and drift constraints.
