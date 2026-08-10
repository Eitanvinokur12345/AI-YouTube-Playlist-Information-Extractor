# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-555` (dept) · 2026-08-10T15:33:21.345805+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s pipeline and benchmark its impact on excavation edge preservation in motion-blurred footage.
2. Run a single-frame face fidelity test comparing InstantX-ComfyUI’s depth-aware upscaler and RealVisXL 5.0’s face-preserving upscaler to assess static frame quality.
3. If InstantX-ComfyUI shows superior edge preservation, proceed to full pipeline testing; otherwise, evaluate RealVisXL’s face upscaler for static face fidelity.
4. Measure processing speed trade-offs for both upscalers and document any motion artifact persistence.
5. If neither upscaler resolves core distortions, escalate to model retraining or alternative tooling.

**What changed:** Prioritized depth-aware upscaling for edge preservation before face fidelity, with single-frame validation to isolate core distortions.
