# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-72150` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Taste-tag 20% of designs via Arena live + NOSG wiring; refine G8 fit iteratively.

**Steps:**
1. **Tag 20% of designs** – Use `scripts/taste_tag.py` to sample 20% of designs from `data/designs/` (seed=42) and append tags to `data/taste_tags.jsonl` with fields: `design_id`, `tag`, `confidence`, `timestamp`.
2. **Arena live learning** – Deploy `arena/serve.py` (FastAPI) with `data/taste_tags.jsonl` as seed data; log interactions to `arena/logs/interactions.jsonl` (fields: `user_id`, `design_id`, `vote`, `timestamp`).
3. **NOSG wiring** – Update `config/nosg.yaml` with new taste tags; run `scripts/nosg_sync.py` to regenerate `data/nosg_graph.gexf` and validate with `scripts/validate_nosg.py` (checks for cycles/isolated nodes).
4. **G8 fit adjustment** – Recompute G8 metrics via `scripts/g8_metrics.py` using updated `data/taste_tags.jsonl` and `arena/logs/interactions.jsonl`; log results to `metrics/g8_fit.json` (fields: `personal_fit`, `tagged_pct`, `nosg_edges`).

**Needs:**
- `data/designs/` (17 designs, JSONL format: `{id, features, image_url}`)
- `scripts/taste_tag.py` (existing, but must support `--sample_pct=20`)
- `arena/serve.py
