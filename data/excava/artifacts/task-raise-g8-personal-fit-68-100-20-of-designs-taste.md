# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-72570` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Curate 20% of taste-tagged designs via Arena learning + NOSG wiring to push G8 Personal fit from 68 → 85/100.

**Steps:**
1. **Tag extraction:** Run `scripts/taste_tag_extractor.py` on `designs/` → output `taste_tags.jsonl` (filter: `taste_score >= 0.7`).
2. **Arena learning:** Deploy `arena_learning.py` with `taste_tags.jsonl` as seed → generate `arena_learning_output.json` (params: `--epochs 10 --batch 32`).
3. **NOSG wiring:** Patch `nosg_config.yaml` with `arena_learning_output.json` → validate via `nosg_validate.py --config nosg_config.yaml`.
4. **Fit update:** Trigger `g8_personal_fit_update.sh` with `nosg_config.yaml` → verify via `g8_status.py` (target: `fit >= 85`).

**Needs:**
- `designs/` (local dir, 17 files)
- `scripts/taste_tag_extractor.py` (existing)
- `arena_learning.py` (existing, GPU access)
- `nosg_config.yaml` (existing)
- `g8_personal_fit_update.sh` (existing)
```
