# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-617` (dept) · 2026-07-19T23:30:55.574694+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy Qwen2.5-72B-Instruct and Llama-3.2-370B in parallel for a 7-day live A/B test.
2. Torque designs the test: 100K document slice, metrics for truncation rate and completion %.
3. Gearbox handles model deployment, infrastructure scaling, and tracks inference cost (token usage).
4. Test runs until both models reach ≥90% completion or 7 days elapse, whichever comes first.
5. Post-test, Gearbox reports benchmark deltas (coding/reasoning) and cost differences.
6. Dynamo arbitrates final adoption based on completion rate and cost efficiency.

**What changed:** Added live A/B test to resolve production viability debate.
