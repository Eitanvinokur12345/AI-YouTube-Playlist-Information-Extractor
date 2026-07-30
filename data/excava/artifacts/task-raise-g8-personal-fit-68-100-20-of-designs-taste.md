# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-43353` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Taste-tag 20% of designs in the live Arena learning pipeline, then wire NOSG for taste-based routing beyond.

**Steps:**
1. **Tag 20% of designs** in `designs/` using `scripts/taste_tag.py` (filters by `taste_tag: true` in metadata).
2. **Run Arena learning** with `python arena_learning.py --taste_tags --batch_size 32` to update G8 fit.
3. **Wire NOSG** by adding `taste_router.py` to `nosg/` with `route(taste_tag=True)` for live traffic.

**Needs:**
- `designs/` directory with metadata files (JSON/YAML).
- `scripts/taste_tag.py` (existing or to be created).
- `arena_learning.py` (existing pipeline).
- `nosg/` repo with routing hooks.
```
