# Agent systems — the basics, a curated reading list

**Purpose:** upload these into a NotebookLM notebook so you can ask cross-source questions
like *"what do all of these agree an agent actually is?"* or *"where do they disagree about
memory?"* NotebookLM accepts URLs directly as sources — paste them in as website sources.

## ⚠️ Read this first — an honesty note

**I could not open a single one of these links.** This session has restricted network egress,
so every URL below comes from my training knowledge, not from checking. They were accurate as
of my knowledge cutoff (May 2026). Treat them as *pointers*, not verified facts:

- If a link 404s, the project almost certainly still exists — search the name.
- Documentation URLs move often. Repo URLs move rarely.
- I have marked confidence on each. **HIGH** = stable, long-lived, unlikely to have moved.

This matters because you asked whether I might be feeding you incorrect data. On this list,
the risk is dead links, not wrong ideas.

---

## Tier 1 — Start here. These four give you the whole mental model.

| Resource | Why it matters | Confidence |
|---|---|---|
| **Anthropic — Building Effective Agents**<br>`https://www.anthropic.com/engineering/building-effective-agents` | The single best starting point. Distinguishes *workflows* (predefined code paths) from *agents* (the model directs its own process), and argues most production systems should be workflows. Directly relevant: EXCAVA's departments are workflows pretending to be agents. | HIGH |
| **Anthropic — Model Context Protocol docs**<br>`https://modelcontextprotocol.io` | MCP is the standard for giving agents tools. Your hub already holds ~40 MCP servers. This explains what they actually are. | HIGH |
| **OpenAI — A Practical Guide to Building Agents** (PDF)<br>`https://openai.com/business/guides-and-resources/` | A different house's take on the same problem. Useful precisely because it disagrees with Anthropic in places — good NotebookLM cross-source material. | MEDIUM |
| **12-Factor Agents** — Dex Horthy / HumanLayer<br>`https://github.com/humanlayer/12-factor-agents` | Twelve concrete engineering principles for agents that survive production. The most practical thing on this list. Factor 1 ("natural language to tool calls") and Factor 8 ("own your control flow") are exactly where EXCAVA is weak. | HIGH |

## Tier 2 — The frameworks the END PLAN names but the hub never mined

| Resource | Why it matters | Confidence |
|---|---|---|
| **LangGraph**<br>`https://github.com/langchain-ai/langgraph` | Graph-based orchestration: nodes, edges, explicit state. The END PLAN picks this as the orchestra layer. Read the concepts docs, not the API reference. | HIGH |
| **CrewAI**<br>`https://github.com/crewAIInc/crewAI` | Role/goal/backstory agents that delegate to each other. The "departments with personas" idea in your plan is essentially CrewAI's model. | HIGH |
| **Aider**<br>`https://github.com/Aider-AI/aider` | An AI pair programmer that actually edits repos and commits. The best-documented example of an agent that *does* things rather than describing them. | HIGH |
| **OpenHands** (formerly OpenDevin)<br>`https://github.com/All-Hands-AI/OpenHands` | A full agent platform with sandboxed execution. Closest existing thing to what EXCAVA wants to be. | HIGH |
| **Microsoft AutoGen**<br>`https://github.com/microsoft/autogen` | Multi-agent conversation framework. The "rooms where agents debate and converge" design in your plan is AutoGen's core pattern. | HIGH |
| **smolagents** — Hugging Face<br>`https://github.com/huggingface/smolagents` | Deliberately tiny (~1k lines). Read this one *end to end* — it is the fastest way to understand what an agent loop really is, with nothing hidden. **If you only read one repo, read this.** | HIGH |

## Tier 3 — The ideas underneath (papers)

| Resource | Why it matters | Confidence |
|---|---|---|
| **ReAct: Synergizing Reasoning and Acting**<br>`https://arxiv.org/abs/2210.03629` | The think→act→observe loop nearly every agent uses. Short and readable. | HIGH |
| **Reflexion**<br>`https://arxiv.org/abs/2303.11366` | Agents that critique their own output and retry. This is the honest version of "self-improvement" — your #2 priority. | HIGH |
| **Toolformer**<br>`https://arxiv.org/abs/2302.04761` | How models learn to call tools at all. | HIGH |
| **Generative Agents (Stanford "Smallville")**<br>`https://arxiv.org/abs/2304.03442` | 25 agents with memory, reflection, and planning in a simulated town. The origin of most "agent memory" design. | HIGH |

## Tier 4 — Self-hosting free models (relevant to your zero-cost constraint)

| Resource | Why it matters | Confidence |
|---|---|---|
| **Ollama** `https://github.com/ollama/ollama` | Run models locally. You already use this on EITAN-PC. | HIGH |
| **vLLM** `https://github.com/vllm-project/vllm` | Fast self-hosted serving; what you would use on a VPS. | HIGH |

---

## How to use this in NotebookLM

1. Create one notebook, call it **"Agent Basics"**.
2. Add Tier 1 as website sources first. Ask it: *"What is the difference between a workflow and an agent, and which one should I build?"*
3. Add Tier 2. Ask: *"How do LangGraph, CrewAI, and AutoGen each handle agents talking to each other? Where do they disagree?"*
4. Add Tier 3 last. Ask: *"What does Reflexion say about self-improvement that the frameworks don't implement?"*

That third question is the one I most want your answer to, because self-improvement is your
stated #2 priority and EXCAVA currently implements none of it.
