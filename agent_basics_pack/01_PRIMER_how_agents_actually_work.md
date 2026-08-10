# How agent systems actually work — a primer

Written for Eitan, 2026-08-09. This is my own explanation, not a mined document. Upload it
alongside the reading list so NotebookLM can check my claims against the primary sources —
if it finds me contradicting Anthropic or the LangGraph docs, believe them, not me.

---

## 1. The one distinction that explains everything

Almost every confusion about agents dissolves once you separate two things:

**A workflow** is a predefined path written by a human. Step 1 fetches, step 2 filters, step 3
formats. An LLM might do the work inside a step, but *a human decided the steps*. Workflows are
predictable, cheap, testable, and boring. Most production "AI agents" are workflows.

**An agent** decides its own steps. You give it a goal and tools; it chooses what to do next,
looks at the result, and chooses again, until it decides it is done. Agents are flexible,
expensive, non-deterministic, and hard to test.

The industry's most repeated piece of advice — from Anthropic's *Building Effective Agents*
onward — is: **use a workflow unless you genuinely need an agent.** Agency is a cost you pay
for open-ended tasks, not a feature you add for prestige.

The trap in between is the one worth naming: **a workflow wearing agent costumes.** Named
roles, personas, "departments," debate transcripts — but the actual behavior is a fixed code
path. It looks impressive and produces uniform output, because uniform output is what fixed
code paths produce.

## 2. The agent loop

Strip away every framework and an agent is this:

```
while not done:
    thought  = model(context)        # decide what to do
    action   = parse_tool_call(thought)
    result   = execute(action)       # actually do it
    context += (thought, result)     # remember what happened
```

That is ReAct — reason, act, observe — and it is genuinely all there is. Everything else is
engineering around this loop: what goes in `context`, what `execute` is allowed to touch, when
`done` becomes true.

Two consequences follow that people find counterintuitive:

- **If there is no `model()` call in the loop, it is not an agent.** It is a program. This
  sounds obvious and is the single most common way agent systems are faked — including in
  your own Creators department, where `draft()` is a string-formatting loop with no model in it.
- **If `execute` cannot change anything real, it is not acting.** An agent that only produces
  text describing what it would do is a very expensive author.

## 3. The four hard parts

Frameworks differ mostly in how they answer these.

**Tools.** How the model invokes real capability. MCP (Model Context Protocol) is now the
common standard: a server exposes tools, any MCP-speaking client can call them. This is why
MCP servers matter — each one is a capability an agent gains without custom integration code.

**Memory.** The context window is not memory; it is a desk. Real memory means deciding what to
write down, and what to retrieve later. Retrieval is the hard half: an agent that stores
everything and recalls the wrong thing is worse than one that stores little. NotebookLM is
itself an interesting answer here — hand the synthesis problem to a system built for it rather
than assembling a vector database.

**Control flow.** Who decides what happens next? Options, roughly in order of how much control
you keep: a fixed chain, a graph with conditional edges (LangGraph), a router that picks a
specialist, a manager agent that delegates (CrewAI), or free-for-all conversation (AutoGen).
More agent freedom means more capability and less predictability. Pick deliberately.

**Verification.** How you know the output is good. This is the part everyone skips, and it is
the part that decides whether the system is real. An agent that cannot tell good output from
bad will confidently produce bad output forever, and will report success while doing it.

## 4. Multi-agent systems — when they help and when they don't

The honest summary of the evidence: **multiple agents help when the subtasks are genuinely
separable and each needs different context.** Research-then-write is a good split. They hurt
when agents must agree on something, because agreement costs many rounds of expensive tokens
and often converges on whatever the loudest agent said first.

Your plan's instinct here is right and worth keeping: using *different model families* rather
than the same model with different prompts. Same model plus different persona produces
**correlated errors** — all the agents are wrong in the same direction and then agree with each
other, which reads as consensus and is actually an echo. Different lineages fail differently,
and disagreement is the signal you are paying for.

## 5. Self-improvement, honestly

The real mechanism has four parts, and skipping any one makes it theater:

1. **Measure** something concrete. A success rate over a repeatable task set.
2. **Find** the largest single failure cause. Not a list — the top one.
3. **Change** one thing to address it.
4. **Re-measure** and keep the change only if the number moved.

Without step 1 and step 4 you have a system that changes itself and calls it improvement.
Reflexion (in the reading list) is the research version: the agent critiques its own output
and retries. Note what makes it work — an *external* signal of failure. Self-critique with no
ground truth mostly produces confident revision.

## 6. What "good" looks like — a checklist you can hold me to

For any agent system, including this one:

- [ ] Does a model actually get called in the decision loop?
- [ ] Can the agent change something real, or does it only emit text?
- [ ] Is there a check that can *fail*, and has it ever actually failed?
- [ ] If two runs produce identical output, is that because the task was identical — or because
      nothing is generating?
- [ ] Can you point at the number that says it is working, and did that number move?

The fourth question is the one that catches the failure you spotted in the Prompts tab. Uniform
output is not a tuning problem. It is the signature of code where generation should be.
