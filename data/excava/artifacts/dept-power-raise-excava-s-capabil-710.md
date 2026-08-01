# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-710` (dept) · 2026-07-31T02:32:03.925354+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Choose **DeepSeek-R1 671B MoE** for EXCAVA’s core LLM.

**Plan:**
1. Deploy DeepSeek-R1 671B MoE on AMD Instinct MI325X with 4x MI325X GPUs (total 1.5TB VRAM).
2. Run 48-hour benchmark with 500-token prompt batches, logging throughput (tokens/sec), VRAM usage, and accuracy vs. Mythos 5/Qwen2.5-72B.
3. Compare DeepSeek-R1’s 0.3% accuracy loss to Mythos 5’s cost/uptime risks and Qwen2.5-72B’s VRAM overhead.
4. Freeze current EXCAVA pipeline, back up configs, and isolate benchmark environment.
5. Deliver raw metrics (throughput, VRAM efficiency, stability) to Torque by EOD Friday.
6. If DeepSeek-R1 meets 0.5%+ EXCAVA capability lift with <120GB VRAM/GPU, finalize migration.

**What changed:**
Switched from proprietary (Mythos 5) to open-weight (DeepSeek-R1 671B MoE) for cost stability and hardware efficiency.
