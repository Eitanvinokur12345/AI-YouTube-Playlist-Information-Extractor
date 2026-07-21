# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-326` (dept) · 2026-07-21T16:08:31.995267+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Adopt Command R+ for EXCAVA.

**Plan:**
1. Replace Qwen2.5-72B-Instruct with Command R+ in EXCAVA’s model stack.
2. Validate Command R+’s 128K long-context performance via LongBench stress tests.
3. Benchmark Command R+ against Llama-3.3-72B-Instruct at 64K/128K to confirm +0.5%+ lift.
4. Optimize compute allocation for Command R+’s resource demands (e.g., dynamic batching).
5. Document trade-offs (latency, cost) and fallback to Kimi K2 if Command R+ underperforms.
6. Integrate Command R+ into production pipeline with phased rollout (10% → 50% → 100%).

**What changed:** Switched from unverified Qwen2.5-72B/Llama-3.3-72B claims to Command R+’s proven 128K long-context.
