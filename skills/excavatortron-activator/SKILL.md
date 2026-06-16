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
   for the task, each with `slug`, `score`, `quality`, `target_tool`, `url`, and a short `desc`.

2. **Show** the user the top 2–3 matches per relevant type, with one line each, and ask which to
   activate (or activate the clear best one if they said "just set me up").

3. **Activate** the chosen item by type:
   - **Skill (technique) →** `python activate.py skill <slug>`
     Installs the SKILL.md into `~/.claude/skills/<slug>/` so Claude auto-loads it. In Claude Code
     it's live immediately; in Claude Desktop, tell the user to restart. THIS is the real
     activation — the technique is now part of the environment.
   - **MCP connector →** `python activate.py connector <slug>`
     Prints the `mcpServers` JSON to add to `claude_desktop_config.json` (Desktop) or the
     `claude mcp add …` command (Claude Code), plus the install/source. Then: restart → its tools
     appear in the session.
   - **Tool / prompt / command →** `python activate.py paste tool|prompt|command <slug>`
     Emits the ready-to-use text + source so it can be applied immediately.
   - **Any OTHER tool** (ChatGPT, Gemini, Cursor, GitHub Copilot, Google Antigravity, Stitch, Gamma,
     Omni, …) → `python activate.py paste skill <slug> --tool "<tool name>"`
     Emits a deploy block formatted for THAT tool's instruction/rules surface (custom GPT, Gem,
     rules file, system prompt) — the "as if uploaded to the environment" equivalent.

4. **Confirm** it's active. If it's a skill, optionally demonstrate it on the user's task right away.

## Rules
- NEVER invent a skill/tool/connector — only activate what `find.py` returns from the real hub.
- Prefer the highest-`quality` match; surface 2–3 so the user can choose.
- For Claude, installing the SKILL.md (or adding the MCP server) IS the activation. For every other
  tool, the deploy block is the equivalent — paste it into that tool's instruction surface.
- If a script errors (offline, etc.), fall back to reading the hub JSON directly and proceed.
