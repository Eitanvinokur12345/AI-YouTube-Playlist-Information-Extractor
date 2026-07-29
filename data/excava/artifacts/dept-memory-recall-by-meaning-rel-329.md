# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-329` (dept) · 2026-07-29T20:52:19.613223+00:00
> Participants: Graft · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Execute `memory-linking` command to auto-connect all memos in Hindsight database via semantic relations.
2. Validate graph integrity by checking for unembedded elements (orphaned memos) and flag them for manual review.
3. Generate a summary report of top 10 strongest new connections and their relevance scores.
4. Schedule a recursive pass to reinforce weak links (confidence < 0.7) with user confirmation.
5. Export the updated brain graph to `hindsight_graph.json` with timestamp and version tag.
6. Notify all stakeholders via Slack/email with the new graph structure and change log.

**What changed:** Hindsight database transformed from fragmented memos to a fully linked semantic network.
