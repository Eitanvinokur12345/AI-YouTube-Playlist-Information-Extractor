# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-71300` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Curate 20% of designs with explicit taste tags, then wire NOSG for live Arena learning.

**Steps:**
1. **Tag 20% of designs** – Run `scripts/taste_tag.py --threshold 0.8 --output data/taste_tags.json` on `designs/` (filter first 20% by `design_id`).
2. **Generate receipts** – Use `scripts/receipt_frame.py --input data/taste_tags.json --output frames/receipt_*.png` to frame-tagged designs.
3. **NOSG wiring** – Update `config/nosg.json` with `arena_learning: true` and `taste_module: taste_tags.json`.
4. **Live Arena sync** – Deploy via `make deploy-now` and monitor `logs/arena_learning.log` for taste drift.

**Needs:**
- `designs/` directory (17 small designs)
- `scripts/taste_tag.py` (existing taste classifier)
- `scripts/receipt_frame.py` (frame generator)
- `config/nosg.json` (write access)
- `make deploy-now` (CI hook)
```
