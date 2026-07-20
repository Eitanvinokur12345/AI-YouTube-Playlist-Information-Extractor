# EXCAVA — MASTER PROMPT (everything in place; paste into a fresh session) — 2026-07-15

This is the single, comprehensive prompt. It contains the core premise, current→desired map, the plan,
the guardrails for running on Eitan's PC, the full question bank, the loop, and the laws. A fresh
session pasted this has exactly what it needs to genuinely execute.

---

## A. CORE PREMISE (the thing that must be embedded — verify it is)
**EXCAVATORTRON = the HUB** — mined AI knowledge + ~8,311 elements incl. ~1,883 free open-source GitHub repos, Chinese tools, free utilities. **EXCAVA = an AGENT ORCHESTRA that GENERATES tools/projects** from Eitan's parameters by **orchestrating OTHER free/existing tools** (OpenCode / Claude Code on his existing Claude Pro = frontier quality at zero marginal cost) and **integrating the free OSS in the hub**. **Purpose: GENERATE projects/tools and assist Eitan's work. NOT for sale** — "sellable-grade" is only the *excellence bar*. **Ultimate goal: every component integrates perfectly — one connected system, nothing orphaned.**

## B. CURRENT STATE → DESIRED STATE (the gap this plan closes)
| Dimension | CURRENT (measured 2026-07-15) | DESIRED |
|---|---|---|
| **Memory/brain** | Fragmented: 3 graph files + memory_index; 2 modules orphaned; memory + history (663KB) + requests (82KB) siloed | ONE queryable brain, WIRED so agents read it at every decision |
| **Hub usability** | 8,311 elements but **0.8% runnable**, 25% stubs, 16% enriched; "100% verified" is a facade | Curated set fully enriched with real run/install info; honest usable-vs-stub labels |
| **Agents** | 619 rooms, ~0 turns, debate on 1 engine | 2–3 DIFFERENT brains that EXECUTE by orchestrating other tools |
| **Code health** | 97 modules, ~30 wired, **21 dead** | Lean fully-wired core; dead code deleted |
| **Frontend** | Static GitHub Pages, organic sprawl | Professional desktop-panels cockpit; everything visible |
| **Backend** | GitHub Actions batch job (no real server) | Real always-on host (Oracle VPS or Eitan's PC) running the orchestra |
| **Execution** | Approvals only; no real actions | Assistive generation of real tools/projects, visible as it works |
| **Visibility** | Features built but orphaned/invisible | Every feature wired + visible or it doesn't count as done |
| **Ultimate goal** | Sprawl of parts; "tasks complete, nothing changes" | A connected system that generates pro-grade tools for Eitan |
| **Marketability (hypothetical)** | Not a product; ~25–55/100 depending on focus/host/enrichment | If (only if) ever sold, it competes — used as the *quality bar*, not a goal |

## C. THE PLAN (integration-first)
- **Phase 0 — ONE BRAIN.** Merge memory + history + requests + the 3 graphs into ONE queryable brain, WIRED so agents read it every decision; visible in-app. *(No owner input.)*
- **Phase 1 — USABLE HUB.** Kill the "100% verified" facade; enrich ~25–50 top OSS repos with real run/install info; label usable-vs-stub honestly in-app. *(No owner input.)*
- **Phase 2 — ASSISTIVE GENERATOR (the product's heart — spec it, don't hand-wave it).** The engine pipeline: **(1) intake** Eitan's spec/parameters → **(2) decompose** into ordered steps → **(3) retrieve** the right elements/tools from the brain+hub per step → **(4) execute** via an adapter that drives OpenCode/Claude Code → **(5) verify** each step's output → **(6) sandbox** all OSS/generated code so his PC is never at risk → **(7) assemble + hand off** the finished tool, visible as it works, assist-first. Build ONE end-to-end generation before widening. *(Needs the PC/VPS host — see §E.)*
- **Phase 3+ — EXPAND** from the sorted backlog (the §G answers), one wired+visible piece per loop.

## D. LOOP PROTOCOL (each iteration)
1. Standing checks: git pull (quarantine-never-delete), engine canary, regression.
2. Advance the CURRENT phase by ONE increment that ends **WIRED + VISIBLE**. Never start a second thing before the first is visible.
3. Verify the READ side in a browser (number/screenshot) — never claim done from input alone.
4. Log WHY; ship ONLY via `python -m src.git_safe ship`.
5. Report with harsh 100% criticism of BOTH Claude and Eitan.
**Progress = "Eitan can do something new," never "a commit happened."**

## E. GUARDRAILS FOR RUNNING ON EITAN'S PC (established together — needs his explicit sign-off before autonomous host mode)
1. **Workspace jail** — EXCAVA reads/writes ONLY the repo + a dedicated `excava-workspace/` folder. Never system files, browser data, saved credentials, or personal documents.
2. **Command policy** — allowlist: python, node/npm, git *via git_safe only*, file ops inside the jail. BLOCK: `rm -rf` outside the jail, disk formatting, registry/system edits, anything requiring admin, any credential/keychain access.
3. **Network** — may fetch public repos/docs/APIs. NEVER upload Eitan's personal data anywhere; never post/publish/DM without approval.
4. **Money** — never spend, never enter payment info or passwords; ask Eitan to do those himself.
5. **Autonomy tiers** — tier-1 (safe) auto; tier-2 (self-code) only behind a passing test; tier-3 (new tools / anything outward) STOPS and asks Eitan. Standing PC mode keeps tier-3 owner-gated.
6. **Kill switch** — a `STOP` file (or one command) halts the beat immediately; Eitan can always stop it.
7. **Full audit** — every action logged to a visible in-app log Eitan can review.
8. **Git safety** — only `git_safe ship`; never force-push, never `git clean -fd`.
9. **Sandbox untrusted code** — any mined OSS or generated code runs in an isolated sandbox (container / jailed dir / disposable venv), never directly against his real environment. This is the safety spine of Phase 2, not an afterthought.
*Autonomous PC mode is OFF until Eitan says the guardrails are right and explicitly enables it.*

## F. DECONSTRUCTION MANDATE (Eitan's order — NOT a yes-man)
Challenge his assumptions with evidence, every step. Keep re-raising: (a) "integrate countless tools" vs "everything fits perfectly" — force a small deeply-integrated set first; (b) "generate pro tools" = autonomous software generation, the hardest unsolved AI problem — insist assist-first; (c) "free/pro-grade via OSS" needs enrichment first (0.8% runnable today); (d) "free" leans on his Pro sub + a real host. If evidence contradicts a preconception, say so plainly with the number.

## G. THE QUESTION BANK (~111 questions — the FULL text lives in `EXCAVA_MASTER_AUDIT.md`, Sections A–M)
**Do NOT use the index below as the questions — READ `EXCAVA_MASTER_AUDIT.md` and ask every one of its ~111 numbered items** as a CLICKABLE multiple-choice question, 4 per batch: one plain sentence of what it is; options **KEEP / FIX / IMPROVE / WIRE / REBUILD / BACKLOG / REMOVE** (each described); recommended verb FIRST as "(Recommended)". Save answers to `data/excava/overhaul_decisions.json`. Ask Section K first, then A→M. **Section M (the GENERATION ENGINE, items 100–111) is the product's missing heart — do not skip it.** The lines below are ONLY a one-line index for reference:

**K — strategic forks (first):** 90 Phase-0 proof capability (→ONE BRAIN) · 91 timeline? · 92 the one "now it's real" test?
**A — foundation:** 1 Oracle VPS→KEEP · 2 local Ollama→KEEP · 3 different-provider keys→IMPROVE · 4 OmniRoute→BACKLOG · 5 "buy Gemini Pro?"→REMOVE-worry · 6 in-app write→REBUILD · 7 keys-without-PC→KEEP(yes)
**B — identity:** 8 EXCAVATORTRON=HUB/EXCAVA=agents→KEEP · 9 one-product def→KEEP · 10 agentic-OS study→KEEP · 11 24/7→KEEP · 12 9 North-Stars→REBUILD(→2-3)
**C — hub/elements:** 13 element library→KEEP · 14 all 6 element types usable→IMPROVE · 15 activator→KEEP+IMPROVE · 16 OSS usable in-app not links→FIX · 17 more sources→IMPROVE · 18 multi-site extraction→BACKLOG · 19 newly-discovered+auto-promote→KEEP · 20 post-extraction verify→FIX · 21 HUB browser UI→REBUILD · 22 under-filled hub→IMPROVE
**D — agents/departments:** 23 Self-Improvement→REBUILD · 24 Power→KEEP · 25 Creators(assemble)→REBUILD · 26 Analysis→KEEP · 27 Security→IMPROVE · 28 Memory→KEEP · 29 Mining→KEEP · 30 News→KEEP · 31 Transcripts→KEEP · 32 Visual→BACKLOG · 33 Watch→KEEP · 34 Visualization dept→BACKLOG · 35 Accessibility dept→BACKLOG · 36 Links dept→REMOVE · 37 multi-model debate→REBUILD · 38 agents EXECUTE not debate→REBUILD · 39 dept hand-offs→BACKLOG · 40 conversations visible→FIX · 41 per-dept history→KEEP · 42 war-room/group-chat tabs→BACKLOG · 43 results in sentences→FIX · 44 all-convos-same-length→FIX · 45 open dept→see work→KEEP
**E — execution/checks:** 46 EXCAVA actually DOES actions→REBUILD · 47 self-improve more/bigger→IMPROVE · 48 Supervisor→KEEP · 49 Systemcheck→KEEP · 50 ≥10 guardrails→KEEP · 51 guardrail firing test→KEEP · 52 value>action-count→IMPROVE · 53 external missed-systems check→BACKLOG · 54 real dept executors→REBUILD
**F — interaction/governance:** 55 conversational EXCAVA executes→REBUILD · 56 clickable questions→KEEP · 57 pitch system→KEEP-simplify · 58 pitch detail→BACKLOG · 59 see designs w/o approving→KEEP · 60 ask at stages→KEEP · 61 harsh criticism→KEEP · 62 token-reduction ironclad→KEEP · 63 plan-first→KEEP · 64 new-session prompt→KEEP · 65 push-to-owner Telegram→BACKLOG · 66 teach-me (understand)→KEEP
**G — visual:** 67 full visual overhaul→BACKLOG · 68 desktop-panels cockpit→REBUILD(core) · 69 5 design versions→BACKLOG · 70 impeccable/de-generic→BACKLOG · 71 Arena "say what I like"→BACKLOG · 72 Obsidian+Graphify view→BACKLOG · 73 Yahoo-style readable→FOLD 68 · 74 massive intro→BACKLOG · 75 Fable 60%+→KEEP
**H — data brain:** 76 brain holds Q&A+problems+history→IMPROVE · 77 Obsidian brain fix→BACKLOG · 78 star/combined skills→BACKLOG · 79 link processors→BACKLOG
**I — multi-project/money:** 80 parent panel→BACKLOG · 81 monetization ad-skill→BACKLOG
**J — process/loop:** 82 weekly tutorial→BACKLOG · 83 drain transcripts+health.json→KEEP · 84 EXCAVA picks intervals→KEEP · 85 the ledger/list→KEEP · 86 retire "everything-first"→REMOVE · 87 8-min cadence→REBUILD · 88 recall+log-WHY→KEEP · 89 git_safe+quarantine→KEEP
**L — reality-driven:** 93 social source (mine_social orphaned)→WIRE · 94 social graph view→BACKLOG · 95 workflows→REBUILD · 96 integrations (MCP real)→BACKLOG · 97 visibility law→KEEP(enforce) · 98 delete 21 dead modules→REMOVE-dead/WIRE-wanted · 99 multi-brain agents→REBUILD

## H. LAWS
Free (via OSS + his existing Pro; never per-token billing). Everything operable IN THE APP. Real-not-facade. Ship only via git_safe; quarantine-never-delete. Recall-before-change + log WHY. Teach as you go. Retired: "fulfill EVERY request before anything new" → "one core, integrated + visible, then expand from the backlog."

## I. WHAT EITAN PROVIDES
Nothing to START (Phases 0–1 are pure integration of existing data). The ONE dependency is the **always-on host** — his PC (under §E guardrails) or the Oracle VPS — needed at **Phase 2**. Optionally: pick which OSS tools to enrich first, or approve a shortlist ranked by quality_score.

## J. FIRST MOVE
Management verdict → STEP-0 module inventory (tag 97 modules; delete 21 dead) → run §G question bank as clickable batches → begin Phase 0 (ONE BRAIN), one wired+visible increment → verify in browser → ship → criticize both. Then loop.
