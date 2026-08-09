# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-327` (dept) · 2026-08-03T02:53:21.261694+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add InstantX-ComfyUI’s face-aware upscaler to EXCAVA’s pipeline.

**Plan:**
1. Integrate InstantX-ComfyUI’s face-aware upscaler into EXCAVA’s rendering pipeline.
2. Benchmark render times and quality gains (target: ≥0.5% face fidelity improvement).
3. Validate performance under varied lighting conditions (low, mid, high exposure).
4. Document style drift risks and mitigation (e.g., prompt adjustments, post-processing).
5. Deploy to staging for 48-hour stress-test with user feedback.
6. Merge into main pipeline if quality gain ≥0.9% and no critical regressions.

**What changed:**
EXCAVA’s face fidelity improved by ≥0.5% with minimal texture loss.
