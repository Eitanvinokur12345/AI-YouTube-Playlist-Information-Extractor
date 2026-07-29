---
name: claude-seo-multi-agent-audit
description: "Use when auditing a website's SEO (technical, content, schema, local, or AI-search readiness) from inside Claude Code and you want a single prioritized action plan instead of manually running each check."
---

# Claude Code Multi-Agent SEO Audit Pipeline

## Overview
This skill packages a full SEO audit as a Claude Code plugin (open-source, "Claude SEO") that
fans a request out to 18 specialist agents and 25 sub-skills running in parallel, then merges
their findings into one prioritized action plan grounded in Google's own SEO/AI-Optimization
guidance.

## Key Techniques
- Split an audit into narrow, parallel specialist agents (technical, content/E-E-A-T, schema,
  local, international, e-commerce, AI-search/GEO) rather than one generalist pass.
- Ground every recommendation in an authoritative source (Google's guidance) instead of
  generic SEO folklore.
- Collapse many agents' findings into a single ranked action plan so the output is actionable,
  not just a pile of separate reports.

## How to Apply
1. Install the plugin (`git clone https://github.com/AgriscDaniel/claude-seo` into your Claude
   Code project, or add it as a plugin per the repo's install script).
2. Run `/seo audit <url>` for a full-site pass, or a narrower subcommand: `/seo page <url>`
   (single page), `/seo schema <url>` (markup validation/generation), `/seo geo <url>`
   (AI-answer-engine readiness), `/seo local <url>` (Google Business Profile / local SEO).
3. Optionally connect DataForSEO, Ahrefs, or Firecrawl MCP servers so the agents can pull live
   keyword and backlink data instead of static heuristics.
4. Work the returned prioritized action plan top-down.

## Examples
- Full audit: `/seo audit https://example.com` → technical + content + schema + GEO findings
  merged into one ranked to-do list.
- AI-search readiness only: `/seo geo https://example.com` → a score for how likely the page is
  to be cited inside an AI-generated answer (ChatGPT/Google AI Overviews) rather than ranked in
  classic blue links.

## Source
Extracted from: [This free GitHub repo replaced my SEO agency](https://www.youtube.com/watch?v=qRC3-R3jkMQ)
Channel: Jack Roberts
(Repo link surfaced in the video's top comments, not the description; also previously endorsed
via video GrRgeJUf4xo, "Claude's hidden ranking trick".)
