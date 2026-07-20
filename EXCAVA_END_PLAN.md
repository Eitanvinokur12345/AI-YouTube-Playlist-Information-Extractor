# EXCAVA — THE END PLAN (definitive execution prompt) — 2026-07-16

**Purpose:** the single, complete, self-contained plan to build EXCAVA to a high standard. A fresh
session should open with: *"Read EXCAVA_END_PLAN.md and execute."* It covers every feature (niche and
major) and every refinement decided through 2026-07-16.

## 0. READ ORDER (context lives in these — this file is the index + the refinements)
1. This file (END PLAN) — architecture, feature inventory, metrics, timeline, what to do.
2. `EXCAVA_V2_PLAN.md` + `EXCAVA_V2_STEPS.md` — the detailed M1→M5 task list (the "do").
3. `PROTOCOLS.md` — P1–P14 laws.
4. `EXCAVA_MASTER_AUDIT.md` — the 122-item / ~300-decision question bank (Eitan authors; §8).
5. `EXCAVA_FUNDAMENTALS.md` — teach Eitan as you go.

## 1. IDENTITY
**EXCAVATORTRON = the HUB**: ~8,300 mined AI elements incl. **1,620 real GitHub repos**. **EXCAVA = an
AGENT ORCHESTRA** that GENERATES tools/projects by orchestrating free OSS tools + free models + the hub.
Purpose: generate/assist Eitan's work. **NOT for sale** ("sellable" = quality bar only). Ultimate goal:
every component integrates, nothing orphaned.

## 2. ARCHITECTURE (all refinements folded in)
**The brains — 3–4 GENERALIST brains, distinct model FAMILIES** (similar strength, different lineage → real
diversity, not an echo chamber; NOT a blend). Each wields a distinct toolset. Brains deploy AGENTS that
converse + converge:
- Brain A **GLM-5.2** (MIT,1M ctx, leader) + code/repo tools · Brain B **DeepSeek V4** (reasoning,cheap) +
  search/analysis · Brain C **Qwen 3.6** (tool+vision) + vision/design · Brain D(opt) **Kimi K2.7 Code**
  (long-ctx,−30% tok) + long-read/ingest.
- **Diversity is stacked:** different-family models (deep) × agent role/persona guidelines (behavioral twist:
  doer/checker/improver + personas). Same-model-only-prompt-twist is banned (correlated errors).
**The class overhaul (M2)** — the 97 fragmented modules (21 dead) collapse into 5 clean classes on
LangGraph/CrewAI: `Router` (routes any task to any brain), `Agent` {name,role,engine,tools}, `Tool`
(wraps one OSS repo/MCP), `Room` (conversation), `Element`/`Package` (the hub). The 3–4 brains sit behind
the ONE Router — never all 4 per task, only the agents in a room.
**The engine is ASSEMBLED from mined OSS, not built (Ponytail):** LangGraph/CrewAI (orchestra) + OpenCode/
Aider (execution, each on a brain) + vLLM/Ollama (self-host GLM-5.2/Qwen = zero quota) + MCP servers
(GitHub/Exa/Playwright/Memory) + OpenClaw (channels/shell). Fallback pool: Groq·Cerebras·Gemini×6·Mistral·
GH-Models. Claude Pro = rationed premium (hard architecture only, P1).
**Repo→running-tool pipeline (sandbox, P12):** read README (Kimi) → detect run (Docker/pip/npm/MCP) →
sandbox-run → wrap as an Element with install + Open target + callable adapter → live tool. `discovery_agent`
pulls new repos hourly.
**Runtime:** GitHub Actions beat (24/7) + Eitan's PC/VPS host (for the orchestra; §13). Memory: unify the
3 fragmented graphs + history + requests into ONE queryable brain agents read at every decision.
**Image (monsters/design), free-first:** Qwen-Image · Hunyuan · CogView · FLUX.1-schnell via HF free /
Cloudflare Workers AI. Design tooling: Penpot/Figma + design MCP · Excalidraw · Lucide/Tabler icons.

## 3. TOKEN / EFFORT SYSTEM — Ponytail first
1 **Ponytail** (reuse a mined OSS tool/element before building; minimal diffs; plan-first; fewest tokens) ·
2 **Caveman** (terse agent prompts; Eitan's reports stay full sentences) · 3 right model (Kimi −30%,
DeepSeek V4 Flash) · 4 OmniRoute routing (4-tier, ~1.6B free tok/mo) · 5 caching + Anthropic Compaction API ·
6 LLMLingua compression ONLY on retrieval/reading, NEVER agent prompts · 7 deterministic-first · 8 per-dept
token budgets/leases.

## 4. SELF-IMPROVEMENT — first-class pillar (Eitan's #2 priority; audit Section N)
**Mechanism: measure success → find the #1 failure → fix it (prompt/brain/tool/code) → verify the number
moved.** Safe fixes auto-apply behind a regression test; overhaul/new-tool/deeper-access → pitch (P5). Scope:
agents/prompts/brains/routing/hub-content/own-code AND **UI/UX + cosmetic**. **Per-department** self-improve
+ a **meta-brain** (cross-dept learning). **Visible:** a success-rate number that climbs, per department, in
the app. Runs frequently (per Eitan: "much more frequently"). Tractable now *because* everything is on the
5-class layer (real surfaces to act on).

## 5. THE COMPLETE FEATURE INVENTORY (every feature — niche + major; full questions in MASTER_AUDIT)
**A Foundation:** 1 Oracle VPS · 2 Ollama · 3 diff-provider keys · 4 OmniRoute · 5 no-paid-Gemini · 6 in-app
write · 7 keys-without-PC. **B Identity:** 8 naming · 9 one-product · 10 agentic-OS study · 11 24/7 · 12
North-Stars→2-3. **C Hub:** 13 library · 14 6 element types usable · 15 activator · 16 OSS-usable-not-links ·
17 more sources · 18 multi-site · 19 auto-promote · 20 post-extract verify · 21 hub browser · 22 fill hub.
**D Agents/depts:** 23 self-improve→N · 24 Power · 25 Creators(assemble) · 26 Analysis · 27 Security · 28
Memory · 29 Mining · 30 News · 31 Transcripts · 32 Visual · 33 Watch · 34 Visualization · 35 Accessibility ·
36 Links(remove) · 37 multi-model debate · 38 agents EXECUTE · 39 hand-offs · 40 convos visible · 41 per-dept
history · 42 war-room/group tabs · 43 sentences-not-code · 44 same-length-fix · 45 open-dept-see-work.
**E Execution/checks:** 46 DO-actions · 47 self-improve-bigger→N · 48 supervisor · 49 systemcheck · 50 ≥10
guardrails · 51 firing test · 52 value>action-count · 53 missed-systems · 54 dept executors. **F Interaction:**
55 conversational-executes · 56 clickable Qs · 57 pitches · 58 pitch detail · 59 designs-no-approve · 60 ask-
at-stages · 61 harsh criticism · 62 token-law · 63 plan-first · 64 new-session prompt · 65 Telegram push · 66
teach-me. **G Visual:** 67 visual overhaul · 68 desktop-panels shell · 69 5 designs · 70 de-generic · 71
Arena-pick · 72 Obsidian/Graphify view · 73 readable · 74 intro/identity · 75 Fable 60%. **H Data brain:** 76
graph holds Q&A+history · 77 Obsidian fix · 78 star/combined skills · 79 link processors. **I Multi-project:**
80 parent launcher · 81 monetization. **J Process:** 82 tutorials · 83 transcripts+health · 84 pick-intervals ·
85 the-ledger · 86 retire-everything-first · 87 cadence · 88 recall+log-WHY · 89 git_safe+quarantine. **K
Forks:** 90 Phase-0 capability · 91 timeline · 92 "now-it's-real" test. **L Reality:** 93 social source(WIRE) ·
94 social graph · 95 workflows · 96 integrations · 97 visibility law · 98 delete-21-dead · 99 multi-brain. **M
Generation engine:** 100 intake · 101 decompose · 102 retrieve · 103 execute-adapter · 104 verify · 105
assemble · 106 sandbox · 107 output quality bar · 108 learning loop · 109 enrichment-at-scale · 110 failure-
handling · 111 recipes. **N Self-improvement:** 112 success-measure · 113 top-failure-finder · 114 fix-apply ·
115 auto-vs-pitch · 116 cadence · 117 scope(incl UI/UX) · 118 learning loop · 119 per-dept · 120 meta-brain ·
121 safety · 122 visible progress.

## 6. MILESTONES (execute per EXCAVA_V2_STEPS.md, task by task)
- **M1 usable hub:** deep_retrieve enrichment (stub≈0) · unified element model · sandbox-verify all types ·
  trust gate (dead-only prune, keep niche) · per-card Activate/Open/Use · <10s pre-warm · detail view · RELATE
  · delete 21 dead modules · unify memory to one brain.
- **M2 real agents:** PROTOCOLS self-audit · engine layer + 5 classes on LangGraph (§2) · leases/budgets ·
  named roster (3–5/dept, personas) · agents→workers · conversation engine (multi-brain debate→converge) ·
  rooms PRODUCE committed artifacts · beat 24/7 + live parity · **self-improvement dept real (§4)**.
- **M3 shell+design:** design system (Heavy-Machinery) · app shell (sidebar+topbar+search) · monster art ·
  isometric floor + animation catalog · messenger chat UI · element card/detail/results · North-Star
  constellation · brain graph · **direct EXCAVA console + floating ask** · steering/pitches · taste panel ·
  mobile.
- **M4 activator+launcher:** portable SKILL.md [OPUS] · HORSE (10→merge) · packages · parent launcher (own
  brand) · hub-as-database · prove real (overnight artifact + goal→package).
- **M5 (deferred):** manage projects · post/monitor channels · build+deploy · make money · spin up projects.
- **Breadth:** 52 goals · omni-source tiers 2–3 · per-tab self-improve + meta-brain · portability ·
  EXCAVA-as-MCP-server · cleanup.

## 7. QUESTIONS ARE EITAN'S (~300 decision-points)
The 122 items above = ~300 sub-decisions (see the coverage map). **Eitan authors/edits; Claude proposes
verdicts (KEEP/FIX/IMPROVE/WIRE/REBUILD/BACKLOG/REMOVE), Eitan decides.** Ask clickable, 4/batch; save to
`data/excava/overhaul_decisions.json`. Never impose a generated set — elicit. Verdicts are honored before a
milestone touches a feature.

## 8. METRICS + PLAN TO 80 (sales = product-quality only; ignore distribution/logistics)
- **Confidence 60→80:** OSS-assembled engine (not DIY) · lock V2 scope · multi-brain+fallback · assist-first.
- **Completeness 65→80:** loop drains the backlog past M4 · enrichment-at-scale.
- **Sales 50→80:** OSS-orchestra + 8k-hub differentiator · full M3 design · output quality bar · GLM-5.2-class
  brains · 3–4-brain diversity raises accuracy.
80 on all three is realistic; the highest-leverage lever is repos-as-running-tools (§2).

## 9. TIMELINE
Now→Jul29 M1 · Jul30→Aug5 M2 · Aug6→19 M3 · Aug20→26 M4 · Aug27→Sep5 polish. **Product ≈ Sep 5.** All three
metrics at 80 ≈ **mid-October.** M5 + full 52-goal breadth Oct+.

## 10. LOOP + LAWS
**Loop:** standing checks (git pull quarantine-never-delete, engine canary, regression) → advance the CURRENT
milestone by ONE increment ending WIRED+VISIBLE (reuse OSS before building) → verify READ side in a browser →
log WHY → ship ONLY via `python -m src.git_safe ship` → harsh 100% criticism of BOTH. Progress = "Eitan can do
something new," never "a commit happened." **Laws P1–P14:** free-only · depth-before-breadth · task-relative
value (prune only dead) · real-not-display · 3 pitch-gates · triggers NOSG/HORSE/PLAN/RESEARCH/WATCH · offline-
online parity · elements&packages · provenance+independent-test · recall+log-WHY · consistency check · security/
sandbox first · visible work · quality>quantity. All in-app; quarantine-never-delete.

## 11. FIRST MOVE
Management verdict → STEP-0 inventory (delete 21 dead; map wired/orphaned) → **prove the engine skeleton**
(LangGraph + OpenCode + GLM-5.2 execute ONE real task, self-tested — the make-or-break) → start M1.C1
(deep_retrieve) as ONE wired+visible increment → verify in browser → ship → criticize both. Then loop.

## 12. WHAT EITAN MUST DO (see chat message for the live checklist)
Start (M1): nothing. Within ~2 weeks (M2): choose the host (PC under §E guardrails, or the Oracle VPS).
Optional now: confirm engine secrets live (engine_selftest) + an OpenRouter key for the free Chinese models;
give final metric target figures. Nothing to buy (free-only).
