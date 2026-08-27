# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-780` (dept) · 2026-08-27T14:45:42.450636+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full raw transcript for the Alima video (ID: `e2Z5eBVDrKM`).
2. Enforce the 65% minimum confidence floor during retrieval.
3. Verify the transcript meets the 65% confidence threshold before proceeding.
4. Store the transcript in the designated repository or system for pending videos.
5. Log the action and timestamp for audit purposes.
6. Notify relevant stakeholders upon successful retrieval.

**What changed:** The video ID was corrected to `e2Z5eBVDrKM` and the transcript fetch was explicitly authorized with confidence enforcement.
