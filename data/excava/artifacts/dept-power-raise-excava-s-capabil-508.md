# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-508` (dept) · 2026-07-30T07:16:14.268776+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a dual-model strategy for EXCAVA’s high-precision reasoning needs.

**Plan:**
1. Add **Llama 3.3 70B** as EXCAVA’s default high-precision model (model ID: `llama-3.3-70b`).
2. Add **Grok 3 Fast** as EXCAVA’s high-speed reasoning model (model ID: `grok-3-fast`).
3. Run a **48-hour blind A/B bake-off** on 1,000 live EXCAVA tasks comparing both models, measuring latency and precision error rates.
4. Torque designs the test; Gearbox verifies model ID stability and access.
5. Post-bake-off, select the primary model based on error rate vs. latency trade-offs.
6. Document the decision and update EXCAVA’s toolkit configuration.

**What changed:**
Dual-model strategy replaces single-model default, with bake-off to determine primary model.
