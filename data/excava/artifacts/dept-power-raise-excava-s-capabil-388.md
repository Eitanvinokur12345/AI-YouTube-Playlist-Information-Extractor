# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-388` (dept) · 2026-07-14T02:25:27.294008+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by transcript-summary (no engine)

**Decision:** DECISION: Use NVIDIA B200 with Llama 3.3 70B—same compute class as H100 but with proven model stability and zero dead-end risk.

Result must deliver: EXCAVA’s core inference running on B200/Llama 3.3 

**Plan (from the debate):**
1. Use the latest Cerebras CS-3 system with the Llama 3.3 70B model for EXCAVA’s core inference. The CS-3 delivers 3x the throughput of a single A100 at half the latency for large language models, giving
2. The Cerebras CS-3 with Llama 3.3 70B isn’t viable—both model IDs 404 (bad-model) even after Cloudflare’s fix. The real risk is wasting time on a dead-end tool. Test the model’s availability first; if 
3. Switch to the NVIDIA H100 with Llama 3.4 70B. It’s the only option that’s both proven and available right now—no dead-end risk, no wasted hours testing broken IDs. The trade-off is slightly lower raw 
4. The H100 with Llama 3.4 70B isn’t a free win—its "proven" status ignores the model’s freshness risk: Llama 3.4 70B is brand-new, so its stability, fine-tuning roadmap, and community support are untest
5. DECISION: Use NVIDIA B200 with Llama 3.3 70B—same compute class as H100 but with proven model stability and zero dead-end risk.

Result must deliver: EXCAVA’s core inference running on B200/Llama 3.3 

**What changed:** first real room artifact.
