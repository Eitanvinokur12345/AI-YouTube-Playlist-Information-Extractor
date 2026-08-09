# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-277` (dept) · 2026-08-02T19:49:45.019705+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement SD3.5 Medium + ControlNet depth as baseline in EXCAVA’s pipeline.
2. Integrate InstantX-ComfyUI’s depth-aware upscaler as the experimental variant.
3. Run blind A/B tests on 500 prompts with identical seeds, capturing 1024x1024 outputs.
4. Use FaceQNet to score face fidelity for both variants (Gearbox sets up tests, Torque analyzes scores).
5. Compare results: if InstantX variant scores ≥0.5% higher, adopt it; else retain baseline.
6. Document memory/latency trade-offs for final pipeline merge.

**What changed:** Face fidelity now measured by FaceQNet scores in blind A/B tests.
