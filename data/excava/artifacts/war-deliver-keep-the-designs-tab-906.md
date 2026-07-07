# Deliver: Keep the Designs tab pure: designs only, live previews, taste-ranked

> Decision artifact · room `war-deliver-keep-the-designs-tab-906` (war) · 2026-07-07T10:09:38.771818+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** We will conduct a comprehensive review of the designs directory to maintain the purity of the Designs tab.

**Plan:**
1. Run the command `find designs/ -type f \( -name "*.sketch" -o -name "*.fig" -o -name "*.xd" -o -name "*.psd" \) -print0 | xargs -0 ls -ltr` to list all design files.
2. Review the output files for relevance, quality, and completeness.
3. Filter out any outdated, incomplete, or poor-quality design files from the directory.
4. Establish a system for ongoing updates to the Designs tab to ensure its purity.
5. Set criteria for taste-ranking the remaining designs to curate the best quality for the tab.

**What changed:** The decision to comprehensively review design files ensures a systematic approach to maintaining quality and relevance.
