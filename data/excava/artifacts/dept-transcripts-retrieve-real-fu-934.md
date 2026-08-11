# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-934` (dept) · 2026-08-11T16:57:31.274082+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Re-run the `kimtaeyoon83/mcp-server-youtube-transcript` tool on all 10 pending videos.
2. Ensure the output JSON includes three fields: `timestamp`, `transcript`, and `video_id` for each entry.
3. Add a new field `"source_type": "youtube"` to every JSON entry to clarify the origin.
4. Deliver the updated JSON file to Reel for verification.
5. Confirm the output meets the schema requirements before finalizing.

**What changed:** Added `"source_type": "youtube"` field to the JSON schema.
