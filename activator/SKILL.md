---
name: excavatortron-activator
description: Find and ACTIVATE the best AI skill, tool, MCP connector, prompt, or command from the Excavatortron hub for any task, and set it up right where you are. Portable — works in Claude chat, cowork, and Claude Code, and can be adapted to other AI tools. Triggers on "activate X", "set me up with X", "set me up to do X", "is there a skill/tool/connector for X", or "install X from Excavatortron".
---

# Excavatortron Activator

Take the user from **"I want to do X"** to **X is set up and usable in the tool they're in right now**. Do the setup where you can; give an exact copy‑paste command where you can't. Only hand over a link for the one step you genuinely cannot do (a hosted product's sign‑in or an API key).

## Step 0 — sense the environment (this decides what you can do)
- **Can run shell commands + write files** (e.g. Claude Code): you will **perform** the setup.
- **Chat / cowork / another tool** (no shell): you will **output the exact command(s)** for the user to paste, and open the live tool.

## Step 1 — find the capability
Try these in order; use the first that works in your environment:
1. **Bundled engine** (Claude Code, this skill folder present): `python activate.py "<request>" --top 3 --json`
2. **Fetch the public hub** (if you can fetch URLs): read and name‑match across
   `https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data/tools.json`, `/skills.json`, `/connectors.json` — each match has a `setup` recipe.
3. **Your own knowledge** (chat with no fetch): if you already know the tool, proceed from what you know.

Prefer a **Claude skill or MCP connector** (directly usable in the user's tools) over a raw repo, unless they want the source. Mention 1–2 runner‑up matches.

## Step 2 — determine the setup (from the item's `setup.kind`, or infer)
- **claude skill** → the skill's `SKILL.md` goes in `~/.claude/skills/<slug>/SKILL.md`.
- **mcp connector** → `claude mcp add <slug> -- npx -y <package>` (use the recipe's exact command).
- **open‑source tool** → `git clone <github>` then install/run per its README.
- **hosted product** → no local install; open its site and (if needed) sign in / add an API key.

## Step 3 — act
- **If you can run commands:** ask permission, then do it (write the skill file / run `claude mcp add` / clone+install). 
- **If you can't:** print the single exact command in a code block and say "paste this in Claude Code" (or the relevant tool), plus the live link.
- If `setup.needs_key` is true, tell them exactly which key/sign‑in and where — never enter credentials yourself.

## Step 4 — verify + report
Confirm the result where possible (`claude mcp list`, the skill file exists, repo cloned) and state the one next action for the user (reload / sign in / run). If nothing matched, say so and give the closest alternatives.

## Test me (30 seconds)
Type: **`activate n8n`** → I should return (and run, if I can) `claude mcp add n8n -- npx -y n8n`, and offer the n8n repo as an alternative.
Or: **`set me up with Playwright`** → the Playwright MCP connector, with the exact `claude mcp add` command.

## Notes
- Portable: the steps above are generic — the same skill works in Claude chat, cowork, Claude Code, Cursor, etc.
- The Excavatortron **OS (EXCAVA)** can also run activations inside the project itself — that's a separate, project‑side path (not required for this skill to work).
