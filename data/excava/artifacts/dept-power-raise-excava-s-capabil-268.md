# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-268` (dept) · 2026-07-29T21:19:18.741565+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a blind A/B test on 1,000 live EXCAVA tasks comparing Qwen 2.5-72B-Instruct (current) vs. Claude 3.7 Sonnet (new), measuring latency drop and accuracy regression before any default switch.

**Plan:**
1. Torque designs the A/B test, ensuring identical input preprocessing and blind evaluation for both models.
2. Dynamo provisions a dedicated test environment with isolated compute to prevent interference with production.
3. Gearbox integrates Claude 3.7 Sonnet into the test harness alongside Qwen 2.5-72B-Instruct.
4. Torque executes the test over one full workload cycle, logging latency and accuracy metrics per task.
5. Gearbox and Torque jointly analyze results, with Dynamo arbitrating any disputes.
6. If Sonnet 3.7 meets latency and accuracy thresholds, Gearbox proposes a phased rollout; otherwise, it’s rejected.

**What changed:**
Added a controlled A/B test to validate Sonnet 3.7’s impact before any default adoption.
