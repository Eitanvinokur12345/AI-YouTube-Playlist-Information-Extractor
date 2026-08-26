# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-458` (dept) · 2026-08-26T20:42:47.481799+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a blind A/B test comparing InstantX-ComfyUI’s depth-aware upscaler, Cerebras-Grit v1.1, and VFI-Flow to determine the optimal ≥0.5% visual gain with minimal speed cost.

**Plan:**
1. Select EXCAVA’s 10 worst-case motion blur scenes for testing.
2. Implement each tool (InstantX-ComfyUI, Cerebras-Grit v1.1, VFI-Flow) into EXCAVA’s pipeline.
3. Conduct blind A/B tests with 50+ evaluators, scoring visual sharpness and speed impact.
4. Measure blur reduction (≥0.5%) and speed penalty (≤15% for upscalers, ≤20% for temporal models).
5. Rank tools by highest net gain (visual improvement minus speed cost).
6. Integrate the top-performing tool into EXCAVA’s default pipeline.

**What changed:**
Prioritized empirical validation of all debated tools before integration.
