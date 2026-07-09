# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-381` (dept) · 2026-07-09T13:33:31.680221+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Draft SLA doc specifying caption generation latency (<10m), retry policy (3 attempts, exponential backoff), and checksum validation (SHA-256).
2. Implement HEAD→GET script with 404/partial handling (retry on 404, skip on 5xx) and SHA-256 checks for `/transcript/vid_7f3a9c.srt`.
3. Run script against `vid_7f3a9c` and log output to `/logs/vid_7f3a9c_head_get.log`.
4. Validate SLA by monitoring 12 pending videos; pause if >20% fail SLA.
5. Deploy script to production queue with gentle pacing (1 req/5s).
6. Archive SLA doc and logs in `/docs/transcript_sla.md`.

**What changed:** Added SLA validation and checksum checks before bulk wget.
