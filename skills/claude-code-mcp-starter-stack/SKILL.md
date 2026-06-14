---
name: claude-code-mcp-starter-stack
description: "Use when setting up Claude Code for real development work — installs the three essential MCP servers that turn Claude Code from a chatbot into a full coding agent."
---

# Claude Code MCP Starter Stack

## Overview
Without MCP servers, Claude Code is just a chatbot. The three-MCP starter stack gives it live access to your repo, your real task specs, and a browser to verify builds — the minimum to do professional development work.

## Key Techniques
- **GitHub MCP**: Real-time access to repo files, issues, pull requests, and branches
- **Notion or Linear MCP**: Pull actual task specs and requirements (not made-up assumptions)
- **Playwright MCP**: Open a real browser and verify the UI actually works after building

## How to Apply
1. **Install GitHub MCP**:
   - Configure via Claude Code's MCP settings panel
   - Authenticate with your GitHub account
   - Verify Claude can read your repo structure: `list all files in src/`

2. **Install Notion MCP** (if you use Notion for task management):
   - Add Notion MCP from the MCP marketplace
   - Connect to your workspace
   - Test: `list my open tasks in the Engineering database`

   OR **Install Linear MCP** (if you use Linear):
   - Add Linear MCP and authenticate
   - Test: `show me open issues assigned to me`

3. **Install Playwright MCP**:
   - Install via Claude Code MCP config
   - Test: `open a browser and navigate to localhost:3000`

4. Work flow: GitHub context → task from Notion/Linear → Claude builds → Playwright verifies → PR opened via GitHub MCP

## Examples
- "Fix the bug in issue #47" → Claude reads the issue via GitHub MCP, reads the relevant code, makes the fix, opens the browser via Playwright to verify, creates a PR
- "Build the feature from this Linear ticket" → Claude pulls the full spec via Linear MCP, implements it, verifies via Playwright, commits via GitHub MCP

## Source
Extracted from: [Claude Code Gets These 3 MCPs or It's Useless](https://www.youtube.com/watch?v=i7I3sW_lxGs)
Channel: Sebastian Hardy | AI Marketing
