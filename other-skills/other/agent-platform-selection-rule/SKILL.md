---
name: agent-platform-selection-rule
description: "Use when deciding which agent platform to use for a task — match task type (code, life automation, visual, low-friction) to the right platform."
---

# Agent Platform Selection Rule

## Overview
A quick decision rule matching agent task types to the right platform. Each of the four major agent platforms wins at a specific category — using the wrong one adds friction without improving output quality.

## Key Techniques
- Task-type routing rather than picking one platform for everything
- Evaluating "interpretable reasoning" need (Claude Code) vs "friction minimization" (Codex)
- Distinguishing code/text tasks from visual/multimodal tasks (Antigravity)
- Considering where the agent needs to live (messaging apps = OpenClaw)

## How to Apply
- **Words and code tasks, complex reasoning**: Claude Code — watch the model think step-by-step and steer mid-flight
- **Already in ChatGPT / lowest friction**: OpenAI Codex — same account, already covered by Plus plan, VS Code integration
- **Life automation from a chat window**: OpenClaw — text it from Telegram/WhatsApp, the agent works on your computer and texts back
- **Visual or front-end work**: Google Antigravity — best multimodal reasoning for UI, design, images, and video

## Examples
Need to clean up 80 files and build a spreadsheet → Claude Code. Want to spin up a side project with zero new accounts → Codex. Need email triage and reminders from your phone → OpenClaw. Building landing page UI and need agent to check layout screenshots → Antigravity.

## Source
Extracted from: [AI Agents Explained: How to Create and Use AI Agents in 2026](https://www.youtube.com/watch?v=4TvH-OZhwxI)
Channel: AI Master
