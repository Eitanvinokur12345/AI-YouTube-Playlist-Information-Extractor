# EXCAVA — the plan and milestones

_Assembled from the EXCAVA repo for NotebookLM upload._



---

# ===== FILE: EXCAVA_END_PLAN.md =====

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



---

# ===== FILE: EXCAVA_V2_PLAN.md =====

# EXCAVA v2 — the "MAKE IT REAL" master plan

_Built by Opus 4.8 from a 76-question direction interview with Eitan (2026-07-03/04), to be
executed by Fable. Combines with `EXCAVA_PROGRAM.md` (phases 0–9, still valid) — this document
supersedes it wherever they conflict, because it encodes Eitan's corrected direction._

> **Eitan's verdict that triggered this:** "This whole project for now is a display without
> content." Agents/departments do nothing (they were brainless Python file-readers with no
> engine), no SKILL.md/activator works, nothing is openable/runnable from inside the project,
> the 52 goals are unfinished, and self-improvement never worked. **v2 makes it real.**

---

## 1. VISION (one paragraph)
Excavatortron is a real, living workshop: named **monster agents** (Monsters-Inc-style), each
powered by real free LLM engines, work in visible **conversations** (department threads,
cross-department hand-offs, an open group room, per-task war rooms) to build and maintain a
hub of **elements** (skills, tools, connectors, news, designs, formats, prompts, commands, MCP
servers, repos) and combine them into **packages** for any task — all free, 24/7, offline or
online, watchable like a boss watching employees. You **access** everything for real (activate
into your tool, open ready-to-run in <10s, use for a task), talk to **EXCAVA directly** inside
the app, and steer with a lightweight approval flow. A clean **parent launcher** sits above it
as the control center for all your projects, with Excavatortron's hub as their shared database.

---

## 2. PROTOCOLS — Eitan's approach, codified as law  → build `PROTOCOLS.md` (every agent reads it; EXCAVA self-audits against it every beat)
- **P1 Free-only forever.** A free tier that needs a card = paid = skip. Design tooling included: test free tools first; add a specific/paid tool only if the design genuinely can't be excellent without it.
- **P2 Depth before breadth.** Make a small set genuinely real before adding scope.
- **P3 Task-relative value (hard rule).** No global "best/better." Never bury or prune an element for being low-rated — a "1" may be perfect for one niche task; that is *why* holding so many elements is worthwhile. Prune ONLY dead/fake elements. Comparison and effectiveness scoring are always per-task.
- **P4 Real, not display.** Every feature must actually do / open / run. Visualisation that does nothing useful is a bug.
- **P5 Autonomy with three pitch-gates.** Agents may autonomously build and change almost anything (features, outlines/formats, prompts, commands, designs, packages). **Only three things need Eitan's OK, each delivered as a PITCH conversation:** (1) building a brand-new **tool**, (2) any **overhaul** (a better working method / full redesign / a change to how agents work), (3) **deeper access to Eitan's computer**.
- **P6 Trigger words.** Default of activation = find or build the right **package** and act. `NOSG` = skip options, do the single best thing, one-line report. `HORSE` = 10 agents each *fully execute* the goal, then merge the best of the *results* (not the plans), tuned to Eitan's taste. `PLAN` = show the plan first instead of acting; **absent PLAN = act silently in the background**. `RESEARCH` = deep multi-source brief. `WATCH` = ongoing tracking of a topic/source.
- **P7 Offline/online parity.** Every EXCAVA action runs at the same speed and quality whether Eitan is present or not; agents converse identically in his absence; all chats archived and scrollable by day.
- **P8 Elements & packages.** "**Elements**" = every information item in the hub. "**Packages**" = bundles of elements for a task. Every element ALSO stands alone with direct access — never hidden inside packages only.
- **P9 Provenance + independent test.** Anything created enters the project labeled **"Created by EXCAVA"**; an **independent test re-runs before its first use**. Publishing beyond the project stays behind the outward gate.
- **P10 Recall before change; log the WHY.** Every tool (incl. EXCAVA's agents) recalls from the project memory master before changing anything and logs a one-line WHY after (`PROJECT_MEMORY.md`).
- **P11 Consistency check every task** against the goals + these protocols; flag + fix drift.
- **P12 Security first.** Untrusted content is gated (`security_preflight`); keys/data never leak; the sandbox tests before anything runs.
- **P13 Visible work.** Agents work out loud in conversations; Eitan is the boss watching employees, with a one-sentence "what they debated since you left" digest.
- **P14 Quality over quantity** (300 verified > 3000 dead) — reconciled with P3: keep niche elements, cut only dead ones.

---

## 3. MAKE THE AGENTS REAL — the root fix (why nothing worked)
Departments had no brain. v2 gives them real engines and makes their work be *conversation
that produces artifacts*.

### 3.1 Engines (free, multiple) → `src/excava_engines.py`
- Wire, behind one interface: the **8 Gemini keys** (present), **Groq**, **Cerebras**, **OpenRouter free models** (Eitan to add these three keys — no card). Optional later: agent-reach for web/social reach; Gemini Plus + Claude↔Codex when there's budget.
- **Spend policy:** fast engines first (Cerebras/Groq) for the bulk, Gemini for the hard/grounded parts, round-robin within a tier, **per-department daily token budget** enforced by a lease arbiter. Hard ceilings; never spend money.
- **Parity:** a local light path (Ollama on the optional Pi / cached embeddings) so offline behaves like online.

### 3.2 Agents → rewrite `src/excava_agents.py`
- **3–5 agents per department**, differing by a mix of **sub-specialty** (e.g. links: resolve / verify / re-embed) **and role** (doer / checker / improver); the same engine may repeat.
- Two visible tiers: **named persistent AGENTS** (identity, memory) and the **generic WORKERS** they dispatch. **Lead agents** (tier-2) have personality and, in chats, appear raised above their bubble in suit-and-tie.
- Each agent has: a scoped toolset (guardrail G-7), an engine, a specialty, a role, and a name.

### 3.3 Conversations — the real work mechanism → `src/excava_chat.py`
- Four spaces: **within-department**, **between-departments** (hand-offs), an **open group room** (any agent, any department, builds the best thing), and **per-task war rooms** (round table, task pinned, archived when done).
- Threads **produce real artifacts** committed to the project (a resolved-links batch, a new skill, a package) — the transcript is proof, the artifact is the point.
- Every message stores **agent + engine + timestamp**; everything **archived by day**, scrollable; live-updating while open; identical whether Eitan watches or not.

### 3.4 Runtime → extend `src/excava.py` beat + optional Pi
- **CI heartbeat 24/7** (agents make real calls and converse each beat) **+ live/faster when the dashboard is open**. Optional **Raspberry Pi** at home unlocks true real-time, a residential IP (fixes the transcript drain + social scraping), pre-warming, and local compute — the plan works fully without it and lights up with it.

### 3.5 Self-improvement — every crevice → `src/excava_selfimprove.py`
- Autonomously improves **its agents/prompts/engines, the hub's content, AND its own code** — deepest internals to the most superficial surface, nothing exempt — each change gated by the three pitch-rules (P5). This is the part that was completely dead; it becomes a first-class department.

---

## 4. ELEMENTS & PACKAGES — the content layer
- **Unified element model** across all types; a shared card + detail view.
- **Eight tab-control actions** EXCAVA runs on every tab: **Curate** (rank to taste, prune ONLY dead), **Act** (buttons wired to EXCAVA), **Generate** (fill gaps, labeled), **Converse** (a thread per tab), **Verify** (keep every item real/working via sandbox+links+trust), **Relate** (connect + bundle into packages), **Update** (track upstream changes/deprecation), **Teach** (explain + generate a short explainer **video** and **podcast audio**).
- **Per-card actions:** activate-into-my-tool / open-ready-to-run (<10s, pre-warmed) / use-for-a-task, plus **video**, **video-bundle**, and **original-source** links. Compact card, actions on hover; verified/free/engine badges.
- **Element detail view:** everything + live actions (what it is, source video/bundle, how-to, verified status, action row, related elements, use-for-a-task).
- **Packages:** built three ways (on request from a goal, editable before saving, auto-suggested from reuse); shown as a **"kit" you open** to run each element or the whole thing; **frequently-used packages are saved/pinned** (not all — avoid bloat), reusable by Eitan and EXCAVA.
- **More powers:** proactive suggestions, a cost/free-limit guard, per-task effectiveness scoring.

---

## 5. THE ACTIVATOR — one portable `SKILL.md` for any AI tool → `activator/SKILL.md` + `src/build_activator.py`
- A single file Eitan uploads to **any** tool (Claude, Cursor, ChatGPT, Gemini…) that gives that tool a Claude-like "skills" capability: on request it finds or builds the right **package** and acts.
- **Carries a bundled hub snapshot** (works fully offline, incl. running an uploaded **task** — "send a task and it just works") **and reaches live EXCAVA** (engineering-prompt/loop) when the tool can fetch, refreshing.
- Obeys all trigger words (P6). Rebuilt every day from the hub; this is the reserved-for-Opus item that must finally work end-to-end.

---

## 6. THE PARENT LAUNCHER — control center for all projects → new `launcher/`
- A **clean, minimal** top-level tab (feel of Claude's new-chat screen / CMD): a centered grid of **project cubes** (logos/names) in the Excavatortron **yellow** palette but as clean as if it were white.
- Click a project → its **full app opens** (each project defines its own open target), not the Excavatortron UI.
- **EXCAVA can create new projects** → they auto-appear here. The hub is the **shared database** for those projects (via the activator + an optional API/endpoint) — a North-Star goal.

---

## 7. DIRECT EXCAVA CHAT + STEERING
- **Talk to EXCAVA inside the app** (no external tool): a **console panel** in the cockpit + a **floating quick-ask** on every tab; dispatch tasks from within.
- **Direction loop:** state a direction → EXCAVA replies with *its reading* → you correct by re-stating; major changes preview against active directions.
- **Pitches** (the three P5 gates) arrive as **conversations** in the relevant room, fronted by a **dismissible "something needs your approval in ___" banner** on open.
- **Away-digest:** the one-sentence "what they debated since you left" appears three ways — top banner, first line in the console, and a "while you were away" floor card.
- **Notifications:** a bell with a count, and a monster that walks up to tell you.

---

## 8. DESIGN SYSTEM & ART DIRECTION
**Scope split:** the clean/minimal look is the **parent launcher only**; inside Excavatortron it stays **"Heavy Machinery," refined and professional** — must feel like a real established product, not a freshly-made website.

**Build method (P1 free-first):** design-**system first** (tokens / type / spacing / components), then screens; use **real design tools** (Figma/Adobe MCP) + **AI-generated monster art**; **test whether free tools give accurate, perfect results before** proposing Gemini/Higgsfield or anything paid.

- **Palette:** yellow signature + (leaning) warm ink/steel neutrals — **Fable produces color samples for Eitan to choose.** Light default, dark optional. English only.
- **Fonts:** bold display + clean readable body pairing.
- **Icons:** one bespoke set, no emoji mixing. Generous spacing/grid.
- **The floor:** a stylized **isometric factory**; departments each have their own **station/building** + **monster species** + signature icon/texture.
- **Monsters (Monsters-Inc-style):** one species per department, unique colors/features; **named agents** are distinct individuals, **lead agents** in suit-and-tie with personality (raised above their chat bubble), **workers** smaller and generic.
- **Animation catalog (per action):** fix (weld), build/create (hammer), test (magnifier), verify (checkmark-stamp), deliver-a-result (celebrate), research (dig/scan), make-media (film), hand-off (carry a parcel to another station), pitch/stuck (wave for the boss), idle/rest/maintenance; **warming an element to open** = a monster "flipping pancakes" + a short progress cue (<10s).
- **Chat UI:** messenger (Telegram/WhatsApp), monster avatars, "agent · engine" badges, day dividers, department channels in a side rail; war rooms = round-table situation rooms; open room = a big communal hall.
- **Element card / detail / results:** per §4; **results feed** viewable by day, by department, and by sub-agent, with open/use/send-to-project, plus inline-in-the-chat-that-made-it and a "new" badge on the element's tab.
- **North Star:** Excavatortron at the **center**, the **9 goals orbiting as distinct rotating stars**, each with its meaning below.
- **Relate:** an interactive **brain graph** + "related" rows on each element. **Packages** = openable kits.
- **Navigation:** left sidebar (departments/tabs) + top bar (global search + EXCAVA + account/settings/shortcuts).
- **Mobile:** read / review / approve / send tasks + directions from the phone; **nothing runs or builds on the phone.**

---

## 9. THE 52 GOALS (+G9) — the make-real slice & order
Depth-first order (Eitan's): **1) everything real/verified/connected (G3) → 2) access it, know→do (G2,G5) → 3) agency, the agent OS genuinely working (G9,G4) → 4) personal fit + database (G8,G6).** G1 omniscience keeps climbing throughout; G7 security is always-on. Every goal maps to a phase below; the North-Star constellation scores all 9 each cycle.

---

## 10. BUILD PLAN — milestones in Eitan's order (step-by-step; Fable never has to ask)
Each milestone ships a **change-tutorial**, bumps `APP_BUILD` + `sw.js`, and is verified before commit. Fresh app shell; migrate real data; keep the proven CI pipeline underneath.

- **M1 — REAL/VERIFIED ELEMENTS + ACCESS.** Finish sandbox-verifying all 1,142 connectors; verify every element's links/installs; wire the per-card action row (activate/open/use/video/source) and the <10s pre-warmed open; unify the element model + detail view. _Done: you can open/run real elements; dead ones are gone, niche ones kept._
- **M2 — REAL AGENTS CONVERSING + PRODUCING.** Engines layer; 3–5 real agents/department; the four conversation spaces, visible + archived by day; a war room that produces one real artifact end-to-end; self-improvement department live. _Done: agents actually build something you can use, out loud._
- **M3 — NEW SHELL + LAUNCHER.** The refined Heavy-Machinery app shell (sidebar + top bar + search), the Monsters-Inc floor with the animation catalog, the messenger chat UI, the North-Star constellation, the direct-EXCAVA console + floating ask, the parent launcher. Design-system-first, real tools, color samples for approval. _Done: it looks and feels like a real product._
- **M4 — ACTIVATOR END-TO-END.** The portable `SKILL.md` (bundled snapshot + live EXCAVA + task execution + all triggers), proven in a second tool; packages saved/reused; the database/endpoint for other projects. _Done: know→do works anywhere; EXCAVA proven real by agency + goal→package._
- **Then breadth:** finish remaining goals, tiers 2–3 of omni-source intake, portability, cleanup (per `EXCAVA_PROGRAM.md` P7–P9).

**Reserved for Opus 4.8** (accuracy-critical): the activator working end-to-end, the engines layer correctness, data-retrieval accuracy, and fixing anything Fable builds inaccurately. All visuals = Fable.

---

## 11. OPEN DECISIONS → resolved via mockups + labeled defaults (for Eitan's review)
These weren't worth a live question but need your eye; Fable will **mock each and default as noted**, you change on review:
- Exact **color palette** (samples) · exact **monster cast** per department (mock the 11) · **fonts** (2–3 pairings) · first-run **guided tour** (default: helpful empty states, tour optional) · war-room/round-table **generated scene** (default: illustrate, don't video, unless free tools fall short) · notification **sound** (default: off) · command-palette **Cmd-K** (default: add) · exact **station shapes** on the floor.

_This plan is a living draft: reopen any thread, add design rounds, or bring improvement points — every decision here is sourced from the interview and captured in memory (`project-excava-direction-2026-07`)._



---

# ===== FILE: EXCAVA_V2_STEPS.md =====

# EXCAVA v2 — STEP-BY-STEP EXECUTION PLAN (the "do" doc)

_Companion to `EXCAVA_V2_PLAN.md` (why) + `EXCAVA_V2_ADDITIONS.md` (the finalized interview answers,
which this doc now folds in). Every task = **Build** (files/what) + **Done when** (acceptance). Order
is strict within a milestone. Fable does everything except **[OPUS]**; **[OWNER]** = an action from
Eitan (never blocks). Every task: recall-before-change, log the WHY, obey `PROTOCOLS.md`, free-only._

**Global rules folded in from the interview:**
- **CORE = SPOT-ON is priority #1** (the M1.C block below); retrieval depth is the single biggest fix.
- **Claude runs autonomously on Eitan's Pro** via `CLAUDE_CODE_OAUTH_TOKEN_REAL` (already wired), so
  **[OPUS] tasks can run in CI too** — budgeted to highest-value work, premium-marked.
- **Designs have NO approval gate** — Fable creates, Eitan reviews the result (samples shown, not pre-approved).
- **Every milestone ships an INTERACTIVE tutorial + an explainer video + podcast**, bumps `APP_BUILD`+`sw.js`,
  verifies in preview, commits.

---

## M1 — REAL / VERIFIED ELEMENTS + ACCESS  (+ the SPOT-ON core)
Nothing on any tab is dead or fake, everything is deep + accurate, and you can open/run/use it.

### CORE (priority #1 — runs continuously, folds through M1)
**M1.C1 — Retrieval depth (THE #1 fix).** Build: `src/deep_retrieve.py` — re-analyze every element from
its **FULL source** (whole transcript / repo README + docs) **+ enrich from ≥1 other source**; explicitly
recover things currently **missed from the playlist or unfindable online**. Done when: every kept element
has full-source + ≥1 enrichment source; stub-rate ≈ 0.
**M1.C2 — The discovery agent (hourly, everywhere).** Build: `src/discovery_agent.py` + hourly workflow —
scan GitHub trending/new + release feeds · HN/Reddit/X · Product Hunt/awesome-lists · official + company +
national releases · **every social network via agent-reach** · the playlist. New items → the gated intake
queue; inclusion = **AI-relevant + a quality signal** (stars/activity/real README). Done when: a brand-new
notable tool/repo lands in the hub **same-day**; the agent runs hourly.
**M1.C3 — Verify, re-verify, reconcile.** Build: verification = **cross-check ≥2 sources + a live link/
install test**; **rolling re-check (weekly) + on-access**; conflicts → **reconcile, keep best-supported,
note the conflict**; a **minimum enrichment + verification bar** — below it an item is **"unverified",
never shown as real**. Done when: real items carry 2-source proof; stale/changed items get caught; conflicts flagged.

### Access
**M1.0 — Unified element model.** Build: `data/schema/element.json` (id, type, name, what, source_videos,
links{website,github,open_code}, install, verified{status,method,at,log}, trust, related, video_bundle,
created_by); `src/element_model.py` normalizes every per-type file → read-only `data/elements_index.json`;
`set_field()` writes back to the owning file only. Done when: `--count` prints per-type totals + a sample;
no source file mutated except via `set_field`.
**M1.1 — Finish connector sandbox verification (all 1,142).** Build: keep `verify_connectors.yml` (6-hourly,
30/batch, tree-kill fix); add `--catchup 60`; npm+pip preflight. Done when: `connectors_verified.json.summary.checked == total`.
**M1.2 — Verify ALL element types.** Build: `src/verify_elements.py` — URL/repo → parallel HEAD liveness;
MCP/repo → sandbox runner; skills/prompts/formats → schema + `security_preflight`; **feeds the ≥2-source +
live-test standard from M1.C3** → `data/elements_verified.json`; `verify_elements.yml`. Done when: every
element carries `verified{status,at}` at the M1.C3 standard.
**M1.3 — Trust gate + "dead only" pruning (P3).** Build: join `source_trust.json`; status ∈
verified|unverified|niche|dead; **only dead (link+install+sandbox all fail) is hidden**; **never delete for
low rating** (keep niche); items under the M1.C3 min-bar show as **unverified**, not real. Done when: a
low-rated-but-working niche element stays visible; only dead ones hide.
**M1.4 — The per-card ACTION ROW.** Build: `elementActions(el)` → **Activate** (recipe+copy now, real setup
in M4), **Open** (github.dev/Codespaces/hosted MCP — a real runnable target), **Use for a task** (opens the
console prefilled), **Video**, **Video bundle**, **Source**. Done when: every card shows the row; Open opens
a runnable target; Video plays.
**M1.5 — The <10s pre-warm / open.** Build: `src/prewarm.py` keeps top-N repos/MCP warm (`data/prewarm.json`);
Open = instant if warm, else the **pancake-warming** animation + progress <10s. Done when: warm = instant;
cold resolves <10s (timed in preview).
**M1.6 — Element DETAIL view.** Build: `renderElement(id)` at `#element/<id>` — what it is, embedded
video/bundle, how-to, verified status, action row, related, use-for-task. Done when: any element opens a full page.
**M1.7 — RELATE (related rows).** Build: `src/relate.py` — related from memory-graph topics + same source
video + co-occurrence → `related[]`. Done when: each detail shows 3–8 real related elements.
**M1.8 — Dashboard reads the unified index.** Done when: all tabs render from `elements_index.json` with
verified/trust badges; no console errors.
**M1.9 — Ship M1.** Done when: interactive tutorial + explainer video/podcast + build bump + preview-verified + committed.

---

## M2 — REAL AGENTS CONVERSING + PRODUCING
Agents get real engines; their work is a visible conversation that produces artifacts.

**M2.0 — `PROTOCOLS.md` + self-audit.** Build: write P1–P14; extend the beat `_audit_spine()` to check it;
drift → SAFE mode. Done when: beat prints "audit OK vs PROTOCOLS.md"; deleting a rule trips SAFE.
**M2.1 — The engine layer (existing engines KEPT first-class; OmniRoute ADDED as a central option, not a
replacement or sole path).** Build: `src/excava_engines.py` keeps the **9 already-wired free families**
(Gemini ×6 · Groq ×2 · Cerebras ×2 · OpenRouter incl. **free DeepSeek R1 / Qwen3 Coder** · NVIDIA Nemotron ·
SambaNova · Mistral · GH-Models) as **first-class, directly-callable** engines, **+ self-hosted Hermes**
(Ollama/Pi) **+ Claude via the Pro OAuth token** (budgeted, premium-marked). **OmniRoute is ADDED alongside
them as an additional, central routing option** (never replacing them, never the only path): a free
self-hosted OpenAI-compatible gateway that fronts 160+ providers with **4-tier fallback (Subscription →
API-key → cheap → free)** + **token compression (15–95%)** + **90+ free tiers (~1.6B free tokens/mo)**.
`pick_engine(dept,difficulty)` may route **via OmniRoute** (central smart-routing + compression + widest free
reach) **or call an engine directly** — configurable per department; **direct calls always work if OmniRoute
is off or down**. Done when: `--selftest` returns real completions **both directly AND via OmniRoute**, and
turning OmniRoute off still works.
**M2.1a — [OWNER] Confirm keys (already added).** Eitan's ~20 secrets are already in the repo; run
`engine_selftest.yml` to confirm which families answer. **No new purchase.** Done when: the selftest report
shows the live set.
**M2.1b — External free tools (OPTIONAL — Fable/EXCAVA self-configures; no manual owner step required).**
**OmniRoute** — OPTIONAL central gateway (`npm install`, port 20128; per-CI-run or on a host). Eitan
installed it locally 2026-07-05 (it runs) but left the provider-key step; **Fable wires it up autonomously
later**, so no owner action now. **OpenClaw** (channels/browse/shell), **agent-reach** (M1.C2 discovery
reach), optional **Ollama/Hermes** + **Raspberry Pi** — all likewise Fable-set-up, deferred until needed.
Done when: each is reachable from a run whenever Fable brings it online; nothing here blocks M1–M4.
**M2.2 — Lease arbiter + budgets.** Build: `src/excava_leases.py` — per-dept daily token budget, hard
ceilings, per-engine RPM caps, **+ a tight Claude/Pro budget** so automation never eats Eitan's Desktop quota.
Done when: a department at budget is held+traced; Claude usage stays within its daily cap.
**M2.3 — The agent roster (named leads + workers).** Build: rewrite `agents.json` — per department 3–5 agents
`{name,engine,specialty,role∈doer|checker|improver,tier}`; **~11 distinct NAMED leads** with personas
(suit-and-tie), generic workers; **personality matches the department** (security = paranoid guard, creators =
eccentric inventor, links = meticulous librarian) and **affects tone AND behavior** (a cautious agent verifies
more); tone = characterful-but-competent; **EXCAVA proposes the cast, Eitan tweaks**. Borrow SOUL.md /
agency-agents patterns. Done when: `--roster` prints the named cast with engines+roles+personas.
**M2.3b — OpenClaw as a tool.** Build: expose OpenClaw's channels (WhatsApp/Telegram/…), browse/forms/shell,
and Canvas as scoped tools agents may call. Done when: an agent completes a task using an OpenClaw capability, traced.
**M2.4 — Agents vs workers.** Build: persistent AGENTS spawn ephemeral WORKERS (temp id → one unit → report →
dissolve); `state.json` tracks live workers. Done when: a task shows an agent dispatching workers that finish
and vanish, traced.
**M2.5 — The conversation engine.** Build: `src/excava_chat.py` — `Room(kind∈dept|cross|group|war, goal,
max_turns, done_criteria)`; agents take turns via real engine calls, with **productive debate then converge**
(a checker can push back on a doer before the room decides); messages → `data/excava/chats/<YYYY-MM-DD>/<room>.jsonl`.
**War rooms are the showpiece.** Done when: a room runs a real multi-turn debate ending on its done-criteria;
archived by day; replayable.
**M2.6 — Conversations produce artifacts.** Build: a room ends by calling a scoped tool (resolve-links / draft
an element / assemble a package); artifact committed + linked from the transcript. Done when: one war room
produces a real committed artifact you can open.
**M2.7 — Wire into the beat (24/7 + live, parity).** Build: each beat advances top rooms (bounded turns);
dashboard-open runs more turns in-browser via the same engines; identical code path. **Fully parallel, NO
concurrency cap** (it stays legible because it's organized by agent/department/room with drill-down); a
**visible timing readout** on the floor; **creations may take a while but never > ~1 hour (target < 30 min)**,
while **anything Eitan-facing responds fast**. Done when: rooms progress every CI beat unattended; opening the
dashboard accelerates them; output identical either way; timings visible.
**M2.8 — Self-improvement department (real).** Build: `src/excava_selfimprove.py` — agents review
prompts/engines/routing/hub/own-code; safe changes auto-apply+test; overhaul/new-tool/deeper-access → a PITCH.
The **strict quality bar applies to things EXCAVA CREATES** (small prompts/commands may be light). Done when:
≥1 real safe self-improvement + ≥1 pitch, both visible.
**M2.9 — Ship M2.**

---

## M3 — NEW SHELL + LAUNCHER + FULL DESIGN  (all Fable · NO approval gate)
It looks and feels like a real, professional product; the living workshop is real.

**M3.0 — Design system (direction DECIDED — build it, show samples, don't gate).** Build: `docs/design/tokens.css`
+ primitives + gallery, to this direction (ADDITIONS §I): **refined Heavy-Machinery + playful + clean-tech
touches**; **yellow + warm ink, real metal framing, pockets of greenery**; **light default, dark optional**;
**spacious**; **bold industrial** display + clean body; **refined-neobrutalist ≈ textured-industrial** finish;
**rounded, organic, characterful shapes** (no plain circles/squares); **bespoke line icons**. Done when: tokens
+ gallery render in that look; **Eitan sees it, no pre-approval blocks the build**.
**M3.1 — The app shell.** Build: new `index.html` — left sidebar + top bar (search, EXCAVA, account/settings/
shortcuts); migrate tabs in. Done when: sidebar+topbar+search work; feels like a real product; zero console errors.
**M3.2 — Monster art (samples first, no pre-approval).** Build: 11 species + agent/lead(suit-and-tie)/worker(small)
variants via image-gen (free-first) → `docs/assets/monsters/`; **friendly-but-distinctive with a cool/edgy edge**,
each **matched to its department**. Fable **shows Eitan a sample set** to judge quality, then proceeds. Done when:
11 distinct species; leads/workers distinct.
**M3.3 — Isometric factory floor (+ side cutaways).** Build: `docs/floor/` — **isometric** stations/buildings,
monsters walking, wired to real bus/room state, with **side-view cutaway moments** when you enter a department.
Done when: floor reflects real activity; stations open departments; cutaway on entry.
**M3.4 — Animation catalog.** Build: ~11 animations (fix=weld, build=hammer, test=magnifier, verify=stamp,
deliver=celebrate, research=dig, make-media=film, hand-off=carry parcel, pitch=wave, idle=rest, open=pancake-flip),
each from the real action; overall **lively but purposeful** (floor alive, elsewhere event-driven). Done when:
every action type plays its distinct animation from real events.
**M3.5 — Messenger chat UI.** Build: department channels rail; bubbles with monster avatars + "agent · engine"
badges + day dividers; **war-room round-table** (showpiece); open-room hall. Done when: you read any room's real
conversation, scroll by day, see who+engine per message.
**M3.6 — Element card + detail (final visual).** Build: apply the design system; compact card, actions on hover,
badges. Done when: cards match the system; actions on hover.
**M3.7 — Results feed.** Build: filterable by day/department/sub-agent; result card = what/preview/open/use/
send-to-project; also inline in the making-chat + "new" badge on the tab. Done when: real artifacts appear,
attributed, openable, in all three places.
**M3.8 — North-Star constellation.** Build: Excavatortron centered; **9 goal-stars** orbit (rotating), each
distinct, meaning below; live scores. Done when: shows live scores; each star opens its goal.
**M3.9 — Brain graph (relate, full).** Build: interactive element+link graph; click to explore; cluster → a
package. Done when: navigable; a cluster becomes a package.
**M3.10 — Direct EXCAVA console (full bar + floating).** Build: `#excava` **hero console like the screenshot** —
engine/agent selector · mic · attach file/task · "+" context · slash-commands for triggers (NOSG/HORSE/PLAN/
RESEARCH/WATCH); opens with the away-digest; **streams like a chat and dispatches** to departments; plus a
context-aware **floating quick-ask on every tab**. Done when: typing a task dispatches it and EXCAVA replies;
floating ask works on any tab.
**M3.11 — Steering (direction, pitches, notifications).** Build: direction card (state → EXCAVA's reading);
dismissible "needs your approval in ___" banner; bell+count; a monster walks up on new approvals; pitches as
conversations. Done when: a pitch shows the banner, opens as a conversation, approve/decline works.
**M3.11b — Editable taste panel.** Build: a visible, editable taste profile — **separate design-taste vs
work-taste**, learned + explicit; feeds HORSE merges + designs. Done when: you can view/tune your taste weights.
**M3.12 — Mobile pass.** Build: responsive shell — read/review/approve/send on phone; execution disabled on
phone. Done when: phone shows chats/results/approvals + send; no run buttons.
**M3.13 — Ship M3.**

---

## M4 — ACTIVATOR END-TO-END + LAUNCHER
Know→do works anywhere; EXCAVA proven real by agency + goal→package.

**M4.1 — [OPUS] Portable activator.** Build: `src/build_activator.py` → `activator/SKILL.md` — compressed hub
snapshot (elements + package recipes + PROTOCOLS + triggers) AND a live-EXCAVA fetch path; obeys NOSG/HORSE/
PLAN/RESEARCH/WATCH; runs an uploaded task offline; daily rebuild. Done when: uploaded to a second tool, it
finds/builds a package and runs a task; triggers behave; works offline.
**M4.2 — HORSE execution.** Build: `src/horse.py` — 10 agents (varied engines) each fully execute the goal;
merge best-of-**results** to your **work-taste**. Done when: `HORSE <goal>` returns one merged artifact from
10 real executions.
**M4.3 — Packages: build/edit/save/reuse.** Build: `data/packages.json` — on-request + editable + auto-suggested;
pin frequent; kit UI (open → run each/all). Done when: assemble → pin → reuse in one click.
**M4.4 — Parent launcher (its OWN brand).** Build: `launcher/` — a **distinct clean minimal brand with its own
identity** (not Excavatortron's look, not reused as a default frame); centered project-cube grid; each cube opens
the project's own app in a **full context switch**; EXCAVA-created projects auto-appear. Done when: it lists
Excavatortron + your projects; each opens its full app; a new EXCAVA-made project shows.
**M4.5 — Hub-as-database.** Build: `hub_api.json` / endpoint + activator as carrier so Budoaris/FreeDup pull
elements/packages. Done when: another project pulls a package via the activator or endpoint.
**M4.6 — Ship M4 + prove "real".** Done when: (a) agents build a real artifact overnight unattended, AND (b)
you type a goal → get a working package you use — both demonstrated.

---

## M5 — EXCAVA ACTS ON THE WORLD  (DEFERRED behind CORE + M1–M4)
The significant external reach — built only once the core is spot-on.
**M5.1** Manage Eitan's projects' tasks. **M5.2** Post to / monitor his channels (OpenClaw + agent-reach) +
alert. **M5.3** Build + deploy sites/tools. **M5.4** **Find ways to make money** for Eitan. **M5.5** Interact
with **systems Eitan adds later** + **spin up whole projects independently**. Gate = **hybrid**: low-risk/
read-only auto, **anything risky or money-related pitches first**. Done when: ≥1 external action runs end-to-end
under the gate, traced + tutorialized.

---

## BREADTH (after M1–M4, alongside M5)
B1 finish the 52 goals per §9 order · B2 omni-source tiers 2–3 · B3 per-tab self-improvement + meta-brain ·
B4 portability (Budoaris first if you ask) · B5 cleanup (formats filter, brain white-nodes, token-split) ·
B6 EXCAVA-as-MCP-server. _(Expand B1/B3/B6 to full steps first, then the rest.)_

## OPEN DECISIONS → fold into the build (Fable creates, you review — NO pre-approval)
O1 palette (direction already set §I) · O2 the 11-monster cast (samples shown) · O3 fonts · O4 first-run tour
(default: empty states, tour optional) · O5 war-room scene (default: illustrate) · O6 notification sound
(default: off) · O7 Cmd-K (default: add) · O8 floor station shapes. _These come after the program is finalized
in build; Fable mocks and you see the result._



---

# ===== FILE: EXCAVA_V2_ADDITIONS.md =====

# EXCAVA v2 — ADDITIONS  (finalized from the full interview; does NOT alter PLAN or STEPS)

_`EXCAVA_V2_PLAN.md` and `EXCAVA_V2_STEPS.md` remain byte-identical. All corrected/new direction
lives here and supersedes on conflict. Built 2026-07-04/05 from the complete multiple-choice
interview. **Top priority: §F CORE SPOT-ON**, then M1→M4, breadth (M5 external DEFERRED)._

## A. Claude — via your PRO, and it CAN run autonomously
- No paid API. Claude runs on your **Pro** through the existing **`CLAUDE_CODE_OAUTH_TOKEN_REAL`**
  secret (already wired into analyze/claude/discover/improve/review workflows) — so it works **even
  when you're not in a session**, in CI, on Pro.
- **Budgeted:** used only for the **highest-value work** (final HORSE merges, design taste, accuracy
  fixes, hardest problems), a few runs/day, so it never drains the Pro quota you also use in Claude
  Desktop. **Premium-marked** in the UI (a badge shows when the heavy model ran).
- The free-engine pool does all the bulk 24/7 (see §B).

## B. Engines & external tools (final)
- **Engines already wired (free):** Gemini ×6 · Groq ×2 · Cerebras ×2 · OpenRouter · NVIDIA
  (Nemotron) · SambaNova · Mistral · GH-Models — **9 families**, plenty. DeepSeek R1 + Qwen3 Coder
  come **free through OpenRouter**. Confirm live set by running `engine_selftest.yml`. **These stay
  first-class + directly callable — nothing below replaces them.**
- **OmniRoute** (diegosouzapw/OmniRoute): free self-hosted OpenAI-compatible **gateway** (160+ providers,
  4-tier fallback Subscription→API-key→cheap→free, token compression 15–95%, ~1.6B free tokens/mo).
  **ADDED as an additional, CENTRAL routing option — NOT a replacement, NOT the sole path**; the 9
  engines above remain directly callable and everything still works with OmniRoute off. (M2.1 + M2.1b.)
  **STATUS: OPTIONAL / deferred.** Eitan installed it locally 2026-07-05 (it runs) but stopped at the
  provider-key step (fiddly). **No owner action needed** — EXCAVA/Fable wires it up autonomously later
  (per-CI-run or on a host); until then the direct engines cover everything. Keep it on the options list.
- **Hermes** ("Hadishan"): open-weights, added on the **free self-host path** (Ollama on the optional
  Pi / a capable machine); the paid endpoint stays off.
- **OpenClaw: ADD as a tool** (Eitan's call) — used for its capabilities (channels, browse/shell,
  SOUL.md personalities, multi-agent patterns); EXCAVA's own bus/memory/gate stays the spine; do NOT
  replace the existing engines with it.
- **agent-reach** (GitHub): the multi-platform reader — the backbone of the discovery agent's reach
  across every social network (§F).
- **Borrow patterns** from gitagent (git-native), agency-agents (personalities), governance-toolkit
  (security), CrewAI/open-multi-agent (parallel roles). No hard dependency.

## C. Design tooling (final) + the "show me the creatures first" step
~80% of the M3 UI is code Fable writes with design skills; asset tools are a small stack (image-gen
for monsters, optional Figma). **Before committing monster details, Fable generates a small SAMPLE of
creatures so Eitan can judge the quality/style first** (J3), then we pick tools + finalize. A
**design-only interview** happens before M3 (Eitan's choice).

## D. Hermes = "Hadishan" — resolved, free self-host path (see §B).

## E. THE ANSWERS — folded into the plan (each becomes acceptance-tested build detail)

**E1 · Agent personalities.** Distinct **named characters**; **leads named (~11), workers generic**;
personality affects **tone AND behavior** (a cautious agent really verifies more); **productive debate
then converge** (a checker can push back on a doer before the room decides); **personality matches the
department** (security = paranoid guard, creators = eccentric inventor, links = meticulous librarian);
tone = **characterful but competent** (a real workshop, light not cartoonish); **EXCAVA proposes the
cast, Eitan tweaks**. _Source: SOUL.md configs + agency-agents patterns._

**E2 · Pace / parallelism / quality.** **Fully parallel, non-blocking** — no department waits on
another; an agent hands off a finished sub-part without completing its whole task. **No concurrency
cap** (it stays legible because everything is organized by agent / department / room, with drill-down).
**Visible timing readout** on the floor. **Creations are quality-first**: may take a while but
**never > ~1 hour, target < 30 min**; anything **Eitan-facing** (console, his tasks, approvals)
responds **fast**. **Quality gate is strict for things EXCAVA CREATES**; for **existing elements**,
keep almost everything (incl. niche) and exclude only **dead / fake / empty / broken** (matches P3).

**E3 · Creators department.** They **enrich every tab as much as possible** (max real info) **and build
packages** (packages first; both combine + net-new). **Only the three P5 pitch-items wait** (new tool /
overhaul / deeper access); everything else flows autonomously, labeled "Created by EXCAVA" + tested
before first use. Cadence: **a few high-quality per day**, but **small prompts/commands may be light/
simple**. Triggered by **detected gaps + your requests + a dedicated DISCOVERY agent's finds** (§F).

**E4 · The console (like the screenshot).** **Full bar** — engine/agent selector · mic · attach file/
task · "+" context · slash-commands for triggers (NOSG/HORSE/PLAN/RESEARCH/WATCH). Lives as a
**home screen AND a floating quick-ask on every tab**. **Streams like a chat and dispatches** tasks
straight to departments/agents.

**E5 · Taste.** **Broaden beyond design** (tone/tools/approaches, not just Arena votes); **learned +
explicit**; **separate "design taste" vs "work taste"**; a **visible, editable** taste panel. Feeds
HORSE merges + designs.

**E6 · Launcher.** **Its own name/brand + its own unique look** (not reused as a default frame);
opening a project is a **full context switch** (the project's app takes over, no launcher chrome);
Excavatortron stays "Heavy Machinery" inside — the two designs are **independent**.

**E7 · Tutorials (M1.9).** **Every milestone** ships a tutorial; **always an explainer video + podcast**
(the Teach action) **plus an interactive walkthrough for big changes** that **highlights the new thing
on-screen and lets you try it**.

**E8 · M5 external actions (DEFERRED behind the core).** Scope when it comes: manage your projects'
tasks · post/monitor your channels (OpenClaw + agent-reach) · build + deploy sites/tools · **find ways
to make you money** · **interact with systems you add later + spin up whole projects independently.**
Gate = **hybrid**: low-risk/read-only auto, **anything risky or money-related pitches first**.

## F. CORE = SPOT-ON  (TOP PRIORITY — folds into M1, runs continuously)
The #1 job: make what EXCAVA already does the **deepest, freshest, most accurate** it can be.
- **F1 Retrieval depth — the #1 accuracy fix by a wide margin** (Eitan): every element analyzed from
  its **full source** (whole transcript / repo README + docs) **+ multi-source enrichment** — never a
  stub. Explicitly recover what's currently **missed from the playlist or not found at all** online.
  _Done when: every kept element has full-source + ≥1 enrichment source; stub-rate ≈ 0._
- **F2 Freshness & discovery — hourly, everywhere.** A **dedicated discovery agent** scans **hourly**:
  GitHub trending/new + release feeds · HN/Reddit/X · Product Hunt/awesome-lists · **official sites +
  companies + national/"country" releases** · **every social network via agent-reach** · the playlist.
  _Done when: a brand-new notable tool/repo appears in the hub same-day._
- **F3 New-repo bar:** AI-relevant **+ a quality signal** (stars/activity/real README) — no junk.
- **F4 Verification:** **cross-check ≥2 sources + a live link/install test** before an item is "real."
- **F5 Re-verification:** **rolling background re-check (weekly) + on-access** — catches dead/changed.
- **F6 Success metric:** **both coverage % AND depth/accuracy** per item.
- **F7 Conflicts:** EXCAVA **reconciles, keeps the best-supported answer, and notes the conflict.**
- **F8 "Known/real" gate:** a **minimum enrichment + verification bar**; below it = **"unverified",
  never shown as real.**
- **F9 Fix order:** **retrieval/analysis depth ≫ link resolution > activator (know→do).**

## G. WHAT EITAN NEEDS TO DO (setup — nothing to buy)
1. **Confirm engines live:** run `engine_selftest.yml` (Actions → Run workflow); it reports which of
   the ~9 free families answer. Your keys look complete; this is the definitive check.
2. **Claude autonomous budget:** confirm you're OK with EXCAVA using a **few Claude-Code runs/day** on
   your Pro token (`CLAUDE_CODE_OAUTH_TOKEN_REAL`) for the highest-value work only — leaves Desktop
   headroom. (If Pro limits bite, we dial it down.)
3. **agent-reach + OpenClaw:** installed/self-hosted when we reach the core-discovery + M2 work — I'll
   give exact commands then (both free; OpenClaw self-hosts on your machine/Pi).
4. **Optional Raspberry Pi:** unlocks real-time + residential IP (fixes transcript drain + social
   scraping) + local Hermes/Ollama. Plan works without it; lights up with it.
5. **Design tools:** nothing now — Fable will first show you **sample monster creatures** to judge
   quality; we pick asset tools at the design round.

## I. DESIGN DIRECTION (final 2026-07-05 — Fable builds autonomously; NO approval gate; Eitan reviews results)
- **Aesthetic:** refined **Heavy-Machinery** (premium industrial) **+ playful game-UI liveliness** +
  **clean-tech touches at points**. Must feel like a real, established product.
- **Palette:** signature **yellow + warm ink**, with **real metal framing** and **pockets of greenery/
  vegetation** in certain areas (life against the industrial). **Light default, dark optional.**
- **Density:** **spacious** (premium, calm).
- **Type:** **bold industrial** display (Archivo Black-ish), clean readable body.
- **Finish:** **refined neobrutalist** (hard offset shadows + chunky borders, cleaned up) as the primary,
  with a **near-equal amount of textured industrial** (subtle metal/brushed/grain surfaces).
- **Shapes:** **rounded but organic and characterful** — nothing is a plain circle or square; creatures
  and UI elements get distinctive, interesting silhouettes.
- **Icons:** one **bespoke line-icon set**, no emoji mixing.
- **Floor:** **isometric factory** (primary) with **side-view cutaway moments** (e.g. when you enter a
  department). Departments = their own station/building.
- **Monsters:** **friendly-but-distinctive with a cool/edgy edge**; one species per department, **matched
  to its function**; **named + suited leads**, generic smaller workers. Fable **generates sample creatures
  for Eitan to see first** (quality check) — but no pre-approval blocks the build.
- **Animation:** **lively but purposeful** — the floor is alive; elsewhere motion is tied to real events.
- **Showpieces (make these sing):** the **living factory floor** + the **chat / WAR ROOMS** (Eitan's
  most-anticipated) + the North-Star constellation + the console hero.
- **Already set (earlier rounds):** messenger-style chat UI · central hero **console** like the screenshot
  (home + floating) · **launcher** = its own clean minimal brand, full context switch.
- **No approval gate on designs:** EXCAVA/Fable create designs autonomously; Eitan **sees** them, doesn't
  pre-approve. O1–O8 mockups fold into the build the same way.

## H. NEXT / WORKING
- All interviews DONE (~100 questions, incl. this design round). This doc is the finalized answer-set;
  `EXCAVA_V2_PLAN.md` + `EXCAVA_V2_STEPS.md` remain byte-identical.
- **Fable is on Eitan's Pro until July 7** → **front-load building, visuals first**, over the next ~2 days.
- On switch to Fable: start **M1 core (retrieval depth + verification)** and the **design system + sample
  monsters** in parallel; show results, no approval gate.

## J. TWO NEW DEPARTMENTS (owner 2026-07-06 — enter into roster + floor + goals; build via Fable)
- **Visualization** — owns the visibility of the ENTIRE Excavatortron interface and how everything is
  presented (distinct from `visual`, which mines AI website/product designs). Its job: continuously
  improve the shell/floor/cards/chat presentation. **Goals it drives up:** (1) more liveliness in the
  project, (2) improved user access to information, (3) user enjoyment following changes. _(Owner invited
  more goals — pending Q; candidates: clarity/legibility, speed/perf, accessibility, consistency.)_
- **Power** — owns raising EXCAVA's raw capability. Mandate: chase every option that improves ability
  **even by 0.5%** — find new tools to add, update agents onto the **best + newest models available**,
  **combine "elements"** for compounding gains, and change agent **formation / planning / mode of
  operation / action plan** for productivity. **Always displays a POWER %** (a single headline number for
  how capable EXCAVA is) that **can exceed 100%**. Each improvement is logged with its measured % delta.
- Personas match department (per §E1). Monsters: friendly-but-distinctive, matched to function — BUT the
  whole cast is being reworked (see §L: real image tool, monsters need legs/body). Do not hand-draw new
  ones in the old style; regenerate the full cast together once the art tool is chosen.

## K. TWO NEW PITCH CONDITIONS + THE PITCH MONSTER (owner 2026-07-06)
- EXCAVA **always prioritizes improvements it can make ITSELF** (auto, no pitch). It pitches the owner ONLY
  when it truly needs him. Two NEW pitch triggers added to the existing P5 set:
  - **(P5d) Owner-only high-leverage:** something **only Eitan can add** to the system that would help a
    lot (a key/account/hardware/permission/decision EXCAVA cannot self-provide). Pitch = **why + what it
    unlocks**. Still secondary to anything EXCAVA can do itself.
  - **(P5e) New-department creation:** proposing a brand-new department. Pitch = **why it's needed + what
    it will include** (mandate, goals, which existing gap it fills).
- **NOT a pitch — notify only:** adding new **agents / employees** to an existing department needs no
  approval; EXCAVA just **tells the owner through the existing channels** that it happened.
- **The pitch MONSTER:** when a pitch is waiting, a monster **walks up to signal it, styled to the group
  that produced the pitch** — a lone agent (single monster), a department (its lead + workers), a group
  chat (a small cluster), or a **war room** (the round-table cast). The signal's form tells Eitan at a
  glance who is asking. (Extends M3.11 "a monster walks up on new approvals".)

## L. HONESTY AUDIT — 2026-07-06 (Opus 4.8), READ BEFORE BUILDING MORE
Ground truth, verified against real data + the 5 project sessions (not asserted from handoffs):
- **REAL and working:** the M1 pipeline — lanes extract/analyze/verify elements, write hand-off docs,
  grow memory (6,400+ elements; floor "working/ran Xh" statuses are real git-commit recency).
- **FACADE — not actually happening:** the M2 "agents conversing → converge → ARTIFACT" layer. Across 33
  beats there are **0 real agent turns and 0 artifacts** — every engine call fails (`beat_log:
  "no engine here (gemini:HTTPError)"`). The code is genuinely wired to call real engines, but no engine
  has ever answered where the beat runs (keys not reaching the beat / endpoint rejects). So the rooms,
  the bustling floor, and "M2 COMPLETE" are presentation over a core that does not run yet.
- **Console leaves the app:** typing a task opens a GitHub *new-issue* page (`_exIssue`). Owner wants it
  **fully in-app**. Needs a client-side run path or a tiny always-free backend (open decision).
- **Monsters/animations:** code-drawn SVG (by Fable). Owner: they "don't look good… should have legs,"
  and animations must sit **on the specific thing being acted on**. Likely needs a **real image/video
  generation tool** (available now), not hand-drawn SVG.
- **Scores corrected:** G4 (Autonomy) + G9 (Agency) were scored off proxies (lanes/beats/dept count) and
  showed 90/100 while the agentic layer is 0. Now **CAPPED at 30** in `goals_check.py` until a real
  conversation turn/artifact exists (the cap self-lifts on real evidence). Overall dropped ~76 → 62.
- **PRIORITY REORDER (proposed):** before adding more visual scope or the 2 new departments, make ONE
  real vertical work end-to-end — one engine call answers → one room actually debates → one artifact is
  produced in-app — and make the floor/rooms show only what's real. Pending owner Q (this session).

## M. OWNER DECISIONS + ROOT-CAUSE FIX — 2026-07-06 (Opus 4.8; hand this to Fable)
**Owner decided (4 questions):**
1. **Priority = MAKE ONE VERTICAL REAL FIRST.** Pause new visual scope + the 2 new departments until:
   an engine answers → one room runs real turns → one artifact is produced IN-APP → floor/rooms show
   ONLY real activity. Then resume the program.
2. **Monsters + animations = use a REAL image/video generation tool** (not code-drawn SVG). Regenerate
   ALL department monsters (lead/agent/worker, **with legs + full body + character**) as one cohesive
   cast, plus the 11 action animations, each placed **on the exact object being acted on**.
3. **Console = FULLY IN-APP.** No GitHub-issue page. Typing a task dispatches to an in-app queue and
   streams EXCAVA's reply in place (client-side run or a tiny always-free backend). Remove `_exIssue`
   as the primary send path.
4. **Visualization department goals** = owner's 3 (liveliness, info access, enjoyment) **+ clarity/
   legibility + speed/performance + accessibility**. (Consistency intentionally not added.)

**ROOT CAUSE of the M2 facade — FOUND + FIXED (2026-07-06, commit b47ffe0f):** the beat
(`python -m src.excava`, in `bulk_analyze.yml`) runs LAST in a job that already drained the Gemini
free-tier quota (analysis/links/news), and the beat step's env carried **only the 6 Gemini keys** — so
rooms hit HTTP 429 with **no fallback family** → `gemini:HTTPError` → 0 turns for 33 beats. Fix: added
the full pool (Groq/Cerebras/OpenRouter/NVIDIA/SambaNova/Mistral/GH-Models) to the beat step so rooms
fall through to fast, separate-quota engines. **PROOF PENDING:** the next CI run of `bulk_analyze.yml`
should show real agent turns in `data/excava/chats/**` and beat_log lines like "`<name> spoke (groq…)`".
If it still fails, run `engine_selftest.yml` and read which families answer.

**FABLE'S NEXT STEPS (in order):** (1) confirm the fix — after the next beat, verify rooms have real
turns + at least one artifact; if not, route chat explicitly to Groq/Cerebras in `pick_engine` and/or
run `engine_selftest.yml`. (2) Make the floor/rooms render ONLY real activity (no "working" without a
real turn/commit behind it). (3) Console fully in-app (decision 3). (4) Real-tool monster+animation
cast (decision 2). (5) THEN the 2 new departments (§J) + 2 pitch conditions + pitch-monster (§K).
Everything still: free-only, guardrails (`GUARDRAILS.md`), ship via `python -m src.git_safe ship`.

## N. AUTONOMOUS-OPERATION SPEC — 2026-07-06 (/loop; owner-decided; build via Fable across loop ticks)
DONE this session: `src/excava_backlog.py` (real-gap tasks + value bar + size score) wired into the beat;
`excava_beat.yml` cron → **every 10 min** (public repo = free, cloud, **no computer needed**; GH cron is
best-effort so timing ≈10 min).
- **≥30 CAPABILITIES (not tasks).** EXCAVA must be able to DO ≥30 distinct things. Fable drafts
  `data/excava/capabilities.json` + a dashboard "Capabilities" view; each tagged **live / planned /
  pitch-needed / gated-M5**, honestly (per §L audit). Owner reviews/tweaks.
- **Departments run INDEPENDENTLY — no cross-waiting, no task cap.** Each dept runs as many parallel
  tasks as it has real-gap work for (small/medium), sized honestly.
- **Size → WAR ROOM (owner resolution of the earlier "big waits" rule):** a genuinely HUGE task is not
  blocked — it converts to a **war room** (needs several departments, or all of one dept's agents at full
  capacity). Medium → an agent multitasks or one-agent-per-task (not on trivially small work). Only the
  5 pitch conditions pitch the owner.
- **GROUP CHAT = an open cross-agent space.** ANY agent can talk to ANY other agent across departments;
  agents **join/leave by relevance** to what's written and can **call another agent in**. War rooms live
  here as **scheduled meetings** — urgency sets the time (**critical = now, else the next daily slot**),
  with **full departments or representatives** for deep/important issues.
- **WAR ROOMS auto-open on a REAL cross-department need** (a task spanning 2+ depts): the relevant leads
  (+ EXCAVA-core as chair) or reps convene, produce a **shared committed decision artifact**, split the
  work back to departments.
- **FOCUS — two levels:** (a) a **per-department focus** EXCAVA auto-picks from that dept's biggest gap
  and **rotates**, shown on its floor station; (b) a **global self-improvement focus** for the whole
  system. (Focus originated as a self-improvement lever — keep both.)
- **DAILY SELF-IMPROVEMENT:** runs every day; **auto-applies + tests SAFE changes** (prompts, routing,
  schedules, focuses); **PITCHES** on the **5 conditions** — new tool · complete overhaul · deeper/outward
  access · **owner-only-high-leverage** (something only Eitan can add) · **new department**. Emits a daily
  digest (what changed + pending pitches). Never pitches for adding agents/employees — just notifies.
- **PACE = dizzying + honesty:** push hard, but **rate-aware backpressure** keeps it from fully crashing
  the 5 live engines (Gemini is 429-dead); when more speed needs more fuel, it files the **owner-only
  high-leverage pitch** (add free keys / bring OmniRoute online). Owner accepted "fast + tolerate some
  429 + pitch for fuel."
- **ROSTER:** bring every department to **4–6 agents** (add the missing improvers to the 7 three-agent
  depts). Per owner: adding agents is **notify-only, never a pitch**.



---

# ===== FILE: EXCAVA_SEPTEMBER_PLAN.md =====

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
