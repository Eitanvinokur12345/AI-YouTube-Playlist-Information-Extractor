---
name: excavatortron-activator
description: "Find and ACTIVATE the best AI skill, tool, MCP connector, prompt, or command from the Excavatortron knowledge hub for any task — installs Claude skills, adds MCP connectors, or emits a ready-to-deploy block for any other tool (ChatGPT, Gemini, Cursor, Google Antigravity, Stitch, Gamma, Omni, …). Use whenever the user asks 'is there a skill/tool/connector for X', 'set me up to do X', or wants to apply something from Excavatortron."
---

# Excavatortron Activator

Excavatortron is a self-running hub of AI **skills** (techniques), **tools** (products), **models**,
**MCP connectors**, **prompts**, **commands**, and **news**, mined from a YouTube playlist + 80+ web
sources. This skill turns that catalogue into something you can ACTUALLY USE in a session — not
copy-paste. Given a task, it finds the best match and activates it in the current environment.

The hub is a public, machine-readable API, so this works from any machine:
`https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data/hub.json`
(or the local `data/` folder when you're inside the Excavatortron repo).

## When to use
Trigger when the user asks any of: "is there a skill/tool/connector for X?", "set me up to do X",
"what's the best way to <task> with AI", "give me a memory/MCP/retrieval setup", or asks to
apply / install / activate anything from Excavatortron.

## How to run it
This skill folder ships two scripts. Always FIND first, then ACTIVATE the user's choice.

1. **Find** the best matches for the task:
   ```
   python find.py "<the user's task in their own words>"
   ```
   It searches the hub and prints JSON: the top skills, tools, MCP connectors, prompts and commands
   for the task, each with `slug`, `score`, `quality`, `target_tool`, `url`, and a short `desc` —
   PLUS a `recipe` object: the assembled **combination** for the task (`components` with a `role`
   each — primary / connector / supporting / command / prompt), a one-line `why`, an ordered
   `activation_plan`, and `activate_all` (a single command that activates the whole combination).

2. **Show** the user the `recipe` first — "for this task, use **A** (the technique) + **B** (the MCP
   connector it needs) + **C** (a supporting tool)" — that combination is the point. Then list the
   2–3 alternatives per type so they can swap any component. Ask which to activate, or if they said
   "just set me up", run the recipe's `activate_all`.

   - **Activate the whole combination at once →** run the recipe's `activate_all`, e.g.
     `python activate.py combo skill:<slug> connector:<slug> tool:<slug> --tool "claude"`.
     It installs the skill, prints the MCP connector setup, and deploys the supporting tool(s) —
     all logged to the manifest. Use this when the user wants the combination, not one item.

3. **Activate** the chosen item by type:
   - **Skill (technique) →** `python activate.py skill <slug>`
     Installs the SKILL.md into `~/.claude/skills/<slug>/` so Claude auto-loads it. In Claude Code
     it's live immediately; in Claude Desktop, tell the user to restart. THIS is the real
     activation — the technique is now part of the environment.
   - **MCP connector →** `python activate.py connector <slug>`
     Prints the `mcpServers` JSON to add to `claude_desktop_config.json` (Desktop) or the
     `claude mcp add …` command (Claude Code), plus the install/source. Then: restart → its tools
     appear in the session.
   - **ANY OTHER TOOL** (ChatGPT, Gemini, Cursor, GitHub Copilot, Google Antigravity, Stitch, Gamma,
     Omni, Midjourney, Higgsfield, AIR — anything that exists or will exist) →
     `python activate.py deploy skill|tool|prompt|command <slug> --tool "<tool name>"`
     It WRITES the real NATIVE artifact for that tool under `./excavatortron-deploy/` — a Cursor
     `.cursor/rules/<slug>.mdc`, a Copilot `.github/copilot-instructions.md`, a ChatGPT/Gemini
     instructions file, or (for any tool without a known native format) a portable
     `<tool>/<slug>.instructions.md`. This is the "skills system, but inside each tool."
   - Every activation is logged to `~/.claude/excavatortron-activated.json`; `python activate.py
     manifest` lists what's active (so it can later be swapped/uninstalled).

4. **Confirm** it's active. If it's a skill, optionally demonstrate it on the user's task right away.

## Reading across EVERY tab
`find.py` searches the WHOLE hub — skills, tools, **models**, connectors, prompts, commands — not a
single category. Always consider the full picture: a task may be best served by a skill, by a tool,
by wiring an MCP connector, by choosing a particular **model**, by a prompt or command, or (usually)
by a COMBINATION of these. Use the `recipe` to assemble that combination across tabs.

## Choosing vs. asking (the options protocol)
After `find.py`, decide whether the best path is clear:

- **One clearly-best approach** → just do it. Show the `recipe`, activate it, confirm.
- **No single best answer** — several viable approaches, an ambiguous goal, or a real trade-off the
  existing data can't settle → DON'T silently guess. Present **2–4 concrete options**, each with a
  one-line **explanation** of what it gives up and gains, then ask the user to pick with a
  multiple-choice question (an "American-style" choice — use the `AskUserQuestion` tool, each option
  = one viable recipe/approach). Recommend one and mark it. Then activate whatever they choose.

  Good triggers for options: "find me a way to do X" where X maps to 2+ strong but different stacks
  (e.g. a no-code path vs a coded MCP path), or where free-vs-paid / simple-vs-powerful genuinely
  diverge.

- **NOSG override** — if the user's message ends with **`NOSG`** (No Options, Skip Guessing — "choose
  what's best yourself"), NEVER present options. Pick the single best approach on the user's behalf,
  activate it, and just report what you chose and why in one line. Strip the `NOSG` token before
  acting on the request.

## Token frugality (important)
This skill must NOT eat the user's token budget. Keep it cheap:
- Run `find.py "<task>" --lean` by default — it prints ONLY the recipe (the combination + one
  activation command), not the full per-type lists. Use the full (non-lean) output only when the
  user explicitly wants to browse alternatives.
- Don't paste raw JSON back to the user; report the recipe in one or two short lines.
- Activate, then stop. Don't re-run `find.py` repeatedly for the same task.

## Real access (give working links, never just a name)
Each `find.py` result now carries real links: `homepage`, `github`, `deploy` (one-click deploy),
`install` (for MCP/CLI), and `source` (the first video that revealed it). ALWAYS hand the user the
real access for whatever you recommend — the homepage to read, the GitHub to clone, the deploy link
to run it, or the install command for an MCP. If a result has none yet (links still resolving), say
so and point to the `source` video. This is the difference between a usable tool and a dead name.

## Building from a Design (the Designs tab)
When the user says "build something like <design>", find it in `designs.json` and reproduce its
ACTUAL style — its colors, typography, layout, components and vibe (and `style_tags`: the owner
likes bold / colorful / maximalist + playful / retro / brutalist). Do NOT output a generic AI look.
Pull the real reference: open its `homepage`/`github`, match that aesthetic faithfully, and use the
`impeccable` / `frontend-design` skills to execute it. The point is "looks like THAT," not "looks AI-made."

## Rules
- NEVER invent a skill/tool/connector/model — only activate what `find.py` returns from the real hub.
- Lead with the assembled `recipe` (the combination), then surface 2–3 alternatives per type so any
  component can be swapped.
- For Claude, installing the SKILL.md (or adding the MCP server) IS the activation. For every other
  tool, the deploy block is the equivalent — paste it into that tool's instruction surface.
- If a script errors (offline, etc.), fall back to reading the hub JSON directly and proceed.
