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
