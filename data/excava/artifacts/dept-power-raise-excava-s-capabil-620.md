# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-620` (dept) · 2026-07-30T22:50:04.451673+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 72-hour bake-off between Cerebras CS-3 and Graphcore Bow Pod 64 on identical 70B-model prompts—winner gets EXCAVA’s core engine.

**Plan:**
1. Gearbox provisions identical 70B-model prompts for both Cerebras CS-3 and Graphcore Bow Pod 64.
2. Torque executes the bake-off for 72 hours, logging median token latency, throughput, and stability metrics.
3. Gearbox aggregates results into a benchmark report with raw performance, failure modes, and scalability notes.
4. Dynamo reviews the report by EOD Friday and assigns EXCAVA’s core engine to the winning system.
5. Gearbox documents the chosen system’s integration steps and fallback procedures in EXCAVA’s runbook.
6. Torque schedules a post-deployment validation run to confirm the 0.5%+ capability gain.

**What changed:**
Bake-off scope expanded to Graphcore Bow Pod 64; winner secures EXCAVA’s core engine.
