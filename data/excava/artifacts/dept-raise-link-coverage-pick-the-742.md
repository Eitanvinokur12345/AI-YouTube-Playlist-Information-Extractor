# Raise link coverage: pick the next 200 unlinked elements and the fastest resolution path

> Decision artifact · room `dept-raise-link-coverage-pick-the-742` (dept) · 2026-07-07T14:34:27.455707+00:00
> Participants: Fetch, Probe, Ledger · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Proceed with the revised script to ensure a focused selection of unlinked elements.

**Plan:**
1. Run `./scripts/find_unlinked.sh --limit 200 --output unlinked_200.csv --exclude-patterns "test_*,mock_*,generated_*"` to filter unlinked elements appropriately.
2. Verify the contents of `unlinked_200.csv` to ensure it excludes unwanted patterns.
3. Pipe the output to `./scripts/resolve_links.py --mode fastpath --priority oldest-modified` for suggested fixes.
4. Review the generated suggestions for resolving links, focusing on their relevance and feasibility.
5. Implement fixes on the identified unlinked elements, documenting the changes for future reference.

**What changed:** Excluded certain file patterns to improve the quality of the unlinked elements being addressed.
