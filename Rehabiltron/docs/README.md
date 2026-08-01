# Rehabiltron

A privacy-first personal growth platform. Built primarily for one person — its owner — with an
architecture that can grow to many users without a rewrite.

---

## What it is

Rehabiltron is a private alternative to the current generation of personal improvement and coaching
apps. It tracks who you are trying to become and shows you whether you are getting there: goals,
habits, tasks, health, appearance, communication, productivity, and knowledge — with an XP and level
system that makes long-horizon progress visible day to day.

The difference from the apps that inspired it is not the feature list. It is that **your data never
leaves your device unless you personally decide it should**, per category, revocably, with the app
telling you exactly where every piece of processing happened.

## Goals

1. **Privacy is the product.** Progress photos, voice recordings, and journals are among the most
   sensitive data a person can generate. Local-first storage, encryption at rest, no telemetry, no
   accounts, no silent uploads. The default answer to "should this leave the device?" is no.
2. **Make invisible progress visible.** Personal growth fails because feedback is slow. XP, levels,
   streaks, timelines, and before/after comparisons compress months of change into something you can
   see this week.
3. **One coherent system, not eight apps.** Sleep, workouts, skin, speech, tasks, and reading all
   feed the same profile and the same progress model.
4. **Useful on day one, extensible for years.** Phase 1 must be a genuinely good habit-and-goals
   tracker on its own, before any AI is involved.
5. **Never lock the owner in.** Full export, readable formats, user-controlled backups.

## Non-goals

- Not a social network. No feeds, no followers, no comparison to strangers.
- Not a content library. Where high-quality material exists — books, papers, courses — the app links
  to it rather than reproducing it.
- Not a medical device. It gives no diagnoses and makes no clinical claims.
- Not ad-supported, not affiliate-funded, not data-monetized. There is no business model to protect,
  which is precisely what makes the privacy guarantees credible.

## Technology direction

| Layer | Choice | Why |
|---|---|---|
| App framework | React Native + Expo, TypeScript (strict) | One codebase for iOS/Android now, web/desktop later |
| Navigation | Expo Router (file-based) | Typed routes, deep links, minimal boilerplate |
| Local database | SQLite, encrypted at rest (SQLCipher) | Mature, relational, offline by nature, encrypts as a whole file |
| Files (photos/audio) | App-private filesystem, encrypted per file, referenced from the DB | Blobs never belong in a database; keeps the DB small and fast |
| Keys | OS keychain/keystore + passphrase-derived backup key | Hardware-backed where available |
| State | Local component state → module stores → repositories | UI holds no business logic |
| AI | Provider-agnostic `AiService` abstraction | Local, self-hosted, or external — swappable, per-category consent |
| Sync (future) | Encrypted append-only event log, zero-knowledge relay | Server can never read your data, by construction |
| Tests | Jest + React Native Testing Library; domain logic tested first | Business rules must be verifiable without a simulator |

Exact package versions are pinned when the project is scaffolded, not guessed in advance.

## Development philosophy

**Seams now, systems later.** The architecture puts hard boundaries in place from the first commit —
repositories, an event bus, an AI abstraction, a `user_id` on every user-scoped row — because those
are the things that cannot be added cheaply later. It does *not* build sync servers, plugin systems,
dependency-injection containers, or microservices for an app with one user. Complexity is paid for
only when a real requirement demands it.

The four rules that are never bent:

1. **UI contains no business logic.** Components render state and emit intent. Rules live in the
   domain layer, where they can be tested in milliseconds.
2. **No feature reaches into another feature's data.** Cross-feature communication happens through
   published events and public service interfaces only.
3. **All database access goes through repositories.** No SQL outside the data layer, ever.
4. **All AI calls go through the AI service.** No component, screen, or feature talks to a model
   provider directly — that is how privacy guarantees stay enforceable in one place.

Beyond those: small vertical slices, working software at the end of every sprint, and no phase that
leaves the app in a state where it cannot be opened and used.

## Documentation map

| Document | What it answers |
|---|---|
| [`MISSING_INFORMATION.md`](./MISSING_INFORMATION.md) | What still needs a decision, and what was assumed |
| [`PRODUCT_REQUIREMENTS.md`](./PRODUCT_REQUIREMENTS.md) | Every feature, MVP scope, privacy requirements |
| [`ARCHITECTURE.md`](./ARCHITECTURE.md) | System structure, modules, data flow, AI, sync, security |
| [`MVP_PLAN.md`](./MVP_PLAN.md) | Phase 1 sprint by sprint, and what comes after |
| [`DATABASE_DESIGN.md`](./DATABASE_DESIGN.md) | Entities, relationships, migrations, encryption |
| [`API_CONTRACTS.md`](./API_CONTRACTS.md) | Service interfaces, events, module communication, AI contracts |
| [`CODING_RULES.md`](./CODING_RULES.md) | TypeScript, testing, security, naming, organization |
| [`DEVELOPMENT_ROADMAP.md`](./DEVELOPMENT_ROADMAP.md) | Milestones, priorities, dependencies, order |
| [`PRE_IMPLEMENTATION_REVIEW.md`](./PRE_IMPLEMENTATION_REVIEW.md) | Risks, contradictions, readiness assessment |

## Project layout

```
Rehabiltron/
  docs/     architecture and product documentation (this folder)
  src/      application source — empty until Sprint 1 is approved
  tests/    test suites — empty until Sprint 1 is approved
```

## Status

**Foundation documentation complete. Implementation not started, pending approval and answers to the
five Critical questions in `MISSING_INFORMATION.md`.**
