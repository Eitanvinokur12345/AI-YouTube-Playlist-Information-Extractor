# AGENTIC OS — the study (owner request 2026-07-12)

Why this document: the "agentic OS / master database of AI info" is a core direction of
EXCAVATORTRON. This is the map of the field — the approach, who leads it, what to steal,
where EXCAVA already stands, and how future projects reuse ours.

## 1. What an "agentic OS" actually is
A normal OS manages programs that want CPU, memory, disk, and permissions.
An **agentic OS** manages AI agents that want **model calls, context, memory, tools, and
permissions**. The translation (from the AIOS paper, the field's reference architecture):

| Classic OS | Agentic OS |
|---|---|
| CPU | the LLM (a shared brain every agent borrows) |
| process | an agent |
| system call | a tool call (goes through the kernel, never direct) |
| RAM / virtual memory | the context window, paged in/out (Letta/MemGPT's insight) |
| disk | long-term memory (vectors, knowledge graphs, files) |
| scheduler | who runs next, with which engine, at what budget |
| permissions | which agent may touch which tool / act outward |

## 2. The leaders and their ONE key idea each
- **AIOS** (Rutgers, COLM 2025): a real kernel for agents — scheduler + context manager +
  memory manager + storage + tool manager + access manager, isolated from the agents
  themselves. Result: ~2.1× faster serving vs naive chaining. THE reference design.
- **Letta (MemGPT)**: treat context like virtual memory — actively page facts in and out
  instead of accumulating; agents that self-edit their own memory.
- **Zep / Graphiti**: memory as a TEMPORAL knowledge graph — facts know when they were true.
- **Mem0**: memory as a drop-in layer (the community default, 48k stars).
- **cortexOS (Goldbach — already in our project memory)**: "without the hand-off layer between
  agents you don't have an OS, you have a tab pile — the biggest mistake is skipping shared
  memory." This insight built EXCAVA's Phase 0.
- **Karpathy's LLM-OS sketch**: the LLM as kernel of a new computer; everything else is
  peripherals — the framing everyone builds toward.

## 3. Where EXCAVA already IS an agentic OS (honest mapping)
| Agentic-OS organ | EXCAVA today |
|---|---|
| kernel + scheduler | `src/excava.py` beat: routes tasks, budgets ticks, leases |
| processes (agents) | 13 departments, casts with roles, tier system |
| syscalls (tool calls) | Worker contract → REAL_TOOL registry, gated outward actions |
| shared memory | file bus + `history_index` + vector index + project memory |
| access manager | guardrails + autonomy tiers + owner pitch gate |
| health/telemetry | engine canary, supervisor, systemcheck, proof |
| package manager | the hub itself (6.8k elements) + packages/kits |

## 4. What the leaders have that EXCAVA lacks (the improvement list, free-first)
1. **Context paging (Letta's idea)** — agents get raw recent history; nothing pages the most
   RELEVANT older facts into a turn. We have the vector index; wire recall-per-turn.
2. **True kernel isolation (AIOS's idea)** — our agents' work functions call tools directly;
   a thin "syscall" layer would let the supervisor veto/track EVERY tool call uniformly.
3. **Temporal memory (Zep's idea)** — our facts don't know when they stopped being true
   (e.g. deepseek-r1:free going paid). Timestamped validity on hub elements.
4. **Multi-agent scheduling with budgets (AIOS)** — we round-robin rooms; a real scheduler
   would prioritize by goal-impact × engine-budget.
5. **Agents as installable apps** — the hub stores tools; the OS could INSTALL an agent from
   a hub element (the Activator already gestures at this).

## 5. How future tools/projects use it (the portable answer)
`PORTABLE_HARNESS.md` already defines the export: bus + agents + guardrails + project-memory
move as a unit to any repo with a `data/` folder (Budoaris, FreeDup, anything). That IS
"creating their own version": fork the harness, swap the department list and the WORK
handlers, keep the laws. The VPS (R1) adds the always-on runtime any port can share.

## 6. What makes an agent an AGENT (owner asked, 2026-07-12 — plain words)
An **engine** answers a question and forgets you existed. An **agent** is an engine given
five things, stacked:
1. **A job** — a goal it owns ("keep the hub's links alive"), not a one-off question.
2. **Memory** — it remembers what it tried, what worked, what it believes; yesterday shapes today.
3. **Tools** — it can DO things (run a scan, write a file, call an API), not just talk about them.
4. **Initiative** — it acts when it sees a reason, without being asked each time.
5. **Accountability** — its actions are traced, so trust can be earned or lost per agent.
Engines are interchangeable brains; agents are colleagues. EXCAVA today: jobs ✓, tools ✓
(department-level), traces ✓ (syscall log) — the gap is per-agent MEMORY, then a visible
TRACK RECORD, then INITIATIVE, then broader EXTERNAL ACTION (owner's build order, 2026-07-12).

## Sources
- AIOS paper: arxiv.org/abs/2403.16971 (COLM 2025) · openreview.net/forum?id=L4HHkCDz2x
- Letta / "LLMs as operating systems": letta.com/blog/deeplearning-ai-llms-as-operating-systems-agent-memory
- 2026 memory-OS landscape: agentmarketcap.ai (Letta/Zep/Mem0/LangMem), evermind.ai blogs
- Agent-native OS overview: medium.com/@marc.bara.iniesta (who is building the agent-native OS)
