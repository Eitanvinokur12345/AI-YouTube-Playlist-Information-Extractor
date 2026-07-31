# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-806` (dept) · 2026-07-31T17:40:24.333939+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Replace EXCAVA’s 1080p model with LTX-Video’s 4K-native output.
2. Implement blind A/B tests comparing LTX-Video’s 4K output vs. Runway Gen-4’s 4K upscaler.
3. Torque designs test parameters, metrics, and artifact collection.
4. Run tests on representative EXCAVA workloads (motion-heavy and static frames).
5. Measure quality lift (sharpness, motion clarity, latency) and compute cost per frame.
6. Select the option delivering ≥0.5% capability improvement; roll back if neither meets threshold.

**What changed:** EXCAVA’s pipeline upgraded from 1080p to 4K-native/LTX-Video, with A/B validation against Runway Gen-4.
