# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-192` (dept) · 2026-07-10T01:30:22.528943+00:00
> Participants: Reel, Scriv, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use `yt-dlp` to extract and verify SRT auto-captions for residential IP videos.

**Plan:**
1. Pull the pending video list from `pending_videos_2024-06-14.csv`, targeting 47 rows.
2. Filter the list for videos tagged with residential IP and gentle pacing.
3. Run `yt-dlp --write-auto-sub --sub-lang en --skip-download --convert-subs srt` on the 12 flagged videos to extract SRT auto-captions.
4. Use `yt-dlp --list-subs` to verify and compare the extracted subtitles against the native CC tracks for speaker diarization and accuracy.
5. Document findings to ensure clarity between auto-generated captions and verified transcripts.

**What changed:** Clarified the process to ensure accurate transcript quality by incorporating verification steps.
