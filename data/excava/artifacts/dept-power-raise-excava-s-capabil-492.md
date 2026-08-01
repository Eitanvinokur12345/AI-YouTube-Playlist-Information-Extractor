# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-492` (dept) · 2026-07-31T10:26:25.743978+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a 12-hour synthetic stress test on the worst 10% of EXCAVA’s live queries using Anthropic’s Claude 3.7 Sonnet.
2. Measure drift against current Haiku variant; if drift ≤ 0.1%, proceed.
3. If stable, dispatch 2 workers to execute a 48-hour live A/B test between Sonnet 3.7 and Haiku on the same query slice.
4. Log response time, accuracy, and drift metrics in real time during the A/B test.
5. If Sonnet 3.7 outperforms Haiku by ≥ 0.5% with no critical drift, approve the 20% cost premium for full deployment.
6. If drift exceeds 0.1% in stress test or underperforms in A/B, revert to Haiku and reassess.

**What changed:** Added synthetic stress test before live A/B to mitigate drift risk.
