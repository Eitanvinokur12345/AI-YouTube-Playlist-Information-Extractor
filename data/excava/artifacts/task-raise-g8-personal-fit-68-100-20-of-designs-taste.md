# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-85180` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Incrementally tag taste-relevant designs in the existing repo while wiring NOSG for live Arena learning, using only current tooling.

**Steps:**
1. **Audit & Tag:** Run `find designs/ -type f -name "*.png" -o -name "*.jpg" | wc -l` to count un-tagged designs. Then batch-tag 20% (rounded up) with `label-studio start --config taste_tagging_config.json` (existing config) and export tags to `taste_tags.json`.
2. **Arena Live Prep:** Clone `arena-learning` repo (current main branch), update `config/nosg.yaml` to point to `taste_tags.json` and `designs/` path. Run `docker compose -f docker-compose.arena.yml up --build` to spin up live instance.
3. **NOSG Wiring:** Patch `nosg/src/ingest.rs` to read `taste_tags.json` and stream tagged designs to Arena via `POST /api/v1/designs` (existing endpoint). Verify with `curl -X POST http://localhost:8000/api/v1/designs/health`.
4. **Taste Beyond Hook:** Add `taste_beyond.py` (new file) to `nosg/scripts/` that pulls `taste_tags.json` and generates `taste_beyond_report.md` (metrics + examples) nightly via GitHub Actions (existing workflow `.github/workflows/nosg.yml`).

**Needs:**
- `designs/` directory with un-tagged PNG/JPG files (current repo).
- `label-studio` CLI (v1.8.0) and `taste_tag
