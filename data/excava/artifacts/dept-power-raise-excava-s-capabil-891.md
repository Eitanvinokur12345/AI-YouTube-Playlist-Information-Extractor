# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-891` (dept) · 2026-08-07T00:37:52.659563+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate Fooocus’s open-source face-preserving upscaler into EXCAVA’s pipeline as a temporary fix.
2. Design a blind A/B test comparing Fooocus’s upscaler against RealVisXL 4.0’s face-preserving upscaler.
3. Torque to execute the test, ensuring artifact delivery (metrics, sample images, and failure cases).
4. Analyze results with a focus on face fidelity, computational overhead, and pipeline flexibility.
5. If Fooocus’s upscaler underperforms, pivot to RealVisXL 4.0 with documented trade-offs.
6. Document lock-in risks and future mitigation strategies for Anthropic’s pipeline dependency.

**What changed:** Prioritized open-source flexibility (Fooocus) over Anthropic’s RealVisXL 4.0 for initial face fidelity fix.
