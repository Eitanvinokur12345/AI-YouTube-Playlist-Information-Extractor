# Excavatortron Activator — Reference (worked examples + per-tool templates)

Load this only when you need a concrete example or the exact format for a tool's artifact. The main
`SKILL.md` is the protocol; this file makes it precise.

---

## Worked example 1 — "scrape a website into Notion" (a COMBINATION)
**Recommended plan** (free, coded):
- primary: **Firecrawl** — web scraping (MCP)
- connector: **Notion MCP** — write the result into Notion
- prompt: "scrape {url}, extract the main content, create a Notion page with it"

Exact setup (Claude Code — or hand these to the user to paste):
```
claude mcp add firecrawl -- npx -y firecrawl-mcp
claude mcp add notion    -- npx -y @notionhq/notion-mcp-server
claude mcp list
```
Then: "scrape {url} and create a Notion page with the result."
**Alternative plan** (no-code): n8n or Zapier flow — trade-off: no coding, but less control and a paid tier.

## Worked example 2 — "build a landing page like a design I saw"
**Recommended plan:**
- primary: the **frontend-design** (or **impeccable**) Claude skill
- supporting: a match from `designs.json` (open its live URL, copy its REAL colors/type/layout/vibe)
- prompt: "build a landing page in the style of {design name}: {its style_tags}"

Setup: ensure the frontend-design skill is installed; open the design's `source_url`; reproduce the real style (not a generic AI look).

---

## Native-artifact templates (when activating a found item for a NON-Claude tool)
Write under `./excavatortron-deploy/{tool}/…`. Fill the item's name + instructions.

### Cursor → `.cursor/rules/{slug}.mdc`
```
---
description: {one-line what this does}
alwaysApply: false
---
{the skill/tool instructions, adapted for Cursor}
```

### GitHub Copilot → `.github/copilot-instructions.md`
```
# {name}
{instructions Copilot should follow}
```

### ChatGPT / Gemini / any tool with a "custom instructions" box → `{tool}/{slug}.instructions.md`
```
# {name} — paste into {tool}'s custom instructions / system prompt
{instructions}
```

### Universal fallback (any tool without a known format) → `{tool}/{slug}.instructions.md`
Plain markdown with the instructions. Paste it into whatever instruction/system-prompt surface the tool exposes. If the tool can fetch URLs, it can instead pull the latest from the hub.

---

## Deriving the exact connector command (when a recipe has no package)
1. If the item's `setup.command` exists → use it verbatim.
2. Else if a GitHub repo is known → `claude mcp add {slug} -- npx -y {repo-name}` (or `uvx {repo}` for Python).
3. Else → open the connector's homepage/README, copy its exact `npx` / `uvx` / `pip` command. If none is published, give the homepage and say "add per its README."

---

## Every-tool portability checklist
- **Claude Code:** drop this folder in `~/.claude/skills/excavatortron-activator/`.
- **Claude chat / cowork:** upload `SKILL.md` (or the zipped folder for SKILL.md + REFERENCE.md).
- **Cursor:** save `SKILL.md`'s text as `.cursor/rules/excavatortron-activator.mdc`.
- **ChatGPT / Gemini / other:** paste `SKILL.md`'s text into the custom-instructions / system-prompt box.
- **Any tool that can fetch URLs:** it can pull the current version from the hosted docs URL.
- The main `SKILL.md` is fully self-contained, so the Activator works even in tools that can't fetch or run scripts — this reference just makes it sharper.
