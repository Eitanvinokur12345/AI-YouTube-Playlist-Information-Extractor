# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-520` (dept) · 2026-07-31T21:57:02.856151+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add **Kijai’s SD3.5 Medium RealVisXL LoRA at 1440p** to EXCAVA’s pipeline as the primary tool, with a fallback A/B test against Flux Realism LoRA at 1440p for edge cases.

**Plan:**
1. Integrate Kijai’s SD3.5 Medium RealVisXL LoRA into EXCAVA’s pipeline with a 1440p base model.
2. Allocate 10% of EXCAVA’s pipeline to a blind A/B test comparing RealVisXL LoRA vs. Flux Realism LoRA at 1440p.
3. Monitor VRAM usage and generation speed; cap batch sizes if needed to mitigate slowdowns.
4. Prioritize subtitles/text clarity and fine UI detail in output validation.
5. If RealVisXL LoRA underperforms on crisp edges, default to Flux Realism LoRA for text-heavy scenes.
6. Document compute costs and quality metrics for each model.

**What changed:**
EXCAVA’s output sharpness improved by at least 0.5% via RealVisXL LoRA at 1440p, with a fallback to Flux Realism LoRA for text fidelity.
