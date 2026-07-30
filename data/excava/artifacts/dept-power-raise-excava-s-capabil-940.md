# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-940` (dept) · 2026-07-30T19:31:44.457432+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Torque benchmarks EXCAVA on distilled 32B vs. fine-tuned 70B across 1000 samples, measuring quality (target ≥0.5% gain) and latency (target ≤30ms).
2. Torque logs raw metrics (throughput, accuracy, frame drops) and publishes results in `/benchmarks/excava_distilled_32b_vs_70b_YYYYMMDD.md`.
3. If 32B meets ≥0.5% quality at ≤30ms, Torque submits a PR to switch EXCAVA’s default model to the 32B variant.
4. Gearbox reviews the PR within 24h, validating no regressions in core reasoning tasks.
5. Dynamo merges the PR post-review, triggering a canary deployment to 5% of users for 48h.
6. Dynamo monitors SLA metrics (latency, error rates) and rolls back if degradation >0.1% or latency spikes >5ms.

**What changed:** EXCAVA’s model choice now hinges on benchmarked trade-offs between 32B and 70B distilled variants.
