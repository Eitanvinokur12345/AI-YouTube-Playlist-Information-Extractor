# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-701` (dept) · 2026-07-12T10:09:00.332005+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Prioritize diagnosing the root cause of the worst-performing prompt’s failures before applying any changes.

**Plan:**
1. Identify the prompt with the highest error rate in logs (user-facing).
2. Run its current output through its assigned engine *as-is* to log errors, latency, and response quality.
3. Gauge compiles a report on whether the bottleneck is the prompt’s structure, missing context, or engine routing.
4. Sprocket reviews the report to confirm the diagnosis aligns with plain-language rewrite risks.
5. If engine is the issue, route to testing a different engine (per Gauge’s suggestion).
6. If prompt is the issue, rewrite it in plain language *only* after structural flaws are ruled out.

**What changed:**
Diagnostic testing replaces immediate prompt rewrites to isolate the true bottleneck.
