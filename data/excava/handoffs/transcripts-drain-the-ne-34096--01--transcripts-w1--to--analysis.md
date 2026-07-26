# Hand-off — Transcripts: drain the next batch of 1281 pending (residential IP)

| | |
|---|---|
| task | `transcripts-drain-the-ne-34096` (step 1/8) |
| from | **transcripts-w1** |
| to | **analysis** department |
| at | 2026-07-26T02:48:24.763341+00:00 |

## What was done
Residential drain state assessed: **1281 videos re-queued** in data/_pending/ with recovered/updated records awaiting deep re-analysis; 1389 still lack a real transcript. Today's drain auto-stopped on an IP block (correct behavior — bursting escalates the block); the remainder retries next residential session.

## Artifacts (where the work lives)
- `data/_pending/`
- `data/processed/`
- `src/backfill_transcripts.py`

## What remains
Deep re-extraction of the 1281 pending records under the anti-boilerplate gate, then draining the remaining 1389 on future residential sessions (gentle pacing).

## Context the next agent needs
bulk_analyze consumes data/_pending hourly. Records carry transcript_source='transcript' + caption_complete=true when the caption spans the full video; incomplete captions were deliberately left for Whisper.

## Done criteria (unchanged unless stated)
a committed artifact that measurably closes this gap
