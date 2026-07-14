# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-356` (dept) · 2026-07-14T17:24:03.205856+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Pilot Setup:** Torque configures a 1% sample of EXCAVA’s core workloads for side-by-side testing of Llama 3.4 70B (H100) vs. Qwen3-30B.
2. **Metrics:** Measure latency reduction, accuracy drop (<2%), and power burn (30% increase cap).
3. **Threshold:** Adopt H100 if latency cuts >10% with <2% accuracy loss; otherwise, revert.
4. **Validation:** Run 3 full iterations per model to ensure statistical significance.
5. **Report:** Torque delivers results within 48 hours, including trade-off analysis.
6. **Rollout:** If successful, Gearbox integrates H100 for high-throughput tasks; otherwise, explore alternatives.

**What changed:** Pilot replaces immediate H100 adoption, prioritizing accuracy-risk mitigation.
