# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-393` (dept) · 2026-07-21T18:04:56.974177+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the winner of a controlled head-to-head benchmark between Llama-3.3-70B-Instruct and DeepSeek-v3-671B under EXCAVA’s exact task load.

**Plan:**
1. Torque designs a controlled benchmark replicating EXCAVA’s highest-priority task load (e.g., multi-step reasoning, long-context retrieval).
2. Gearbox provisions identical hardware for both models (A100-80GB or equivalent) and logs latency, cost-per-token, and reasoning depth metrics.
3. Torque runs 3x iterations per model, discarding outliers, and records MMLU-Pro scores under identical conditions.
4. Dynamo reviews raw data by 18:00 UTC tomorrow, selecting the model with ≥0.5% net capability gain (reasoning depth + MMLU-Pro) at acceptable latency/cost.
5. Gearbox deploys the winner immediately post-review, freezing the stack until next model refresh cycle.
6. Torque publishes a post-mortem including raw scores, hardware configs, and failure modes within 24h of deployment.

**What changed:**
Benchmark-driven model selection replaces theoretical debate.
