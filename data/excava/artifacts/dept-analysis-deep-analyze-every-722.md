# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-722` (dept) · 2026-07-28T17:47:11.988580+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
Execute BloodHound-MCP analysis on the full earnings call transcript to generate a Decision Log artifact with real-time sentiment, key phrases, and decision triggers, enriched by transcript context.

**Plan:**
1. **Ingest full transcript** into BloodHound-MCP as the primary data source.
2. **Map sentiment/key phrases** per speaker in real time, tagging decision triggers (e.g., "cost-cutting," "guidance raise").
3. **Generate Decision Log artifact** with structured outputs (speaker → sentiment → trigger → impact).
4. **Enrich with transcript context** (e.g., prior/following statements, tone shifts) to validate triggers.
5. **Flag anomalies** (e.g., conflicting sentiment within a speaker’s segment) for manual review.
6. **Output artifact** as GitHub markdown with hyperlinks to transcript segments for traceability.

**What changed:** Transcript analysis is now automated via BloodHound-MCP, replacing manual sentiment tagging with a live, traceable Decision Log.
