---
name: skill-creation-optimization
description: "Developing and refining custom AI capabilities within Claude Code, ensuring measurable improvements and optimal performance."
---

# Skill Creation & Optimization

## Overview
The ability to create new AI skills, modify and improve existing ones, run evaluations, benchmark performance, and conduct A/B tests on different skill versions to optimize their effectiveness and triggering.

**Use case:** Developing and refining custom AI capabilities within Claude Code, ensuring measurable improvements and optimal performance.

## Key steps
1. Decide what you want the skill to do and roughly how it should work.
2. Write a draft of the skill.
3. Create a few test prompts and run claude-with-access-to-the-skill.
4. Help the user evaluate the results both qualitatively and quantitatively.
5. While the runs happen in the background, draft some quantitative metrics or modify if you feel something needs to change about the ones that already exist.
6. Use the eval-viewer/generate_review.py script to show the quantitative metrics.
7. Rewrite the skill based on feedback from the user's evaluation and from the quantitative benchmarks.
8. Repeat until you're satisfied.
9. Expand the test set and try again at larger scale.
10. Optimize the triggering of the skill using the eval-viewer/generate_review.py script.

## Details
- **Category:** agents
- **Tool:** claude  ·  **Quality:** 5/10

## Source
Extracted from: https://www.youtube.com/watch?v=FBwTIUKxUTI
