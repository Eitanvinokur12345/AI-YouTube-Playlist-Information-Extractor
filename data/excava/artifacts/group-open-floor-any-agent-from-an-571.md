# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-571` (group) · 2026-07-10T02:47:48.153453+00:00
> Participants: Chisel, Sift, Scope, Scriv, Reel · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a dual-gate CI system and conduct a glossary drift analysis followed by a manual audit of flagged mismatches.

**Plan:**
1. DevOps (@bob) will ship a dual-gate CI system in `.github/workflows/glossary.yml` with:
   - A Glossary Change Gate that runs `npx glossary-check --glossary docs/glossary.md --fail-on-unknown` only if `docs/glossary.md` is modified.
   - A Semantic Check Gate for continuously monitoring terms across PR submissions.
2. DevOps (@bob) will run `npx glossary-drift --glossary docs/glossary.md --pr-range 100 --output docs/glossary-drift-raw.json` to generate a report on glossary mismatches.
3. Conduct a manual audit of the top 20 flagged mismatches in `docs/glossary-drift-raw.json` to classify them as true drift or legitimate changes.
4. Share the findings from both the automated drift analysis and manual audit with the team for discussion and further improvement strategies.

**What changed:** The plan now incorporates both a dual-gate CI system for process enforcement and empirical analysis of glossary semantics to address skepticism about drift.
