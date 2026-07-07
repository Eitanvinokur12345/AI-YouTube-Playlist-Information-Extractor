# Mining: discover new AI repos/tools + verify this cycle

> mining · task `mining-discover-new-ai-r-26252` · synthesized by mistral/mistral-small-latest

**Decision:** Mine this cycle for odd gems—discard shiny junk fast.

**Plan:**
1. Query GitHub API for repos with `ai`, `tool`, `framework` in name/desc, created in last 30 days, stars < 100.
2. Filter out obvious junk (e.g., "ai-starter-kit", "awesome-ai" clones) using regex: `(\b(awesome|starter|template|boilerplate)\b|-ai$)`.
3. Manually inspect top 20 candidates: check README, license, last commit, issues/PRs for activity.
4. Clone and run basic tests (e.g., `pip install -e . && pytest`) on repos with >50% test coverage.
5. Log gems in `~/mining/gems_YYYYMMDD.md` with: name, stars, license, 1-line pitch, test result.

**Done when:** 3 verified repos added to `~/mining/gems_YYYYMMDD.md` with tests passing.
