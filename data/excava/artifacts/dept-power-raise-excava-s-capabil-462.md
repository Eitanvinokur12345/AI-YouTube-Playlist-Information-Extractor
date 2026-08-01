# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-462` (dept) · 2026-07-31T15:10:21.760679+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Audit EXCAVA’s footage to flag shots with lighting, depth, or motion inconsistencies.
2. Pre-process only flagged shots using Runway Gen-4 for stabilization, preserving unflagged shots’ original style.
3. Validate pre-processed outputs against EXCAVA’s visual signature to ensure consistency.
4. Insert new elements into pre-processed shots using EXCAVA’s toolkit for pixel-perfect blending.
5. Batch-test a subset of outputs to measure quality uplift before full pipeline rollout.
6. Document compute cost vs. quality gains for future optimization.

**What changed:** Pre-processing is now selective (problematic shots only) instead of universal.
