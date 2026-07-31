# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-326` (dept) · 2026-07-31T04:29:36.811803+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 48-hour live A/B benchmark comparing Anthropic Claude 3.7 Sonnet vs. 3.5 Haiku on EXCAVA’s core reasoning workload—if the delta is <0.5%, lock in Haiku 3.5 with a fine-tuned distillation layer and reallocate the saved budget to tooling upgrades. Torque owns the benchmark.

**Plan:**
1. Deploy identical EXCAVA reasoning workloads to both 3.7 Sonnet and 3.5 Haiku endpoints.
2. Measure real-time excavation planning accuracy, resource allocation efficiency, and latency.
3. If Sonnet’s delta <0.5%, switch to Haiku 3.5 + fine-tuned distillation layer.
4. Redirect 70% of Sonnet’s budget savings to tooling upgrades (e.g., data pipeline optimizations).
5. Document benchmark results and model selection rationale in EXCAVA’s tech wiki.
6. Finalize tooling upgrade priorities by EOD Friday.

**What changed:**
Benchmark-driven model selection with cost-efficient fallback if gains are marginal.
