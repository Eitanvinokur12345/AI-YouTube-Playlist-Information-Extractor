---
name: excavatortron-activator
description: Find and ACTIVATE the best AI skill, tool, MCP connector, prompt, or command from the Excavatortron hub for any task — and actually SET IT UP in-session (install the Claude skill, add the MCP connector, clone+run the repo), not just hand over a link. Use whenever the user asks "is there a skill/tool/connector for X", "set me up to do X", "activate X", or wants to apply something from Excavatortron.
---

# Excavatortron Activator — find the right capability AND set it up

Your job is to take the user from **"I want to do X"** to **X is set up and usable in their tools**, in this session. Do the setup; only hand over a link for the one step you genuinely cannot do for them (a hosted product's sign-in or an API key).

## 1. Find the capability
Prefer the activation engine — it reads each hub item's machine-readable `setup` recipe:

- If the Excavatortron repo is available: `python -m src.activate "<the user's request>" --top 3 --json`
- Otherwise fetch and match by name across these (read each match's `setup` field):
  `https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data/{tools,skills,connectors}.json`

Pick the best match. **Prefer a Claude skill or MCP connector** (directly usable inside the user's tools) over a raw repo, unless the user explicitly wants the source. Show the runner-up matches so the user can redirect.

## 2. Do the setup in-session (ask permission before anything that writes or installs)
Act on the item's `setup.kind`:

- **claude skill** → create `~/.claude/skills/<slug>/SKILL.md` (fetch the skill's content from its source repo/homepage), then tell the user to reload Claude Code. Verify the file exists.
- **mcp connector** → run the recipe's command (`claude mcp add <slug> -- npx -y <package>`), then confirm with `claude mcp list`.
- **open-source tool** → `git clone <github>` and install/run per its README.
- **hosted web product** → you cannot install it; give the homepage link and note it needs sign-in / an API key.

If `setup.needs_key` is true, tell the user exactly which key/sign-in is required and where — do **not** enter credentials yourself.

## 3. Verify + report
Confirm the result (skill file present / `claude mcp list` shows it / repo cloned + deps installed). Report what's now set up and the single next action for the user (reload, sign in, or run). If nothing matched, say so and suggest the closest alternatives from the hub.

## Principles
- **Setup happens here, not via a link.** A link is the exception (signup/keys), not the default.
- Match the user's actual tool (Claude, Cursor, ChatGPT, Gemini-CLI…) when choosing skill vs connector vs repo.
- Every hub item already carries a `setup` recipe — use it as the source of truth.
