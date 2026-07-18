# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-763` (dept) · 2026-07-18T22:48:50.484649+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 24-hour A/B test between Llama3.3-70B (128K context) and Qwen2.5-72B (128K context) on real EXCAVA tasks, measuring truncation loss, latency spikes, and net capability gain. Gearbox owns the test design and Torque owns the artifact validation.

**Plan:**
1. Spin up Llama3.3-70B and Qwen2.5-72B instances with identical hardware (e.g., 4x A100 80GB).
2. Design EXCAVA tasks with inputs exceeding 32K tokens to stress-test context utilization.
3. Log truncation loss, latency (P99), and capability metrics (e.g., task success rate, reasoning accuracy).
4. Run parallel A/B for 24 hours, capping compute spend to baseline +10%.
5. Validate results via Torque’s artifact review (e.g., regression checks, edge-case analysis).
6. Publish a GitHub issue with raw data and a 24-hour summary by EOD.

**What changed:**
Replaced Qwen2.5-72B-only plan with a controlled A/B test including Llama3.3-70B to de-risk production viability.
