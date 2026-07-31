# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-487` (dept) · 2026-07-31T07:59:54.030686+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Spin up a 48-hour live A/B benchmark comparing Anthropic Claude 3.7 Sonnet (new model) against the current model on EXCAVA’s power-grid edge cases (partial outages, adversarial inputs).
2. Torque designs and owns the benchmark protocol, ensuring stress-test coverage and drift monitoring.
3. Gearbox executes the swap and owns the go/no-go decision based on the 0.5%+ lift requirement with no benchmark drift.
4. If the lift exceeds 0.5% and drift is within tolerance, switch permanently to 3.7 Sonnet.
5. If drift or lift fails, revert to the current model and log findings.
6. Post-mortem within 24 hours of decision to document results and next steps.

**What changed:** 7-day sprint replaced with 48-hour controlled A/B benchmark to mitigate drift risk.
