# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-83429` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Curate and tag 20% of designs with taste attributes, then integrate live Arena feedback to refine G8 fit.

**Steps:**
1. **Tagging Pipeline Setup**
   - Use `scripts/tag_taste.py` (existing) to apply taste tags to 20% of designs in `data/designs/` (filter by `./scripts/tag_taste.py --sample 20 --input data/designs/ --output data/tagged/`)
   - Validate tags with `tests/validate_tags.py` (checks for consistency in `taste_tags.json` schema)

2. **Arena Learning Integration**
   - Deploy `arena/learn.py` (live) to poll Arena API (`POST /feedback`) for taste preferences from last 24h
   - Update `config/g8_fit_weights.yaml` with new weights (run `python arena/learn.py --update-weights`)

3. **NOSG Wiring**
   - Modify `services/nosg.py` to subscribe to taste-tagged designs (listen to `data/tagged/*.json`)
   - Log NOSG adjustments in `logs/nosg_taste.log` (format: `timestamp|design_id|taste_tag|weight_adjustment`)

**Needs:**
- `data/designs/` (raw designs, ~10k files)
- `scripts/tag_taste.py` (existing taste tagger)
- Arena API credentials (`ARENA_API_KEY` in `.env`)
- `arena/learn.py` (live feedback collector)
- `config/g8_fit_weights.yaml` (G8 weight config)
```
