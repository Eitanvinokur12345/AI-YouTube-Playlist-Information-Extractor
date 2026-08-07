# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-158` (dept) · 2026-08-07T07:55:16.845116+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate ComfyUI’s open-source FaceDetailer node with SD3.5’s face model into EXCAVA’s pipeline to lock face fidelity.
2. Process outputs through InstantX-ComfyUI’s depth-aware upscaler to sharpen details without hallucination.
3. Benchmark face clarity and detail retention against EXCAVA’s current output in a controlled side-by-side.
4. Measure EXCAVA’s overall output quality improvement (target: ≥0.5% boost in capability).
5. If results meet or exceed expectations, merge the pipeline changes into the main branch.
6. Document trade-offs (e.g., 1-2% speed drop during upscaling) and validate downstream task compatibility.

**What changed:** EXCAVA’s pipeline now combines FaceDetailer for face fidelity + depth-aware upscaling for detail retention.
