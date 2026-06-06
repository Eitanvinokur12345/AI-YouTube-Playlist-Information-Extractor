---
tags: [content, rules]
---

# Skills vs Tools

**The #1 content rule.** A *skill* and a *tool* are never the same record and never
share a tab. Mixing them is the single most common quality failure, so the analyze
engine ([[Engines|CLAUDE.md]]) and the [[Self-Improvement Loop]] both guard it.

## Definitions
- **Skill / technique** — *something you do.* A repeatable method, workflow, or
  prompt pattern you can apply yourself. Examples: "agentic loop with self-critique",
  "build a 3D website with Claude", "MCP-powered research workflow".
  → lives in `data/skills.json` → the **[[Tabs|Skills Library]]** tab.
- **Tool / product** — *something that exists.* A product, app, model, service, or
  website someone ships. Examples: Claude, Cursor, Nano Banana, Veo, a specific MCP
  server. → lives in `data/tools.json` → the **[[Tabs|Tools]]** tab.

## The model subset
**Models** (Claude Opus, GPT-x, Gemini, Veo, …) are a *subset of tools*. They're
tracked in `tools.json` and **mirrored** into `data/models.json` for the ranked
**[[Tabs|Models Ranking]]** tab (the podium 🥇🥈🥉). A model is still a tool.

## Connectors are their own thing
**MCP servers / connectors** are products too, but they get their own
`data/connectors.json` and **[[Tabs|Connectors]]** tab because they have extra
fields (free/paid, which Claude surface they run in, install/source).

## Quick test
> "Could I *do* this with my own hands and a prompt?" → **skill**.
> "Is this a thing someone *built and named*?" → **tool** (or model/connector).

## Why it matters
Visitors come to *learn techniques* (skills) **and** to *discover products* (tools).
Conflating them makes both worse: the Skills Library fills with product ads, and the
Tools tab fills with vague how-tos. Keeping them apart is what makes the dashboard
genuinely useful versus the competitors benchmarked in [[Three-Agent Review]].

## Related
- [[Tabs]] · [[Data Files]] · [[Engines]]
