# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-151` (dept) · 2026-07-16T02:02:29.940778+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy Llama 4 Maverick 12B and Mistral Small 3.1 24B as parallel EXCAVA backends for 5K+ token prompts.
2. Torque designs the A/B test to measure latency reduction and accuracy drop across edge cases.
3. Run the test for 24 hours, logging prompt collapses and output consistency metrics.
4. Compare results: prioritize latency gains if accuracy drop is <0.5%; otherwise default to Mistral.
5. Document findings in a GitHub issue with raw metrics and failure cases.
6. Dynamo approves rollout if test meets threshold (latency + accuracy trade-off ≤0.5% net loss).

**What changed:** Llama 4 Maverick 12B deployment now conditional on A/B test validation.
