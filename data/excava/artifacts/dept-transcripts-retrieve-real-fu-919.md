# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-919` (dept) · 2026-08-14T13:56:48.615527+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Execute `kimtaeyoon83/mcp-server-youtube-transcript` on pending video ID `e2Z5eBVDrKM` to fetch raw transcript.
2. Scriv verifies artifact existence and integrity post-generation.
3. Save raw transcript as `transcript_e2Z5eBVDrKM_raw.txt` in `/transcripts/pending/`.
4. Format transcript (clean timestamps, speaker labels, etc.) into `transcript_e2Z5eBVDrKM_final.md`.
5. Move formatted transcript to `/transcripts/verified/` and archive raw file.
6. Log completion in `transcripts.log` with timestamp and video ID.

**What changed:** Tool execution initiated for `e2Z5eBVDrKM` with Scriv validation.
