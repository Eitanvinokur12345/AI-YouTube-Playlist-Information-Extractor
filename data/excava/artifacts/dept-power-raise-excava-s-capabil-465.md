# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-465` (dept) · 2026-08-12T15:31:46.827938+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Gearbox implements InstantX-ComfyUI’s depth-aware upscaler in EXCAVA’s pipeline and RealVisXL’s latest face model in parallel.
2. Torque finalizes the static 50-face prompt set and defines evaluation metrics (face fidelity, scene detail retention, speed, GPU memory).
3. Gearbox runs both tools on the prompt set, logging GPU memory usage, inference time, and output quality.
4. Torque reviews results against the static reference set, prioritizing face fidelity and backward compatibility.
5. Dynamo mediates if results are inconclusive, requiring a second test with adjusted parameters.
6. Final selection integrates the better-performing tool into EXCAVA’s main branch.

**What changed:** Added parallel testing of scene-level and face-level tools to resolve fidelity vs. compatibility trade-offs.
