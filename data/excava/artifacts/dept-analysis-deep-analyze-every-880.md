# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-880` (dept) · 2026-07-29T21:28:12.033548+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run BloodHound-MCP on the full earnings call transcript to generate a Speaker Attribution Map, outputting a live doc with speaker identities, roles, and speaking patterns.
2. Cross-reference the Speaker Attribution Map with the full transcript to validate speaker roles and speaking patterns.
3. Enrich the Speaker Attribution Map with additional context (e.g., speaker reputation, past statements, or industry role) from >=1 external source.
4. Analyze speaker dynamics (e.g., interruptions, dominance, sentiment shifts) using the enriched Speaker Attribution Map.
5. Compile findings into a structured report for credibility and dynamic analysis.

**What changed:** Speaker attribution and dynamics analysis now includes enriched external context for deeper validation.
