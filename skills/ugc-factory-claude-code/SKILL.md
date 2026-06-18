---
name: ugc-factory-claude-code
description: "Use to generate a complete UGC-style video advertisement from a product brief using Claude Code, Higgsfield Element, Seedance 2.0, and ffmpeg — no filming or human creators required."
---

# UGC Factory — AI UGC Ad Studio for Claude Code

## Overview
A Claude Code skill (installable via npm as `ugc-factory`) that converts a product description into a finished UGC video advertisement in ~15 minutes. The skill interviews the user, casts a consistent AI creator with Higgsfield Element, generates Seedance 2.0 video clips across 16 genre styles, and stitches them into the final ad with ffmpeg.

## Key Techniques
- **Five-phase pipeline**: interview → creator casting → genre routing → script generation → ffmpeg stitching
- **Stateless character generation**: each run creates a fresh creator, avoiding locked-avatar drift across brands
- **Full scene scripting**: every Seedance 2.0 clip receives a complete scene description, preventing hallucinated output
- **16 genre styles**: ecommerce, fashion, SaaS, food/beverage, real estate, cinematic, 3D CGI, anime, comic-to-video, motion-design, music video, social hook, brand story, fashion lookbook, product 360, and fight scene

## How to Apply
1. Install: `npx ugc-factory install` (deploys to `~/.claude/skills/ugc-factory/`)
2. Restart Claude Code.
3. Run `/ugc-factory` — the interview begins.
4. Answer: product name, offer, topic, creator specs (appearance/style), desired length, aspect ratio.
5. Pick a genre or accept the auto-routed one from the 16 templates.
6. Wait ~15 minutes; find your finished ad + source assets in a dated output folder.

## Examples
- Ecommerce skincare brand: `/ugc-factory` → "Glow Serum", "50% off launch deal", "results in 7 days" → cinematic female creator → ecommerce genre → finished 30-second ad.
- SaaS tool demo: interview with SaaS genre → hook, demo clips, CTA stitched into a 60-second ad.

## Source
Extracted from: [THIS 1 Skill Creates All My UGC Ads in Minutes](https://www.youtube.com/watch?v=NM-chy8yBsE)
Channel: Charlie Automates
Resource: https://www.charlieautomates.com/free-resources/#ugc-factory
GitHub: https://github.com/charlesdove977/UGC-Factory
