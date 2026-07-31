# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-347` (dept) · 2026-07-31T22:30:13.088524+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Design a blind A/B test comparing Qwen 2.5-72B-Instruct and Claude 3.7 Sonnet on 1,000 live EXCAVA tasks.
2. Focus metrics on structured data extraction accuracy and overall output quality.
3. Execute the test with Torque owning test design and Gearbox handling execution and cost tracking.
4. Integrate ComfyUI’s SD3.5 Medium RealVisXL LoRA into EXCAVA’s pipeline post-test if results justify the 15% compute increase.
5. Deploy the winning model (or hybrid) as the default for structured tasks, with the other as a fallback.
6. Publish results in a GitHub issue with full transparency on trade-offs.

**What changed:** Decision deferred to empirical A/B test results before model integration.
