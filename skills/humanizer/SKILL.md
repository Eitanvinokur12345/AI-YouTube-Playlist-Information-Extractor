---
name: humanizer
description: "Use when AI-generated text (landing pages, proposals, posts, emails) needs to be rewritten so it no longer reads as AI-generated, by removing known LLM writing tells while preserving facts and meaning."
---

# Humanizer

## Overview
Humanizer is a portable, Markdown-based agent skill that rewrites AI-generated text to sound
natural and human. It is built from ~500 Wikipedia-tagged examples of AI-written articles,
distilled into 33 concrete "tells" (vocabulary choices, structural quirks, hedging patterns,
promotional language, "significance inflation," copula avoidance, and more).

## Key Techniques
- Run a two-pass rewrite: first an "obviously AI generated" audit against the 33-pattern
  checklist, then a rewrite pass that removes the flagged patterns.
- Apply a strict no-fabrication rule: never invent facts, names, dates, or citations while
  humanizing — only restyle, never re-report.
- Optionally calibrate to the user's own voice by seeding examples of their writing so the
  output matches their real style rather than a generic "human" register.

## How to Apply
1. Install via the Skills CLI (`npx skills add blader/humanizer --global`), as a Claude Code
   plugin (`/plugin marketplace add blader/humanizer`), or manually by copying `SKILL.md` into
   a skills directory.
2. Invoke it as a slash command, a direct request, or point it at a file to rewrite.
3. Run it on any AI-drafted copy before publishing — landing pages, proposals, posts, emails.
4. It is not about avoiding a single tell (e.g. the em dash) but about breaking the *stacking*
   of multiple tells in the same rhythm, which is what actually triggers AI detection.

## Examples
The source video frames this as reverse-engineering an AI-detection manual: Wikipedia
volunteers tagged 500+ AI-written articles and documented every tell over several years;
Humanizer runs that detection manual "backwards" to strip those same tells from new text
before it is posted.

## Source
Extracted from: [The FREE GitHub skill that deletes every AI tell.](https://www.youtube.com/watch?v=dUHpFuUIyi0)
Channel: Jack Roberts
Also referenced in: [5 Best Claude Skills Use for Free](https://www.youtube.com/watch?v=NrVSidALzb8)
