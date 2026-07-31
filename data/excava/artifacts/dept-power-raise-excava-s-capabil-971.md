# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-971` (dept) · 2026-07-31T20:59:45.099447+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Integrate **Claude Mythos 5** into EXCAVA’s pipeline only if a stratified 10% slice A/B test proves ≥0.5% quality uplift over Fable 5.

**Plan:**
1. Torque designs a stratified 10% A/B test (balanced by task type, input length, user tier) for 72 hours.
2. Gearbox provisions parallel Mythos 5/Fable 5 endpoints with identical batch processing configs.
3. Torque logs per-task quality uplift (primary) and latency impact (secondary) for all 72 hours.
4. Torque generates a controlled A/B report with statistical significance analysis by hour 72.
5. Dynamo reviews report; if uplift ≥0.5%, Gearbox integrates Mythos 5 at 15% higher cost. Else, reject.
6. Gearbox documents integration spec post-decision.

**What changed:** Upgraded from 2%/48h to 10%/72h stratified test for robust proof.
