# Raise G8 Personal fit (68/100): 21% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-84730` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Systematically tag taste-relevant designs in the G8 corpus using curated aesthetic heuristics and Arena feedback, then wire NOSG for live learning.

**Steps:**
1. **Audit & Curate:** `find ./g8/designs -type f -name "*.png" -o -name "*.jpg" | wc -l` → confirm 17 files. Manually review each, assigning binary taste tags (`taste:yes`/`taste:no`) in `./g8/tags.csv` (columns: `file_hash,tag,reason`).
2. **Automate Tagging:** Run `python scripts/tag_taste.py --input ./g8/tags.csv --output ./g8/taste_model.json` to train a lightweight classifier (CLIP + Arena rankings) on tagged subset. Validate with `python scripts/validate_tags.py --test 0.2`.
3. **NOSG Wiring:** Update `./nosg/config.yaml` with `taste_model_path: ./g8/taste_model.json` and `arena_endpoint: http://arena.local/api/feedback`. Deploy via `docker-compose -f nosg/docker-compose.yml up --build`.
4. **Arena Learning:** Trigger live feedback loop: `curl -X POST http://arena.local/api/start_learning --data '{"corpus": "g8", "model": "taste_model"}'`. Monitor via `docker logs nosg_arena_1`.
5. **Taste Expansion:** For untagged designs, run `python scripts/expand_taste.py --corpus g8 --threshold 0.75` to auto-tag with confidence >75%. Log conflicts to `
