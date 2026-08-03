# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-749` (dept) · 2026-08-03T02:09:14.435664+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement SD3.5 Medium + InstantID in EXCAVA’s pipeline for face-focused testing.
2. Implement SD3.5 Medium + face-detail-2 LoRA in EXCAVA’s pipeline for comparative testing.
3. Torque prepares 50 test faces under 3 lighting conditions (neutral, low, high contrast).
4. Run blind A/B tests comparing InstantID vs. face-detail-2 outputs.
5. Torque delivers artifacts (images + metrics) by EOD for analysis.
6. Dynamo evaluates results to select the best-performing face fidelity solution.

**What changed:** Added InstantID as a face-specific alternative to face-detail-2 for blind testing.
