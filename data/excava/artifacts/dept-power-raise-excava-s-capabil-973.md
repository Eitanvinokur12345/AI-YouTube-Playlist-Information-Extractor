# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-973` (dept) · 2026-08-01T15:39:32.554140+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Blind A/B Test Setup**: Torque prepares a controlled test comparing **RealVisXL 4.0 + DPM++ SDE sampler** vs **SD3.5 Medium + RealVisXL LoRA** on EXCAVA’s high-contrast outputs.
2. **Metric Definition**: Define photorealism (e.g., FID/CLIP-IQA) and fine texture retention (e.g., LPIPS, manual review) as primary metrics.
3. **Sampling Consistency**: Use identical prompts, seeds, and EXCAVA’s pipeline settings for both models to isolate model impact.
4. **Artifact Documentation**: Torque logs side-by-side comparisons, flagging over-smoothing, artifacts, or texture loss in a shared repo (e.g., GitHub Issues).
5. **Threshold Enforcement**: RealVisXL 4.0 must achieve **≥0.5% photorealism gain** without exceeding a **2% fine texture loss** vs baseline.
6. **Rollback Clause**: If RealVisXL 4.0 fails, default to **SDXL Lightning 1.0 + DPM++ 2M Karras** as the backup.

**What changed:** Prioritized **RealVisXL 4.0 + DPM++ SDE** for testing over LoRA/SD3.5, with strict photorealism/texture metrics and artifact tracking.
