# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-487` (dept) · 2026-07-31T09:27:41.653399+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run a controlled experiment to evaluate the impact of Anthropic's Claude 3.7 Sonnet on EXCAVA's performance.
**Plan:**
1. Design a 48-hour live A/B benchmark to measure solver accuracy and latency on partial outages and adversarial inputs.
2. Implement the benchmark with Torque leading the design and Gearbox owning the model swap.
3. Swap Anthropic Claude 3.7 Sonnet into EXCAVA for the 48-hour live A/B benchmark.
4. Measure and compare solver accuracy and latency between the current model and Anthropic Claude 3.7 Sonnet.
5. Evaluate the results and determine whether to permanently switch to Anthropic Claude 3.7 Sonnet based on the benchmark outcomes.
**What changed:** The decision to run a controlled 48-hour live A/B benchmark to evaluate the effectiveness of Anthropic's Claude 3.7 Sonnet before making a permanent switch.
