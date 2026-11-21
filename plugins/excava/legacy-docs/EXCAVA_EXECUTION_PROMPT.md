# EXCAVA — FULL EXECUTION PROMPT (paste into a fresh session) — 2026-07-16

The comprehensive, detailed handoff. Read the canonical spec first, then execute on the loop.

## 0. READ FIRST, in order (these already exist — do NOT re-plan)
1. `EXCAVA_V2_PLAN.md` — vision, the 14 protocols, the design system (the "why").
2. `EXCAVA_V2_STEPS.md` — milestones M1→M5 + breadth, every task as Build + Done-when (the "do"; this is the detailed step list — follow it task by task).
3. `PROTOCOLS.md` — P1–P14 laws; self-audit against them every beat.
4. `EXCAVA_SEPTEMBER_PLAN.md` — current state, dated schedule, verified free tools, token system.
5. `EXCAVA_MASTER_AUDIT.md` — the 111-question checklist (Eitan's — see §7).
6. `EXCAVA_FUNDAMENTALS.md` — teach Eitan as you go.

## 1. IDENTITY
**EXCAVATORTRON = the HUB**: mined AI knowledge — 8,311 elements incl. **1,620 verified GitHub repos**
(vLLM, llama.cpp, LangChain, Flowise, OpenCode, Aider, Playwright MCP, GitHub MCP Server, Exa MCP…).
**EXCAVA = an AGENT ORCHESTRA** that GENERATES tools/projects by **orchestrating those mined OSS tools +
the free models**, and by integrating the hub's knowledge. Purpose: generate/assist Eitan's work.
**NOT for sale** — "sellable" is a *quality bar only*. Ultimate goal: every component integrates, nothing orphaned.

## 2. THE THREE METRICS + THE PLAN TO 80 (Eitan's target; his reframe applied)
Sales metric is **product-quality-vs-competitors ONLY** — assume everyone has access; ignore distribution,
staffing, logistics, go-to-market (hypothetical, so those are omitted).
- **Confidence 60 → 80.** Raised by: (a) **assemble the engine from proven OSS agent frameworks, do NOT
  build autonomy from scratch** (§4); (b) lock V2 scope, stop re-planning; (c) multi-engine + OmniRoute +
  self-host fallback kills free-tier-reliability risk; (d) assist-first on hard steps. These four move it to ~80.
- **Completeness 65 → 80.** Raised by: the loop keeps **draining the 111-question backlog past M4** (2–4
  extra weeks) + **enrichment-at-scale** makes the whole hub usable (not a hand-picked 50). 80 ≈ late Sept.
- **Sales (product-only) 50 → 80.** Raised by: (a) the OSS-orchestra + 8k-element hub is a **genuine
  differentiator** nobody else has; (b) full **M3 professional design**; (c) a proven **output quality bar**
  (item 107); (d) near-frontier free models (GLM-5.2). Under the no-distribution reframe, **80 is realistic.**
**Verdict: 80 on all three is realistic — the single highest-leverage addition is §4 (OSS repos as the
real running tools). Without it, confidence and sales stay ~55–60.**

## 3. THE BRAINS — 3–4 generalist brains for diverse, accurate results (Eitan's design 2026-07-16)
NOT one primary + specialists. Instead **3–4 GENERALIST brains** — each a capable model that can do ANY
task — chosen from **different model FAMILIES** (similar in strength, different in lineage, so they
genuinely disagree = real diversity, not an echo chamber). Each brain wields a **distinct toolset** (its
unique attribute). Brains deploy agents that **converse and converge** → more accurate + diverse output.
- **Brain A — GLM-5.2** (MIT, 1M ctx, intelligence leader) + code/repo tools.
- **Brain B — DeepSeek V4** (strong reasoning, cheap) + web-search/analysis tools.
- **Brain C — Qwen 3.6** (tool-calling + vision) + vision/design tools.
- **Brain D (optional) — Kimi K2.7 Code** (long-context, −30% tokens) + long-read/repo-ingest tools.
**GitHub repos are NOT brains** — they're the TOOLS each brain wields and the SERVERS that run the brains
(vLLM/Ollama self-host GLM-5.2/Qwen = zero quota). One `Router`/`Agent` class assigns each agent its
brain + tools, so the 3–4 brains sit behind ONE interface — never all 4 per task, only the agents in a
given room. Fallback pool: Groq · Cerebras · Gemini ×6 · Mistral · GH-Models. Claude Pro = rationed
premium for the hardest architecture only (P1). Image: Qwen-Image · Hunyuan · CogView · FLUX.1-schnell.

## 4. GITHUB OSS REPOS AS THE ACTUAL RUNNING TOOLS  ← the key addition (Eitan 2026-07-16)
Do NOT build the engine from scratch. **Assemble it from mined OSS** (this IS Ponytail: reuse-before-build):
- **Orchestration backbone:** **LangGraph** / **CrewAI** (mined) — the agent-orchestra runs ON these, not on
  hand-rolled room code. Flowise for a visual view.
- **Code execution (the doers):** **OpenCode** + **Aider** — agents dispatch real coding/build tasks to these,
  each pointed at a free model (GLM-5.2 / Kimi K2.7). This is how EXCAVA "generates tools" for real.
- **Model serving (free, unlimited):** **vLLM** / **llama.cpp** / **Ollama** — self-host GLM-5.2 / Qwen 3.6 on
  the host so there's zero quota; free-tier APIs are the overflow.
- **Tools the agents call:** **GitHub MCP Server** (repos), **Exa MCP** (search), **Playwright MCP** (browse),
  **Memory MCP**, **OpenClaw** (channels/shell).
- **The repo→running-tool pipeline** (per M1.2/M1.4, run inside a sandbox — P12): read README (Kimi K2.7) →
  detect run method (Docker/pip/npm/MCP) → **sandbox-run** → wrap as an element with `install` + an **Open**
  target + a **callable adapter** the orchestra invokes → now it's a live tool. `discovery_agent` (M1.C2)
  keeps pulling new repos hourly.
**Why this hits 80:** you're standing on battle-tested tools (thousands of contributors) instead of DIY —
higher quality, higher reliability, far less to build, and it's the honest meaning of "free + pro-grade."

## 5. TOKEN / EFFORT REDUCTION — "Ponytail"-style systems first (Eitan's clarification)
This is about *working-method efficiency* (reuse, minimal work), not only prompt compression:
1. **Ponytail (reuse-before-build)** — the top law: use a mined OSS tool/element before writing anything;
   minimal diffs; plan-first for big batches; fewest tokens. §4 IS Ponytail applied to the engine.
2. **Caveman** — agent prompts are terse, no filler (Eitan's reports stay full sentences).
3. **Right model** — token-frugal per task (Kimi K2.7 −30%; DeepSeek V4 Flash cheapest).
4. **Routing** — OmniRoute → cheapest capable engine (4-tier fallback, ~1.6B free tokens/mo).
5. **Caching** — cache repeated context/results; **Anthropic Compaction API** for Claude history.
6. **Selective compression** — LLMLingua/LongLLMLingua (4–10×) ONLY on retrieval/reading; **NEVER on
   agent-decision prompts** (it breaks agents — a hard rule).
7. **Deterministic-first** — code beats an LLM call wherever possible; every un-made call is savings.
8. **Budgets** — per-dept daily token leases + hard ceilings (M2.2).
Mine `github.com/pleasedodisturb/awesome-llm-token-optimization` + the playlist for more, via M1.C2.

## 6. THE MILESTONES (execute per EXCAVA_V2_STEPS.md — summarized)
- **M1 Real/usable hub:** deep_retrieve enrichment (stub-rate≈0) · unified element model · verify ALL types
  in sandbox · trust gate (dead-only pruning, keep niche) · per-card Activate/Open/Use row · <10s pre-warm ·
  detail view · delete the 21 dead modules · unify memory into one brain.
- **M2 Real agents:** PROTOCOLS self-audit · engine layer (§3, on LangGraph/CrewAI per §4) · lease/budget ·
  named agent roster (3–5/dept, personas) · conversation engine (multi-brain debate→converge) · rooms
  PRODUCE committed artifacts · wire into beat 24/7 · self-improvement dept real.
- **M3 Shell + design:** design system (Heavy-Machinery) · app shell (sidebar+topbar+search) · monster art
  (free image-gen) · isometric floor + animation catalog · messenger chat UI · cards/results/constellation/
  brain-graph · **direct EXCAVA console + floating ask** · steering/pitches · mobile.
- **M4 Activator + launcher:** portable SKILL.md [OPUS] · HORSE (10 executions→merge) · packages ·
  parent launcher (own brand) · hub-as-database · prove real (overnight artifact + goal→package).
- **M5 (deferred):** manage projects · post/monitor channels · build+deploy · make money · spin up projects.
- **Breadth:** 52 goals · omni-source tiers 2–3 · per-tab self-improvement · portability · EXCAVA-as-MCP.

## 7. THE 100 QUESTIONS (Eitan's — read the FULL text in EXCAVA_MASTER_AUDIT.md, Sections A–M, 111 items)
**Eitan authors/edits these; Claude proposes verdicts, Eitan decides.** Ask each as CLICKABLE
multiple-choice (4/batch): intro sentence + options KEEP/FIX/IMPROVE/WIRE/REBUILD/BACKLOG/REMOVE,
recommended verb first. Save to `data/excava/overhaul_decisions.json`. They are the keep/cut checklist
layered on M1–M4; every feature's verdict is honored before a milestone touches it. Do NOT impose a
generated set — this list is a DRAFT for Eitan to prune/rewrite/extend.

## 8. LOOP PROTOCOL (each iteration)
1. Standing checks: git pull (quarantine-never-delete), engine canary, regression.
2. Advance the CURRENT milestone by ONE increment that ends **WIRED + VISIBLE** (runs in the beat AND shows
   in the cockpit). Never start a second before the first is visible. Reuse an OSS tool before building (§5.1).
3. Verify the READ side in a browser (a number/screenshot) — never claim done from input alone.
4. Log WHY; ship ONLY via `python -m src.git_safe ship`.
5. Report with harsh 100% criticism of BOTH Claude and Eitan.
**Progress = "Eitan can do something new," never "a commit happened."**

## 9. LAWS (P1–P14 + standing)
Free-only forever (P1) · depth-before-breadth (P2) · task-relative value, prune only dead (P3) · real-not-
display (P4) · autonomy with 3 pitch-gates: new tool / overhaul / deeper PC-access (P5) · trigger words
NOSG/HORSE/PLAN/RESEARCH/WATCH (P6) · offline/online parity (P7) · elements & packages (P8) · provenance +
independent test (P9) · recall-before-change + log WHY (P10) · consistency check (P11) · security/sandbox
first (P12) · visible work (P13) · quality over quantity (P14). Everything operable IN THE APP. Ship only via
git_safe; quarantine-never-delete. Retired: "fulfill everything before anything new" → "one core, then expand."

## 10. TIME TO READY (honest, factoring ALL tools integrated)
- **The product (M1–M4), high standard:** ~7 weeks → **~Sep 5** (stretch-but-real, free engines 24/7).
- **All three metrics at 80** (backlog drained + full design + OSS-engine hardened): ~10–13 weeks →
  **late Sept to mid-October.**
- **M5 (acting on the world) + full 52-goal breadth:** beyond that — Oct+.
Anyone promising *literally everything at 80* in 7 weeks is lying; the honest line is product by early Sept,
80-across-the-board by mid-October.

## 11. FIRST MOVE
Management verdict → STEP-0 inventory (delete 21 dead modules; map wired/orphaned) → wire the OSS-engine
skeleton (§4: LangGraph + OpenCode + one free model, self-tested) → start M1.C1 (deep_retrieve) as ONE
wired+visible increment → verify in browser → ship → criticize both. Then loop, milestone by milestone.
