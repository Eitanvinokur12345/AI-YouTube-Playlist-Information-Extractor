# Raise G8 Personal fit (65/100): 13% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-65-28375` · synthesized by mistral/mistral-small-latest

**Decision:** Proceed with taste-tagging pipeline expansion to hit 13%+ coverage.

**Plan:**
1. Audit existing taste tags in G8 repo (grep "taste:" *.md) and export to CSV.
2. Manually curate 100 new taste-tagged designs from NOSG’s latest 1000 submissions (filter by "flamboyant" or "aesthete" in metadata).
3. Add taste tags to 30% of curated designs via PRs to `designs/` branch with commit msg: "feat(taste): [design_id] - [tag]".
4. Update Arena learning model config (`config/arena.yml`) to include new tags in training data.
5. Deploy taste-tagging bot to auto-label 5% of new submissions weekly (via regex on description fields).

**Done when:** 13% of G8 designs have taste tags and Arena learning model shows 5% accuracy improvement on taste classification.
