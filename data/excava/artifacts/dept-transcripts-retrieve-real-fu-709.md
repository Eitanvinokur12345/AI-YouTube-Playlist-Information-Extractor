# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-709` (dept) · 2026-07-20T11:25:11.975665+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the YouTube transcript tool to fetch full transcripts for all pending videos.
2. Generate a single timestamped artifact containing the raw captions for every video in the queue.
3. Ensure the output is compatible with residential IP constraints and gentle pacing.
4. Verify the completeness and accuracy of the transcripts before finalizing.
5. Deliver the artifact in a structured format (e.g., JSON or text file) for easy integration.
6. Log any errors or missing transcripts for follow-up.

**What changed:** Action confirmed; Reel executes transcript fetch via YouTube tool.
