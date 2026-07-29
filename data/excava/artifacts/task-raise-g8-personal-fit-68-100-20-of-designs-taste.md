# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-59103` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Taste-tag 20% of designs via Arena live feedback, then wire NOSG to propagate signals beyond current scope.

**Steps:**
1. **Tag 20% of designs** – Run `scripts/taste_tag.py --split 0.2 --arena-live` to generate taste-tagged subset (output: `data/taste_tags.jsonl`).
2. **Arena learning loop** – Deploy `arena/learn.py --input data/taste_tags.jsonl --epochs 10` to train taste model (logs: `logs/arena_YYYYMMDD.log`).
3. **NOSG wiring** – Update `config/nosg.yaml` with new taste model path, then run `nosg/wire.sh --model-path models/arena_v1.pt` to propagate signals (output: `nosg/signals.json`).

**Needs:**
- `scripts/taste_tag.py` (existing, but requires `--arena-live` flag)
- `arena/learn.py` (existing, needs `--input` and `--epochs` args)
- `nosg/wire.sh` (existing, needs `--model-path` arg)
- `data/taste_tags.jsonl` (will be created in Step 1)
- `models/arena_v1.pt` (output of Step 2)
```
