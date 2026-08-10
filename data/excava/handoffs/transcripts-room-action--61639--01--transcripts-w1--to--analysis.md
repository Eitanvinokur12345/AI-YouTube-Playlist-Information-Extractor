# Hand-off — [transcripts room action] Scriv fetches Luma’s built-in transcript tool for every pending video outside Luma’s ecosystem to produce clean, structu

| | |
|---|---|
| task | `transcripts-room-action--61639` (step 1/8) |
| from | **transcripts-w1** |
| to | **analysis** department |
| at | 2026-08-10T19:32:53.476112+00:00 |

## What was done
Residential drain state assessed: **1643 videos re-queued** in data/_pending/ with recovered/updated records awaiting deep re-analysis; 1625 still lack a real transcript. Today's drain auto-stopped on an IP block (correct behavior — bursting escalates the block); the remainder retries next residential session.

## Artifacts (where the work lives)
- `data/_pending/`
- `data/processed/`
- `src/backfill_transcripts.py`

## What remains
Deep re-extraction of the 1643 pending records under the anti-boilerplate gate, then draining the remaining 1625 on future residential sessions (gentle pacing).

## Context the next agent needs
bulk_analyze consumes data/_pending hourly. Records carry transcript_source='transcript' + caption_complete=true when the caption spans the full video; incomplete captions were deliberately left for Whisper.

## Done criteria (unchanged unless stated)
the stated action is done and verifiable
