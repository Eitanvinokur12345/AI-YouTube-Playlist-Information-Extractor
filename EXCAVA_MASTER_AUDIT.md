# EXCAVA — Master Audit & Decision Prompt (built from your 253-item history, 2026-07-15)

**Purpose:** decide the fate of *every* feature you've ever asked for, so the overhaul keeps what
matters, cuts the rest, and produces ONE finished, standing-on-its-own product. Read
`EXCAVA_FUNDAMENTALS.md` first if any word is fuzzy.

**Why this exists:** your history ledger holds **253 things you've asked for — only 2 are marked
done.** The system completes tasks daily but your experience doesn't change, because the work has
been *internal churn + new features* instead of *making one thing you can use work*. This audit ends
that. We decide, we cut, we focus.

---

## How to answer

Each item = **what it is** + **my recommendation**. Pick one verb per item:

- **KEEP** — leave as-is, it works.
- **FIX** — it's broken; repair it.
- **IMPROVE** — it works but expand/upgrade it.
- **REBUILD** — the idea is right, the current version is wrong; redo it.
- **WIRE** — it's already built but disconnected/invisible; connect it into the beat + surface it in the app.
- **BACKLOG** — good, but not now; park it until the core works.
- **REMOVE** — cut it entirely.

Answer by writing e.g. `12: rebuild` — or tell Claude **"run the audit as clickable buttons"** and it
will present these 4-at-a-time as click options. Add a note anytime to say *why*.

---

## SECTION A — The foundation (host, fuel, money) — *nothing works well until this is settled*

1. **Free Oracle VPS (24/7 backend)** — an always-on free cloud computer; your #1 ask, raised 45×. Unlocks real-time + unlimited local models. → *Rec: KEEP (do it — the single biggest unlock).*
2. **Local Ollama on the VPS** — unlimited free AI brain, no rate limits, the cure for the room starvation. → *Rec: KEEP.*
3. **More engine keys from DIFFERENT providers** (Groq/Cerebras/Together/Cloudflare) — free capacity that actually adds up (unlike 6 Gemini keys sharing one quota). → *Rec: IMPROVE (add 2-3).*
4. **OmniRoute free gateway** — one open-source router that auto-falls-back across engines so outages don't freeze rooms. → *Rec: BACKLOG (nice, but Ollama matters more first).*
5. **"Should I just buy Gemini Pro?"** — you asked if paying is the only way. → *Rec: REMOVE the worry (free path via VPS+Ollama is real; don't pay).*
6. **Direct in-app write to EXCAVA (no GitHub step)** — you type in the app and it lands, no GitHub. Needs the VPS. → *Rec: REBUILD (async now, real-time after VPS).*
7. **API keys working "offline / without my computer on"** — your question whether keys run without your PC. → *Rec: KEEP the answer (yes — the cloud beat/VPS runs them, not your PC).*

## SECTION B — What EXCAVA IS (identity)

8. **EXCAVATORTRON = HUB, EXCAVA = agents** — the canonical naming you corrected. → *Rec: KEEP (lock it everywhere).*
9. **One-product definition** — "a living HUB of elements a team of agents + I act on." → *Rec: KEEP (this is the spine).*
10. **"Agentic OS" study** — you wanted to learn what an agentic OS actually is. → *Rec: KEEP (done in FUNDAMENTALS; extend on request).*
11. **Runs 24/7 autonomously** — the OS should never stop working. → *Rec: KEEP (real after VPS).*
12. **The 9 North-Star goals** — liveliness, user access, enjoyment, truth, etc. → *Rec: REBUILD (collapse to 2-3 you actually track).*

## SECTION C — The HUB / EXCAVATORTRON (elements & sourcing)

13. **The element library (~6,800, you said ~100k exist)** — the collected abilities. → *Rec: KEEP (the moat).*
14. **All 6 element types usable** (skill/tool/MCP/model/prompt/command) — not just "tools." → *Rec: IMPROVE (make each type actually usable in-app).*
15. **Activator skill** — find + set up the best element for a task, in-app (not a GitHub link). → *Rec: KEEP + IMPROVE (this is close to your core).*
16. **Open-source tools USABLE in-app (activation, not links)** — raised repeatedly; you don't touch GitHub. → *Rec: FIX (many are still just links).*
17. **More retrieval sources beyond the playlist** (HuggingFace/arXiv/GitHub/ProductHunt) — raised 34×. → *Rec: IMPROVE.*
18. **Multi-site info extraction** (YouTube + other sites) — pull knowledge from many places. → *Rec: BACKLOG (after core).*
19. **"Newly discovered" surface + auto-promote** — new finds staged, best ones auto-added. → *Rec: KEEP.*
20. **Post-extraction verification pass** (check links are real, then analyze) — raised 31×. → *Rec: FIX (fold into Security).*
21. **HUB browser UI (view + learn from the hub)** — you browse, learn, improve. → *Rec: REBUILD (make it genuinely browsable/teachable).*
22. **"~100k elements — there must be more/other things"** — your sense the hub is under-filled. → *Rec: IMPROVE (widen sources).*

## SECTION D — The agents / departments (EXCAVA)

23. **Self-Improvement dept** — EXCAVA improving itself. → *Rec: REBUILD (measure success → fix top failure).*
24. **Power dept** — finds ways to add tools/capacity beyond manual keys. → *Rec: KEEP.*
25. **Creators dept** — should ASSEMBLE packages/elements; today only writes prompts + debates. → *Rec: REBUILD (make it actually create).*
26. **Analysis dept** — analyzes the mined content. → *Rec: KEEP.*
27. **Security dept** — safety + (new) reality-verification of finds. → *Rec: IMPROVE.*
28. **Memory dept** — the system's memory/brain. → *Rec: KEEP.*
29. **Mining dept** — digs up new elements. → *Rec: KEEP.*
30. **News dept** — refreshes AI news. → *Rec: KEEP (as a background service).*
31. **Transcripts dept** — pulls video transcripts. → *Rec: KEEP.*
32. **Visual dept** — visual analysis of no-transcript videos. → *Rec: BACKLOG (Gemini-quota-gated).*
33. **Watch dept** — watches videos, extracts tools. → *Rec: KEEP.*
34. **Visualization dept** (you asked to add it) — makes the project livelier/visual. → *Rec: BACKLOG (part of the visual overhaul).*
35. **Accessibility dept** (you asked to add it) — improves user access to info. → *Rec: BACKLOG.*
36. **Links dept** — you asked to REMOVE it and move verification to Security. → *Rec: REMOVE.*
37. **Real multi-model debate (not one engine talking to itself)** — you flagged all agents used only Mistral. → *Rec: REBUILD (moot once agents EXECUTE instead of debate).*
38. **Agents EXECUTE, not debate** — the core shift. → *Rec: REBUILD (the whole point).*
39. **Departments hand off work to each other** — real inter-dept flow ("else it's not an OS"). → *Rec: BACKLOG (after single-agent execution works).*
40. **Agent conversations are visible/readable** — "I don't see where the agents' conversations are." → *Rec: FIX.*
41. **Per-department conversation history** — scrollable full history per dept. → *Rec: KEEP.*
42. **War-room + group-chat tabs per department** — Rooms-as-OS v2. → *Rec: BACKLOG.*
43. **Results show sentences, not code/JSON** — outputs must be human-readable. → *Rec: FIX.*
44. **Conversation lengths all identical (a red flag)** — you noticed every convo was the same length. → *Rec: FIX (symptom of fake/templated talk).*
45. **Departments organized by name; open one → see its work** — a clean per-dept view. → *Rec: KEEP.*

## SECTION E — Execution, checks & self-improvement

46. **EXCAVA actually DOES real actions (not just approvals)** — "you're mostly just in approval stages." → *Rec: REBUILD (the headline fix).*
47. **Self-improvement runs MORE often + bigger** — including UI/UX/cosmetic improvements. → *Rec: IMPROVE.*
48. **Supervisor (intent charter check)** — checks every tool against what you intended. → *Rec: KEEP.*
49. **Systemcheck ("does everything work" probe)** — systematic check of all subsystems each loop. → *Rec: KEEP.*
50. **Guardrails, at least 10** — so nothing is lost as the project grows. → *Rec: KEEP.*
51. **Guardrail FIRING test** — prove each guard actually triggers, not just exists. → *Rec: KEEP.*
52. **Value over action-count (dedupe reruns)** — only run a dept when there's NEW input. → *Rec: IMPROVE (kills the churn you're frustrated by).*
53. **External agent checks for MISSED systems** — an outside checker finds gaps in the brain. → *Rec: BACKLOG.*
54. **Executors for departments (real capability, not just decision.md)** — depts can DO fixes, not only propose. → *Rec: REBUILD.*

## SECTION F — Interaction & governance

55. **Conversational EXCAVA (chatbot that EXECUTES) — SEE it think + act** — your strong recent ask. → *Rec: REBUILD (Phase-0 candidate).*
56. **Clickable questions in the chat** — you pick options by clicking (like this audit). → *Rec: KEEP (you love this; keep using it).*
57. **Pitch/approval system (real pitches, in-app decide)** — big changes stop and ask you. → *Rec: KEEP-but-simplify.*
58. **Pitch detail (concrete plan/steps/impact)** — you're the boss, want full specifics. → *Rec: BACKLOG (I already over-built this; park it).*
59. **See designs WITHOUT approving each** — you don't want to approve every design. → *Rec: KEEP.*
60. **Ask me questions at stages** — check in at the right moments. → *Rec: KEEP.*
61. **Harsh 100% criticism every loop (me + you)** — never soften. → *Rec: KEEP.*
62. **Token-reduction (Caveman) as ironclad law** — it's too slow otherwise. → *Rec: KEEP.*
63. **Plan-first, then act on approval** — a concrete plan before building. → *Rec: KEEP.*
64. **New-session prompt** — clean handoff to a fresh session. → *Rec: KEEP (done; keep updated).*
65. **Push-to-owner notifications (Telegram)** — EXCAVA pings you when something needs you. → *Rec: BACKLOG.*
66. **"I don't read Python, I want to understand the project"** — you want to own it, not just receive it. → *Rec: KEEP (FUNDAMENTALS + teach-as-we-go).*

## SECTION G — Visual & design

67. **Full visual overhaul** — professional look; you said ONLY after history is functional. → *Rec: BACKLOG (per your own rule) — but the new cockpit shell is core.*
68. **Desktop-with-panels cockpit** — your chosen shape. → *Rec: REBUILD (this is core, not deferred).*
69. **5 different design versions (different overall, not just color)** — real alternatives to choose from. → *Rec: BACKLOG (do at overhaul-design time).*
70. **Impeccable / design skills to de-generic the look** — it still looks generic. → *Rec: BACKLOG.*
71. **Arena-design inspiration ("say what I like inside the project")** — pick styles you like, in-app. → *Rec: BACKLOG.*
72. **Obsidian + Graphify brain visualization** — the data/system brain as a graph. → *Rec: BACKLOG.*
73. **Easier-to-read UI (Yahoo/news-site style)** — friendlier reading layout. → *Rec: FOLD into #68.*
74. **Massive EXCAVA intro / connected visual identity** — a strong branded entrance. → *Rec: BACKLOG.*
75. **Fable for 60%+ of work, especially visuals** — use Fable heavily for design. → *Rec: KEEP (workflow rule).*

## SECTION H — Data brain / memory

76. **Brain graph holds Q&A + problems + project history** — not just tools ("not ALL info is in it"). → *Rec: IMPROVE.*
77. **Obsidian brain fix** — the current graph is malformed. → *Rec: BACKLOG.*
78. **Star skills + combined skills in the system brain** — reusable skill combos. → *Rec: BACKLOG.*
79. **Link processors to improve memory + effectiveness** — connect the pieces of the brain. → *Rec: BACKLOG.*

## SECTION I — Multi-project & money-making

80. **Multi-project "parent panel"** — EXCAVA manages your other repos, maybe opens PRs. → *Rec: BACKLOG (after core).*
81. **Monetization ad-skill** — a skill that runs ads to offset AI costs. → *Rec: BACKLOG (your rule: after history).*

## SECTION J — Process & the loop itself

82. **Weekly Tutorial system (no decisions, reviews changes)** — so you never lose your bearings. → *Rec: BACKLOG (built; not core right now).*
83. **Drain transcripts fast + health.json progress readout** — watch the numbers climb. → *Rec: KEEP.*
84. **EXCAVA chooses the run intervals** — it schedules its own cadence. → *Rec: KEEP.*
85. **"Make a list so nothing is missed" (this ledger)** — the rehab plan itself. → *Rec: KEEP (it's now the backlog).*
86. **Retire "fulfill EVERY request before anything new"** — the law that traps us in breadth. → *Rec: REMOVE (replace with "one core, done well, then expand").*
87. **The 8-minute loop cadence** — build one item per tick. → *Rec: REBUILD (fewer, bigger, outcome-measured sessions?).*
88. **Recall-before-change + log WHY** — the memory discipline. → *Rec: KEEP.*
89. **Ship only via git_safe; quarantine-never-delete** — the safety rails. → *Rec: KEEP.*

## SECTION K — The three big strategic forks (answer these even if you skip others)

90. **Phase-0 proof-of-life** — which ONE capability do we make fully work first, visible to you? (activator / research / artifact / video-extract)
91. **Timeline** — is there a real deadline, or is "someday" fine?
92. **Success test** — what's the ONE thing that, working, makes you say "NOW it's real"?

## SECTION L — reality-driven items (added after the 2026-07-15 code inventory)

*The inventory found **97 modules built, ~30 wired into the beat, 21 referenced by nothing.** The biggest lever isn't building — it's wiring and surfacing what already exists.*

93. **Social network analysis as a SOURCE** — mine Reddit/Telegram/X/HN for AI tools & trends. `mine_social.py` is BUILT but ORPHANED (never runs, never shown). → *Rec: WIRE.*
94. **Social/network GRAPH analysis** — map who-builds/shares-what and what's surging, as a visible view. → *Rec: BACKLOG (after 93).* 
95. **Workflows** — chain elements into repeatable multi-step jobs, not one-shot actions. → *Rec: REBUILD (part of "agents execute").* 
96. **Integrations** — make the MCP-connector element type real so EXCAVA connects to outside apps. → *Rec: BACKLOG.* 
97. **Visibility law** (your #1 theme, 25× in history) — every built feature must be visible + operable in the app or it doesn't count as done. → *Rec: KEEP (enforce it).* 
98. **Delete the dead code** — 21 modules are referenced by nothing (mine_competitors, mine_designs, visual_extract, news_digest, recategorize, make_monsters, export_graphml…). → *Rec: REMOVE the dead; WIRE the wanted.* 
99. **Multi-brain agents** — 2–3 DIFFERENT models as different agents (Ollama models + cloud engines), never one model talking to itself (fixes the "all conversations same length" tell). → *Rec: REBUILD.*

## SECTION M — THE GENERATION ENGINE (the missing heart — added 2026-07-15)

*The plan specified the plumbing (brain, hub) but not the engine that turns your parameters into a tool. This is the actual product. Every item here is a real question.*

100. **Task intake / spec** — how you tell EXCAVA what to generate (a form? plain language? a parameter template?). → *Rec: DEFINE (design it with you).* 
101. **Task decomposition** — the engine breaks a goal into ordered steps. Nothing does this today. → *Rec: REBUILD (new core).* 
102. **Element retrieval** — for each step, the engine picks the right element(s) from the brain/hub. → *Rec: REBUILD.* 
103. **Execution adapter** — HOW EXCAVA actually drives OpenCode / Claude Code to do the work (the hardest plumbing). → *Rec: REBUILD.* 
104. **Verification loop** — the engine checks each step's output before continuing (not blind chaining). → *Rec: REBUILD.* 
105. **Assembly / handoff** — how the finished tool/project is packaged and delivered to you. → *Rec: REBUILD.* 
106. **Sandbox / safety** — run mined OSS + generated code WITHOUT risking your PC (containers/jailed dirs). → *Rec: REBUILD (critical, currently a hole).* 
107. **Output quality bar** — define + measure what "professional-grade generated tool" means. → *Rec: DEFINE.* 
108. **Learning loop** — generation outcomes feed self-improvement so it gets better over time. → *Rec: REBUILD.* 
109. **Enrichment-at-scale** — an automated pipeline to make the hub usable beyond a hand-enriched 50. → *Rec: REBUILD.* 
110. **Failure handling** — what happens when a generation fails midway (rollback / retry / ask you). → *Rec: DEFINE.* 
111. **Recipes / templates** — reusable generation recipes for common project types. → *Rec: BACKLOG.* 

## SECTION N — SELF-IMPROVEMENT (first-class pillar — Eitan's #2 priority; elevated 2026-07-16)

*You flagged it was under-weighted — correct. It now has its own section with a real mechanism. The old items (23, 47, 108) fold in here. Draft for you to edit; you author, Claude proposes verdicts.*

**The core mechanism (this is what "self-improvement" actually means):** measure success → find the #1 failure → fix it → verify the number moved. Everything below serves that loop.

112. **Success measurement** — define how EXCAVA scores each task (per-task, per-department) so it can *tell* whether it improved. Without this, "self-improvement" is theater. → *Rec: DEFINE (the foundation).* 
113. **Top-failure finder** — each cycle, surface the single biggest recurring failure to fix next. → *Rec: REBUILD.* 
114. **Fix application** — how a fix lands: tune a prompt / swap a brain / rewire a tool / change code. → *Rec: REBUILD.* 
115. **Auto vs pitch** — safe fixes auto-apply behind a regression test; overhaul / new-tool / deeper-access → a pitch (P5). → *Rec: KEEP.* 
116. **Cadence** — how often the cycle runs (you said "much more frequently" — every beat? hourly? daily?). → *Rec: DEFINE.* 
117. **Scope** — improves agents / prompts / brains / routing / hub-content / its OWN code AND **UI/UX + cosmetic** (your explicit ask). → *Rec: IMPROVE.* 
118. **Learning loop** — generation outcomes feed back so the engine gets *better at generating* over time. → *Rec: REBUILD.* 
119. **Per-department self-improvement** — each department improves its own work ("external arms per dept," your ask). → *Rec: REBUILD.* 
120. **Meta-brain** — cross-department learning: a fix discovered in one helps the others. → *Rec: BACKLOG.* 
121. **Safety** — regression test + quarantine-never-delete so self-improvement can never break the system. → *Rec: KEEP.* 
122. **Visible progress** — you SEE it improve: a success-rate number that climbs, per department, in the app. → *Rec: REBUILD.* 

---

*When you've marked these, I'll produce the Phase-0 build plan from your answers — and from then on,
progress is measured as "Eitan can do something new," never as "a commit happened."*
