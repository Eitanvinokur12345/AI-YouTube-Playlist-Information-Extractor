# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-73415` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Taste-tag 20% of designs via Arena learning, wire NOSG, then expand taste beyond.

**Steps:**
1. **Tag 20% of designs** – Run `scripts/taste_tag.py --sample 20` (uses `designs/` dir and `taste_tags.csv`).
2. **Arena learning** – Deploy `arena/learn.py` with `--live` flag (requires `arena/models/` and live API keys).
3. **Wire NOSG** – Update `config/nosg.json` with new taste vectors (needs `nosg/` repo access).
4. **Expand taste** – Run `scripts/expand_taste.py --beyond` (uses `taste_tags.csv` and `designs/`).

**Needs:**
- `designs/` directory (17 small designs)
- `taste_tags.csv` (existing or empty)
- `arena/models/` (pre-trained)
- Live API keys (Arena learning)
- `nosg/` repo access (write to `config/nosg.json`)
```
