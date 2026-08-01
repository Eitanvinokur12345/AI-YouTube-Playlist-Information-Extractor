---
name: openclaw-discord-bot-integration
description: "Give a self-hosted AI agent a presence inside a Discord server for team or community use."
---

# OpenClaw Discord Bot Integration

## Overview
A setup workflow for self-hosting an OpenClaw AI agent on a VPS and binding it to a Discord server as a bot, so the agent responds directly in allow-listed channels.

**Use case:** Give a self-hosted AI agent a presence inside a Discord server for team or community use.

## Key steps
1. Create the bot in the Discord developer portal and enable the Message Content and Server Members intents before inviting it.
2. Allowlist specific channel IDs so the agent only listens/responds where intended.
3. Set require_mention to false to let the agent respond to any message in an allow-listed channel, not just @-mentions.
4. Bind separate channels to separate agents for a multi-agent Discord setup, routing messages by channel.

## Details
- **Category:** integration
- **Tool:** other  ·  **Quality:** 6/10

## Source
Extracted from: https://www.youtube.com/watch?v=ulDkvWa1k34
