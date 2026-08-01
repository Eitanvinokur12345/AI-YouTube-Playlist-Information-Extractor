# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-345` (dept) · 2026-07-31T01:43:13.699945+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy DeepSeek-V3 (671B MoE) on Cerebras CS-3 for a 48-hour benchmark.
2. Torque to own the artifact proving throughput vs. Qwen2.5-72B on EXCAVA’s core workloads.
3. Compare latency, cost, and iteration speed between DeepSeek-V3 and Qwen2.5-72B.
4. If DeepSeek-V3 meets or exceeds Qwen2.5-72B’s performance, adopt it as EXCAVA’s core LLM.
5. If throughput bottlenecks emerge, evaluate hybrid MoE/dense fallback (e.g., Mistral 8x22B).
6. Freeze model choice for 30 days post-decision to allow stability validation.

**What changed:** Switched from Qwen2.5-72B to DeepSeek-V3 for EXCAVA’s core LLM workloads.
