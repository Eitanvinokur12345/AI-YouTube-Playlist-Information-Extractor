# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-928` (dept) · 2026-07-12T22:47:28.665552+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by transcript-summary (no engine)

**Decision:** DECISION: Enforce a risk-based prompt review at task initiation—auto-flag vague or missing success criteria/constraints *immediately* when a task is defined, forcing human review only for high-risk ca

**Plan (from the debate):**
1. Add a mandatory prompt review step at the start of every task. This forces us to verify the prompt’s clarity, scope, and constraints before execution, cutting wasted work from misaligned inputs. The t
2. Mandatory prompt review risks review fatigue where reviewers gloss over prompts after the 10th task, turning a safeguard into a checkbox. Instead, automate a lightweight pre-check that flags only high
3. Do this: Run a weekly automated scan of all prompts in our system, flagging any that lack clear success criteria or constraints. Flagged prompts go to a human for review before execution.

This cuts w
4. Gauge: A weekly scan misses urgent misalignments—vague prompts in fast-moving tasks slip through until the next scan, wasting work now. Instead, tie the pre-check to *task initiation*: auto-flag promp
5. DECISION: Enforce a risk-based prompt review at task initiation—auto-flag vague or missing success criteria/constraints *immediately* when a task is defined, forcing human review only for high-risk ca

**What changed:** first real room artifact.
