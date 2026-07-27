# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-923` (dept) · 2026-07-27T22:32:06.482645+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Llama-4-Maverick-12B-Instruct as EXCAVA’s primary inference engine after blind benchmark validation.

**Plan:**
1. Gearbox sets up a blind A/B benchmark comparing Qwen3-235B-A22B-Instruct and Llama-4-Maverick-12B-Instruct.
2. Torque executes the benchmark on 100 long EXCAVA documents, measuring long-document accuracy and sustained throughput.
3. Torque analyzes results and reports findings within 48 hours.
4. If Llama-4-Maverick-12B-Instruct meets or exceeds the 0.5% capability gain with no >20% context-window penalty, Gearbox deploys it.
5. If Qwen3-235B-A22B-Instruct wins, Gearbox adopts it with MoE throughput optimization.
6. Dynamo archives the benchmark data and updates EXCAVA’s model registry.

**What changed:**
Primary inference engine now pending benchmark validation (Llama-4-Maverick-12B-Instruct or Qwen3-235B-A22B-Instruct).
