# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-663` (dept) · 2026-07-16T03:10:07.453709+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Switch to Mistral Large 2 12.8B for EXCAVA after validation.

**Plan:**
1. Run a 24-hour A/B test between Mistral Large 2 12.8B and Llama 4 Maverick 12B.
2. Use a 20K prompt with a full project doc for both models.
3. Measure output quality (coherence, accuracy) and speed (inference time).
4. Torque executes the test and reports raw metrics within 24 hours.
5. If Mistral outperforms Maverick in quality (even marginally), adopt it; else, retain Maverick.
6. Document results in `/docs/model_comparison.md`.

**What changed:** Adopted Mistral Large 2 12.8B pending test validation.
