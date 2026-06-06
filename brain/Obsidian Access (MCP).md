---
tags: [reference, obsidian, mcp, setup]
aliases: [Obsidian Access, Obsidian MCP, Give Claude Obsidian Access]
---

# Obsidian Access (MCP)

**Goal:** let Claude (Desktop **or** Claude Code) read and write *this* brain vault. This note
is the "tell me what to do" answer. Pick **Option A** (simplest) or **Option B** (full Obsidian
integration). Both keep any key **local** — nothing secret ever goes in the repo
(see [[Standing Constraints]]).

## First: open the vault
The vault already exists in the repo at **`C:\Users\eitan\AI-YouTube-Skills\brain`**. In
Obsidian → *Open folder as vault* → choose that `brain` folder. (No Desktop mirror needed;
editing it edits the repo. The local runner can also copy it to the Desktop — see
[[Operations and Setup]].)

---

## Option A — Filesystem MCP (simplest, recommended)
Gives Claude direct read/write to the `brain/` files. Needs **Node.js** installed.

1. Edit Claude **Desktop**'s config:
   `C:\Users\eitan\AppData\Roaming\Claude\claude_desktop_config.json`
2. Add a server under `mcpServers` (merge with any existing servers):
```json
{
  "mcpServers": {
    "excavatortron-brain": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\eitan\\AI-YouTube-Skills\\brain"
      ]
    }
  }
}
```
3. **Save and fully restart Claude Desktop.** The brain files now appear as tools.

> For **Claude Code**, the equivalent is one command:
> `claude mcp add excavatortron-brain -- npx -y @modelcontextprotocol/server-filesystem "C:\Users\eitan\AI-YouTube-Skills\brain"`

---

## Option B — Obsidian Local REST API + an Obsidian MCP server
Use this if you want Claude to work *through* Obsidian (search, backlinks, open notes) while
Obsidian is running.

1. In Obsidian: **Settings → Community plugins → Browse →** install **"Local REST API"**,
   enable it, and copy its **API key** (stays on your machine).
2. Install an Obsidian MCP server that talks to that API (e.g. an `obsidian-mcp` /
   `mcp-obsidian` package). **Package names change** — verify the current, maintained one on
   npm/GitHub before trusting it.
3. Add it to `claude_desktop_config.json` with the API key as an **env var** (never in the
   repo), e.g.:
```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "<the-verified-obsidian-mcp-package>"],
      "env": { "OBSIDIAN_API_KEY": "PASTE_LOCAL_KEY_HERE" }
    }
  }
}
```
4. **Restart Claude Desktop** (and keep Obsidian open so the REST API is reachable).

---

## Notes
- Restart Claude Desktop after **any** config edit.
- The repo also ships a project MCP server (`mcp_server/`) for the dashboard data — that's
  separate from vault access (see [[Operations and Setup]]).
- If Node/npx isn't installed, install Node.js LTS first.
