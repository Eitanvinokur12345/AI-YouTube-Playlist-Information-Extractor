# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-643` (dept) · 2026-08-11T07:49:02.392007+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Re-run `kimtaeyoon83/mcp-server-youtube-transcript` on the 10 pending videos using residential IP with gentle pacing.
2. Ensure the output is a strict JSON file for each video.
3. Include fields: `timestamp`, `speaker_id`, `text`, and **new** `confidence` (low-quality flag).
4. Validate JSON structure and confidence field before finalizing outputs.
5. Store results in the designated repository path.
6. Log execution details (IP, pacing, timestamps) for audit.

**What changed:** Added `confidence` field to JSON output for low-quality transcript flagging.
