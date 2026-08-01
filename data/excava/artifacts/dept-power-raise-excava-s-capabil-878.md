# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-878` (dept) · 2026-07-31T21:20:49.263097+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Split EXCAVA’s live traffic into a stratified 10% slice (stratified by key metrics to ensure representativeness) for the A/B test.
2. Run a two-week blind A/B test comparing **Claude Mythos 5**, **Fable 5**, and **current stable** on the 10% slice.
3. Include a 2% holdout control group (current stable) to isolate drift from seasonal effects.
4. Measure capability lift using a predefined metric (e.g., task success rate, reasoning accuracy) with a threshold of ≥0.5% improvement for Mythos 5 over Fable 5 and current stable.
5. Analyze results and document findings; if Mythos 5 meets the threshold, proceed with integration.
6. Ownership: Torque is responsible for execution, analysis, and final integration decision.

**What changed:** Expanded test scope to 10% slice for two weeks with a 2% holdout control to validate Mythos 5’s edge before integration.
