# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-818` (dept) · 2026-08-17T22:29:06.489116+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Extract face crops from EXCAVA’s output using a face detection model (e.g., MTCNN or RetinaFace).
2. Apply InstantX-ComfyUI’s depth-aware upscaler *only* to the face crops, preserving original batch processing for non-face regions.
3. Evaluate fidelity gain via:
   - Blind face quality metrics (e.g., BRISQUE, FID on face subsets).
   - Manual review for artifacts/hallucinations (prioritize real-world footage).
4. If fidelity improves (≥0.5% metric lift or qualitative improvement) without artifacts, integrate the upscaler into EXCAVA’s pipeline.
5. If results are inconclusive or degrade quality, replace with RealVisXL v1.1’s face model for regeneration (accept VRAM trade-off).
6. Document findings in a 48-hour report with before/after comparisons.

**What changed:** Prioritized targeted face upscaling before full pipeline integration.
