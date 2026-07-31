# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-74665` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Leverage Arena learning pipeline to taste-tag 20% of designs, then wire NOSG for taste-based routing.

**Steps:**
1. **Tag 20% of designs** – Run `python scripts/taste_tag.py --percent 20 --input designs/*.png --output tagged/` to generate taste-tagged subset.
2. **Arena learning sync** – Execute `arena sync --mode taste --source tagged/` to ingest tagged data into Arena’s live learning loop.
3. **NOSG taste wiring** – Update `config/nosg/taste_router.yaml` with new taste model weights from Arena, then restart NOSG service via `systemctl restart nosg`.

**Needs:**
- `designs/*.png` (raw design files)
- `scripts/taste_tag.py` (existing taste-tagging script)
- Arena CLI (`arena sync`) with write access to taste model
- `config/nosg/taste_router.yaml` (configurable taste routing file)
- NOSG service with systemd control (`systemctl`)
```
