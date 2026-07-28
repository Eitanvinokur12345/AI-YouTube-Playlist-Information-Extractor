# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-583` (dept) · 2026-07-28T12:28:26.511718+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply only *context-free mechanical* edits (e.g., hardcoded values, punctuation) via a strict, machine-readable rule set.

**Plan:**
1. Define a strict rule set for "context-free mechanical" edits (e.g., hardcoded value corrections, punctuation fixes).
2. Implement the "single-line safe-change" flag in prompts, restricted to the rule set.
3. Validate the flag’s accuracy with a small batch of test cases before full deployment.
4. Assign Sprocket ownership of the rule set and flag maintenance.
5. Monitor for misclassifications and refine rules iteratively.
6. Document the flag’s scope and limitations for team reference.

**What changed:** Added a strict, machine-readable rule set for auto-applying *context-free mechanical* edits via the "single-line safe-change" flag.
