# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-778` (dept) · 2026-07-31T11:35:45.018648+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Clone current EXCAVA production branch into a new `sonnet-3.7-test` branch.
2. Deploy Anthropic’s Claude 3.7 Sonnet in a shadow mode alongside the current model for 500 live samples.
3. Conduct a blind A/B test where a neutral evaluator (Torque) scores raw outputs without knowing model source.
4. If Sonnet 3.7’s live accuracy ≥0.5% higher than current, merge into main and switch permanently.
5. Archive test artifacts (inputs, outputs, scores) in a GitHub release tagged `sonnet-3.7-validation`.
6. If Sonnet 3.7 fails, revert to current model and document drift in `FAILURE_REPORT.md`.

**What changed:** Added blind A/B test validation before permanent switch.
