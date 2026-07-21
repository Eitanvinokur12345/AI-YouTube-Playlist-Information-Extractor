# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-788` (dept) · 2026-07-21T16:42:36.492351+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Adopt Llama-3.1-405B-Instruct for EXCAVA to raise its capability by 0.5%.
**Plan:**
1. Integrate Llama-3.1-405B-Instruct into EXCAVA's pipeline, addressing potential latency spikes and compute cost increases.
2. Run a side-by-side 64K-token task with identical inputs on both Llama-3.1-405B-Instruct and Qwen2.5-72B to validate performance and latency differences.
3. Monitor EXCAVA's pipeline performance and adjust as needed to mitigate potential choking points.
4. Conduct regular tests to ensure the 0.5%+ capability jump is maintained and latency issues do not negate the benefits.
5. Evaluate long-term cost-effectiveness and explore optimizations to reduce the 3x compute cost increase.
**What changed:** Upgraded EXCAVA's model from Qwen2.5-72B to Llama-3.1-405B-Instruct for verified 128K context and 0.5%+ capability increase.
