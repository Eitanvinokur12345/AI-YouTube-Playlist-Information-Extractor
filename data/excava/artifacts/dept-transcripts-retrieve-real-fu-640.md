# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-640` (dept) · 2026-07-20T17:06:46.249994+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the YouTube transcript tool to fetch full transcripts for all pending videos.
2. Verify each transcript exists and is complete before proceeding.
3. Store transcripts in a structured format (e.g., JSON/CSV) for easy retrieval.
4. Log any failures or missing transcripts for review.
5. Notify the user upon successful completion of all transcript fetches.
6. Archive the transcripts in a designated folder (e.g., `transcripts/`).

**What changed:** Automated transcript fetching replaces manual or partial methods.
