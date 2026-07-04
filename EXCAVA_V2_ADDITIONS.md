# EXCAVA v2 — ADDITIONS  (additions only; does NOT alter PLAN or STEPS)

_`EXCAVA_V2_PLAN.md` and `EXCAVA_V2_STEPS.md` remain byte-identical. Everything new or corrected
lives here and supersedes on conflict. Built 2026-07-04 from research + Eitan's tool asks. The
answer-dependent expansions (§E) are filled after Eitan's multiple-choice answers._

## TOP PRIORITY (Eitan 2026-07-04): CORE FIRST, breadth later — see §F.

## A. Correction — Claude runs on Eitan's PRO, not a paid API
Eitan has Claude Pro; **no `ANTHROPIC_API_KEY` purchase.** Claude participates as a **session-time
premium agent** (Claude Code / coworking, like the session writing this) — free under Pro — doing
the highest-value work: final HORSE merges, design taste, accuracy fixes, hard problems. The
**autonomous CI cron uses only the free engines** (Gemini ×8 · Groq · Cerebras · OpenRouter-free ·
self-hosted Hermes); it cannot call Claude (Pro is not an API). Supersedes any "Claude when there's
budget" line. → pending confirm: questions C1–C3.

## B. External tools researched (Eitan's ask: OpenClaw + Hermes) + bonus repos
| Tool | What it is | Verdict | Plugs into |
|---|---|---|---|
| **OpenClaw** (openclaw/openclaw) | self-hostable personal AI agent; talks on WhatsApp/Telegram/Discord/Slack/Signal/iMessage; browses/forms/shell/files; community skills; **SOUL.md personality configs**; multi-agent add-ons | ✅ **strong fit** — free, self-hostable (pairs with the optional Pi); channels + external actions + personalities | M5 (channels/external), M2 (agent runtime + SOUL.md personas), M1 (browse/verify) |
| **Hermes 4** (Nous) — *this is Eitan's "Hadishan"* | **open-weights** reasoning + tool-use model (405B / 70B); JSON + function calling | ✅ **add via the FREE path** — self-host (Ollama on the Pi / a capable machine when on) or a free host; the **paid** OpenRouter Hermes endpoint stays OFF. 70B / distilled = realistic free local size | M2.1 engine layer (free/local tier) + Nous **hermes-agent** framework as a borrow-pattern |
| **OpenRouter free models** | DeepSeek R1 (reasoning) · Qwen3 Coder (tool-use/code) · Nemotron — free, no card, ~200/day | ✅ add as the reasoning/tool tier | M2.1 engine layer |
| gitagent (open-gitagent) | git-native agent: identity/rules/memory/tools = version-controlled files | ✅ validates EXCAVA's design; borrow | M2 (confirms bus + PROJECT_MEMORY) |
| agency-agents (msitarzewski) | an "AI agency" — each agent a personality with processes + deliverables | ✅ borrow for personalities + creators | M2.3, M2.8, creators |
| agent-governance-toolkit (microsoft) | policy / sandbox / zero-trust (OWASP Agentic Top 10) | ✅ borrow for guardrails/security | PROTOCOLS.md, security dept |
| open-multi-agent / CrewAI | goal→parallel task DAG / role-based crews | ✅ borrow parallel-DAG + role patterns | M2 parallelism + routing |

**Recommendation:** adopt **OpenClaw** for the channel + external-action layer and as a source of
personality (SOUL.md) + multi-agent patterns; keep EXCAVA's own bus / memory / gate as the spine;
borrow patterns from gitagent / agency-agents / governance-toolkit; engines = the free tier
(Gemini/Groq/Cerebras/OpenRouter-free) **plus self-hosted (free) Hermes** where a capable machine/Pi
is available — never the paid Hermes endpoint. Pending Eitan's answers to R1–R3.

## C. Design tooling reality (Eitan's concern — correct)
One MCP is not enough, but the fix isn't more MCPs: ~80% of the M3 UI is **code** Fable writes
directly with design skills (frontend-design / impeccable / canvas-design). Asset tools are a small
stack — an **image generator** for the monsters, **optional Figma** for the design system, optional
Adobe/Canva; OpenClaw's Canvas may help. Whichever asset tools we use need **Eitan's authorization**
in claude.ai settings. Decided at M3 (question J3).

## D. "Hadishan" = HERMES (resolved 2026-07-04)
Eitan confirmed "Hadishan" was Hermes. Added per §B on the **free path only** — open-weights Hermes,
self-hosted (Ollama on the optional Pi / a capable machine when on) or a free host, as a reasoning +
tool engine in the M2.1 layer; the **paid** OpenRouter Hermes endpoint stays off (free-only). Nous's
open **hermes-agent** framework is a borrow-pattern for tool-use loops.

## E. Answer-dependent expansions — filled after the multiple-choice rounds
Placeholders (each becomes a detailed, acceptance-tested block like STEPS): agent personalities ·
pace/parallelism/quality bars · creator-department detail · console spec · taste model · launcher
separation · tutorials (M1.9) · external-actions milestone M5 (**DEFERRED — see §F**) · breadth
expansions · **CORE-ACCURACY spec (§F, TOP priority)**.

## F. CORE CAPABILITY = SPOT-ON  (NEW TOP PRIORITY — Eitan 2026-07-04)
Directive: for now **do NOT add more external breadth** (M5 external-actions is DEFERRED). Instead
make **what EXCAVA already does the most powerful and accurate it can be** — this outranks the breadth
milestones and folds into M1 as its quality spine, running continuously. Three pillars (to be
specified by the 10-question round, then written here as acceptance-tested steps):
- **Retrieval depth** — every element carries *enough* real information (full transcript / repo README
  + docs / multi-source enrichment), never a thin stub.
- **Freshness & discovery** — EXCAVA catches brand-new tools and suddenly-appearing GitHub repos *as
  they emerge* via continuous multi-site scanning (GitHub trending/new, Product Hunt, HN, Reddit, X,
  awesome-lists, official release feeds), not weeks later.
- **Accuracy** — every fact / link / install is verified, cross-checked across sources, and
  re-verified on a rolling cadence so nothing is stale or wrong. Applies to **every** ability — named
  or not (retrieval, links, designs, activator/know→do, creators…).
This is the reserved-for-Opus "retrieval accuracy" track made first-class + the memory-roadmap
"source-hunting protocol", elevated to priority #1.
