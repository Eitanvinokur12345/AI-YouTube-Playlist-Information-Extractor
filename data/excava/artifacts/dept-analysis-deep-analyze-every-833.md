# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-833` (dept) · 2026-08-13T11:24:05.000286+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Extract all instances** of "guidance" and "outlook" from the full earnings call transcript using BloodHound-MCP, capturing surrounding context (e.g., 50 words before/after each mention).
2. **Structure the output** as a JSON array where each entry includes:
   - `phrase`: the keyword ("guidance" or "outlook")
   - `quote`: the full sentence or clause containing the keyword
   - `speaker`: the executive or role (if identifiable)
   - `timestamp`: approximate time in the transcript (if available)
3. **Validate coverage** by cross-referencing the extracted list against the transcript to ensure no forward-looking statements are missed (e.g., synonyms like "expect," "forecast," or "target" if flagged in context).
4. **Enrich with metadata** by appending:
   - A frequency count of "guidance" vs. "outlook" mentions.
   - A summary of themes (e.g., revenue, margins, macroeconomic risks) derived from the surrounding context.
5. **Store the output** in a new file (`forward_looking_statements.json`) in the repo’s `/analysis/` directory with a timestamp.
6. **Flag outliers** for manual review (e.g., ambiguous phrasing, contradictions between statements, or deviations from historical guidance).

**What changed:** Added "outlook" to the extraction scope and formalized structured output with metadata enrichment.
