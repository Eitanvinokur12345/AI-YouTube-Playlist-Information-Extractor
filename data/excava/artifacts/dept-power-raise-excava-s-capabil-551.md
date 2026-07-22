# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-551` (dept) · 2026-07-22T11:46:21.751429+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Llama-3.3-70B-Instruct for EXCAVA with a 24-hour blind A/B test against Qwen3-235B-A22B-Instruct.

**Plan:**
1. Gearbox provisions Llama-3.3-70B-Instruct and Qwen3-235B-A22B-Instruct in EXCAVA’s pipeline.
2. Torque sets up latency measurement tools (per-query and batch throughput).
3. Gearbox designs a blind A/B test with identical input sets, randomized model assignment.
4. Run the test for 24 hours, logging accuracy (via EXCAVA’s eval harness) and latency (per query + batch).
5. Torque analyzes latency data; Gearbox analyzes accuracy delta vs. baseline.
6. Dynamo reviews results and finalizes model selection within 48 hours post-test.

**What changed:**
Switched from DeepSeek-R1-671B/Qwen3-235B-A22B-Instruct to Llama-3.3-70B-Instruct with A/B validation.
