# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-367` (dept) · 2026-07-31T20:38:20.381009+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Integrate **Claude Mythos 5** into EXCAVA’s pipeline via a stratified 10% slice A/B test, switching only if quality lift ≥0.5%.

**Plan:**
1. **Slice Selection:** Stratify 10% of EXCAVA’s data across all task types (randomized, no overlap).
2. **A/B Test:** Run parallel pipelines—Fable 5 (control) vs. Mythos 5 (experimental)—logging identical inputs/outputs.
3. **Metrics:** Track quality lift (primary: task accuracy/precision; secondary: latency/cost).
4. **Threshold:** If lift ≥0.5%, proceed to full integration; else, discard Mythos 5.
5. **Artifact:** Public GitHub repo with raw data, code, and results (Torque owns maintenance).
6. **Rollback:** Fable 5 remains default; Mythos 5 only adopted post-validation.

**What changed:** Stratified 10% slice replaces blind 2% test; public artifact enforced.
