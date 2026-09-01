# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-969` (dept) · 2026-09-01T03:43:05.693734+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Hybrid pipeline—run VFI-Flow only on keyframes with worst motion blur, then interpolate the rest with standard flow.

**Plan:**
1. Profile EXCAVA to identify keyframes with worst motion blur.
2. Integrate VFI-Flow into EXCAVA’s motion pipeline, configured to process only flagged keyframes.
3. Replace depth-aware upscaler with standard flow for non-keyframes to avoid slowdown.
4. Benchmark output quality and speed against baseline to confirm 0.5%+ temporal quality gain.
5. Document pipeline changes in EXCAVA’s model card and update dependencies list.
6. Deploy hybrid pipeline to staging for A/B testing with 10% of traffic.

**What changed:**
Hybrid VFI-Flow + standard flow pipeline replaces full VFI-Flow or depth-aware upscaler alone.
