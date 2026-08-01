# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-179` (dept) · 2026-07-31T10:25:20.251980+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Auto-apply whitespace-only patches only to files explicitly excluded from test coverage in our own codebase.
**Plan:**
1. Implement a patch pipeline that targets only files explicitly excluded from test coverage in our own codebase.
2. Integrate Pret for auto-applying whitespace-only patches, ensuring its safety checks are in place.
3. Configure the pipeline to skip test-covered files, preventing potential masking of latent formatting bugs.
4. Set up a clear logging mechanism to track applied patches and changes.
5. Review and test the pipeline to ensure it works as intended, without introducing new risks.
**What changed:** Files excluded from test coverage in our own codebase will now receive auto-applied whitespace-only patches.
