---
name: video-to-agent-skill-apify
description: "Use when watching an AI tutorial — automatically converts any video or social post URL into a structured, actionable skill file for your AI agent via Apify scraping."
---

# Video-to-Agent-Skill Pipeline via Apify

## Overview
Instead of manually noting what videos teach, this skill sends an agent the URL of any video or social post. Apify scrapes the full transcript, comments, and description; the agent enriches it with web research; and the output is a concrete, applicable skill file ready to load into your AI agent.

## Key Techniques
- **Multi-platform scraping**: Works on YouTube, LinkedIn posts, X threads — one Apify API key handles all
- **Comments mining**: Captures corrections, missing links, and resource names from comments alongside the main content
- **Web research enrichment**: Agent searches for latest docs/repos mentioned in the video to fill gaps
- **Skill distillation**: Converts raw content into a sequenced set of actionable steps

## How to Apply
1. Get an Apify API key (apify.com)
2. Create a Claude Code skill that:
   - Takes a URL as input
   - Calls Apify's YouTube/web scraper actor with the URL
   - Receives transcript + comments + description as output
   - Runs a web research step for any repos/tools mentioned
   - Passes all content to Claude with prompt: "Convert this into a step-by-step skill file I can apply to my AI setup"
3. Invoke the skill by sending a video URL: "Skill this for me: https://youtu.be/..."
4. Review and save the output skill file

## Examples
- Watch an MCP tutorial → skill extracts the install commands, config JSON, and use cases → loads as a ready-to-use connector guide
- Watch a prompt engineering video → skill extracts the specific prompt patterns → saves as reusable templates
- Watch a competitor product demo → skill extracts the key capabilities → loads as a competitive intelligence document

## Source
Extracted from: [I built a skill that turns any video into an agent skill](https://www.youtube.com/watch?v=n6HEw2kEdBE)
Channel: James Goldbach
