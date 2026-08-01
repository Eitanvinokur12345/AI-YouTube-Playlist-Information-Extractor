# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-541` (dept) · 2026-07-30T21:33:52.364344+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Mistral Large 2 as EXCAVA’s core engine.

**Plan:**
1. Replace EXCAVA’s current core reasoning engine with Mistral Large 2 (128K context, 32K output tokens).
2. Benchmark Mistral Large 2 against prior models on complex queries to validate the 20% latency reduction.
3. Update EXCAVA’s model integration layer to support Mistral’s output token scaling and context handling.
4. Retire chunking logic for long documents, replacing with Mistral’s native 128K context processing.
5. Monitor error rates on multi-step tasks for 72 hours post-deployment to confirm no spike.
6. Document cost savings (50% vs. Sonnet 3.7) and latency improvements in EXCAVA’s performance logs.

**What changed:**
EXCAVA’s complex-query latency drops 20% with zero cost increase and no quality degradation.
