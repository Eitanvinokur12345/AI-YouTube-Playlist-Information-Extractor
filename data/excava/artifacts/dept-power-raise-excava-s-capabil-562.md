# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-562` (dept) · 2026-07-30T20:29:37.648589+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Use Anthropic Claude 3.7 Sonnet as EXCAVA’s core reasoning engine after validating its real-world impact via a live pilot.

**Plan:**
1. **Pilot Setup:** Deploy both Claude 3.7 Sonnet and Mythos 5 in parallel for 1,000 live user tasks.
2. **Metrics:** Track user complaints (hallucinations/errors) and latency for both models.
3. **Blind Evaluation:** Hide model identities from users and analysts to prevent bias.
4. **Threshold:** If Claude 3.7 Sonnet reduces complaints by ≥0.5% *or* improves latency by ≥0.5% over Mythos 5, promote it to primary.
5. **Rollback Plan:** Revert to Mythos 5 if complaints spike >1% or latency degrades >2%.
6. **Ownership:** Torque leads pilot execution and analysis.

**What changed:**
Live pilot replaces blind benchmarking to prioritize real-world EXCAVA performance.
