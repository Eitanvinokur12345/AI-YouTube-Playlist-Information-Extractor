---
name: ai-executive-assistant-build
description: "Use when you want to build a personal AI executive assistant that connects to your real tools (email, calendar, tasks) and compounds capability through reusable skills."
---

# AI Executive Assistant Build Pattern

## Overview
A practical approach to building a fully functional AI executive assistant using an agent loop, markdown context files, MCP tool connections, and reusable skills. Once built, the assistant handles email, calendar, research, and task management and gets progressively more capable as you add skills.

## Key Techniques
- **Context files**: Markdown files that give the agent persistent memory of your preferences, workflows, and project context
- **MCP tool connections**: Connect the agent to real tools (Gmail, Calendar, Notion, Slack) for actual execution
- **Reusable skills**: Each installed skill makes the assistant more specialized — they compound over time
- **Agent loop**: The cycle of Observe → Plan → Act → Observe that runs everything — same across all platforms

## How to Apply
1. Write a CONTEXT.md (or CLAUDE.md) describing who you are, your goals, your preferences, your regular tasks
2. Connect high-impact MCP tools: start with email + calendar
3. Build 3-5 core reusable skills for your most repeated tasks (e.g., "morning briefing", "email triage", "meeting prep")
4. Test the assistant on real tasks and refine the context file based on what the agent misses
5. Gradually add more skills and tool connections as you discover gaps

## Examples
- Morning briefing skill: reads calendar, email, news, and generates a daily plan
- Email triage skill: categorizes and drafts replies to the 10 most important emails
- Research skill: looks up relevant information and formats it as a brief for the next meeting

## Source
Extracted from: [Building AI Agents that actually work (Full Course)](https://www.youtube.com/watch?v=eA9Zf2-qYYM)
Channel: AI Master / Remy Gaskell
