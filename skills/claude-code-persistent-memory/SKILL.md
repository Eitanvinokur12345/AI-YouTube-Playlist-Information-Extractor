---
name: claude-code-persistent-memory
description: "Use when setting up Claude Code on a project to give it persistent memory across sessions — so it remembers your project context, preferences, and file structure without re-briefing each time."
---

# Claude Code Persistent Memory Setup

## Overview
A one-time setup technique that gives Claude Code persistent memory across sessions. Once configured, Claude remembers your project context, conventions, and file structure, eliminating the need to re-explain the codebase at the start of every new session.

## Key Techniques
- Single setup command to enable persistent memory in Claude Code
- Store project context in a persistent file (CLAUDE.md or equivalent) that Claude reads at session start
- Eliminates context-limit errors caused by having to repeat project background in every session

## How to Apply
1. Run the one-time memory setup command in your Claude Code project directory
2. Create (or populate) a `CLAUDE.md` file at your project root with key context:
   - Project overview and goals
   - Architecture decisions and conventions
   - Key file locations and their purposes
   - Your workflow preferences
3. Claude Code will now read this file at the start of each session automatically
4. Update `CLAUDE.md` when significant changes occur so the memory stays accurate

## Examples
- A developer working on a React app adds architecture notes, component conventions, and environment setup to `CLAUDE.md` — Claude never asks "what stack are you using?" again
- An AI automation engineer stores their preferred tools, API patterns, and project folder structure so Claude picks up exactly where it left off
- A solo founder stores business context (customer, goal, revenue model) so Claude stays on-brand across multi-session builds

## Source
Extracted from: [Persistent memory just saved Claude Code](https://www.youtube.com/watch?v=Nj-j3eL7e2w)
Channel: Sebastian Hardy | AI Marketing
Full setup guide: https://docs.google.com/document/d/1oLwbqQ3JBL-EbJQEOo-Z9CrtZkD93ePp/edit
