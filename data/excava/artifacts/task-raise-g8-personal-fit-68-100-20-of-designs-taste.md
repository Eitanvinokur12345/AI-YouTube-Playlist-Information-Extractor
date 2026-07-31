# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-34565` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Taste-tag 20% of designs via automated tagging pipeline + manual curation; feed tagged data into Arena learning loop; wire NOSG for live taste inference.

**Steps:**
1. **Tag 20% of designs**
   - Run `scripts/tag_designs.py --sample 0.2 --output taste_tags.jsonl` (uses `designs/` dir as input).
   - Manually curate `taste_tags.jsonl` with `scripts/curate_tags.py --input taste_tags.jsonl --output curated_tags.jsonl`.

2. **Arena learning loop**
   - Train taste model: `python train_arena.py --data curated_tags.jsonl --epochs 10 --output models/taste_v1.ckpt`.
   - Evaluate: `python evaluate_arena.py --model models/taste_v1.ckpt --output arena_metrics.json`.

3. **NOSG wiring**
   - Deploy taste model to NOSG: `nosg deploy --model models/taste_v1.ckpt --endpoint /taste/v1`.
   - Test live inference: `curl -X POST /taste/v1 -d '{"design_id": "123"}'`.

**Needs:**
- `designs/` dir (input designs, 17 files).
- `scripts/tag_designs.py`, `scripts/curate_tags.py` (existing).
- `train_arena.py`, `evaluate_arena.py` (existing).
- NOSG CLI (`nosg deploy`).
```
