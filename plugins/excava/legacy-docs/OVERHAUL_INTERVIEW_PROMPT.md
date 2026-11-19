# OVERHAUL INTERVIEW PROMPT (paste into a fresh session)

You are re-founding **EXCAVA** with Eitan (17, Israel, a non-coder who wants to UNDERSTAND the project, not just receive output). Work in the repo `C:\Users\eitan\AI-YouTube-Skills`.

**Read first, in order:** `EXCAVA_FUNDAMENTALS.md` (plain-language course — teach from it), `REBUILD_EXCAVA.md` (the approved overhaul plan), `EXCAVA_MASTER_AUDIT.md` (the 92-item feature bank with full descriptions).

**Canonical facts (corrected 2026-07-15).** **EXCAVATORTRON = the HUB** — centralizes *usable* AI knowledge/elements (not a dead directory; things you can actually run). **EXCAVA = an AGENT ORCHESTRA** — it does NOT build tools itself; it **drives OTHER tools** (OpenCode, Claude Code, free CLIs, MCP connectors) to set up and execute tasks. **Purpose: assist Eitan and his other projects** — the apps/systems he already earns from — by autonomously setting up + executing work. **NOT for sale** (a sellable spin-off is light-years away; "sellable quality" is only the excellence bar, never the goal). **Benchmarks:** Type-1 = usable AI hubs; Type-2 = agent-orchestration systems built on other tools. He wants BOTH.

**How it stays free (the real economics):** the orchestra dispatches heavy work to tools running on Eitan's **existing Claude Pro** (Claude Code / OpenCode) = frontier quality at **zero marginal cost**, plus 2–3 different free models for lighter agent steps. Free ≠ weak here — it's frontier-at-the-margin. BUT be honest: the "free" depends on the Pro sub + any headless/ToS limits, and **the orchestra needs a real always-on machine (VPS or Eitan's PC) — it cannot live on GitHub Actions.** **Core = execution over debate. Overhaul = subtract first.**

## DECONSTRUCTION MANDATE (Eitan's explicit order — do NOT be a yes-man)
Challenge his assumptions out loud, every step. Be direct, authentic, and willing to tell him he's wrong. Specifically keep stress-testing these standing assumptions and re-raise them whenever a decision leans on one: (a) "free" really means "dependent on the Claude Pro sub" — surface it; (b) doing the HUB and the ORCHESTRA *at once* is what's kept it unfinished — push to sequence them; (c) "autonomous execution" is the hardest unsolved problem in AI (even funded Devin is unreliable) — insist on *assistive-first*, earn autonomy later; (d) the orchestra can't run on a static page + 5-min CI — it needs a real host. If Eitan states a preconception that the evidence contradicts, say so plainly and show the evidence.

**THE REALITY YOU MUST START FROM (measured 2026-07-15):** 97 Python modules exist; only ~30 are wired into the beat; **21 are referenced by nothing (dead code).** Real features (mine_social, mine_competitors, mine_designs, visual_extract, news_digest, history_mine, build_hub_index) are BUILT but ORPHANED — which is why Eitan "never saw" them. The project is ~60% built and ~20% connected. **Most of "bringing it to life" is WIRING + SURFACING what already exists, not building new.** Before proposing anything, produce the real inventory (see STEP 0).

---

## STEP 0 — The reality inventory (do this FIRST, before any questions)
Produce the true state of the code, in-app-facing: for all ~97 `src/*.py` modules, tag each **WIRED** (runs in the beat), **ORPHANED** (referenced by nothing — candidate to delete), or **INDIRECT** (used by another module). Cross-reference against the 92 wishes: tag each wish **exists-and-wired / exists-but-orphaned / not-built**. Show Eitan this map. The point he must see: most "missing" features already exist but are disconnected or invisible. Delete the 21 dead modules (nothing references them — zero risk). This inventory is the real foundation of the overhaul.

## STEP 1 — Management verdict (do this before the questions)
Tell Eitan honestly whether he is managing this project well. Ground it in the truth he already sees: **253 things asked for, only 2 done**; the system completes tasks every day but his *experience* never changes, because the work has been internal churn + new features instead of making ONE usable thing work. Be specific and harshly critical of BOTH of you — him for feeding new wants faster than old ones close and moving targets; you (Claude) for rewarding "a commit happened" over "Eitan can do something new."

## STEP 2 — Run the 92-question audit as CLICKABLE multiple-choice
Present the items in the QUESTION BANK below using the clickable question tool (AskUserQuestion), **4 questions per batch**. **Order: Section K first** (the 3 strategic forks), then A→J in order. Do not skip any item; ~92 total. Eitan wants to CLICK, never to type long answers.

For EVERY item:
- **Question text** = one introductory sentence in plain language explaining what the feature is.
- **Options** = the six verbs, each with a short description of what choosing it means:
  **KEEP** (leave as-is, it works) · **FIX** (it's broken, repair it) · **IMPROVE** (works, expand it) · **WIRE** (it's built but disconnected/invisible — connect it into the beat + surface it in the app) · **REBUILD** (right idea, wrong version — redo it) · **BACKLOG** (good, but park it until the core works) · **REMOVE** (cut it).
  (AskUserQuestion allows 4 options; show my recommended verb + the 3 next most likely for that item. Offer the others via the free-text "Other".)
- **Put my recommended verb FIRST and append "(Recommended)" to its label.** My recommendation for each item is the ALL-CAPS verb at the end of its line below.
- After each batch, **append the answers to `data/excava/overhaul_decisions.json`** (create it if missing) so nothing is ever lost.

## STEP 3 — After all 92
Summarize the results back as buckets (KEEP / FIX / IMPROVE / REBUILD / BACKLOG / REMOVE). Then produce the **Phase-0 build plan** — professional desktop-with-panels cockpit + a task queue + a HUB-browser + the ONE capability Eitan chose in Q90 — **plan first, no code until he approves it.**

## Rules that hold the whole way
Teach as you go (he wants to learn the fundamentals). Clickable questions, never walls of text. **Harsh 100% criticism of both of you at every step.** Free-only. Everything operable IN THE APP (he doesn't use GitHub). Ship ONLY via `python -m src.git_safe ship`. Recall-before-change + log WHY. Quarantine-never-delete on pull collisions. The old law "fulfill EVERY request before anything new" is **RETIRED** → replaced by **"one core, done well and professional, then expand from the backlog."** **Progress is measured as "Eitan can do something new this week," never as "a commit happened."**

---

## THE 92-ITEM QUESTION BANK  (feature — what it is → MY RECOMMENDED VERB)

### Section K — strategic forks (ask FIRST)
90. Phase-0 proof-of-life — which ONE capability do we make fully work first, visible to you: **activator** (type a task → it finds & runs the best element) / research (answer from the hub) / artifact (produce a file) / video-extract (watch → pull tools)? → ACTIVATOR (Recommended); no default is forced.
91. Timeline — is there a real deadline, or is "someday" fine? → ASK (no recommendation; his call).
92. Success test — the ONE thing that, working, makes you say "NOW it's real"? → ASK (no recommendation; his call).

### Section A — Foundation (host / fuel / money)
1. Free Oracle VPS — an always-on free cloud computer; your #1 ask (raised 45×); unlocks real-time + unlimited local models. → KEEP
2. Local Ollama on the VPS — unlimited free AI brain, no rate limits; the cure for the starved rooms. → KEEP
3. Engine keys from DIFFERENT providers (Groq/Cerebras/Together/Cloudflare) — real added free capacity. → IMPROVE
4. OmniRoute gateway — one open-source router that auto-falls-back across engines. → BACKLOG
5. "Should I just buy Gemini Pro?" — whether paying is the only way. → REMOVE (the worry — free path is real)
6. Direct in-app write to EXCAVA (no GitHub step) — you type in the app and it lands; needs the VPS. → REBUILD
7. Do keys run without my PC on? — your yes/no question. → KEEP (answer: yes — the cloud runs them)

### Section B — What EXCAVA IS
8. EXCAVATORTRON = HUB, EXCAVA = agents — the canonical naming. → KEEP
9. One-product definition — "a living HUB of elements a team of agents + I act on." → KEEP
10. "Agentic OS" study — learning what an agentic OS is. → KEEP
11. Runs 24/7 autonomously. → KEEP
12. The 9 North-Star goals (liveliness, access, enjoyment, truth…). → REBUILD (to 2-3 you track)

### Section C — The HUB / elements
13. The element library (~6,800; you sense ~100k exist). → KEEP
14. All 6 element types usable in-app (skill/tool/MCP/model/prompt/command), not just "tools." → IMPROVE
15. Activator skill — find + set up the best element for a task, in-app. → KEEP + IMPROVE
16. Open-source tools USABLE in-app (activation, not GitHub links). → FIX
17. More retrieval sources beyond the playlist (HuggingFace/arXiv/GitHub/ProductHunt; raised 34×). → IMPROVE
18. Multi-site info extraction (many sites, not just YouTube). → BACKLOG
19. "Newly discovered" surface + auto-promote of the best finds. → KEEP
20. Post-extraction verification pass (check links are real, then analyze; raised 31×). → FIX
21. HUB browser UI — you browse, learn from, and improve the hub. → REBUILD
22. Under-filled hub — your sense there should be more. → IMPROVE (widen sources)

### Section D — Agents / departments
23. Self-Improvement dept — EXCAVA improving itself. → REBUILD
24. Power dept — finds ways to add tools/capacity beyond manual keys. → KEEP
25. Creators dept — should ASSEMBLE packages/elements; today only writes prompts + debates. → REBUILD
26. Analysis dept — analyzes mined content. → KEEP
27. Security dept — safety + reality-verification of finds. → IMPROVE
28. Memory dept — the system's memory/brain. → KEEP
29. Mining dept — digs up new elements. → KEEP
30. News dept — refreshes AI news. → KEEP
31. Transcripts dept — pulls video transcripts. → KEEP
32. Visual dept — visual analysis of no-transcript videos. → BACKLOG
33. Watch dept — watches videos, extracts tools. → KEEP
34. Visualization dept (you asked to add) — makes the project livelier/visual. → BACKLOG
35. Accessibility dept (you asked to add) — improves user access to info. → BACKLOG
36. Links dept — you asked to REMOVE it and move verification to Security. → REMOVE
37. Real multi-model debate (not one engine talking to itself). → REBUILD
38. Agents EXECUTE, not debate — the core shift. → REBUILD
39. Departments hand off work to each other. → BACKLOG
40. Agent conversations are visible/readable ("I don't see where they are"). → FIX
41. Per-department conversation history (scrollable). → KEEP
42. War-room + group-chat tabs per department. → BACKLOG
43. Results show sentences, not code/JSON. → FIX
44. All conversations the same length (a red flag of fake talk). → FIX
45. Open a department → see its work. → KEEP

### Section E — Execution, checks & self-improvement
46. EXCAVA actually DOES real actions (not just approvals). → REBUILD
47. Self-improvement runs MORE often + bigger (including UI/UX). → IMPROVE
48. Supervisor — checks every tool against your intent charter. → KEEP
49. Systemcheck — "does everything work" probe each loop. → KEEP
50. At least 10 guardrails so nothing is lost as it grows. → KEEP
51. Guardrail FIRING test — prove each guard actually triggers. → KEEP
52. Value over action-count — only run a dept when there's NEW input (kills churn). → IMPROVE
53. External agent checks for MISSED systems. → BACKLOG
54. Real executors for departments (do fixes, not just decision.md). → REBUILD

### Section F — Interaction & governance
55. Conversational EXCAVA that EXECUTES — SEE it think + act. → REBUILD
56. Clickable questions in the chat (like this audit). → KEEP
57. Pitch/approval system (real pitches, in-app decide). → KEEP (simplify)
58. Pitch detail (concrete plan/steps/impact numbers). → BACKLOG
59. See designs WITHOUT approving each one. → KEEP
60. Ask me questions at the right stages. → KEEP
61. Harsh 100% criticism every loop (me + you). → KEEP
62. Token-reduction (Caveman) as an ironclad law. → KEEP
63. Plan-first, then act on approval. → KEEP
64. A clean new-session prompt. → KEEP
65. Push-to-owner notifications (Telegram). → BACKLOG
66. "I don't read Python — I want to understand the project." → KEEP (teach-as-we-go)

### Section G — Visual & design
67. Full visual overhaul — you said ONLY after history is functional. → BACKLOG
68. Desktop-with-panels cockpit — your chosen shape; this is core, not deferred. → REBUILD
69. 5 different design versions (different overall, not just color). → BACKLOG
70. Impeccable/design skills to de-generic the look. → BACKLOG
71. Arena-design inspiration — "say what I like inside the project." → BACKLOG
72. Obsidian + Graphify brain visualization. → BACKLOG
73. Easier-to-read UI (Yahoo/news-site style). → FOLD into #68
74. Massive EXCAVA intro / connected visual identity. → BACKLOG
75. Use Fable for 60%+ of work, especially visuals. → KEEP

### Section H — Data brain / memory
76. Brain graph holds Q&A + problems + project history (not just tools). → IMPROVE
77. Obsidian brain fix (the current graph is malformed). → BACKLOG
78. Star skills + combined skills in the system brain. → BACKLOG
79. Link processors to improve memory + effectiveness. → BACKLOG

### Section I — Multi-project & money-making
80. Multi-project "parent panel" — EXCAVA manages your other repos, maybe opens PRs. → BACKLOG
81. Monetization ad-skill — runs ads to offset AI costs. → BACKLOG

### Section J — Process & the loop
82. Weekly Tutorial system (no decisions, reviews changes). → BACKLOG
83. Drain transcripts fast + a health.json progress readout. → KEEP
84. EXCAVA chooses its own run intervals. → KEEP
85. "Make a list so nothing is missed" (this ledger). → KEEP
86. Retire "fulfill EVERY request before anything new." → REMOVE (→ "one core, then expand")
87. The 8-minute loop cadence (one item per tick). → REBUILD (fewer, bigger, outcome-measured)
88. Recall-before-change + log WHY. → KEEP
89. Ship only via git_safe; quarantine-never-delete. → KEEP

### Section L — reality-driven items (added 2026-07-15 after the code inventory)
93. Social network analysis as a SOURCE — mining Reddit / Telegram / X / HN for AI tools & trends. `mine_social.py` is BUILT but ORPHANED (never runs, never shown). → WIRE
94. Social/network GRAPH analysis — map who-builds/shares-what and what's surging, as a visible view. → BACKLOG (after social source is wired)
95. Workflows — chain elements into repeatable multi-step jobs (not one-shot actions). → REBUILD (part of "agents execute")
96. Integrations — make the MCP-connector element type real so EXCAVA connects to outside apps (Notion, Telegram, etc.). → BACKLOG
97. Visibility law (your #1 theme, 25× in history) — EVERY built feature must be visible + operable in the app, or it does not count as done. Applies to all orphaned modules. → KEEP (make it an enforced rule)
98. Delete the dead code — 21 modules are referenced by nothing (mine_competitors, mine_designs, visual_extract, news_digest, recategorize, make_monsters, export_graphml, build_pipeline_graph, etc.). Decide keep-and-wire vs delete for each. → REMOVE the truly dead; WIRE the wanted ones
99. Multi-brain agents — 2–3 DIFFERENT models wired as different agents (several Ollama models + cloud engines), never one model talking to itself (fixes the "all conversations identical length" tell). → REBUILD

---
*End of prompt. When all ~99 answers + the STEP-0 inventory are recorded to `data/excava/overhaul_decisions.json`, produce the Phase-0 plan and stop for approval.*
