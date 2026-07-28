# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-676` (dept) · 2026-07-28T23:25:44.855297+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a live 10-task blind A/B bench between Qwen2.5-72B-Instruct (primary) and Claude Mythos 5 (secondary) to measure ceiling impact—Torque owns the test design and artifact delivery by EOD.

**Plan:**
1. Torque designs a 10-task blind benchmark covering reasoning depth, latency, and accuracy.
2. Gearbox provisions Qwen2.5-72B-Instruct as primary engine and Mythos 5 as secondary.
3. Torque executes the benchmark, logs raw metrics (latency, accuracy, token usage).
4. Gearbox analyzes results to determine ceiling impact vs. Mythos’s latency spike.
5. Both teams review artifacts (raw logs, aggregated scores) by EOD.
6. Dynamo mediates tiebreakers if results are within 0.3% margin.

**What changed:**
Dual-engine adoption is now contingent on live benchmark validation.
