# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-9709` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Curate 20% of taste-tagged designs via Arena live learning + NOSG integration.

**Steps:**
1. **Tag 20% of designs** – Run `python scripts/tag_taste.py --sample 0.2 --output taste_tags.json` (uses `designs/` folder).
2. **Arena live learning** – Deploy `arena_learning.py` with `taste_tags.json` as input (`python arena_learning.py --tags taste_tags.json --output arena_model.pkl`).
3. **NOSG wiring** – Update `config/nosg_config.yaml` with `arena_model.pkl` path and trigger `nosg_sync.sh` to validate integration.

**Needs:**
- `designs/` folder (design files).
- `scripts/tag_taste.py` (taste-tagging script).
- `arena_learning.py` (live learning model).
- `config/nosg_config.yaml` (NOSG config).
- `nosg_sync.sh` (sync script).
```
