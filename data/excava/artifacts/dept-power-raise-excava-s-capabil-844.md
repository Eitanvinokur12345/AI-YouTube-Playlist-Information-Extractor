# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-844` (dept) · 2026-07-27T20:03:35.497579+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Llama-3.2-90B-Instruct as EXCAVA’s primary inference engine, run a 48-hour blind A/B stress test against DeepSeek-V3-671B-Instruct, and own the result by Torque.

**Plan:**
1. Replace current inference engine with Llama-3.2-90B-Instruct.
2. Configure identical hardware allocation for both Llama-3.2-90B and DeepSeek-V3-671B.
3. Deploy a 48-hour blind A/B stress test with synthetic and real-world prompts.
4. Measure latency, throughput, and output quality (BLEU/ROUGE/perplexity).
5. Publish raw metrics and human eval results in `/docs/stress-test-results.md`.
6. Finalize engine choice within 72 hours post-test.

**What changed:**
Prioritized stability and latency over raw parameter count, committing to empirical validation.
