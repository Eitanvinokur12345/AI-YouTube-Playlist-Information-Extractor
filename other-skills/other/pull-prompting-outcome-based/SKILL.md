---
name: pull-prompting-outcome-based
description: "Use when you know the outcome you want but not the exact steps — have AI question you to extract what it needs and drive toward the solution."
---

# Pull Prompting (Outcome-Based Prompting)

## Overview
Instead of writing out every step for AI to follow (push prompting), you state the desired outcome and ask AI to ask you questions — letting the model extract the details it needs and drive toward the solution. This mirrors spec-driven development used by professional coders.

## Key Techniques
- Give AI the role and context, then state your outcome goal, then say "Ask me all the questions you need to create this for me"
- Answer AI's clarifying questions using voice-to-text for speed
- Iterate: after receiving a draft, ask "Ask me more questions to refine this further"

## How to Apply
1. Set role + context as you normally would
2. State the desired outcome: "I need a cold email sequence that converts leads into booked calls"
3. Add: "Ask me all the questions you need to create this, then give it back to me as [format]"
4. Answer each question (use voice-to-text for efficiency)
5. Review output; if needed: "Ask me more questions to make this more relevant"

## Examples
- "You're a conversion copywriter. I need a 5-email nurture sequence for SaaS prospects. Ask me all the questions you need, then write it as a numbered outline."
- "You're a product manager. I need a PRD for a mobile payment feature. Ask me everything you need, then output it as a structured document."

## Source
Extracted from: [You're not behind (yet): How to learn AI in 18 minutes](https://www.youtube.com/watch?v=0Tch0N5nsRU)
Channel: Dan Martell
