# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-725` (dept) · 2026-07-10T10:04:47.131875+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit prompts using runtime call-graphs and import counts to improve prompt quality.

**Plan:**
1. Use `py-spy` to analyze runtime call-graphs and identify the most-executed prompts.
2. Implement `import-analyzer` to rank prompts based on import frequency.
3. Compile a list of the top 10 most-executed prompts based on call-counts and import-freq.
4. Perform a redundancy and clarity review for each of the top prompts, ensuring alignment with "quality first" standards.
5. Document and auto-apply safe changes to improve or remove redundant/prompts lacking clarity.

**What changed:** Transitioned from file definitions to actual usage data for prompt evaluation.
