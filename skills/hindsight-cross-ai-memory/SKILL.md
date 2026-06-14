---
name: hindsight-cross-ai-memory
description: "Use when you want one unified memory layer across Claude, ChatGPT, Gemini, and Claude Code — eliminating the need to re-enter context in each AI tool separately."
---

# Cross-AI Unified Memory with Hindsight MCP

## Overview
Hindsight is a cloud-hosted (also available as a local database) memory system with an MCP server that gives all your AI tools access to a single shared knowledge base. Point Claude, ChatGPT, Gemini, and Claude Code at the same Hindsight endpoint and they all share the same brain.

## Key Techniques
- **retain**: Store a piece of context (decision, preference, project fact) to the shared memory
- **recall**: Pull relevant memories into any active AI session by querying the Hindsight MCP
- **reflect**: Synthesize across all saved memories to surface patterns and connections you haven't explicitly queried

## How to Apply
1. Sign up at Hindsight and get your MCP server endpoint
2. Add the Hindsight MCP server to Claude Code's MCP config
3. Add the same Hindsight MCP to ChatGPT (via OpenAI's MCP support) and Gemini (via Google's MCP support)
4. Use `retain` to save important context as you work: decisions, preferences, project facts
5. In any new AI session, run `recall` with a topic to pull relevant memories in
6. Periodically run `reflect` to surface cross-memory insights

## Examples
- Save your coding preferences once via `retain`: "Always use TypeScript strict mode, prefer functional components"
- Open a new ChatGPT session and `recall "coding preferences"` — same context loads without manual input
- After several projects, `reflect` surfaces: "You consistently prefer edge-less APIs — consider this when choosing new tools"

## Source
Extracted from: [One shared memory across Claude/ChatGPT/Gemini (Hindsight)](https://www.youtube.com/watch?v=yhqLtGAlf0g)
Channel: James Goldbach
