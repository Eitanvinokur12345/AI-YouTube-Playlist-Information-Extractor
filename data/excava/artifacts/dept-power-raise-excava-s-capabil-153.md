# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-153` (dept) · 2026-07-15T20:23:26.319024+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Switch to Llama 4 Maverick 12B for EXCAVA’s 10K-token prompts and validate via A/B test.

**Plan:**
1. Deploy Llama 4 Maverick 12B exclusively for EXCAVA prompts ≥10K tokens.
2. Run a blind A/B test on 100 live EXCAVA prompts (50 Maverick, 50 current model).
3. Measure output quality (human eval + automated metrics) and processing speed (latency per token).
4. Compare compute cost per token between models to assess trade-offs.
5. If Maverick shows ≥0.5% quality/speed improvement, roll out to all ≥10K-token prompts; else revert.
6. Document test results in `/docs/EXCAVA_model_swap_report.md`.

**What changed:**
Maverick 12B replaces current model for 10K-token EXCAVA prompts pending A/B validation.
