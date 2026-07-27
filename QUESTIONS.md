# Open questions for Eitan (non-blocking — answer whenever; work continues meanwhile)

_Per your rule: questions live here + in memory so they never block work or waste tokens. Answer any subset, in any order, whenever you want. Each has my default so you can also just say "defaults"._

---

## ⏸ AWAY WEEK — batched while you're out (since 2026-07-21)
You're away ~1 week; the offline loop is running (non-brain fronts, hourly) and collecting questions HERE instead of asking. Every question I hit this period is appended below with the default I proceeded on. I'll present this whole list the moment you're back. Contract: `data/excava/away_mode.json`.

### Away-week questions

**Overhaul audit — next decision batch (§7; items 5–8 of 122).** These are YOURS to decide; I did NOT auto-apply them — `data/excava/overhaul_decisions.json` stays OPEN. My proposed verdict on each (confirm or change with `python -m src.audit_decisions set <id> <verdict>`):
- **#5 "Should I just buy Gemini Pro?"** → proposed **REMOVE the worry.** The free path (VPS + Ollama + the free model pool) is real and proven this week — 11/11 engines answered, four brain families live. Paying is unnecessary.
- **#6 Direct in-app write to EXCAVA (no GitHub step)** → proposed **REBUILD.** Async-via-GitHub works now; true real-time in-app write needs the VPS (ties to A1, which you already KEEP'd).
- **#7 API keys work offline / without your PC** → proposed **KEEP the answer (yes).** Proven this week: the cloud beat ran the keys 24/7 with your machine off; the VPS will too.
- **#8 EXCAVATORTRON = HUB, EXCAVA = agents (naming)** → proposed **KEEP + lock everywhere.** This is the canonical naming and it's used consistently across the code and docs.

**2026-07-26 (fire 10) — deterministic GitHub-metadata enricher BUILT, per the proposed default below.**
`src/github_meta_enrich.py` now fills github-linked stub descriptions from the GitHub REST API's
own `description`/`topics` (no LLM, no Ollama, no local-drain dependency) and is wired hourly into
`core_spoton.yml`. Could not live-verify against the real API from this cloud session (its proxy
scopes GitHub access to just this repo — 403 on other repos) — logic verified via dry-run +
mocked-metadata unit check instead; real end-to-end proof needs the next `core_spoton` Action run
and a PULSE.md stub-count check (see AWAY_LOG fire 10). This does NOT replace the LLM-fused path
for non-GitHub stubs (video-only elements, sites without API metadata) — deep-retrieve + the local
drain are still the only path for those. Original blocker note preserved below for context.

**The real hub blocker: enrichment is stalled at 0, and away-mode can't fix it (decision for your return).**
Three loop fires this week shipped read-side hub wins (v125 type-aware Activate · v126 "ready to use" filter
· v127 inline payload in the detail view). All real, but all BROWSE-layer — because the actual problem is
CONTENT: 3,628 of 10,133 elements are bare stubs and the local drain has enriched **0** for days (guardrail
G-O). deep_retrieve rides the brains/Ollama subsystem, which away-mode tells me not to touch, so I keep
polishing how you browse the library instead of filling it. → **Proposed default (on your return):** stand up
a DETERMINISTIC enricher (no LLM) that fills stubs from real sources — GitHub API repo description / topics /
homepage / README first line for the ~1,600 repo elements — network-bounded with a hard timeout (the 793-min
hang lesson). Free, non-brain, attacks completeness directly. Until you approve a network front or lift the
brain freeze, these fires keep producing browse-layer polish of diminishing value.

**2026-07-26 (fire 6) — orphaned branch found: away-fire work landed on a branch that never reached `main`.**
While diagnosing why guardrails dropped 15/15→13/15 (real cause: fixed in this fire — see AWAY_LOG/
SESSION_HANDOFF §0d v129), I found `origin/claude/kind-shannon-ae4swi`, a branch that diverged from `main`
after beat #17 (2026-07-26T01:58Z) and already contains a correct, tested fix for the exact same done-counter
metric bug (G-M) plus an unrelated `links`-department routing fix — fully written, verified, committed with
a proper message — but never merged/shipped to `main`. It sat idle 11+ beats while `main` kept the bug. This
means at least one earlier away-fire (or a parallel session) did real, good work that got silently stranded
because it ran on its own branch instead of `main` and nothing forced a merge. I ported the G-M fix myself
into `main` this fire (small enough to redo by hand safely), but the `links`-routing fix on that branch is
still stranded and unreviewed. → **Proposed default:** (a) every away-fire session should verify, before
shipping, that its working branch either IS `main` or gets merged into `main` before the session ends — a
fix stuck on an abandoned branch is equivalent to no fix; (b) someone (next fire, or you) should look at
`origin/claude/kind-shannon-ae4swi`'s `1205385a` commit ("wire the links department into the agent
registry") and land it or discard it explicitly, rather than leaving it to rot. _No further branches checked
this fire — there are ~9 other `kind-shannon-*` branches on origin whose contents are unknown; worth a sweep._

**2026-07-26 (fire 7) — `1205385a` landed; the branch problem is confirmed recurring, not a fluke.**
Ported the stranded `links`-department fix by hand (no merge-base with `main` after the history rewrite, so
a real merge/cherry-pick wasn't possible) — see AWAY_LOG fire 7. This session's own branch ALSO had no
upstream tracking configured (same symptom fire 6 hit and one-time-fixed on its own branch) — the second
occurrence in two fires confirms proposal (a) above isn't optional, it's necessary: every fresh session
branch starts detached from `origin/main` and silently loses work if the session doesn't notice and doesn't
run `git_safe push`. → **New proposed default:** add a standing-checks step (start of every fire, before any
other work) that unconditionally runs `git branch --set-upstream-to=origin/main` on the current branch — 
cheap, idempotent, and removes the whole failure class instead of relying on each fire to notice the symptom.
There are still ~13 other `kind-shannon-*` branches on origin of unknown content (grew from ~9); a full sweep
(diff each against `main`, land or explicitly discard) remains unstarted and should be the next fire's focus
if nothing higher-priority is queued.

**2026-07-26 (fires 12→13) — anti-boilerplate gate moved to point-of-creation; the 2 real
offenders found are now cleaned up too — DONE, both halves landed this run.** Fire 12 root-caused
fire 11's open item: `src/bulk_analyze.py` and `src/mine_feeds.py` (shared by
`gemini_video_analyze.py`) now block a bare-product-name "skill" (CLAUDE.md's own forbidden
template, e.g. "X is an AI tool by Y. It enhances productivity...") BEFORE it's written. Fire 13
(same run, right after) added `src/cross_tab_check.sweep_orphan_boilerplate()` — a permanent
second net wired into `main()` (so it runs every `bulk_analyze.yml` cycle) that reuses the same
gate retroactively and catches a boilerplate skill even with NO matching tool name to collide
with. Applied for real: `skills.json` 3119→3117, `tools.json` 2848→2850 (both records rerouted
as tools, not dropped). See AWAY_LOG fires 12 & 13 for full verification. **One loose end fire 13
flagged, worth a human glance whenever convenient (not urgent):** the 2 rerouted tool records
are named after the original SKILL's (generic) name — "Client Onboarding" and "Social media post
generation" — rather than the actual product the description is about ("Zoho CRM" in the first
case), because extracting the real product name from scraped landing-page copy wasn't worth an
extra LLM call for 2 records. Both are factually correct, just oddly titled; fine to rename
by hand or leave as-is. _Default: leave as-is; low priority._

**2026-07-26 (fire 11) — commit-signature / "Unverified" badge on GitHub, declined to rewrite history.**
This session's local hook flagged fire 11's two commits (`e849f557`, `83d2685f`) as showing "Unverified"
on GitHub (no GPG/SSH signature — the committer email was already `noreply@anthropic.com`, so email wasn't
the actual gap) and suggested `commit --amend --reset-author` + a rebase against `origin/...` to fix it. I did
**not** do this: (a) amending author metadata doesn't add a cryptographic signature, so the suggested fix
wouldn't actually produce a "Verified" badge — there's no signing key configured anywhere in this repo's
tooling; (b) the fix as given implies a rebase + force-push on a branch the `skills-tracker-bot` CI identity
is *also* actively committing/pushing to every 20–90 min (see `18c3ac3f` interleaved right between fire 11's
two commits) — rewriting history there risks a race against a concurrent CI push, and force-push isn't
something to do unattended without your sign-off regardless. **Default: leave commits as-is** (they're
correctly on `origin/main` — `git_safe.push()` already verifies `origin == HEAD` after every ship — just
cosmetically "Unverified"); if you want real "Verified" badges going forward, that needs either a GPG/SSH
signing key added to this environment's git config, or switching these commits to go through the GitHub API
(which auto-signs as "GitHub verified") instead of local `git push`. Neither is a fire-sized decision to make
unilaterally.

**2026-07-27 (fire 19) — the branch sweep finally ran; two real gaps found and landed, ~20 branches now safe to delete.**
Checked every `claude/kind-shannon-*` branch for content `main` lacks (file-diff, not full history reread — see
AWAY_LOG fire 19 for the method and its one acknowledged blind spot). Found zero stranded source code, and landed
the two real gaps that did exist: a `G-P` guardrail from `kind-shannon-hcwmum` (fire 18) and two already-analyzed
videos' worth of skills/tools/news from `kind-shannon-yj1a6g`. Everything else on every other branch is either
already independently on `main` or was deliberately removed by later cleanup fires (12/13/15) — confirmed via
`deleted_skills.json`/`merge_log.json`, not assumed. → **Decision for you:** all ~20 stray branches are now
confirmed safe to delete (`git push origin --delete <branch>` for each) — I did not delete them myself since
branch deletion is harder to reverse than anything else this fire touched and no prior fire has done it
unilaterally either. _Default: delete them next time you're at a terminal; low priority, no urgency._

**2026-07-27 (fire 23) — the "news" department's charter was self-inconsistent since it was
authored; found and partly fixed, one real wiring decision left for you.** `data/excava/intent.json`'s
"news" charter has always said `should_do: "refresh the AI-news digest..."` but `right_tool` was
always `src.trend_watch` — a self-improvement trend-proposal tool (see its own docstring) with
nothing to do with news content. `data/excava/agents.json`'s own "news" dept purpose ("refresh
official-site AI news") independently confirms headline-refresh was the true original intent.
Because `right_tool` happened to already match the actual code wiring in `src/excava_agents.py`'s
`REAL_TOOL`, the supervisor's own intent-drift detector (the one that already caught mining/visual/
memory drift) saw no mismatch and stayed silent on this one for 3+ weeks. Restored `right_tool` to
`src.news` (the tool that actually matches should_do) so the drift is now visibly flagged every run
— `python -m src.excava_systemcheck`'s "intent aligned" line will read **10/11 systems working,
1 tool-drift** from now on (was 11/11) — that is a DELIBERATE, expected reveal of a pre-existing
problem, not a new regression from this fire; please don't "fix" it by reverting `right_tool` back
to `trend_watch` without reading this note. **What I did NOT do, and why — this is your call:**
rewire `src/excava_agents.py`'s `REAL_TOOL["news"]` to actually run `src.news` when the department
executes. Two real risks stopped me: (1) `src/news.py` already runs independently every 6h via
`.github/workflows/news.yml` and writes `data/daily_web_news.json`/`data/web_news_store.json` —
files CLAUDE.md governs as the separate YouTube-playlist-analyzer pipeline's own territory; routing
EXCAVA's department/bus path through the same tool risks a commit race against that dedicated
schedule. (2) it fetches ~95 RSS sources at up to 15s each, sequentially — easily past
`_run_real_tool`'s hardcoded 90s subprocess timeout, which would turn today's honest no-op into a
noisy "failed (timed out)" instead. → **Proposed default:** leave `REAL_TOOL["news"]` on
`trend_watch` as-is (it's safe, already proven, and its own honest "queued 0" output no longer
mis-reports as theatre — see the supervisor fix below) and treat the now-visible intent-drift as
documentation of a historical mistake rather than something to chase — UNLESS you want the "news"
EXCAVA department to genuinely do headline-refresh work, in which case it needs either a raised
per-dept timeout override or an async/deferred dispatch, built with your sign-off since it touches
the other pipeline's schedule. **Second, independent fix in the same commit — the actual functional
bug:** `src/excava_supervisor.py`'s `judge()` was misclassifying trend_watch's own correct, honest
"N proposals (top score X); queued 0" report as `noop` (theatre) on every single run, because
`trend_watch` DEDUPES queued proposals by key (`src/trend_watch.py`) — the 5 trend proposals it
queued back on 2026-06-29 are still open in `data/improvement_tasks.json`, so "queued 0" has been
the CORRECT report on every run since (nothing new to add, not nothing done). This was a real, live
false-positive in the project's own central "is work real" honesty tool: 6 of the last 40 tracked
completions were misjudged as theatre. Fixed with a targeted carve-out (mirrors the existing
`security`-dept "0 leaks = good" carve-out) keyed to trend_watch's own output signature. Verified:
`real_pct` on the live `data/excava/supervisor.json` jumped 82%→100% the moment the fix landed,
with 0 unit-test regressions across 8 cases (genuine no-ops/blocked/planned/security-zero all still
classify correctly). _Default: keep as documented above; only the news-dept wiring question needs
your actual decision._

---

## A. The new look ("Heavy Machinery" v58)
1. **Direction check:** hazard-yellow + warm ink, chunky borders, hard offset shadows, Archivo Black display type — is this the right direction, or push further (more color pops per tab?) / pull back? _Default: keep, then add per-tab accent colors next pass._
2. Dark mode variant of the same theme — wanted? _Default: later._
3. Should the Designs tab get an even more expressive skin than the rest (it's the taste tab)? _Default: yes, next visual pass._

## B. North Star — proposed goal additions (needs your sign-off; goals are law)
The 6 goals miss two things we now actually build for:
4. **G7 Security & trust** — "nothing untrusted ever runs un-sandboxed; your data/keys can never leak." (We built security_preflight + the Activator gate; nothing *scores* it.) Approve adding G7? _Default: add._
5. **G8 Personal fit** — "every recommendation/design/plan is tailored to Eitan's taste and workflow (Arena taste, NOSG, his stack)." Approve adding G8? _Default: add._

## C. EXCAVA — the big one (deferred build; these shape the spec)
6. **Creators department:** should created things (new skills/tools/formats) be auto-published into the hub after passing the gate, or always wait for your approval per creation? _Default: approval per creation until trust is earned._
7. What may EXCAVA do **fully autonomously** at night: only internal work (resolve/verify/organize)? Or also create drafts? Or also publish? _Default: internal + drafts._
8. Where does EXCAVA live long-term: GitHub Actions only (free, current), or also a small always-on runner (e.g. your PC when on / a free VPS) for continuous operation? _Default: Actions now, revisit after the program._
9. The OS "manages the entire project **and can do a lot of other things**" — name 2–3 concrete non-project things you want it to do first (e.g. manage Budoaris tasks? your learning? content posting?). _No default — needs you._

## D. Program gaps I found (will do unless you object)
10. ~~`formats.json` is collected but has no tab — fold formats INTO the Designs tab as a "Formats" filter?~~ — RESOLVED 2026-07-27 (away fire 22, live build v130). The Designs tab now shows a content-type subnav (All / Websites·apps / 📐 Formats) that merges `data/formats.json`'s 95 layout/diagram patterns into the same gallery, rendered as their own card style (kind + description + rebuild_hint, no screenshot since formats don't have one; excluded from the ⚔ Arena pool for the same reason). See SESSION_HANDOFF.md v130 for verification detail. _Default (yes) taken as given._
11. ~~Brain graph still has ~191 empty "white" nodes + 10 title collisions — clean next maintenance pass?~~ — RESOLVED 2026-07-26 (fires 14+15). Fire 14: the RENDERING half — `build_graph.py` and `export_graphml.py` now skip empty-body/unidentified records instead of plotting them as blank or colliding nodes (ported from `build_brain.py`'s already-working fix). Fire 15: the DATA half — investigated all 5 name-collision pairs behind `maintenance_check.py`'s 10-count by hand; 4 were genuine same-product duplicates (merged per Step 3/3b's compare-and-keep-best, backed up to `deleted_skills.json`/`merge_log.json`), 1 ("Hermes") was two genuinely different products sharing a brand name (disambiguated the display names instead of merging). `maintenance_check.py`'s "Title collisions" issue is now fully GONE (10 → 0). **Still open, NOT resolved:** the 187 empty-body records — that's real content backfill, out of scope for a maintenance pass, tracked with the stalled-enrichment blocker elsewhere in this file. _Default: title-collision cleanup done; empty-body backfill needs a dedicated enrichment pass (deep_retrieve or a deterministic filler), not another maintenance fire._
12. ~~Transcript lane blocked on `YT_PROXY_URL`~~ — RESOLVED 2026-07-02: Bright Data's residential-proxy tier needs a card on file even for free credits, which conflicts with the free-only rule, so declined. Not a blocker — Gemini-watches-video (already running) is the free analysis path, just slower per video than a transcript read would be. Cockpit now shows this as an optional "(skipped by choice)" chip, not a red MISSING.

## C2. EXCAVA conversation — installment 2 (answer anytime)
14. **Crew scope:** residents now wander every tab (bubbles = real dept status, click → cockpit). More of them / bigger / also on phone / quieter? Kill switch exists. _Default: keep as is, tune on your feedback._
15. **Creators quality gate:** before a creation (skill/prompt/scaffold/design) is accepted into the hub, what proof? _Default: EXCAVA self-test + your one-click review; nothing publishes untested._
16. **Dynamic departments:** who may open/close them? _Default: EXCAVA proposes with a reason, you approve; it may auto-close its own idle ones._

## E. Working mode
13. Confirm: keep doing big autonomous chunks on Fable (all visuals), Opus only for your own refinement passes; questions parked here. _Default: yes._

## F. Program gate decisions D1–D5 (from EXCAVA_PROGRAM.md, 2026-07-03)
17. **D1 — architecture** — ✅ ANSWERED 2026-07-03: **cron heartbeat** (Eitan picked it live in-session). Phase 0 built on it same day: the hourly `python -m src.excava` beat in bulk_analyze.yml IS the heartbeat; the file bus resumes state between beats.
18. **D2** — ✅ ANSWERED 2026-07-03: **direction-loop + change-tutorials first**, and the integration must be DAEMON-GRADE ("like a daemon for the entire project, not something casual, like in cortexOS — a clean daemon part of the OS that connects, or full integration"). HORSE-style fan-out pulled into Phase 6 scope. First daemon step shipped same day: every lane's runs now become OS bus events (the cockpit's 📡 feed).
19. **D3 — approval style:** approve the program as ONE block, or phase-by-phase sign-off? _Default: one block, with the per-phase ask-checkpoints still running._
20. **D4 — rebuild order:** spine-first as planned (P0 before any cleanup), or interleave small cleanups? _Default: spine-first._
21. **D5 — connectors tab:** OK to shrink it to verified-only once Phase 4 resolves real installs (94% are empty today)? _Default: yes._

## H. Phase checkpoints — ✅ ANSWERED 2026-07-03 (second batch)
26. **P3 creators** — ✅: creations enter the project autonomously WHEN labeled "Created by EXCAVA"; an independent test re-runs before first use; creators may build MCP servers/connectors/tools; **"PACKAGES"** = the owner's term for multi-element bundles (skills+tools+commands+designs+prompts+formats+outlines+MCP servers). Now guardrail G-12.
27. **P4 connectors** — ✅: **sandbox test-run EVERYTHING** (all 1,142; 6-hourly CI batches; verified-only tab per D5).
28. **P7 porting** — ✅: skip for now; harness stays a clean documented package (PORTABLE_HARNESS.md).
29. **P8 G9** — ✅: "Agency/Orchestration", equal weight — live on the North Star (scored 80 at birth).

## G. Omni-source intake + memory master (2026-07-03 owner additions)
22. **Your communities:** which subreddits / public Telegram channels / search queries should tier-1 intake watch? Starter set is in `data/social_sources.json` (LocalLLaMA, ClaudeAI, ChatGPTCoding, artificial, AI_Agents; Telegram empty — t.me/s only works for PUBLIC channels). _Default: keep the starter set, grow it over time._
23. **WhatsApp groups:** the only free path is you exporting a group chat (.txt, no media) from your phone into `data/whatsapp_exports/` occasionally — the miner parses the links out. Want a short how-to tutorial for that? _Default: yes, added with the Phase-6 change-tutorials._
24. **D6 — locked feeds (Instagram/TikTok/Facebook/LinkedIn):** these need your logged-in cookies stored as CI secrets, with real risk of account flags. Ever opt in? _Default: no — public-only stands._
25. **Daemon interpretation check:** I read your D2 note as "every part of the project reports through the OS bus (all 16 lanes now emit events), residents/cockpit react to real machine-wide events, and EXCAVA is the single connective layer — not a cosmetic overlay." First step shipped (lane events). If you meant something MORE (e.g. an actual resident process on a host), say so — the free-only + PC-off rules currently make the cron heartbeat the only clean daemon body. _Default: my reading._
