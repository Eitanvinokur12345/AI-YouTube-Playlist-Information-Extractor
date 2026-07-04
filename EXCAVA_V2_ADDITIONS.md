# EXCAVA v2 — ADDITIONS  (additions only; does NOT alter PLAN or STEPS)

_`EXCAVA_V2_PLAN.md` and `EXCAVA_V2_STEPS.md` remain byte-identical. Everything new or corrected
lives here and supersedes on conflict. Built 2026-07-04 from research + Eitan's tool asks. The
answer-dependent expansions (§E) are filled after Eitan's multiple-choice answers._

## A. Correction — Claude runs on Eitan's PRO, not a paid API
Eitan has Claude Pro; **no `ANTHROPIC_API_KEY` purchase.** Claude participates as a **session-time
premium agent** (Claude Code / coworking, like the session writing this) — free under Pro — doing
the highest-value work: final HORSE merges, design taste, accuracy fixes, hard problems. The
**autonomous CI cron uses only the free engines** (Gemini ×8 · Groq · Cerebras · OpenRouter-free);
it cannot call Claude (Pro is not an API). This supersedes any "Claude when there's budget" line in
the PLAN. → pending confirm: questions C1–C3.

## B. External tools researched (Eitan's ask: OpenClaw + Hermes) + bonus repos
| Tool | What it is | Verdict | Plugs into |
|---|---|---|---|
| **OpenClaw** (openclaw/openclaw) | self-hostable personal AI agent; talks on WhatsApp/Telegram/Discord/Slack/Signal/iMessage; browses/forms/shell/files; community skills; **SOUL.md personality configs**; multi-agent add-ons | ✅ **strong fit** — free, self-hostable (pairs with the optional Pi); delivers channels + external actions + personalities | M5 (channels/external), M2 (agent runtime + SOUL.md personas), M1 (browse/verify) |
| **Hermes 4** (Nous) | open reasoning + tool-use model | ⚠️ **paid on OpenRouter** (~$1/$3 per M) → **skip** under free-only | — |
| **OpenRouter free models** | DeepSeek R1 (reasoning) · Qwen3 Coder (tool-use/code) · Nemotron — free, no card, ~200/day | ✅ add as the reasoning/tool tier | M2.1 engine layer |
| gitagent (open-gitagent) | git-native agent: identity/rules/memory/tools/skills = version-controlled files | ✅ validates EXCAVA's design; borrow | M2 (confirms bus + PROJECT_MEMORY) |
| agency-agents (msitarzewski) | an "AI agency" — each agent a personality with processes + deliverables | ✅ borrow for personalities + creators | M2.3, M2.8, creators |
| agent-governance-toolkit (microsoft) | policy / sandbox / zero-trust (OWASP Agentic Top 10) | ✅ borrow for guardrails/security | PROTOCOLS.md, security dept |
| open-multi-agent / CrewAI | goal→parallel task DAG / role-based crews | ✅ borrow parallel-DAG + role patterns | M2 parallelism + routing |

**Recommendation:** adopt **OpenClaw** for the channel + external-action layer and as the source of
personality (SOUL.md) and multi-agent patterns; keep EXCAVA's own bus / memory / gate as the spine;
borrow patterns (not whole frameworks) from gitagent / agency-agents / governance-toolkit; use the
**free** OpenRouter models instead of paid Hermes. All pending Eitan's answer to R1–R3.

## C. Design tooling reality (Eitan's concern — correct)
One MCP is not enough, but the fix isn't more MCPs: ~80% of the M3 UI is **code** Fable writes
directly with design skills (frontend-design / impeccable / canvas-design). Asset tools are a small
stack — an **image generator** for the monsters, **optional Figma** for the design system, optional
Adobe/Canva; OpenClaw's Canvas may help. Whichever asset tools we use need **Eitan's authorization**
in claude.ai settings. Decided at M3 (question J3).

## D. "Hadishan" — UNIDENTIFIED, not added
No tool/repo named "Hadishan" was found. Per "make sure nothing else changes," nothing was added
for it. Awaiting Eitan's clarification (name/spelling/what it does), then it goes in as its own task.

## E. Answer-dependent expansions — filled after the multiple-choice round
Placeholders (each becomes a detailed, acceptance-tested block like STEPS): agent personalities ·
pace/parallelism/quality bars · creator-department detail · console spec · taste model · launcher
separation · tutorials (M1.9) · **external-actions milestone M5** · breadth expansions.
