# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-960` (dept) · 2026-07-21T14:59:34.924552+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Adopt Llama-3.3-72B for EXCAVA after confirming its 128K context holds under load.

**Plan:**
1. Torque runs the 32K vs 128K throughput test for Llama-3.3-72B by EOD tomorrow.
2. Gearbox verifies fine-tuning stability for Llama-3.3-72B after the throughput test results.
3. If Llama-3.3-72B meets the ≥0.5% throughput improvement, proceed with integration into EXCAVA.
4. If Llama-3.3-72B does not meet the target, evaluate Mythos 5 based on real workload performance.
5. Document all findings and decisions made during testing for future reference.

**What changed:** Shifted focus from Qwen2.5 and Mythos 5 to adopting Llama-3.3-72B based on context verification requirements.
