# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-603` (dept) · 2026-07-08T11:51:50.050265+00:00
> Participants: Reel, Scriv, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Reel must fetch transcripts via `yt-dlp` then Scriv must verify via forced alignment (e.g., `aeneas`) and checksum against audio.

**Plan:**
1. Reel counts the number of `.mp4` and `.mov` files in `/home/reel/pending/`.
2. Reel retrieves the first 5 video files and runs `yt-dlp --write-auto-sub --sub-lang en --convert-subs srt` on each without using `--skip-download`.
3. Scriv verifies the fetched SRT files using forced alignment tools (e.g., `aeneas`) against the audio.
4. Scriv generates checksums (SHA256) for the audio files and compares these against the transcripts to ensure a verbatim match.
5. Compile SRT files, alignment logs, and audio checksums into a report.

**What changed:** The verification process now includes forced alignment and checksum validation to ensure quality of captions.
