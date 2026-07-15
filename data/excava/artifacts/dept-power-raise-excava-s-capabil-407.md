# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-407` (dept) · 2026-07-15T15:10:06.320786+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run parallel tests integrating Llama 4 70B with Claude Opus 4.8 and Claude Mythos 5 on EXCAVA's worst-case 10K-token prompts.

**Plan:**  
1. Set up controlled A/B testing with Llama 4 70B alone and Llama 4 70B plus Mythos 5, measuring output on a 10K-token prompt.  
2. Simultaneously, create a second test integrating Llama 4 70B with Claude Opus 4.8 for performance comparison.  
3. Allocate the same compute budget for both tests to ensure fairness in measurement.  
4. Collect and analyze end-to-end quality deltas from each test within one week.  
5. Prepare a report summarizing the data-driven comparison of output quality and compute costs for both models.  
6. Present findings to the team to guide the decision on future model integration.

**What changed:** The decision was made to test both advanced and lighter models concurrently for a comprehensive evaluation.
