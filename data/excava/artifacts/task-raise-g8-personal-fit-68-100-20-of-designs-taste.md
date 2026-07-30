# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-34851` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Taste-tag 20% of designs in the live Arena learning pipeline, then wire NOSG for taste signals beyond current scope.

**Steps:**
1. **Tag 20% of designs** in `./designs/` using `taste_tags.json` (schema: `{"design_id": ["tag1", "tag2"]}`) via `scripts/tag_designs.py --sample 0.2 --output taste_tags.json`.
2. **Patch Arena learning** to ingest `taste_tags.json` by updating `arena/learning.py` to include tagged designs in the training loop (add `TasteTagDataset` class).
3. **Wire NOSG** to the taste pipeline by exposing `taste_tags.json` via a REST endpoint (`/taste/tags`) in `nosg/api.py` and subscribing to updates via `nosg/subscribers/taste_updates.py`.
4. **Validate** by running `pytest tests/test_taste_tags.py` and `pytest tests/test_nosg_taste_integration.py`; log failures to `logs/taste_wire_errors.log`.

**Needs:**
- `./designs/` directory with design files (e.g., `design_001.png`, `design_002.svg`).
- `taste_tags.json` schema (shared in repo or provided via `config/taste_tags_schema.json`).
- `scripts/tag_designs.py` (existing or to be created; depends on `Pillow` for image processing).
- `arena/learning.py` (access to modify training logic).
- `nosg/api.py` and `nosg/subscribers/taste_updates.py`
