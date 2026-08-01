# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-376` (dept) · 2026-07-31T22:05:10.090770+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch full transcript for video ID "dQw4w9WgXcQ" via kimtaeyoon83/mcp-server-youtube-transcript.
2. Output the real transcript text or confirmation of unavailability.
3. Validate transcript authenticity (e.g., check for completeness, timestamps, or metadata).
4. If unavailable, log error and suggest alternative methods (e.g., manual caption extraction).
5. Store transcript in designated repository with timestamp.
6. Notify user of completion or failure via GitHub issue/PR.

**What changed:** Resolved redundancy in actions; streamlined to a single, decisive fetch-and-output step.
