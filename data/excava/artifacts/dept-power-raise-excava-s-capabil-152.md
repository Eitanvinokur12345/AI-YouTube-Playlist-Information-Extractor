# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-152` (dept) · 2026-07-28T23:05:24.836479+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Qwen2.5-72B-Instruct as EXCAVA’s primary reasoning engine and Claude Mythos 5 as secondary, contingent on latency validation.

**Plan:**
1. Run a live 10-task A/B benchmark comparing Qwen2.5-72B-Instruct and Claude Mythos 5 with a strict 2-second timeout per task.
2. Measure latency, success rate, and output quality for both models under identical conditions.
3. If Claude Mythos 5 fails the timeout threshold, retain Qwen2.5-72B-Instruct as primary and Mythos as secondary.
4. If Mythos passes, deploy it as secondary with Qwen as primary for non-real-time tasks.
5. Document latency thresholds and model IDs for future reference.
6. Update EXCAVA’s model registry with the validated configuration.

**What changed:**
Latency validation now dictates secondary model adoption.
