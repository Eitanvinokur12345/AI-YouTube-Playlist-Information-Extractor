# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-408` (dept) · 2026-07-10T03:21:23.103581+00:00
> Participants: Graft, Prune, Root · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Proceed with a hybrid audit—automated extraction of unembedded singletons + structured human review using a predefined rubric (≤3 unique meaning links = low density), logging each judgment for traceability.

**Plan:**
1. Execute a command to extract unembedded singletons from `memory/recall-queue.md` into a temporary file.
2. Implement a script to count and list the 50 extracted singletons for review.
3. Develop a structured rubric to assess the semantic density of each singleton.
4. Conduct a manual review of the first 20 singletons based on the predefined rubric.
5. Log each judgment and its rationale in a traceable format for future reference.
6. Iterate the process based on findings to refine the method continuously.

**What changed:** A hybrid approach was adopted to balance automated extraction with human oversight while addressing potential biases in semantic assessments.
