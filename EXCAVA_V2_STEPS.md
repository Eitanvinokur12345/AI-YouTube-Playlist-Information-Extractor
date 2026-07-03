# EXCAVA v2 — STEP-BY-STEP EXECUTION PLAN (the "do" doc)

_Companion to `EXCAVA_V2_PLAN.md` (the "why"). Every task = **Build** (files/what) + **Done when**
(acceptance). Order is strict within a milestone. Fable does everything except tasks tagged
**[OPUS]**. Every task: recall-before-change, log the WHY, obey `PROTOCOLS.md`, free-only.
Tasks marked **[OWNER]** need an action from Eitan (a key, a decision) — they never block; the
lane around them proceeds and lights up when done._

**Milestone order (depth-first, Eitan's):** M1 real/verified elements + access → M2 real agents
conversing + producing → M3 new shell + launcher + full design → M4 activator end-to-end →
BREADTH. Each milestone ends by bumping `APP_BUILD`+`sw.js`, writing a `tutorials.json`
walkthrough, verifying in preview, and committing.

---

## M1 — REAL / VERIFIED ELEMENTS + ACCESS
_Goal: nothing on any tab is dead or fake, and you can actually open/run/use every element._

**M1.0 — Unified element model.**
Build: `data/schema/element.json` (fields: `id,type,name,what,source_videos[],source_url,links{website,github,open_code},install,verified{status,method,at,log},trust,related[],video_bundle[],created_by`). `src/element_model.py`: `load_elements()` normalizes every per-type file (tools/skills/connectors/prompts/commands/formats/designs/news) into Element dicts → writes read-only `data/elements_index.json`; `set_field(id,field,val)` writes back to the owning file only.
Done when: `python -m src.element_model --count` prints per-type totals + one normalized sample; no source file is mutated except via `set_field`.

**M1.1 — Finish connector sandbox verification (all 1,142).**
Build: keep `verify_connectors.yml` (6-hourly, 30/batch, tree-kill fix); add `--catchup 60`; add an npm+pip preflight that marks `sandbox-unavailable` cleanly if a runtime is missing.
Done when: `data/connectors_verified.json.summary.checked == total` (every connector has pass/fail/unresolvable/sandbox-unavailable).

**M1.2 — Verify ALL element types, not just connectors.**
Build: `src/verify_elements.py` — URL/repo → parallel HEAD liveness (thread pool); MCP/repo → reuse the sandbox runner; skills/prompts/formats → schema + content sanity + `security_preflight`. Writes `data/elements_verified.json` keyed by element id. New `verify_elements.yml` (6-hourly).
Done when: every element carries `verified{status,at}`; a verified badge is derivable for any element.

**M1.3 — Trust gate + "dead only" pruning (P3 safety).**
Build: join `source_trust.json`; below-floor items need full verification before "verified"; set `status ∈ verified|unverified|niche|dead`; **only** `dead` (link+install+sandbox all fail) is hidden by default. Never delete for low rating.
Done when: a low-rated-but-working niche element stays visible; only truly dead ones hide; a report lists counts per status.

**M1.4 — The per-card ACTION ROW.**
Build: `docs/dashboard.js` `elementActions(el)` → **Activate** (emit setup recipe + copy now; real setup wired in M4), **Open** (github.dev / Codespaces / hosted MCP — a real runnable target), **Use for a task** (opens EXCAVA console prefilled), **Video** (source video), **Video bundle** (same-topic set), **Source** (original url). Render on every card + the detail view.
Done when: every card shows the row; Open opens a genuinely runnable target; Video plays the source; Use routes to the console.

**M1.5 — The <10s pre-warm / open system.**
Build: `src/prewarm.py` beat-step keeps top-N (use×trust) repos/MCP warm: repos → pre-resolve the github.dev/Codespaces URL + cache readiness; MCP → pre-fetch install to CI cache / Pi. `data/prewarm.json` = warm list + state. Open button: warm → instant; cold → the pancake-warming animation + progress, ready <10s.
Done when: opening a warm element is instant; a cold one resolves in <10s (timed in preview).

**M1.6 — Element DETAIL view.**
Build: `renderElement(id)` route `#element/<id>`: what it is, embedded source video/bundle, how-to, verified status, the action row, related elements (M1.7), use-for-a-task.
Done when: any element opens a fully-populated detail page.

**M1.7 — RELATE (related rows).**
Build: `src/relate.py` — related elements per element from shared memory-graph topics + same source video + co-occurrence; write `related[]` into `elements_index.json`. (Graph UI = M3.9.)
Done when: each detail view shows 3–8 real related elements.

**M1.8 — Dashboard reads the unified index.**
Build: cards/badges/tabs read `elements_index.json`; per-type tabs preserved.
Done when: all tabs render from the unified index with verified/trust badges; no console errors.

**M1.9 — Ship M1.**
Done when: M1 tutorial in `tutorials.json`; `APP_BUILD`+`sw.js` bumped; preview-verified; committed.

---

## M2 — REAL AGENTS CONVERSING + PRODUCING
_Goal: agents get real engines and their work is a visible conversation that produces artifacts._

**M2.0 — `PROTOCOLS.md` + self-audit.**
Build: write `PROTOCOLS.md` (P1–P14, the file agents read). Extend the beat `_audit_spine()` to verify PROTOCOLS.md presence + key rule strings; any drift → SAFE mode.
Done when: beat prints "audit OK vs PROTOCOLS.md"; deleting a protocol line trips SAFE mode.

**M2.1 — The engine layer.**
Build: `src/excava_engines.py` — `Engine` adapters for Gemini (existing 8 keys, rotated), Groq, Cerebras, OpenRouter; `complete()/chat()`; `pick_engine(dept,difficulty)` = fast-first (Cerebras/Groq) → Gemini for grounded/hard; graceful skip if a key is absent.
Done when: `python -m src.excava_engines --selftest` returns a real completion from every configured engine.

**M2.1a — [OWNER] Add free engine keys.**
Build: Eitan adds `GROQ_API_KEY`, `CEREBRAS_API_KEY`, `OPENROUTER_API_KEY` to repo secrets (all free, no card). Documented in `PROTOCOLS.md`.
Done when: the three secrets exist; selftest shows 4 engine families live. (Until then, Gemini-only path runs.)

**M2.2 — Lease arbiter + budgets.**
Build: `src/excava_leases.py` — per-department daily token budget (`data/excava/budgets.json`), `acquire/release`, hard ceilings, per-engine RPM caps; integrate into engines.
Done when: a department at budget is held+traced, never overspends; nothing can cost money.

**M2.3 — Redefine the agent roster (3–5/department, specialty+role).**
Build: rewrite `data/excava/agents.json` — per department 3–5 agents `{id,name,engine,specialty,role∈doer|checker|improver,tier}` (~40 agents); named lead personas.
Done when: `python -m src.excava_agents --roster` prints the full cast with engines+roles; registry validates.

**M2.4 — Agents vs workers.**
Build: persistent AGENTS spawn ephemeral WORKERS for subtasks (temp id → one unit → report → dissolve); `state.json` tracks live workers.
Done when: a task shows an agent dispatching N workers that finish and vanish, all traced.

**M2.5 — The conversation engine.**
Build: `src/excava_chat.py` — `Room(kind∈dept|cross|group|war,id,goal,max_turns,done_criteria)`; `post(agent,text,engine)`; agents take turns via real engine calls; messages → `data/excava/chats/<YYYY-MM-DD>/<room>.jsonl` (by-day). Message = `{agent,engine,at,text}`.
Done when: a dept room runs a real multi-turn conversation (real engine calls) ending on its done-criteria; archived by day; replayable.

**M2.6 — Conversations produce artifacts.**
Build: a room ends by calling a scoped department tool (resolve-links batch / draft an element / assemble a package); the artifact is committed and linked from the transcript.
Done when: one war room end-to-end produces a real committed artifact you can open.

**M2.7 — Wire conversations into the beat (24/7 + live, parity).**
Build: each beat advances top rooms (bounded turns); dashboard-open runs more turns in-browser via the same engines; identical code path offline/online.
Done when: rooms progress every CI beat unattended; opening the dashboard accelerates them; output is identical either way.

**M2.8 — Self-improvement department (real, "every crevice").**
Build: `src/excava_selfimprove.py` — agents review agent-prompts, engine choice, routing, hub content, and its own code; safe changes auto-apply+test; overhaul/new-tool/deeper-access → a PITCH (P5); log `data/excava/improvements.jsonl`.
Done when: it makes ≥1 real safe self-improvement (e.g., re-tunes an agent prompt after a bad result) and files ≥1 pitch, both visible.

**M2.9 — Ship M2.** Done when: tutorial + build bump + preview-verified + committed.

---

## M3 — NEW SHELL + LAUNCHER + FULL DESIGN  (all Fable)
_Goal: it looks and feels like a real, professional product, and the living workshop is real._

**M3.0 — Design system.**
Build: `docs/design/tokens.css` (color tokens, type scale = bold display + clean body, spacing grid) + component primitives (button/card/badge/chip/panel) + a gallery page. Produce via real design tools (Figma/Adobe MCP) — test free-first, only escalate if quality demands.
Done when: tokens + gallery render; **[OWNER]** picks a palette from 3 samples.

**M3.1 — The app shell.**
Build: new `docs/index.html` — left sidebar (departments/tabs) + top bar (global search, EXCAVA, account/settings/shortcuts); migrate all tabs in; refined Heavy Machinery.
Done when: sidebar+topbar+search work; feels like a real product; zero console errors.

**M3.2 — Monster art.**
Build: 11 department species + agent/lead(suit-and-tie)/worker(smaller,generic) variants via image-gen (free-first), consistent set → `docs/assets/monsters/`.
Done when: 11 distinct species exist; leads and workers visually distinct.

**M3.3 — Isometric factory floor.**
Build: `docs/floor/` — isometric floor, per-department stations/buildings, monsters walking, wired to real bus/room state; click a station → that department.
Done when: the floor reflects real activity; stations open departments.

**M3.4 — Animation catalog.**
Build: ~11 animations (fix=weld, build=hammer, test=magnifier, verify=stamp, deliver=celebrate, research=dig/scan, make-media=film, hand-off=carry parcel, pitch/stuck=wave, idle=rest, open=pancake-flip), each triggered by the real action.
Done when: every action type plays its distinct animation from real events.

**M3.5 — Messenger chat UI.**
Build: department channels rail; bubbles with monster avatars + "agent · engine" badges + day dividers; war-room round-table view; open-room hall view; reads the by-day archive.
Done when: you read any room's real conversation, scroll by day, see who+engine per message.

**M3.6 — Element card + detail (final visual).**
Build: apply the design system to M1 cards/detail; compact card, actions on hover, verified/free/engine badges.
Done when: cards match the system; actions reveal on hover.

**M3.7 — Results feed.**
Build: feed filterable by day / department / sub-agent; result card = what/preview/open/use/send-to-project; also inline in the making-chat + a "new" badge on the element's tab.
Done when: real artifacts appear, attributed, openable, in all three places.

**M3.8 — North-Star constellation.**
Build: Excavatortron centered; 9 goal-stars orbit (rotating), each distinct, meaning below; live scores from `goals_status.json`.
Done when: constellation shows live scores; each star opens its goal.

**M3.9 — Brain graph (relate, full).**
Build: interactive element+link graph (from M1.7); click to explore; build a package from a cluster.
Done when: graph is navigable; a cluster → a package.

**M3.10 — Direct EXCAVA chat (console + floating).**
Build: `#excava` console (talk to EXCAVA, dispatch tasks, opens with the away-digest) + a context-aware floating quick-ask on every tab; engine-backed replies; tasks → bus.
Done when: typing a task dispatches it and EXCAVA replies; floating ask works on any tab.

**M3.11 — Steering (direction, pitches, notifications).**
Build: direction card (state → EXCAVA's reading); dismissible "needs your approval in ___" banner on open; bell+count; a monster walks up on new approvals; pitches as conversations.
Done when: a pitch shows the banner, opens as a conversation, approve/decline works.

**M3.12 — Mobile pass.**
Build: responsive shell — read/review/approve/send on phone; execution buttons disabled on phone.
Done when: phone shows chats/results/approvals + send; no run buttons.

**M3.13 — Ship M3.** Done when: tutorial + build bump + preview-verified + committed.

---

## M4 — ACTIVATOR END-TO-END + LAUNCHER
_Goal: know→do works anywhere; EXCAVA is proven real by agency + goal→package._

**M4.1 — [OPUS] Build the portable activator.**
Build: `src/build_activator.py` → `activator/SKILL.md` — compressed hub snapshot (elements index + package recipes + PROTOCOLS + triggers) AND a live-EXCAVA fetch path; obeys NOSG/HORSE/PLAN/RESEARCH/WATCH; executes an uploaded task offline from the snapshot; daily rebuild workflow.
Done when: uploaded to a second tool, it finds/builds a package and runs a task; NOSG/HORSE/PLAN behave correctly; works offline.

**M4.2 — HORSE execution.**
Build: `src/horse.py` — fan out 10 agents (varied engines) that each fully execute the goal; merge best-of-**results** tuned to Eitan's taste weights.
Done when: `HORSE <goal>` returns one merged artifact assembled from 10 real executions.

**M4.3 — Packages: build / edit / save / reuse.**
Build: `data/packages.json` — build-on-request + editable + auto-suggested-from-reuse; pin frequent ones; kit UI (open → run each/all); reusable by Eitan and EXCAVA.
Done when: you assemble → pin → later reuse a package in one click.

**M4.4 — Parent launcher.**
Build: `launcher/` — clean centered project-cube grid (yellow-but-white-clean); each cube opens the project's own app (per-project open target); EXCAVA-created projects auto-appear.
Done when: launcher lists Excavatortron + your projects; each opens its full app; a new EXCAVA-made project shows up.

**M4.5 — Hub-as-database for projects.**
Build: `hub_api.json` / an endpoint + the activator as carrier so Budoaris/FreeDup can pull elements/packages.
Done when: another project pulls a package from the hub via the activator or endpoint.

**M4.6 — Ship M4 + prove "EXCAVA is real".**
Done when: (a) agents build a real artifact overnight unattended, AND (b) you type a goal → get a working package you actually use — both demonstrated; tutorial + build bump + committed.

---

## BREADTH (after M1–M4) — finish the rest
- **B1** Finish the 52 goals per §9 order; North-Star scores all 9 each cycle.
- **B2** Omni-source tiers 2–3 (WhatsApp export lane; opt-in locked feeds only if D6 flips).
- **B3** Per-tab self-improvement + the meta-brain of all history.
- **B4** Portability (`PORTABLE_HARNESS.md`): make the spine importable for Budoaris first if Eitan asks.
- **B5** Cleanup: formats filter in Designs; brain white-node + title-collision fix; split token-reduction into 2 skills.
- **B6** EXCAVA-as-MCP-server (expose the hub to other agents).

## OPEN DECISIONS → mockup tasks (Fable mocks, Eitan picks; defaults noted)
- **O1** palette (3 samples) · **O2** the 11-monster cast · **O3** fonts (2–3 pairings) · **O4** first-run tour (default: helpful empty states, tour optional) · **O5** war-room round-table scene (default: illustrate, not video, unless free tools fall short) · **O6** notification sound (default: off) · **O7** Cmd-K command palette (default: add) · **O8** floor station shapes.

---
_Living doc. ~55 named tasks over the 4 milestones + breadth + mockups = the 150–200 concrete
pieces the interview implied. Reopen any thread; every step traces to the interview and to
`project-excava-direction-2026-07` in memory._
