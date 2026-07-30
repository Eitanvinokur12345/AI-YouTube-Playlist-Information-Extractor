# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-35713` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Taste-tag 20% of designs via Arena live feedback, wire NOSG for taste propagation, and log receipts for G8 uplift.

**Steps:**
1. **Tag 20% of designs** – Run `python scripts/taste_tag.py --sample 0.2 --output tagged_designs.json` (uses `designs/` dir as input).
2. **Arena learning live** – Deploy `arena/taste_feedback.py` as a FastAPI endpoint (`uvicorn arena.taste_feedback:app --host 0.0.0.0 --port 8000`), then POST tagged designs to `/feedback` with user taste votes.
3. **NOSG wiring** – Update `nosg/config.yaml` to ingest `tagged_designs.json` and `arena/feedback_log.csv`; run `nosg sync --taste-propagate`.
4. **Receipt logging** – Append each tagged design’s metadata (ID, tags, feedback score) to `receipts/taste_receipts.md` in a framed format (e.g., `### Design [ID] | Score: [X] | Tags: [Y]`).

**Needs:**
- `designs/` dir (input designs, e.g., `.png`/`.json` files).
- `scripts/taste_tag.py` (pre-written script to sample and tag designs).
- `arena/taste_feedback.py` (FastAPI endpoint for live taste votes).
- `nosg/` dir with `config.yaml` and `sync` CLI tool (pre-configured for taste propagation).
- Write access to `receipts/taste_receipts.md`.
```
