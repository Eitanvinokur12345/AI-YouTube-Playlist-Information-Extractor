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
