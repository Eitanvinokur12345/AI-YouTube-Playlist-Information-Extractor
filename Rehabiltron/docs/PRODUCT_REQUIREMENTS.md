# Product Requirements — Rehabiltron

**Version:** 0.1 (pre-implementation)
**Date:** 2026-08-01
**Status:** Draft for approval

Notation used throughout:
- `MUST` / `SHOULD` / `MAY` carry their usual RFC-2119 weight.
- `ASSUMPTION (unconfirmed)` marks a decision I made because the brief was silent. Each maps to an
  item in [`MISSING_INFORMATION.md`](./MISSING_INFORMATION.md).

---

## 1. Product summary

Rehabiltron is a personal growth operating system for a single owner. It records what you are trying
to change about yourself, captures evidence of change over time, and turns that evidence into
visible progress — levels, streaks, comparisons, and a timeline you can scroll back through.

It is deliberately private. The design assumption is that a user will put their worst photos, their
most awkward voice recordings, and their most honest journal entries into it, and that they will only
do that if the app cannot betray them.

## 2. The primary user

One person: the owner. This shapes several decisions that would be wrong for a commercial app.

- No onboarding funnel, no growth loops, no engagement manipulation.
- No account creation. The app works the moment it is installed.
- Features can be sharp and opinionated rather than broadly palatable.
- Data volume is one person's lifetime, not millions of users' — so SQLite on a phone is not just
  adequate, it is the correct choice for at least a decade of use.

Multi-user support is an **architectural readiness requirement**, not an MVP feature (see C-04).

## 3. Feature vision (complete)

The full long-term scope, grouped as in the brief. Phase assignment is in §5 and
[`DEVELOPMENT_ROADMAP.md`](./DEVELOPMENT_ROADMAP.md).

### 3.1 Personal growth

| Feature | Description |
|---|---|
| User profile | Identity, current focus areas, baseline stats, personal "who I'm becoming" statement |
| Goals | Outcome-oriented targets with a target date, measurable definition of done, and progress % |
| Habits | Recurring behaviours with schedules (daily / N-per-week / specific weekdays), streaks, grace days |
| Tasks | One-off actions, optionally linked to a goal, with due dates and priority |
| Personal development plans | Named collections of goals + habits forming a coherent programme (e.g. "Q3: sleep and strength") |
| Progress tracking | Per-goal, per-habit, and aggregate views over time |
| Timeline / history | An append-only chronological feed of everything meaningful that happened |
| XP system | Points earned from completions, weighted by difficulty and consistency |
| Levels | Derived from cumulative XP, with a configurable curve |
| Achievements | Rule-driven unlocks (first 30-day streak, 100 workouts, etc.) |
| Rewards | User-defined rewards purchasable with XP, and their redemption history |
| Milestones | Personally significant moments, manually marked or auto-detected |

### 3.2 Health

Sleep tracking and sleep-quality analysis; workout tracking with an exercise history; physique
tracking with body measurements; progress photos; recovery tracking; nutrition tracking.

Data entry is manual first. Platform health-store integration (Apple HealthKit, Android Health
Connect) sits behind an interface and is added when the manual model is proven. *ASSUMPTION
(unconfirmed) — I-02.*

### 3.3 Appearance

Skin tracking; hair and grooming tracking; style improvement; progress comparisons (side-by-side and
over time); image-based analysis; skincare and product recommendations informed by stated goals and
concerns.

Recommendations are **informational only** — no affiliate links, no commercial relationships, and an
explicit "not medical advice" disclaimer on anything touching skin or nutrition. *ASSUMPTION
(unconfirmed) — I-10.*

### 3.4 Communication and social development

Voice recording; speech analysis covering volume, speaking speed, and pauses; confidence indicators;
social presence and coaching feedback; improvement tracking over sessions.

The acoustic metrics (volume, pace, pause distribution) are computed on-device with signal
processing and no model. Transcription and higher-level "confidence" judgements are model-dependent
and gated behind the AI privacy controls. *ASSUMPTION (unconfirmed) — I-09.*

### 3.5 Productivity

Task management; focus sessions (timer-based, with interruption logging); productivity analytics;
habit enforcement; optional phone-usage restriction where the OS permits it.

Phone-usage restriction is genuinely constrained by platform policy — iOS requires Apple's Family
Controls entitlement, which is often denied for personal apps. Treated as research-then-decide
(O-04).

### 3.6 Knowledge

A resource library of books, articles, research papers, and courses, with reading/consumption state
and notes. Learning recommendations tied to active goals.

The app **links to** high-quality external resources rather than reproducing their content.

### 3.7 AI features

Image analysis (physique, skin, style); personal recommendations; coaching assistance; pattern
detection across tracked data; progress analysis and narrative summaries.

All of it goes through one abstraction (§4 of [`ARCHITECTURE.md`](./ARCHITECTURE.md)) so the
processing location is a user setting, not a code path.

## 4. MVP scope (Phase 1)

Phase 1 is defined by a single test: **can the owner use this every day for a month, and would
losing it be annoying?** If yes, the foundation is real.

### In scope

| Area | MVP content |
|---|---|
| Foundation | App shell, navigation, encrypted database, migrations, event bus, settings, app lock |
| Profile | One profile: name, avatar (optional), focus areas, "becoming" statement, created date |
| Goals | Create/edit/archive; title, description, category, target date, measurable target, progress, status |
| Habits | Create/edit/archive; schedule; daily check-in; streak with grace days; history calendar |
| Tasks | Create/complete; optional goal link; due date; priority (deliberately minimal in Phase 1) |
| XP & levels | XP ledger, idempotent awards, level curve, level-up event and celebration |
| Timeline | Append-only feed of goal/habit/task/XP/level events, filterable, scrollable back to day one |
| Backup | Encrypted export to a user-chosen location, and restore from that file |
| Privacy | Encryption at rest, biometric/PIN lock, zero telemetry, no network calls at all in Phase 1 |

### Explicitly out of MVP

Health, appearance, voice, AI, sync, achievements/rewards catalogue, notifications, focus sessions,
knowledge library, web/desktop. Each has a phase in the roadmap.

### MVP acceptance criteria

1. Install on a physical device, open, complete first-run setup in under two minutes.
2. Create a goal, a habit, and a task; check in on the habit for several days; see XP accumulate and
   a level-up occur.
3. Force-quit and reopen — all data intact, app locked until biometric/PIN.
4. Airplane mode for the entire session — nothing degrades (Phase 1 makes no network calls at all).
5. Export a backup, wipe the app, reinstall, restore, and verify the data is identical.
6. Inspect the on-device database file with an external tool — it is unreadable without the key.
7. Domain-layer test suite passes with ≥ 90% coverage of business rules.

## 5. Future phases (summary)

| Phase | Content |
|---|---|
| 2 | Health — sleep, workouts, measurements, photos (with the sensitive-media protections of §6.5); notifications; achievements & rewards |
| 3 | AI foundation — provider abstraction, consent system, processing-location transparency, first analyses; appearance tracking |
| 4 | Voice & communication — recording, on-device acoustic analysis, session history |
| 5 | Sync — encrypted multi-device sync between the owner's own devices |
| 6 | Productivity depth, knowledge library, web/desktop |
| 7 | Multi-user, if ever wanted |

Ordering rationale and dependencies are in [`DEVELOPMENT_ROADMAP.md`](./DEVELOPMENT_ROADMAP.md).

## 6. Privacy requirements

These are requirements, not preferences. A feature that cannot be built within them does not get
built.

### 6.1 Local-first

- **P-1** All user data MUST be stored on the device and be fully functional with no network.
- **P-2** The app MUST make **zero** network requests unless a user action explicitly requires one.
  In Phase 1 there are no network requests at all.
- **P-3** There MUST be no analytics, telemetry, crash reporting, or attribution SDK of any kind.
  Adding any later requires an explicit, separate decision and a user-facing toggle that defaults off.

### 6.2 Encryption

- **P-4** The database MUST be encrypted at rest (C-01).
- **P-5** Media files (photos, audio) MUST be encrypted at rest individually, and MUST live in
  app-private storage, never the shared photo gallery.
- **P-6** Encryption keys MUST be held in the OS keychain/keystore, hardware-backed where available,
  and MUST NOT be written to application storage, logs, or backups in plaintext.
- **P-7** Backups MUST be encrypted with a key derived from a user passphrase, so a backup file is
  useless to anyone who obtains it (C-03).

### 6.3 User control

- **P-8** The user MUST be able to export all data in a documented, readable format.
- **P-9** The user MUST be able to delete any record, and to wipe everything, irreversibly.
- **P-10** Deleting a record MUST remove its media from disk, not merely unlink it.
- **P-11** There MUST be no artificial limits on the amount of content uploaded (C-05). The app
  SHOULD surface storage usage so the user can manage a real limit — the device's.

### 6.4 AI processing transparency

- **P-12** No data MAY be sent to any AI provider without an explicit, per-category, revocable opt-in
  that defaults to off.
- **P-13** Every AI result MUST display where it was processed: on this device, on the user's own
  server, or which named external provider.
- **P-14** The app MUST keep a local, user-viewable log of every outbound AI request: what category
  of data, which destination, when. This is the receipt that makes P-12 verifiable.
- **P-15** Requests MUST carry the minimum data needed. Sending a whole journal when a date range
  would do is a defect.

### 6.5 Sensitive media (progress photos, voice)

Progress photos may be intimate; voice recordings may capture other people. Default OS behaviour is
wrong for both.

- **P-16** Photos captured in-app MUST NOT be written to the system photo library.
- **P-17** App storage MUST be excluded from iCloud/Google automatic backups, so sensitive media never
  lands in a cloud the user did not choose.
- **P-18** Viewing photo and voice sections SHOULD require re-authentication (biometric/PIN).
- **P-19** No notification, widget, or app-switcher preview MAY render sensitive media. The app
  SHOULD blur its own snapshot when backgrounded.
- **P-20** The app SHOULD warn once, at first recording, that recording other people may require
  their consent depending on jurisdiction.

### 6.6 Sync (when built)

- **P-21** Sync MUST be end-to-end encrypted; any relay server MUST be unable to read content or
  metadata beyond what routing strictly requires.
- **P-22** Sync MUST be opt-in and MUST work between the user's own devices without a third-party
  account.

## 7. XP, levels, and rewards specification

Concrete so it can be implemented and tested. All numbers are configuration, not constants in code.

### 7.1 Earning XP

| Event | Default XP |
|---|---|
| Habit check-in | 10 × difficulty (1–3) |
| Habit streak milestone (7/30/100/365 days) | 50 / 250 / 1000 / 5000 |
| Task completed | 5 × priority (1–3) |
| Goal milestone reached | 100 |
| Goal completed | 500 × difficulty (1–3) |
| Daily "all scheduled habits done" bonus | 25 |

### 7.2 Rules

- **X-1** XP MUST only be awarded by the XP service, in response to a published domain event. No
  feature awards XP directly.
- **X-2** Every award MUST be idempotent, keyed by the originating event id. Replaying an event, or
  a crash mid-transaction, MUST NOT double-award. This is the single most important correctness rule
  in the gamification layer.
- **X-3** The XP ledger is append-only. A reversal (e.g. un-completing a habit) is a new negative
  entry referencing the original, never a deletion.
- **X-4** XP MUST NOT decay or be lost as punishment. *ASSUMPTION (unconfirmed) — I-06.* Gamified
  self-improvement that punishes bad weeks reliably makes bad weeks worse.
- **X-5** Level is a pure function of cumulative XP, recomputable from the ledger at any time. It is
  cached for display but never the source of truth.

### 7.3 Level curve

Default: `xp_to_next(n) = round(100 × 1.15^(n−1))` — level 2 at 100 XP, level 10 at ~2,000
cumulative, level 25 at ~29,000. Fast early feedback, meaningful long-term climb. Configurable.

### 7.4 Streaks

- **X-6** A streak counts consecutive *scheduled* occurrences met, not calendar days — a
  three-times-a-week habit does not break on Tuesday.
- **X-7** Configurable grace days (default 1 per rolling 30 days) repair a break without resetting.
  *ASSUMPTION (unconfirmed) — I-07.*
- **X-8** Streak copy MUST be neutral. No shaming, no loss-aversion pressure.

### 7.5 Rewards

User-defined: a name, an XP cost, and optionally a limit. Redeeming spends XP from a separate
"spendable" balance so that redeeming never reduces level (level tracks lifetime XP; the spendable
balance tracks currency). Two counters, one ledger.

## 8. Data model requirements (product level)

- **D-1** Every user-scoped record MUST carry a `user_id`, even while there is exactly one user.
- **D-2** Every record MUST carry `created_at`, `updated_at`, and a soft-delete `deleted_at`.
- **D-3** Every record MUST carry the `device_id` that last wrote it, and a monotonic `revision` —
  the minimum needed for future sync conflict resolution, costing nothing now (see §7 of
  [`ARCHITECTURE.md`](./ARCHITECTURE.md)).
- **D-4** Historical/log tables (XP ledger, timeline, habit entries) are append-only.
- **D-5** Media MUST be referenced by an `attachment` row, never stored as a blob in the database.

## 9. Quality, accessibility, and safety

- **Q-1** Cold start to interactive: under 2 seconds on a mid-range device.
- **Q-2** Any list the user scrolls MUST stay at 60fps with 10,000 rows (virtualized lists, indexed
  queries, no full-table scans on render).
- **Q-3** WCAG 2.2 AA contrast; full screen-reader labels; respects OS font scaling and
  reduce-motion.
- **Q-4** RTL-ready layout from the first screen. *ASSUMPTION (unconfirmed) — I-01.*
- **Q-5** No dark patterns: no artificial urgency, no guilt, no streak-loss manipulation.
- **Q-6** Health, skin, and nutrition surfaces MUST carry a clear "not medical advice" disclaimer and
  MUST NOT present outputs as diagnoses.
- **Q-7** Data loss is the worst possible defect. Every write path that touches user data needs a
  test, and backup/restore is verified before Phase 1 is called done.

## 10. Open product questions

Tracked in [`MISSING_INFORMATION.md`](./MISSING_INFORMATION.md). The five blocking ones: encrypted-DB
tradeoff (C-01), platform targets (C-02), key custody and recovery (C-03), single-user semantics
(C-04), and where unlimited content lives (C-05).
