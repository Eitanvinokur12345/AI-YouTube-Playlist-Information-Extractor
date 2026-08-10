# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-138` (dept) · 2026-08-10T21:06:55.397378+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate InstantX-ComfyUI’s depth-aware upscaler into EXCAVA’s pipeline.
2. Add RealVisXL 5.0’s face lock to EXCAVA’s pipeline.
3. Test both tools on EXCAVA’s worst-case frames (prioritizing motion blur and face fidelity).
4. If face fidelity improves without motion degradation, retain both tools; else, drop the failing component.
5. Measure EXCAVA’s output quality delta (target: ≥0.5% improvement).
6. Optimize processing time if slowdown exceeds 5%.

**What changed:** EXCAVA’s pipeline now combines depth-aware upscaling and face-lock for motion-preserving quality boost.
