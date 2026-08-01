---
name: openclaw-discord-bot-integration
description: "Use when you want a self-hosted OpenClaw AI agent to operate as a Discord bot inside specific server channels."
---

# OpenClaw Discord Bot Integration

## Overview
A setup workflow for self-hosting an OpenClaw AI agent on a VPS and connecting it to a
Discord server as a bot, so the agent responds directly in allow-listed channels.

## Key Techniques
- Register the bot in the Discord developer portal and enable the required intents.
- Restrict the bot to specific channels via an allowlist of channel IDs.
- Control mention behavior (respond to every message vs. only @-mentions) per channel.
- Route messages to specific agents in a multi-agent setup by binding each channel to an agent.
- Reach a self-hosted VPS agent securely via an SSH tunnel / port forwarding and a pairing code.

## How to Apply
1. Create a bot application in the Discord developer portal; generate a bot token.
2. Enable the "Message Content" and "Server Members" intents.
3. Invite the bot to the server with the needed permissions.
4. Copy the target channel ID(s) and add them to the agent's allowlist.
5. Set `require_mention: false` if the bot should respond to any message in an allow-listed
   channel, or leave it true to require an @-mention.
6. For multiple agents, bind each Discord channel to a specific agent and route messages
   accordingly.
7. Expose the self-hosted agent to Discord's gateway via an SSH tunnel / port forwarding,
   using a pairing code to complete the connection.

## Examples
The source video shows inviting the OpenClaw bot to a server, approving permissions, and the
bot landing in an allow-listed channel — one channel of a multi-agent Discord setup.

## Source
Extracted from: [Putting my AI agent inside Discord](https://www.youtube.com/watch?v=ulDkvWa1k34)
Channel: Renato Dinis | Build With AI
