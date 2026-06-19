---
name: claude-code-n8n-workflow-builder
description: "Use when you need to generate a complete n8n automation workflow from a plain-language description — Claude Code + n8n MCP handles all node selection and configuration."
---

# Claude Code n8n Workflow Builder

## Overview
By connecting Claude Code to the n8n MCP server, you gain access to knowledge of n8n's 1,851 workflow nodes (822 core + 1,029 community). Describe any automation goal in plain language and Claude generates a complete, importable n8n workflow in under 5 minutes.

## Key Techniques
- Install the n8n-mcp GitHub repo and add your N8n API key to Claude Code
- Describe your workflow goal in natural language — Claude picks the right nodes automatically
- Claude Code can install Cursor as an extension for IDE-based workflow generation

## How to Apply
1. Clone `n8n-mcp` from GitHub
2. Add your N8n API key to the Claude Code config
3. Open Claude Code (or Cursor with Claude Code extension)
4. Describe your automation: "Build an n8n workflow that monitors Gmail for invoices and posts to Slack"
5. Claude generates and returns the complete workflow JSON
6. Import the JSON into your n8n instance and run

## Examples
- "Build a workflow that checks RSS feeds every hour and posts summaries to Notion" → complete 8-node workflow in one prompt
- Complex multi-step automations with webhooks, filters, and API calls generated without manually connecting nodes

## Source
Extracted from: [Claude Code Builds N8n Workflows From One Prompt — Setup Guide](https://www.youtube.com/watch?v/rDCbYQRLG-Y)
Channel: Sani | AI Nexus
