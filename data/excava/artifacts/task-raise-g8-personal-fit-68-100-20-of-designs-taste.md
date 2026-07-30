# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-42479` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Curate and tag 20% of designs with taste attributes, then feed tagged data into Arena learning for live refinement.

**Steps:**
1. **Tagging Pipeline Setup**
   - Clone `design-assets` repo (branch `taste-tagging`).
   - Run `scripts/tag_taste.py --input assets/ --output tags/taste.jsonl --model clip-vit-base-patch32`.
   - Validate tags with `scripts/validate_tags.py --input tags/taste.jsonl --threshold 0.85`.

2. **Arena Learning Integration**
   - Push `tags/taste.jsonl` to `arena-learning` repo (PR to `live-feed` branch).
   - Trigger `arena-server` redeploy via `kubectl rollout restart deployment/arena-server -n taste`.

3. **NOSG Wiring**
   - Update `config/nosg.yaml` with new taste tags (key: `taste_refinement_v1`).
   - Run `make nosg-sync` to propagate changes to staging.

**Needs:**
- `design-assets` repo (access: `git@github.com:org/design-assets.git`).
- `arena-learning` repo (access: `git@github.com:org/arena-learning.git`).
- GPU node for CLIP inference (label: `gpu=true`).
- `kubectl` access to `taste` namespace.
- `make` and `python3.11` with `torch`, `clip` installed.
```
