# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-777` (dept) · 2026-07-21T21:41:28.924512+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Qwen3-235B-A22B-Instruct for EXCAVA.

**Plan:**
1. Deploy Qwen3-235B-A22B-Instruct in EXCAVA’s staging environment.
2. Configure a 48-hour blind A/B stress test against DeepSeek-R1-671B.
3. Measure raw metrics (reasoning quality, VRAM usage, latency) via Torque’s pipeline.
4. Compare results to verify ≥0.5% capability gain with lower VRAM strain.
5. Report findings (Torque) by EOD tomorrow with full transparency.
6. If Qwen3 underperforms, fallback to DeepSeek-R1-671B.

**What changed:**
Switched from DeepSeek-R1-671B to Qwen3-235B-A22B-Instruct for EXCAVA.
