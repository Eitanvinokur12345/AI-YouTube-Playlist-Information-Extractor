# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-877` (dept) · 2026-07-27T18:19:28.906146+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a 48-hour blind A/B stress test on EXCAVA’s 8xA100 node comparing pruned DeepSeek-R1-405B vs. DeepSeek-R1-671B.

**Plan:**
1. Set up the 8xA100 node to run both DeepSeek-R1-405B and DeepSeek-R1-671B models.
2. Design a blind A/B test framework for performance evaluation.
3. Measure and document throughput, latency, and cost for both models during the 48-hour test.
4. Analyze results to determine if pruned DeepSeek-R1-405B achieves a greater than 0.5% capability gain with lower cost and stable latency compared to DeepSeek-R1-671B.
5. Make a final decision based on A/B test results regarding the adoption of the preferred model.

**What changed:** Decided to test a pruned model to potentially improve cost-efficiency and latency.
