# Raise link coverage: pick the next 200 unlinked elements and the fastest resolution path

> Decision artifact · room `dept-raise-link-coverage-pick-the-893` (dept) · 2026-07-07T16:57:54.384596+00:00
> Participants: Fetch, Probe, Ledger · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Prioritize unlinked elements by a combined analysis of unlinked counts and inbound link traffic to identify the top 200 most impactful files.  

**Plan:**  
1. Run `grep -l '\[.*\](?!\(.*\))' /data/src/*.md` to list all files with unlinked elements.  
2. Count unlinked elements per file using `grep -c '\[.*\](?!\(.*\))' /data/src/*.md`.  
3. Collect inbound link traffic metrics for each file using `grep -c '\[.*\]' /data/src/*.md`.  
4. Rank the files by combining unlinked counts and inbound link traffic to determine their impact.  
5. Select the top 200 files based on impact and export this list to `/tmp/top200_unlinked_by_impact.txt`.  

**What changed:** Decision now balances unlinked counts with inbound link metrics to determine impact.
