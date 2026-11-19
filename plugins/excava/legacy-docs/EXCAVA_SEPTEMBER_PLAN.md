# EXCAVA — the September plan (integration + dated schedule) — 2026-07-16

**This does NOT replace anything. It integrates.** The master spec is `EXCAVA_V2_PLAN.md` (why) +
`EXCAVA_V2_STEPS.md` (M1–M5 "do") + `PROTOCOLS.md` (P1–P14). This file adds three things V2 predates:
(1) where we ACTUALLY are today, (2) a dated schedule to early September, (3) the specific free
Chinese models / design tools / repos to use. My recent docs (`EXCAVA_FUNDAMENTALS.md` = teaching;
`EXCAVA_MASTER_AUDIT.md` = the question checklist) fold in as noted; the rest is superseded by V2.

## 0. Who owns the questions (correction, 2026-07-16)
**Eitan authors the questions; Claude organizes, answers, and executes them.** The 111-item list in
`EXCAVA_MASTER_AUDIT.md` is a **DRAFT for Eitan to prune/rewrite/extend — not an imposed set.** This is
now a standing rule so no fresh session re-defaults to generating its own. (Root cause of the repeated
mistake: a Claude behavioral default to *generate* rather than *elicit* — fixed only by writing it here.)

## 1. Where we ACTUALLY are in V2 (measured 2026-07-16 — the honest starting line)
- **M1 (real/usable hub): ~15% done.** 8,311 elements but only 0.8% have run/install info, 25% stubs,
  "100% verified" is a facade. `deep_retrieve`/`discovery_agent` exist partly but under-run.
- **M2 (real agents conversing): ~10%.** Rooms exist (619) but ~0 turns; engine layer partial; agents
  don't truly execute. `mine_social` etc. built but ORPHANED.
- **M3 (shell + launcher + design): ~5%.** Old static cockpit only.
- **M4 (activator end-to-end): ~10%.** Activator skill exists; not proven end-to-end.
- **Code health:** 97 modules, ~30 wired, **21 dead** (delete them — zero references).
- **Memory:** fragmented across 3 graph files + memory_index; unify it (V2 §3.5 / M2.8 depends on it).

## 2. Dated schedule → early September (aggressive but real; free-engine 24/7 + Pro for hard parts)
> Honest scope note: **M1–M4 (the whole PRODUCT) to a high standard by ~Sept 5 is a realistic stretch.**
> **M5 (acting on the world) + full 52-goal breadth do NOT fit by early Sept** — they spill to Sept–Oct.
> "Everything to a high standard by early September" = the product, not the external-reach + full breadth.

- **Week 1 (Jul 16–22): M1.C1–C3 + M1.0–1.3.** deep_retrieve enrichment; unified element model; verify
  all types (sandbox); trust gate. Delete the 21 dead modules. Unify memory into one brain. *(+ M2.0
  PROTOCOLS.md self-audit; M2.1 engine layer wired — see §3.)*
- **Week 2 (Jul 23–29): M1.4–1.9 + M2.2–2.4.** Per-card action row (Activate/Open/Use); <10s pre-warm;
  detail view; ship M1. Lease/budget arbiter; named agent roster; agents→workers.
- **Week 3 (Jul 30–Aug 5): M2.5–2.9.** Conversation engine (real multi-brain debate→converge);
  rooms produce committed artifacts; wire into beat 24/7; self-improvement dept real; ship M2.
- **Week 4 (Aug 6–12): M3.0–3.5.** Design system (Heavy-Machinery); app shell; monster art (free
  image-gen); isometric floor; animation catalog; messenger chat UI.
- **Week 5 (Aug 13–19): M3.6–3.13.** Cards/results/constellation/brain-graph; direct EXCAVA console +
  floating ask; steering/pitches; mobile; ship M3.
- **Week 6 (Aug 20–26): M4.1–4.6.** Portable activator [OPUS]; HORSE; packages; parent launcher;
  hub-as-database; ship M4 — prove "real" (overnight artifact + goal→package).
- **Week 7 (Aug 27–Sep 5): high-standard polish + buffer.** Fix anything below bar; M5.1 (manage
  projects, low-risk only); the change-tutorials/videos per milestone. **Ship the product.**

## 3. SPECIFIC free tools — VERIFIED CURRENT (web-checked 2026-07-16; earlier versions were stale)
**Agent brains (free/open-weight; via OpenRouter free tier · provider free tiers · self-host · OmniRoute):**
- **GLM-5.2** (Zhipu, MIT, 1M ctx) — **the open-weight intelligence leader; default for serious coding/agent work.**
- **DeepSeek V4** (Pro + **Flash** = cheapest at $0.14/$0.28 per 1M) — reasoning + cheap bulk.
- **Kimi K2.7 Code** (Moonshot) — coding-specialized, **~30% fewer thinking tokens** (token-frugal).
- **Qwen 3.6** (Alibaba, compact MoE, runs on 1 GPU) — tool-calling + vision.
- Kept alongside already-wired Groq · Cerebras · Gemini ×6 · NVIDIA · SambaNova · Mistral · GH-Models.
  **Claude Pro = rationed premium lane** (hard architecture only), never the foundation (P1).
- **Routing** `pick_engine(dept,difficulty)`: GLM-5.2 for hard coding/agents, Kimi K2.7 for long reads +
  code, DeepSeek V4 Flash for cheap bulk, Qwen 3.6 for tool/vision, Groq/Cerebras for fast small — via
  **OmniRoute** for compression + widest free reach; direct call if OmniRoute is off.
**Free image-gen for monsters/design (test free FIRST, P1):** Qwen-Image, Hunyuan (Tencent), CogView
(Zhipu), FLUX.1-schnell — via **Hugging Face free inference** / **Cloudflare Workers AI**.
**Free design tooling (OSS):** Penpot (OSS Figma) / Figma free + design MCP; Excalidraw; Lucide/Tabler icons.

## 3a. GITHUB-REPO INTEGRATION (make it front-and-center — 1,620 real repos are already mined)
The playlist holds **1,620 verified GitHub repos** incl. vLLM, llama.cpp, LangChain, Flowise, Playwright
MCP, GitHub MCP Server, Exa MCP, OpenAI Codex. **Turning a mined repo into a usable tool** (the pipeline,
per M1.2/M1.4): (1) read README + docs (Kimi K2.7) → (2) detect run method (Docker / pip / npm / MCP) →
(3) **sandbox-run** it (P12 / M1.2 runner, isolated) → (4) wrap as an element with `install` + an **Open**
target (github.dev / Codespaces / hosted MCP) + a callable adapter → (5) the orchestra can now invoke it.
`discovery_agent` (M1.C2) keeps pulling new repos from the playlist + GitHub trending hourly.

## 3b. TOKEN-REDUCTION SYSTEM (for everything — verified 2026 methods)
A first-class system, six layers (P: Caveman/token-law is layer 5):
1. **Right model** — token-frugal by task (Kimi K2.7 −30% thinking; DeepSeek V4 Flash cheapest).
2. **Routing** — OmniRoute sends each call to the cheapest *capable* engine (4-tier fallback).
3. **Caching** — cache repeated context/results (biggest deterministic win) + **Anthropic Compaction API**
   for Claude conversation history.
4. **Selective compression** — **LLMLingua/LongLLMLingua** (4–10×) ONLY on retrieval/reading/RAG. **NOT on
   agent-decision prompts** (it breaks agents — 11/11 fail) — a hard rule.
5. **Deterministic-first** — do with code what needs no model (Caveman law); every un-made call is savings.
6. **Budgets** — per-dept daily token leases + hard ceilings (V2 M2.2); a dept at budget is held+traced.
Ref: `github.com/pleasedodisturb/awesome-llm-token-optimization` (mine it via M1.C2).

## 4. The questions (yours) — where they attach
`EXCAVA_MASTER_AUDIT.md` (111 items) becomes the **keep/cut/wire checklist layered on M1–M4**: before
each milestone touches a feature, its audit verdict (KEEP/FIX/WIRE/REBUILD/BACKLOG/REMOVE) is honored.
**Eitan edits this list; it is his.** Claude proposes verdicts, Eitan decides.

## 5. What Claude needs from Eitan
- **The final target figures** for the two metrics (completeness %, quality/marketability 1–100) — sets the bar.
- **Go/no-go** on this schedule, and whether to enable the free-engine 24/7 run (PC/host, §E guardrails
  in `EXCAVA_MASTER_PROMPT.md`) so Week-1 can run continuously instead of Pro-throttled.
- Nothing else blocks starting Week 1.
