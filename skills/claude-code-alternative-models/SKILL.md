---
name: claude-code-alternative-models
description: "Use when you want to run Claude Code's agentic coding workflows on free or cheaper models like DeepSeek, Kimi, or Ollama instead of paying for Claude subscriptions."
---

# Claude Code with Alternative AI Models

## Overview
Open-source tools allow Claude Code's powerful agentic coding capabilities to be routed through alternative AI model providers. This breaks provider lock-in and significantly reduces costs while maintaining Claude Code's core features.

## Key Techniques
- Install an open-source model-routing adapter for Claude Code
- Point Claude Code to DeepSeek, Kimi, Ollama, or other alternative providers
- All Claude Code capabilities (file reading, editing, terminal commands, bug fixing) continue to work

## How to Apply
1. Install the open-source model routing layer for Claude Code
2. Configure your preferred model provider (DeepSeek, Kimi, Ollama, etc.) in the Claude Code config
3. Run Claude Code as normal — it routes through your chosen provider instead of Anthropic's API
4. Switch providers freely depending on task requirements and cost constraints

## Examples
- Use DeepSeek for complex code generation (near-free cost)
- Use Ollama for fully local, offline agentic coding
- Use Kimi for fast, low-latency completions

## Source
Extracted from: [Run Claude Code with Free AI Models..](https://www.youtube.com/watch?v=vFyv1dLhm4s)
Channel: Sisinty-One
