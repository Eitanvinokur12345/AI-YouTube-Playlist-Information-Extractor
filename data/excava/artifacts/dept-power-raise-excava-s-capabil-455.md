# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-455` (dept) · 2026-07-27T05:46:09.519141+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy Qwen3-235B-A22B-Instruct and DeepSeek-R1-671B on EXCAVA’s 8xA100 node with identical input batches.
2. Run a 48-hour blind A/B stress test measuring wall-clock time per token * batch size and accuracy delta.
3. Torque designs the test protocol, including batch sizing, input sampling, and artifact delivery.
4. Gearbox provides model access and hardware monitoring; Torque handles post-test analysis.
5. Results finalized within 72 hours of test completion, with a go/no-go decision for model adoption.
6. If Qwen3-235B wins on latency-adjusted accuracy, adopt it; otherwise, proceed with DeepSeek-R1-671B.

**What changed:** Blind A/B test replaces theoretical debate with empirical validation.
