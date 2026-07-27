# Raise G8 Personal fit (68/100): 21% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-74193` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
## Approach:
Augment G8’s taste-tagging pipeline with live Arena feedback loops and NOSG integration to push personal fit beyond 68/100.

## Steps:
1. **Tagger Overhaul**
   - Fork `g8-taste-tag` repo → `g8-taste-tag-v2`
   - Replace static tagger with live Arena model (`arena-live` branch)
   - Add taste-tagging API endpoint (`POST /taste/tag`) using `fastapi` + `torch` (existing model weights)
   - Commit: `feat: live arena taste tagging`

2. **Arena Learning Loop**
   - Deploy `arena-live` to staging (fly.io)
   - Wire NOSG webhook to `/arena/feedback` (listen for `user_vote` events)
   - Log feedback to `arena_feedback.jsonl` (append-only)
   - Commit: `chore: nosg feedback ingestion`

3. **Taste Beyond Metrics**
   - Add `/taste/beyond` endpoint (uses `arena_feedback.jsonl` + `user_history`)
   - Run weekly `python scripts/retrain_taste.py` (uses `pytorch-lightning`)
   - Push new weights to `g8-taste-tag-v2/models/latest.pt`
   - Commit: `feat: beyond-taste retraining`

## Needs:
- `g8-taste-tag` repo (write access)
- NOSG webhook secret (`NOSG_WEBHOOK_SECRET`)
- Arena staging env (`fly.io` token)
- `arena_feedback.jsonl` schema (existing)
- `retrain_taste.py` script (stub in `scripts
