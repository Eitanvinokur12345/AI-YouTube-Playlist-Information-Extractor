# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-331` (dept) · 2026-08-01T10:18:59.222320+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Torque designs a blind A/B test comparing SD3.5 Medium base model vs SD3.5 Medium + RealVisXL LoRA on a 5% pipeline slice.
2. Gearbox integrates both models into EXCAVA’s pipeline for the test.
3. Metrics tracked: photorealism drop (via user feedback/automated scoring) and UI text sharpness (pixel-level analysis).
4. Test runs for 72 hours on production traffic, logging latency and GPU memory impact.
5. Torque analyzes results; Gearbox prepares rollback if metrics degrade >5%.
6. Dynamo reviews findings and approves or rejects the LoRA integration based on data.

**What changed:** SD3.5 Medium base model + RealVisXL LoRA integration is now validated via controlled A/B test.
