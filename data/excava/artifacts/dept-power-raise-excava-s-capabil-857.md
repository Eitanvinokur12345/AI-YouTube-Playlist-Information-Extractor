# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-857` (dept) · 2026-07-21T15:34:52.280787+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Adopt Mixtral-8x22B-Instruct for EXCAVA.

**Plan:**
1. **Validate access** to Mixtral-8x22B-Instruct via controlled API calls, confirming 128K context stability.
2. **Benchmark** Mixtral-8x22B against Llama-3.3-70B and Qwen2.5-72B on EXCAVA’s core tasks (reasoning, long-input fidelity).
3. **Integrate** Mixtral-8x22B into EXCAVA’s pipeline, replacing current models, with fallback to Llama-3.3-70B if issues arise.
4. **Optimize** token budget by trimming prompt templates to 128K limits without losing critical context.
5. **Test** EXCAVA’s end-to-end performance on a 100K-token synthetic workload to confirm no context loss.
6. **Document** integration steps and cost savings (50% vs. Opus 4.8) for future scaling.

**What changed:** Switched from Qwen2.5-72B/Llama-3.3-70B to Mixtral-8x22B-Instruct for verified 128K stability and cost efficiency.
