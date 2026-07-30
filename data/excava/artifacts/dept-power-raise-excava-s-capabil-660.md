# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-660` (dept) · 2026-07-30T17:31:50.565201+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 100-hour blind A/B bake-off on 5,000 live EXCAVA tasks comparing Llama 3.3 70B vs. Mistral Large 2 vs. Claude Mythos 5, defaulting to the fastest model that meets accuracy thresholds, escalating only when uncertainty is flagged—result must deliver quantified capability uplift.

**Plan:**
1. **Define metrics**: Establish accuracy thresholds (e.g., 95% factual correctness) and latency ceilings (e.g., 1.5s p95) for EXCAVA’s core tasks.
2. **Model selection**: Deploy Llama 3.3 70B, Mistral Large 2, and Claude Mythos 5 in parallel, with a distilled 8B-13B model as the baseline default.
3. **Blind testing**: Randomly route 5,000 live tasks across models without user knowledge; log outputs, latency, and uncertainty flags.
4. **Escalation logic**: Auto-escalate to 70B/Claude Mythos 5 if the 8B model’s uncertainty score exceeds a predefined threshold (e.g., 0.7).
5. **Analysis**: After 100 hours, compare accuracy/latency trade-offs; select the fastest model meeting thresholds, with quantified uplift vs. baseline.
6. **Rollout**: Implement the winning model as default, retaining others for edge cases.

**What changed:**
Default to fastest model meeting thresholds, escalate only on uncertainty—quantify capability uplift via bake-off.
