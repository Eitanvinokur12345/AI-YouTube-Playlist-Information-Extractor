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
  come **free through OpenRouter**. Confirm live set by running `engine_selftest.yml`.
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

## H. NEXT
A **design-only interview** before M3 (your choice), and O1–O8 mockups **after** this program is
finalized. This doc is the finalized answer-set; PLAN + STEPS unchanged.
