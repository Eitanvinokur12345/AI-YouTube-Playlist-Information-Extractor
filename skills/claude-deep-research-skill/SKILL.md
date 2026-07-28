---
name: claude-deep-research-skill
description: "Use when Claude Code needs to produce a citation-backed, source-validated research report instead of a single shallow web search."
---

# claude-deep-research-skill

## Overview
An enterprise-grade research skill for Claude Code that runs an 8-phase pipeline (scope,
plan, parallel retrieval, triangulation, synthesis, critique, refinement) and scores source
credibility along the way, producing validated, citation-backed reports.

## Key Techniques
- Run the full 8-phase pipeline instead of a single-pass search-and-summarize.
- Score source credibility and run automated validation (nine structural checks) before
  trusting a claim.
- Auto-continue past the 18K-word report limit via recursive agent spawning for very deep
  reports.
- Keep citation tracking persistent so sources survive context compaction mid-research.

## How to Apply
1. Install: `git clone https://github.com/199-biotechnologies/claude-deep-research-skill.git ~/.claude/skills/deep-research`
2. Optionally install `search-cli` via Homebrew to enable multi-provider search (Brave,
   Serper, Exa, Jina, Firecrawl) instead of a single search backend.
3. Choose a research mode by time budget: Quick, Standard, Deep, or UltraDeep (2-45 minutes).
4. Export the finished report as Markdown, HTML (McKinsey-style), or PDF.

## Examples
The source video pairs this with `research-skill`: research-skill keeps findings persistent
across sessions, while claude-deep-research-skill is invoked to actually run a full, sourced
research pass on a given question.

## Source
Extracted from: [CLAUDE FORGETS EVERYTHING. THESE TWO FIX IT](https://www.youtube.com/watch?v=kqEToneO43g)
Channel: Dubibubi
Repo: 199-biotechnologies/claude-deep-research-skill (962 stars)
