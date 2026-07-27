# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-213` (dept) · 2026-07-27T22:11:34.365290+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Fork only the prompt templates and routing logic from the Claude Self-Improvement Skill Pack into a new **Sprocket Patterns** module, keep the engine pluggable, and run a 2-week shadow test comparing it to the current system—ownership: Sprocket (improve-w1) delivers.

**Plan:**
1. Fork and extract only prompt templates and routing logic from the Claude Self-Improvement Skill Pack into a new `sprocket-patterns/` module.
2. Refactor the self-improvement task engine to use `sprocket-patterns/` as a pluggable dependency, keeping the core engine separate.
3. Implement a 2-week shadow test mode that runs both the new and old systems in parallel, logging outputs for comparison.
4. Set up automated metrics collection (latency, success rate, output quality) for the shadow test.
5. After 2 weeks, review data and decide whether to fully adopt `sprocket-patterns/` or iterate further.
6. Document the extraction process and pluggable engine design in `sprocket-patterns/README.md`.

**What changed:**
Extracted only patterns (templates/routing) into a pluggable `sprocket-patterns/` module instead of forking the entire pack.
