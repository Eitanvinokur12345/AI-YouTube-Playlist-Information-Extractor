# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-28437` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Target 20% of designs with taste tags by leveraging Arena’s live learning loop and NOSG’s taste signals, then refine fit via curated screenshots.

**Steps:**
1. **Tag 20% of designs**
   - Run `python scripts/taste_tag.py --target 20 --input designs/*.png --output tagged/` (uses `taste_model_v3.2` from `models/`).
   - Verify with `./tools/verify_tags.sh tagged/` (checks 20%+ coverage).

2. **Arena live learning**
   - Deploy `arena/serve.py --model taste_model_v3.2 --live` (binds to `localhost:8000`).
   - Stream user feedback via `arena/collect_feedback.py --endpoint http://localhost:8000/feedback`.

3. **NOSG taste integration**
   - Patch `nosg/config.yaml` to include `taste_signals: true` (requires `nosg@1.4.2`).
   - Trigger sync with `nosg sync --taste` (pulls signals from `taste_db/`).

4. **Curate screenshots**
   - Generate frames with `ffmpeg -i tagged/*.png -vf fps=1/5 screenshot_%04d.jpg`.
   - Select top 10% via `python scripts/rank_screenshots.py --input screenshot_*.jpg --output framed/` (uses `taste_model_v3.2`).

**Needs:**
- `taste_model_v3.2` (model weights in `models/taste_model_v3.2/`).
- `designs/` directory with 1
