# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-874` (dept) · 2026-08-10T20:35:27.711189+00:00
> Participants: Chisel, Sift, Marrow · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Use BloodHound-MCP for structured extraction and analysis of the earnings call.
**Plan:**
1. Pull the earnings call file directly (MP3/MP4) instead of using Luma's native transcript feature.
2. Feed the earnings call file to BloodHound-MCP for structured extraction.
3. Run kimtaeyoon83/mcp-server-youtube-transcript on the earnings call file if necessary to support BloodHound-MCP.
4. Extract structured text for analysis from the output of BloodHound-MCP.
5. Conduct a deep review of the extracted transcript for key insights.
**What changed:** The plan now uses raw audio/video input with BloodHound-MCP instead of Luma's native transcript feature.
