# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-22589` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Taste-tag 20% of designs via manual curation + Arena learning, then wire NOSG for taste propagation.

**Steps:**
1. **Tag 20% of designs** (`/designs/`):
   - Run `find ./designs -type f -name "*.png" -o -name "*.jpg" | shuf -n 20% > taste_tags.txt`
   - Manually curate tags in `taste_tags.txt` (e.g., `color:crimson`, `texture:matte`, `vibe:cyberpunk`).
   - Commit to `taste_tags.json` (format: `{ "file": "path/to/design.png", "tags": [...] }`).

2. **Arena learning live**:
   - Deploy `arena_learning.py` (existing) with `--live` flag to scrape user interactions from `/arena/logs/`.
   - Pipe output to `taste_feedback.csv` (columns: `user_id`, `design_id`, `tags`, `timestamp`).

3. **NOSG wiring**:
   - Update `nosg_config.yaml` to include `taste_tags.json` and `taste_feedback.csv` as inputs.
   - Run `nosg sync --taste` to propagate tags to `G8` (output: `g8_taste_graph.json`).

**Needs:**
- `/designs/` (20%+ PNG/JPG files)
- `taste_tags.txt` (empty file to populate)
- `arena_learning.py` (existing, requires `/arena/logs/`)
- `nosg_config.yaml` (existing, needs `taste_tags.json`/`taste
