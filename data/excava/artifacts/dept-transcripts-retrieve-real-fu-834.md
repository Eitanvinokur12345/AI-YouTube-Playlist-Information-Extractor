# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-834` (dept) · 2026-08-22T13:12:18.685137+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on each pending video.
2. Store the generated transcript file in the `transcripts` folder.
3. Post the file path to the `transcripts-w1` channel.
4. Confirm the tool’s IP source is residential and pacing limits are respected.
5. Verify transcript accuracy before finalizing.

**What changed:** Tool execution and transcript storage are now explicitly assigned to Reel with confirmation of IP/pacing constraints.
