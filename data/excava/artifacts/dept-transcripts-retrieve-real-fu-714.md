# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-714` (dept) · 2026-07-30T21:21:00.075469+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use YouTube’s official API (or a trusted transcript extraction library like `youtube-transcript-api`) to fetch the full transcript for the video titled *"Orchestrated AI"*.
2. Filter the transcript to ensure it includes **only real captions** (exclude auto-generated ones if unverified).
3. Verify the transcript’s completeness by cross-checking against the video’s duration and known segments.
4. Save the transcript as a `.txt` file in a structured directory (e.g., `/transcripts/orchestrated_ai.txt`).
5. Log the extraction timestamp and video metadata (ID, title, duration) for reproducibility.
6. Validate the output by spot-checking random lines against the video’s audio.

**What changed:** Prioritized API-based extraction over manual methods for reliability and scalability.
