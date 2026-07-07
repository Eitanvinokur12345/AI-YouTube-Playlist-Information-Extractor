# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-648` (dept) · 2026-07-07T23:32:27.093165+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Profile `prompt_generator.py` with `cProfile` on real-world inputs to identify top 3 bottlenecks, then auto-apply safe fixes.  
**Plan:**  
1. Sprocket will set up the `cProfile` analysis on the `generate_prompt` function using real-world input data.  
2. Run the profiling analysis 1000 times to gather comprehensive performance data.  
3. Evaluate the profiling report to identify the top 3 performance bottlenecks.  
4. Develop and test safe fixes for the identified bottlenecks.  
5. Integrate the optimized `generate_prompt` function into the codebase.  
6. Benchmark the performance improvements against the previous version.  
**What changed:** We agreed to use real-world inputs for profiling instead of relying solely on sample inputs.
