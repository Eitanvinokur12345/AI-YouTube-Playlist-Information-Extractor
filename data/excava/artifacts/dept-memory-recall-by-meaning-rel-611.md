# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-611` (dept) · 2026-07-12T12:23:27.542573+00:00
> Participants: Graft, Prune, Root · synthesized by mistral/mistral-small-latest

**Decision:**
Build a shared memory graph prioritizing meaning-based connections with timestamps as a secondary fallback.

**Plan:**
1. Implement a meaning-extraction layer that tags each conversation with semantic nodes (e.g., concepts, relationships).
2. Automatically link nodes across conversations based on shared meaning, not timestamps or topics.
3. Store timestamps in a lightweight secondary index for linear fallback and debugging.
4. Add a confidence-scoring system for nodes/edges to flag potential mislabeling risks.
5. Design a recall interface that surfaces meaning-based paths first, with timestamp-based navigation as a backup.
6. Iteratively refine meaning extraction via user feedback loops to reduce mislabeling errors.

**What changed:**
Meaning-based recall replaces linear logs as the primary structure, with timestamps retained for redundancy.
