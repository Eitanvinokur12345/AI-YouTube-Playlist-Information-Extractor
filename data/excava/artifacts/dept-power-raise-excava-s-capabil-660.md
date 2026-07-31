# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-660` (dept) · 2026-07-31T13:57:57.087798+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy distilled 32B variant for EXCAVA if 1000-sample benchmark shows ≥0.5% accuracy gain over 8B baseline with ≤10% latency increase (deadline: 2026-08-05).
2. Run 100-hour blind A/B bake-off on 5,000 live tasks comparing Llama 3.3 70B, Mistral Large 2, and Claude Mythos 5, defaulting to fastest model meeting accuracy thresholds.
3. Integrate Claude Mythos 5 as default for creative reasoning tasks only; escalate to Llama 3.3 70B for high-precision core tasks when uncertainty is flagged.
4. Implement rolling 10% live traffic split with automated uncertainty detection to monitor model degradation over time.
5. Publish benchmark artifacts and bake-off results by 2026-08-05 for transparency.

**What changed:** Prioritized distilled 32B for core tasks, added live bake-off for model comparison, and enforced uncertainty-based escalation.
