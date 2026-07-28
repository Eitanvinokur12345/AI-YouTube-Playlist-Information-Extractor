# Hand-off — Transcripts: drain the next batch of 1209 pending (residential IP)

| | |
|---|---|
| task | `transcripts-drain-the-ne-83058` (step 1/8) |
| from | **transcripts-w1** |
| to | **analysis** department |
| at | 2026-07-28T23:57:45.171466+00:00 |

## What was done
Residential drain state assessed: **1209 videos re-queued** in data/_pending/ with recovered/updated records awaiting deep re-analysis; 1496 still lack a real transcript. Today's drain auto-stopped on an IP block (correct behavior — bursting escalates the block); the remainder retries next residential session.

## Artifacts (where the work lives)
- `data/_pending/`
- `data/processed/`
- `src/backfill_transcripts.py`

## What remains
Deep re-extraction of the 1209 pending records under the anti-boilerplate gate, then draining the remaining 1496 on future residential sessions (gentle pacing).

## Context the next agent needs
bulk_analyze consumes data/_pending hourly. Records carry transcript_source='transcript' + caption_complete=true when the caption spans the full video; incomplete captions were deliberately left for Whisper.

## Done criteria (unchanged unless stated)
a committed artifact that measurably closes this gap
