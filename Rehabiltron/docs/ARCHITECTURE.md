# Architecture — Rehabiltron

**Version:** 0.1 (pre-implementation)
**Date:** 2026-08-01

---

## 1. Architectural goals and the tension between them

Two forces pull in opposite directions in this project, and naming them up front explains every
decision below.

**Force 1 — this is one person's app.** Over-engineering is the most likely cause of failure. A solo
project that spends its first month on dependency-injection containers and a sync server never ships
a habit tracker.

**Force 2 — the long-term vision is genuinely large,** and three specific things are effectively
impossible to retrofit: the shape of the data model, the location of encryption, and the boundaries
between modules.

The resolution: **build the seams, not the systems.** Repositories, an event bus, an AI abstraction,
and sync-ready columns cost a few hours now and make later phases additive. Sync servers, plugin
architectures, multi-user auth, and abstraction layers with a single implementation are deferred
until a real requirement arrives.

Concretely, in Phase 1 we build: layered structure, repositories, event bus, encrypted SQLite,
migration runner, AI *interface* (no implementation). We do not build: a DI container (module-level
composition is enough), a sync engine, an auth system, a plugin loader, or a GraphQL/REST layer for
an app with no server.

## 2. System overview

Rehabiltron is a **single-process, offline-first mobile application**. There is no backend. Every
box below runs on the device.

```
┌─────────────────────────────────────────────────────────────────────┐
│                         PRESENTATION                                │
│  Expo Router screens · design-system components · view models       │
│  Rule: renders state, emits intent. No business logic. No SQL.      │
└───────────────────────────────┬─────────────────────────────────────┘
                                │ calls use cases / reads stores
┌───────────────────────────────▼─────────────────────────────────────┐
│                          APPLICATION                                │
│  Use cases (CompleteHabit, CreateGoal, AwardXp…) · feature services │
│  Orchestrates domain + repositories. Owns transactions.             │
└──────┬────────────────────────────────────────────┬─────────────────┘
       │ uses                                       │ publishes/subscribes
┌──────▼─────────────────────┐          ┌───────────▼─────────────────┐
│         DOMAIN             │          │        EVENT BUS            │
│ Entities · value objects · │          │ Typed in-process pub/sub    │
│ business rules · repo      │          │ Cross-module communication  │
│ INTERFACES (no impl)       │          │ Async, ordered, persisted   │
│ Zero framework imports.    │          │ for durable subscribers     │
└──────┬─────────────────────┘          └───────────┬─────────────────┘
       │ implemented by                             │
┌──────▼─────────────────────────────────────────────▼────────────────┐
│                             DATA                                    │
│  SQLite repositories · migration runner · encrypted file store      │
│  query builders · mappers (row ⇄ entity)                            │
└──────┬──────────────────────────────────────────────────────────────┘
       │
┌──────▼──────────────────────────────────────────────────────────────┐
│                          PLATFORM                                   │
│  Encrypted SQLite · Keychain/Keystore · FileSystem · Camera · Mic    │
│  Biometrics · (future) Health stores · (future) network transport    │
└─────────────────────────────────────────────────────────────────────┘
```

Dependencies point **inward only**. The domain layer imports nothing — not React, not Expo, not
SQLite. That is what makes business rules testable in milliseconds and portable to a desktop shell
later.

## 3. Module structure

```
src/
├── app/                        # Expo Router routes — thin, no logic
│   ├── (auth)/lock.tsx
│   ├── (tabs)/index.tsx        # today
│   ├── (tabs)/goals.tsx
│   ├── (tabs)/habits.tsx
│   ├── (tabs)/timeline.tsx
│   ├── (tabs)/profile.tsx
│   └── _layout.tsx
│
├── core/                       # Cross-cutting infrastructure. No feature knowledge.
│   ├── db/                     # connection, migration runner, transactions, query helpers
│   ├── crypto/                 # key management, KDF, file encryption
│   ├── events/                 # event bus, event types, durable dispatch
│   ├── storage/                # encrypted file store, storage accounting
│   ├── config/                 # app config, feature flags, tunables (XP curve etc.)
│   ├── logging/                # redaction-first logger
│   ├── errors/                 # error taxonomy, Result type
│   ├── time/                   # clock abstraction (never call Date.now() directly)
│   └── id/                     # UUIDv7 generation
│
├── domain/                     # Pure business model. Zero dependencies.
│   ├── entities/               # Goal, Habit, Task, XpEntry, TimelineEvent, Profile…
│   ├── values/                 # Streak, Schedule, XpAmount, Progress, DateOnly
│   ├── rules/                  # streakRules, xpRules, levelCurve, scheduleRules
│   └── repositories/           # interfaces only: GoalRepository, HabitRepository…
│
├── features/                   # Vertical slices. A feature owns its tables and screens.
│   ├── profile/
│   ├── goals/
│   ├── habits/
│   ├── tasks/
│   ├── progression/            # XP, levels, achievements, rewards
│   ├── timeline/
│   ├── health/                 # phase 2
│   ├── appearance/             # phase 3
│   ├── voice/                  # phase 4
│   ├── productivity/           # phase 6
│   └── knowledge/              # phase 6
│       ├── data/               # repository implementations, SQL, mappers
│       ├── application/        # use cases, feature service, event handlers
│       ├── ui/                 # screens, components, view models
│       └── index.ts            # the ONLY public surface of the feature
│
├── services/                   # App-wide services behind interfaces
│   ├── ai/                     # AiService, providers, consent, audit log
│   ├── media/                  # capture, encryption, thumbnails
│   ├── backup/                 # export / import
│   ├── notification/           # phase 2
│   └── sync/                   # phase 5
│
└── ui/                         # Design system: tokens, primitives, layout, theming, i18n
```

### 3.1 Enforced boundaries

These are checked by lint rules (`import/no-restricted-paths`), not by discipline alone. A violation
fails CI.

| Rule | Meaning |
|---|---|
| `app/**` → `features/*/ui`, `ui/**` only | Routes wire screens together; they contain no logic |
| `features/A/**` MUST NOT import `features/B/**` except `features/B/index.ts` | No reaching into another feature's internals |
| `features/A/**` MUST NOT import `features/B/data/**` — ever | The "no feature touches another feature's database" rule, mechanically enforced |
| `domain/**` imports nothing outside `domain/**` | Keeps business rules pure and instantly testable |
| `ui/**` MUST NOT import `features/**` or `domain/**` | The design system stays generic |
| Only `features/*/data/**` and `core/db/**` may import the SQLite driver | The repository rule, mechanically enforced |
| Only `services/ai/**` may import a model provider SDK | The AI abstraction rule, mechanically enforced |

The last three are the ones that make the four project rules real instead of aspirational.

### 3.2 Composition

No DI container. Each feature exposes a factory:

```ts
// features/habits/index.ts
export function createHabitsModule(deps: CoreDeps): HabitsModule { … }
```

`src/core/composition.ts` builds every module once at startup and hands the result to a React context
provider. Tests build the same modules with in-memory implementations. This gives the substitutability
of DI with none of the machinery, and it is trivially traceable — one file shows the whole graph.

## 4. Data flow

### 4.1 Read path

```
Screen → view model hook → use case → repository interface
                                          → SQLite repository → encrypted DB
                                          ← entity ← mapper ← row
```

Screens never see rows. Mappers convert `snake_case` rows into domain entities with real types
(`Date`, `Streak`, `XpAmount`) at the data boundary, so nothing downstream deals in raw strings.

### 4.2 Write path — worked example, "user checks in on a habit"

This one flow exercises every rule in the architecture:

```
1. UI            HabitCard onPress → habits.completeToday(habitId)
2. Use case      CompleteHabitUseCase.execute(habitId, now)
3. Domain        Habit.canCompleteOn(date)      → validates schedule, duplicates
                 StreakRules.next(streak, date) → pure computation, grace days applied
4. Transaction   BEGIN
                   habitEntryRepo.insert(entry)
                   habitRepo.updateStreak(habit)
                   outbox.append(HabitCompleted{ eventId, habitId, difficulty, at })
                 COMMIT
5. Dispatch      Event bus reads the outbox and delivers HabitCompleted
6. Subscribers   progression → XpService.award(eventId, +10×difficulty)   [idempotent]
                 progression → AchievementService.evaluate(HabitCompleted)
                 timeline    → TimelineService.record(HabitCompleted)
7. UI            Stores invalidate; the card, XP bar, and timeline re-render
```

Three things to notice, because they are the whole design:

- **The habits feature never imports the XP feature.** It publishes a fact. Whoever cares, cares.
  Adding "log every habit completion to the health module" later touches zero existing code.
- **The event is written inside the same transaction as the data** (transactional outbox). Either
  the check-in and its event both exist, or neither does. This is what prevents the classic
  gamification bug where a crash awards XP for a habit that was never recorded, or vice versa.
- **XP is awarded idempotently, keyed by `eventId`.** Redelivery after a crash is safe by
  construction, not by hoping the crash does not happen.

### 4.3 Event bus semantics

| Property | Behaviour |
|---|---|
| Delivery | At-least-once. Subscribers MUST be idempotent — this is a documented contract, not a hope |
| Ordering | Per aggregate, in write order |
| Durability | Events persist in an outbox table until every subscriber acknowledges |
| Timing | Asynchronous, after the transaction commits. Never inside it |
| Failure | A failing subscriber retries with backoff; it cannot roll back the originating write |
| Scope | In-process only. Not a message queue, not a network protocol |

Events are past-tense facts (`HabitCompleted`), never commands (`AwardXp`). If a subscriber
needs something to happen, it calls a service — the bus does not carry instructions.

## 5. AI architecture

The requirement is that the same feature works whether the model runs on the phone, on the user's own
machine, or at a provider — and that the user always knows which.

```
Feature code
    │  AiService.analyze({ task, inputs, privacyClass })
    ▼
┌───────────────────────────────────────────────────────────────┐
│                         AiService                             │
│                                                               │
│  1. ConsentGate     — is this privacyClass allowed to leave?   │
│  2. Router          — pick a provider for (task, consent)      │
│  3. Redactor        — strip anything the task does not need    │
│  4. Provider.run()  — the only place a model is called         │
│  5. AuditLog        — record destination, category, timestamp  │
│  6. Result          — always tagged with processedAt location  │
└───────────────────────────────────────────────────────────────┘
    │                    │                        │
┌───▼────────┐  ┌────────▼──────────┐  ┌──────────▼────────────┐
│ OnDevice   │  │ SelfHostedProvider│  │ ExternalProvider      │
│ Provider   │  │ (user's server /  │  │ (Anthropic / OpenAI / │
│ (local     │  │  Ollama, LM Studio│  │  Google — user's own  │
│  model)    │  │  on their LAN)    │  │  API key)             │
└────────────┘  └───────────────────┘  └───────────────────────┘
```

### 5.1 Privacy classes

Every AI request declares what kind of data it carries. This is the mechanism behind P-12 and P-13.

| Class | Examples | Default destination |
|---|---|---|
| `derived_metrics` | streak counts, XP totals, aggregate sleep hours | on-device |
| `text_personal` | goal descriptions, journal entries | on-device |
| `image_body` | progress photos, physique, skin | **on-device only, never leaves without explicit opt-in** |
| `audio_voice` | voice recordings | **on-device only, never leaves without explicit opt-in** |

The consent gate is keyed by `(privacyClass, destinationType)`. Every combination defaults to
**denied**. Enabling one is a deliberate toggle in settings with plain-language consequences, and
revocation is immediate.

### 5.2 Honest limitation

On-device models cannot currently match cloud models for image understanding or nuanced coaching
text. This means the privacy-maximal configuration is also the least capable one. The architecture
does not pretend otherwise — it makes the tradeoff **visible and per-category** so it is the user's
choice, made with real information, rather than a default buried in a settings screen. This tension
is discussed further in [`PRE_IMPLEMENTATION_REVIEW.md`](./PRE_IMPLEMENTATION_REVIEW.md) §2.

### 5.3 Cost and failure

Providers report token/credit usage where available; the audit log records it. Every AI call must
handle "unavailable" gracefully — an AI feature that breaks the screen when the model is offline is a
defect, since offline is the normal state of this app.

## 6. Storage architecture

### 6.1 Two stores, one owner

| Store | Holds | Encryption |
|---|---|---|
| SQLite database | All structured data, plus attachment *metadata* | Whole-file (SQLCipher), key from keychain |
| Encrypted file store | Photo and audio bytes, thumbnails | Per-file AES-256-GCM, file key wrapped by the master key |

A photo write is: encrypt bytes to `documents/media/<uuid>.enc` → insert an `attachment` row inside a
transaction → on transaction failure, delete the file. Deleting an attachment shreds the file, then
removes the row (P-10). Orphan scans run at startup to catch crash-interrupted writes in either
direction.

### 6.2 Key hierarchy

```
Device biometric / PIN
        │ unlocks
        ▼
OS Keychain / Keystore  ──────► Master Key (256-bit, hardware-backed where available)
                                     │
                    ┌────────────────┼────────────────────┐
                    ▼                ▼                    ▼
             DB encryption key   File key-wrapping   (Phase 5) sync identity key
                                       key
Backup passphrase ──Argon2id──► Backup key (independent; makes exports portable)
```

The backup key is deliberately *not* derived from the device key — otherwise a backup could only ever
be restored on the device that made it, which defeats the purpose.

## 7. Synchronization strategy (Phase 5, designed now)

Sync is not built in Phase 1, but three cheap decisions made now prevent an expensive migration later.

**Decisions taken now:**
1. Every table carries `device_id`, `revision`, `updated_at`, `deleted_at` (soft delete). Hard
   deletes are unsyncable — a deletion that leaves no trace cannot propagate.
2. IDs are **UUIDv7** — globally unique so two devices never collide, and time-sortable so they index
   as well as autoincrement integers.
3. Log-style tables are append-only, which makes them trivially mergeable.

**The Phase 5 design:**

- **Transport:** encrypted append-only event log. Each device pushes its outbox; each device pulls
  and applies others' entries.
- **Relay:** a dumb, zero-knowledge server (the user's own, or a shared folder / LAN peer). It stores
  ciphertext blobs and never holds a key. LAN-direct peer sync avoids a server entirely.
- **Conflicts:** last-writer-wins per field using a Hybrid Logical Clock, with append-only tables
  (XP ledger, timeline, habit entries) merging by union — no conflicts possible there by design.
  Field-level LWW is adequate because conflicts require the same user editing the same field on two
  devices while offline; that is rare, and the loser is preserved in a conflict log rather than
  discarded.
- **Bootstrap:** a new device restores from an encrypted backup, then catches up from the log.

## 8. Security approach

### 8.1 Threat model

| Threat | Mitigation | Status |
|---|---|---|
| Lost/stolen unlocked device | App lock (biometric/PIN), re-auth for sensitive sections, background snapshot blur | MVP |
| Lost/stolen locked device | Full-DB + per-file encryption, hardware-backed keys | MVP |
| Device backup exfiltration (iCloud/Google) | App storage excluded from OS backup; app backups separately encrypted | MVP |
| Another app on the device | OS sandbox + encryption at rest | MVP |
| Malicious/compromised network | Phase 1 makes no network calls; later, TLS + certificate validation, no plaintext anywhere | Phase 3+ |
| AI provider retaining data | Consent gate default-denied, minimisation, audit log, user-visible processing location | Phase 3 |
| Backup file theft | Passphrase-derived key, Argon2id, no key material in the file | MVP |
| Rooted/jailbroken device | Out of scope — documented honestly rather than pretended away |
| Compelled disclosure / coercion | Out of scope. A duress mode is a real feature, not a default; can be discussed later |

### 8.2 Practices

- Secrets never in source, never in logs, never in error messages. The logger redacts by
  allow-list — it logs known-safe fields rather than trying to filter unsafe ones, because
  deny-lists always miss something.
- All external input (backup files, imported data, AI responses) validated with a schema at the
  boundary before it becomes a typed object.
- SQL exclusively through parameterised statements. String-concatenated SQL fails lint.
- Dependencies kept minimal and audited; every new package that touches crypto, storage, or network
  needs a written justification in the PR.
- The app requests the narrowest OS permissions possible, at the moment of use, with an in-app
  explanation before the system prompt.

## 9. Performance approach

- SQLite in WAL mode; indexes on every foreign key and on the date columns the timeline and calendars
  filter by.
- All lists virtualized. The timeline pages backwards; it never loads a full history.
- Aggregates (XP total, level, streaks) are maintained incrementally on write and recomputable from
  the ledger, so reads are O(1) and correctness is always verifiable.
- Media thumbnails generated on capture; full images decrypted lazily and only when displayed.
- Heavy work (encryption, thumbnailing, audio analysis) runs off the UI thread.

## 10. Testing architecture

| Layer | Approach | Bar |
|---|---|---|
| Domain | Pure unit tests, no mocks needed | ≥ 90% coverage; every rule has a test |
| Repositories | Integration tests against a real temp SQLite file | Every query exercised |
| Use cases | Integration with in-memory repositories + a fake clock and a fake event bus | Happy path + every failure branch |
| Events | Contract tests: publishing X causes subscribers to do Y; redelivery is idempotent | Every event type |
| Migrations | Apply every migration to a fixture DB and assert schema + data survive | Every migration, forever |
| UI | React Native Testing Library on view models and critical screens | Critical paths only |
| E2E | Maestro flows on the acceptance criteria | Before each release |

Time is injected via a `Clock` interface. Streaks, schedules, and "today" logic are date-sensitive,
and tests that depend on the wall clock are tests that fail at midnight.

## 11. Platform expansion

Because the domain and application layers import no React Native APIs, expanding to web/desktop means
replacing the presentation layer and the platform adapters — not rewriting business logic. The
adapters that would need web/desktop implementations: SQLite driver, keychain, filesystem, camera,
microphone, biometrics. This is a real path, but it is Phase 6; nothing in Phase 1 is built *for* it
beyond keeping the domain clean, which is worth doing anyway.

## 12. Architecture decision record (initial)

| ID | Decision | Rationale | Alternatives rejected |
|---|---|---|---|
| ADR-1 | SQLite over a document store | Relational data, mature tooling, encryption available, ships with the platform | Realm (heavier, licensing history), WatermelonDB (adds a sync model we would not use), MMKV (not relational) |
| ADR-2 | Encrypted at rest via SQLCipher | Whole-file protection beats per-column discipline | Field-level encryption — one forgotten column is a permanent leak |
| ADR-3 | Repository pattern | Testability, swappable storage, a single place SQL can live | Direct queries in features — makes rule 3 unenforceable |
| ADR-4 | In-process typed event bus | Decouples features without distributed-system cost | Direct calls (couples features), a real queue (absurd for one process) |
| ADR-5 | Transactional outbox | Data and its events cannot diverge across a crash | Fire-and-forget events — silently corrupts XP |
| ADR-6 | UUIDv7 primary keys | Sync-ready, time-sortable, no collisions | Autoincrement ints (collide across devices), UUIDv4 (poor index locality) |
| ADR-7 | Soft deletes everywhere | Deletions must be syncable and recoverable | Hard deletes — unsyncable and unforgiving |
| ADR-8 | No DI container | One composition file is clearer at this scale | InversifyJS/tsyringe — ceremony without payoff here |
| ADR-9 | Expo Router | File-based, typed, deep links, standard in the ecosystem | React Navigation directly — more boilerplate, same result |
| ADR-10 | AI behind a single service | Makes privacy guarantees enforceable in one place | Per-feature SDK calls — guarantees become unverifiable |
| ADR-11 | No telemetry, at all | The privacy claim must have no exceptions | "Anonymous" analytics — nothing about this data is anonymous |
