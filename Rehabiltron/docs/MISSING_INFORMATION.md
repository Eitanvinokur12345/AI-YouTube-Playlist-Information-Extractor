# Missing Information Report — Rehabiltron

**Date:** 2026-08-01
**Stage:** Requirements audit (before implementation)
**Verdict:** Requirements are **sufficient to produce the foundation documentation**. They are
**not yet sufficient to write Sprint 1 code** — five Critical decisions must be confirmed first.

---

## How to read this report

Every item below is either:

- **Critical** — must be answered before development starts. Getting it wrong is expensive or
  impossible to reverse (data model, encryption, key custody, build pipeline).
- **Important** — should be decided soon, before the phase that depends on it. A wrong guess
  costs rework in one module, not the whole app.
- **Optional** — can be decided later without penalty.

For every Critical and Important item I have recorded a **stated default** in the documentation.
Defaults are marked in the docs as `ASSUMPTION (unconfirmed)` so nothing invented is ever mistaken
for a requirement. Confirming or overriding a default is a one-line answer; discovering a wrong
default after 3,000 lines of code is not.

**No requirement has been invented.** Where the brief was silent, the docs say so explicitly.

---

## Critical — answer before Sprint 1 code

### C-01 — Encrypted database vs. Expo Go development speed

The brief requires "encrypted storage where appropriate." A fully encrypted SQLite database
(SQLCipher) cannot run inside Expo Go — it needs a native module, which means a custom
development build (`expo prebuild` / EAS dev client) from day one. That changes the daily
development loop permanently and is painful to retrofit after a codebase exists.

Options:

| Option | Encryption at rest | Dev workflow | Notes |
|---|---|---|---|
| **A. SQLCipher full-DB encryption** (recommended) | Whole DB file encrypted | Custom dev client required | Strongest; every table protected by default |
| B. Plain SQLite + field-level encryption | Only columns you remember to encrypt | Expo Go works | Easy to leak data by forgetting a column |
| C. Plain SQLite + OS file protection only | Relies on device lock + OS sandbox | Expo Go works | Weakest; loses data if device is unlocked/rooted |

**Stated default:** Option A. Privacy is declared the highest priority, and B's failure mode
(forgetting to encrypt a column) is exactly the kind of silent leak this project exists to avoid.

**Question:** Confirm Option A, accepting that Expo Go is not usable and every device install goes
through a custom dev build?

---

### C-02 — Target platforms for the MVP, and your build capability

The brief says "mobile first" with later desktop/web. It does not say which mobile OS ships first,
and it does not say what hardware you have. This determines the build pipeline, the test devices,
and whether platform-locked features (Apple HealthKit, iOS Screen Time / Family Controls, Android
Health Connect) are even reachable.

**Questions:**
1. MVP target — iOS only, Android only, or both?
2. Do you have a Mac, and an Apple Developer account ($99/yr)? Without both, iOS device builds and
   TestFlight installs are not possible (EAS cloud builds reduce but do not remove this).
3. Which physical device(s) will you actually run this on day to day?

**Stated default:** Both iOS and Android via Expo, developed against whichever device you have,
with EAS Build for binaries. No platform-locked feature enters the MVP.

---

### C-03 — Encryption key custody and the recovery story

This is the single most irreversible decision in the project. Where does the key that decrypts your
data live?

| Option | Protects against | Fails when |
|---|---|---|
| **A. Device keystore only** (iOS Keychain / Android Keystore), unlocked by biometric/PIN | Lost/stolen device, other apps, OS backups | Device is lost **and** no backup exists → data gone |
| **B. User passphrase derives the key** (Argon2id), keystore caches it after unlock | Everything in A, plus device compromise and coerced unlock | You forget the passphrase → **data is permanently unrecoverable, by design** |
| C. Hybrid: keystore for daily use, passphrase required to restore a backup on a new device | Practical middle ground | Passphrase still required for migration |

**Stated default:** Option C. Daily use is biometric/PIN via the device keystore; the *backup and
future device-sync* key is derived from a passphrase you set once. This keeps everyday friction low
while making exports genuinely portable and end-to-end encrypted.

**Questions:**
1. Confirm Option C, or pick A or B?
2. Do you want an app-launch lock (biometric or PIN) in the MVP, or only on sensitive sections
   (progress photos, voice recordings, journals)?
3. Do you accept "forgot passphrase = data unrecoverable" for backups? There is no privacy-preserving
   way to offer a reset. If not, the only alternative is a recovery key you store yourself
   (printed/password manager) — which is the same problem moved one step away.

---

### C-04 — Single user now, multi-user later — confirm the semantics

The brief says "primarily for personal use, with architecture that can support future expansion to
multiple users." Two very different readings:

- **Reading A (assumed):** MVP has exactly one local profile, no accounts, no login server, no
  network identity. Multi-user readiness = every user-scoped table carries a `user_id` column and no
  code assumes a singleton. Adding users later is a feature, not a rewrite.
- **Reading B:** MVP should already support several profiles on one device (e.g. household), or
  already have an account system stubbed.

Reading B roughly doubles Phase 1 scope and adds auth, profile switching, and per-profile key
management immediately.

**Stated default:** Reading A.

**Question:** Confirm Reading A?

---

### C-05 — Where does "unlimited uploaded content" physically live?

"No artificial limits on uploaded content" is a product promise that collides with a phone's finite
storage. Progress photos, before/after comparisons, and voice recordings are the heaviest data in
this app, and the decision affects the database schema (whether attachments are addressable
off-device) — so it cannot be deferred past the schema.

Options:
- **A. Device-only storage** (recommended for MVP): no app-imposed cap; the app shows a storage
  breakdown and lets you export/offload manually. Ceiling is your device.
- **B. Device + user-controlled external target** (your NAS, your own server, an external drive over
  the Files app): unlimited in practice, but requires the sync/transport layer earlier.
- **C. Cloud storage:** rejected — conflicts with the privacy requirements unless it is your own
  self-hosted server, which is Option B.

**Stated default:** Option A for the MVP, with the attachment schema designed so Option B can be
added later without a migration (attachments already carry a location descriptor and an optional
remote reference).

**Question:** Confirm Option A for MVP?

---

## Important — decide before the phase that needs them

| # | Topic | Question | Stated default | Needed by |
|---|---|---|---|---|
| I-01 | Language & RTL | Is Hebrew (or any RTL language) needed in the UI? | **RTL-ready from day one**, English strings first, i18n scaffolding in place. RTL is cheap now and expensive to retrofit — I recommend building it in regardless of the answer. | Sprint 1 |
| I-02 | Health data sources | Integrate Apple HealthKit / Android Health Connect for sleep & workouts, or manual entry only? | Manual entry first; integrations behind a `HealthDataSource` interface added in Phase 2. Note: pulling health data *in* is compatible with privacy; it never leaves the device. | Phase 2 |
| I-03 | AI processing location | Which do you actually intend to use: on-device models, a self-hosted server (Ollama / LM Studio on your machine), or an external provider with your API key? | All three supported by the abstraction; **nothing leaves the device without explicit per-category opt-in**, default off. Every AI result displays where it was processed. | Phase 3 |
| I-04 | AI data classes | Which categories may *ever* leave the device if you opt in: photos? voice? journal text? metrics only? | Default: **none**. Each category is an individual, revocable toggle, off by default. | Phase 3 |
| I-05 | Sync topology | Your devices only via a self-hosted relay, direct LAN/peer sync, or a hosted service you run? How many devices? | Encrypted append-only event log, server is a zero-knowledge relay that never sees plaintext. Build in Phase 5. | Phase 5 |
| I-06 | XP economy | Level curve, XP per action, and whether XP can ever be *lost*. | Configurable curve, default `xp_to_next(n) = round(100 × 1.15^(n−1))`; **XP is never lost** (no punishment mechanics). Full spec in `PRODUCT_REQUIREMENTS.md`. | Sprint 4 |
| I-07 | Streaks & pressure | Should habit streaks have grace/repair days? | Yes — configurable grace days, no shaming copy. Streak mechanics can become genuinely harmful without an escape valve. | Sprint 4 |
| I-08 | Notifications | Local reminders in the MVP or later? | Later (Phase 2). Requires OS permission prompts that are better introduced after the core loop works. | Phase 2 |
| I-09 | Voice analysis scope | Which metrics matter most (volume, pace, pauses, filler words, confidence), and is on-device-only acceptable if it means lower accuracy? | On-device signal analysis (volume/pace/pauses) first, since it needs no model; transcription and "confidence" scoring are model-dependent and deferred. | Phase 4 |
| I-10 | Recommendations posture | Skincare/nutrition/product recommendations — informational only, or commercial/affiliate links? | Informational only, no affiliate links, no monetization, explicit "not medical advice" disclaimer. | Phase 3 |
| I-11 | Offline-only mode | Should the app be fully functional with networking disabled as a supported, tested mode? | Yes — offline is the default state; every network call is optional and user-triggered. | Sprint 1 |
| I-12 | Design language | Any visual direction, or is that mine to propose? | Mine to propose; dark-mode-first, high contrast, accessible (WCAG AA), no dark patterns. | Sprint 2 |
| I-13 | Progress photo sensitivity | Should photos be excluded from the OS photo gallery and OS cloud backups by default? | **Yes, all of it** — app-private storage, excluded from iCloud/Google backup, biometric gate, no previews in notifications. Called out because these photos may be intimate and the default OS behavior is wrong for this use case. | Phase 2 |

---

## Optional — decide later, no penalty

| # | Topic | Note |
|---|---|---|
| O-01 | Desktop/web target | Expo Web vs. Electron vs. Tauri. Not needed until Phase 6. |
| O-02 | Achievement & reward catalog | The content (which achievements exist, what rewards mean) can be authored anytime; the engine is generic. |
| O-03 | Knowledge library seeding | Which books/articles/courses to link initially, and whether entries are hand-curated or imported. |
| O-04 | Phone usage restriction depth | iOS Screen Time requires Apple's **Family Controls entitlement** (a manual approval request to Apple, frequently declined for personal apps). Android has fewer restrictions. Treat as research-then-decide. |
| O-05 | Widgets / watch app / wearables | Nice-to-have, large surface area. |
| O-06 | Multi-user rollout specifics | Invitations, sharing, permissions — only relevant if the app ever leaves personal use. |
| O-07 | Retention & auto-purge policy | Whether old data auto-archives. Default: keep everything, delete only on request. |
| O-08 | Branding | Name is fixed ("Rehabiltron"); icon, palette, typography open. |

---

## What I did **not** assume

To be explicit about the boundary between requirement and assumption:

- I did not assume any external service, account, or backend exists.
- I did not assume any AI provider, API key, or budget.
- I did not assume Hebrew/RTL is required (only that it should be *cheap to add*).
- I did not assume health integrations, notifications, or Screen Time access.
- I did not assume a monetization model, analytics, crash reporting, or telemetry of any kind.
  **Default: zero telemetry.** If you want crash reporting later, it needs its own privacy decision.
- I did not assume a deadline or effort budget, so the roadmap is ordered by dependency, not dates.

---

## Readiness

| Deliverable | Status |
|---|---|
| Foundation documentation (this set) | **Complete** — can be written under stated defaults |
| Sprint 1 implementation | **Blocked on C-01 … C-05** |

Answering the five Critical questions is a short conversation. Everything else can proceed under the
documented defaults and be revised in place.
