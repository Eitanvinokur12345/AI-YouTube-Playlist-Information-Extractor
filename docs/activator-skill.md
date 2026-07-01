---
name: excavatortron-activator
description: Find and ACTIVATE the best AI skill, tool, MCP connector, model, prompt, or command — or a COMBINATION of them — from the Excavatortron hub for any task, and set it up right where you are. One universal skill that works in Claude chat, cowork, and Claude Code, and pastes into any other AI tool (Cursor, GitHub Copilot, ChatGPT, Gemini, and more). Triggers on "activate X", "set me up with X", "set me up to do a task", "is there a skill/tool/connector for X", "what is the best way to do something with AI", or "install X from Excavatortron".
---

# Excavatortron Activator

Turn **"I want to do X"** into **"X — and the stack it needs — is set up and usable in the tool I'm in right now."** Assemble the best combination for the task, set it up where you can, give an exact copy‑paste command/artifact where you can't. Only hand over a link for the one step you genuinely cannot do (a hosted product's sign‑in or an API key).

## Put this ONE skill on any tool (no per-tool versions)
This is a single universal file — the SAME `SKILL.md` goes everywhere:
- **Claude Code** → drop it in `~/.claude/skills/excavatortron-activator/`.
- **Claude chat / cowork** → upload it as a Skill.
- **Cursor** → save its text as `.cursor/rules/excavatortron-activator.mdc`.
- **ChatGPT / Gemini / any other tool** → paste its text into that tool's custom-instructions / system-prompt box.
Same content, everywhere. Update it once, re-drop or re-paste to refresh.

## Step 0 — sense the environment (decides what you can do)
- **Shell + file write** (e.g. Claude Code): **perform** the setup.
- **Chat / cowork / another tool** (no shell): **output** the exact command(s) / native artifact to paste, and open the live tool.

## Step 1 — find (hybrid — use the first that works)
1. **Bundled engine** (Claude Code, this folder present): `python activate.py "<task>" --top 5 --json`
2. **Fetch the public hub** (if you can fetch URLs): name‑match across
   `https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data/{tools,skills,connectors,models,prompts,commands}.json` — each match carries a `setup` recipe + real links.
3. **Your own knowledge** (chat with no fetch): if you already know the tools, proceed.

Search the **WHOLE hub**, not one tab — the best answer is usually a **combination** across tabs (a technique + the MCP it needs + a supporting tool + a prompt/command).

## Step 2 — assemble a FEW combination plans
Build **2–4 candidate plans**, each a recipe with roles:
- **primary** (does the core job) · **connector** (the MCP it needs, if any) · **supporting** (a tool/model that helps) · **prompt/command** (if one fits).
Give each plan a one‑line **trade‑off** (free vs paid, no‑code vs coded, simple vs powerful) and mark the one you recommend.

## Step 3 — choose (options UNLESS `NOSG`)
- **Default:** present the 2–4 plans as an American‑style choice (use `AskUserQuestion` if available, else a numbered list), recommend one, and let the user pick. Don't silently guess when approaches genuinely diverge.
- **`NOSG` override** (No Options, Skip Guessing): if the user's message ends with `NOSG`, do **not** present options or advise — silently pick the single best plan, run it, and report what you chose in one line. Strip `NOSG` before acting.

## Step 4 — activate the chosen plan (per component; ask permission before installing/writing)
- **Claude skill** → write its `SKILL.md` to `~/.claude/skills/<slug>/SKILL.md` (Claude Code) or tell the user to upload it (chat/cowork); reload.
- **MCP connector** → run `claude mcp add <slug> -- npx -y <package>` (Claude Code) or give that exact command; confirm with `claude mcp list`.
- **Open‑source tool** → `git clone <github>` + install/run per its README.
- **Hosted product** → open its site; if `setup.needs_key`, say exactly which key and where (never enter it yourself).
- **ANY OTHER TOOL** (Cursor, Copilot, ChatGPT, Gemini, Antigravity, Stitch, Gamma, …) → **write the native artifact** for that tool under `./excavatortron-deploy/`:
  - Cursor → `.cursor/rules/<slug>.mdc`
  - GitHub Copilot → `.github/copilot-instructions.md`
  - ChatGPT / Gemini / other → `<tool>/<slug>.instructions.md` (portable paste‑in)
  This is "the skills system, inside each tool." **Exact templates + 2 worked combination examples are in `REFERENCE.md` (this folder)** — load it when you need the precise format for a tool.

## Step 5 — verify + report
Confirm where possible (skill file exists / `claude mcp list` shows it / repo cloned / artifact written) and state the ONE next action for the user (reload / sign in / run). If nothing matched, say so and give the closest alternatives.

## Build from a Design (Designs tab)
"Build something like <design>" → find it in `designs.json` and reproduce its REAL style — colors, typography, layout, components, vibe (owner likes **bold / colorful / maximalist + playful / retro / brutalist**) — using the `frontend-design` / `impeccable` skills. Not a generic AI look.

## Rules
- Never invent an item — only activate what the hub returns (or you genuinely know).
- Lead with the recommended plan; stay token‑frugal (report the recipe in 1–2 lines, don't paste raw JSON).
- Prefer directly‑usable kinds (Claude skill / MCP connector) over a raw repo unless the user wants the source.
- Test: `activate n8n` → `claude mcp add n8n -- npx -y n8n` (+ alternatives). `set me up to <task> NOSG` → just build+run the best stack, one‑line report.
