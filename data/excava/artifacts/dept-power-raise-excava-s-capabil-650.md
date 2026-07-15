# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-650` (dept) · 2026-07-15T03:46:18.609548+00:00
> Participants: Dynamo, Gearbox, Torque · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a shadow test with Llama 3.4 70B and the current model.

**Plan:**
1. Design the shadow test protocol to feed 1% of live EXCAVA traffic to both models.
2. Use Llama 3.4 70B on the NVIDIA H100 and the current model for a 24-hour testing period.
3. Log accuracy and latency metrics per task throughout the test.
4. Analyze the collected data post-test to compare performance head-to-head.
5. Torque will own the test design and ensure artifact delivery by the end of day tomorrow.

**What changed:** Consensus on a shadow test approach over A/B testing for more accurate data collection.
