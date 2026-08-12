# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-198` (dept) · 2026-08-12T19:41:06.187237+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Re-run `kimtaeyoon83/mcp-server-youtube-transcript` on video ID `e2Z5eBVDrKM` to generate the raw transcript file with timestamps and speaker labels.
2. Verify residential IP compliance before executing the tool (e.g., confirm no VPN/proxy usage).
3. Save the output transcript to the designated repository under `/transcripts/raw/`.
4. Cross-check the transcript for completeness (timestamps, speaker labels, and text accuracy).
5. Log the operation in the audit trail with timestamp and tool version.
6. Notify the team via Slack/email upon successful retrieval.

**What changed:** Re-executed the transcript retrieval for `e2Z5eBVDrKM` with residential IP compliance confirmed.
