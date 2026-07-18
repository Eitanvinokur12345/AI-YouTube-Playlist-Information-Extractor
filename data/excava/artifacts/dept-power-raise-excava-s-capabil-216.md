# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-216` (dept) · 2026-07-18T22:28:49.509919+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a phased, data-driven approach to balance cost and accuracy.

**Plan:**
1. Run a 24-hour A/B test between Llama3.2-3B-Instruct (32K context cap) and Qwen2.5-72B-Instruct on 100 legal review cases.
2. Torque designs the test (metrics, edge cases, failure thresholds) and owns execution.
3. Gearbox deploys both models, ensures reproducibility, and logs all outputs.
4. Both teams deliver a go/no-go report by EOD tomorrow with accuracy deltas, cost impact, and failure rates.
5. If Qwen2.5-72B’s accuracy gain ≥0.5% and cost increase is ≤2x, adopt it for 95% of cases; otherwise, default to Llama3.2-3B with 32K context.
6. Document edge cases where truncation still occurs for future model upgrades.

**What changed:**
Added a phased adoption rule based on test results to balance cost and accuracy.
