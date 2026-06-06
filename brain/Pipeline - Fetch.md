---
tags: [pipeline, stage]
---

# Pipeline - Fetch

**Stage 1 of the [[Architecture|pipeline]].** Pulls new videos from the playlist
and their transcripts, writing one file per video into `data/_pending/`.

- **Workflow:** `.github/workflows/fetch.yml` (and/or the [[Operations and Setup|local runner]]).
- **Code:** `src/fetch.py`.
- **Secret:** `YOUTUBE_API_KEY` (the *only* key the system strictly needs).
- **Playlist:** `PLxtsVIUtYhNo6pY9FrVqVe2xh---Y8rxB`.

## What it does
1. Lists every video in the playlist (id, title, description, publishedAt, channel).
2. Skips ids already processed (tracked in `data/index.json` / `status.json`).
3. For each new video, fetches the **automatic transcript** via
   `youtube-transcript-api` — **English first, then Hebrew**. The transcript is used
   **exactly as YouTube provides it** (never corrected, rephrased, or translated).
4. Falls back to the description, then the title, if no transcript exists.
5. Writes `data/_pending/<id>.json` with everything [[Pipeline - Analyze|analyze]] needs.

## Deep extraction
Per the owner's "extract everything the video *and its surroundings* offer", the
transcript budget is **80,000 characters** (`config.extraction.transcript_chars`),
far beyond the original 8,000 — and analyze additionally follows AI-relevant links
in the description (Step 2c). The goal: capture all available signal in one pass.

## Local vs cloud, and the residential-IP issue
YouTube can throttle or block datacenter IPs. The **local runner** runs this stage
from a home IP, then commits + pushes the `_pending` files so the cloud continues.
See [[Operations and Setup]].

## Catch-up trigger
When a large burst of new videos appears at once, fetch flips `data/catch_up.json`
to `active`, which makes [[Pipeline - Analyze|analyze]] switch to large, newest-first
batches drained by the `*/30` sprint cron. See [[Cadence]].

## Related
- [[Pipeline - Analyze]] · [[Data Files]] · [[Cadence]]
