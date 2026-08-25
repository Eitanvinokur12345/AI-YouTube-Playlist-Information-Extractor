# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-938` (dept) · 2026-08-25T06:57:58.010305+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add MPRNet blind-deblurring to EXCAVA’s input pipeline before any upscaling—test it against FILM on worst-case samples to cut motion blur at the source.

**Plan:**
1. Integrate MPRNet into EXCAVA’s preprocessing stage as a mandatory step before upscaling.
2. Benchmark MPRNet-deblurred inputs against original frames using EXCAVA’s worst-case samples (high motion blur).
3. Compare MPRNet’s output against FILM upscaler results to quantify clarity gains vs. temporal fixes.
4. Optimize MPRNet’s runtime to minimize latency impact on EXCAVA’s pipeline.
5. If MPRNet improves clarity by ≥0.5% on benchmark samples, merge into main branch; else, iterate.
6. Document integration steps and performance metrics in `/docs/MPRNet_deblur_integration.md`.

**What changed:**
MPRNet blind-deblurring added to EXCAVA’s input pipeline.
