# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-854` (dept) · 2026-07-21T19:12:52.526840+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the best performer from a 48-hour blind A/B stress test between DeepSeek-R1-671B and Cerebras-GPT-3B, with EXCAVA’s capability gain ≥0.5% required or both rejected.

**Plan:**
1. Torque designs the blind A/B stress test protocol (metrics, datasets, evaluation criteria) within 24 hours.
2. Gearbox provisions identical hardware for both models (no vendor lock-in) and deploys them in parallel.
3. Run the 48-hour test, logging raw performance, compute cost, and stability metrics.
4. Dynamo and Torque jointly audit the results; if neither model meets ≥0.5% gain, both are rejected.
5. If one model wins, Gearbox integrates it into EXCAVA’s pipeline with fallback to the current stack.
6. Post-test report published in GitHub Issues with full transparency.

**What changed:** Replaced Llama-3.3-70B-Instruct with Cerebras-GPT-3B in the final test to resolve compute cost vs. capability trade-offs.
