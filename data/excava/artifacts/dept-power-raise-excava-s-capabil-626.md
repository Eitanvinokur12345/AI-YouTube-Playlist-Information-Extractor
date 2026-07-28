# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-626` (dept) · 2026-07-28T23:45:36.105064+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt **Claude Mythos 5** as EXCAVA’s primary reasoning engine, contingent on live validation.

**Plan:**
1. Design a 10-task blind A/B benchmark comparing Mythos 5 (full context) vs. Qwen2.5-72B-Instruct (context trimmed to match Mythos 5’s latency).
2. Measure ceiling lift (accuracy/benchmarks) and real-time trust (latency impact on live performance).
3. Execute tests with Torque owning design and Gearbox handling implementation.
4. If Mythos 5’s ceiling lift holds without catastrophic latency degradation, finalize adoption.
5. If latency criples performance, revert to Qwen2.5-72B-Instruct with optimized context.
6. Document results in `/benchmarks/excava_mythos_qwen_ab_2024.md`.

**What changed:**
Mythos 5 is now the default engine, pending live validation.
