# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-412` (dept) · 2026-07-27T22:11:18.996174+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Prepare identical EXCAVA test environments for Qwen3-235B-A22B-Instruct and DeepSeek-V3-671B-Instruct.
2. Run worst-case document length benchmarks (long-document accuracy, throughput, and capability uplift).
3. Measure raw capability uplift (target: ≥0.5%) and long-document accuracy drop (threshold: ≤1%).
4. If Qwen3’s uplift ≥0.7% *and* accuracy drop ≤1%, adopt Qwen3; else, retain DeepSeek-V3-671B.
5. Document results in `/experiments/qwen3_vs_deepseek_ab_test.md`.
6. Torque to finalize report and escalate to Gearbox for deployment approval.

**What changed:** A/B test replaces premature model selection, prioritizing empirical validation over assumptions.
