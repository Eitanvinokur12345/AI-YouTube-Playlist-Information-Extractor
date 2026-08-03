# OR-1 phase 4 — resolution — FINAL guideline — element type: connector
> 2026-08-03T08:21:03.250091+00:00 · families used: DeepSeek V4, GLM-5.2, GPT-4o-mini, Kimi K2.7

## Ratchet (DeepSeek V4 · mistral/mistral-small-latest)

### **Resolution of Weaknesses**

| **Weakness** | **Resolution** | **Reason** |
|--------------|---------------|------------|
| **Over-indexing on activity metrics (e.g., recent commits) as a proxy for reliability** | **FIXED** | Replaced with concrete maintenance artifacts (e.g., SLA adherence, CVE remediation time, uptime metrics). Activity metrics are now secondary to verifiable signals. |
| **Treating "intuitive design" and "cognitive load reduction" as subjective claims** | **FIXED** | Redefined as measurable outcomes: time-to-first-success in a sandbox, absence of manual steps, and clear error messages. Added "user testing" as an observable signal. |
| **Assuming "two-way communication" is always feasible for all connectors** | **FIXED** | Explicitly separated connectors by read-only vs. interactive use cases. Added "communication direction" as a required specification in the GOOD criteria. |
| **Security trade-offs being hand-waved (e.g., "universal adapter" bypassing OAuth)** | **FIXED** | Added a **non-negotiable security clause** in DISQUALIFIERS: "Hardcoded secrets, API keys, or tokens; violation of platform auth policies." |
| **Conflating activity metrics with maintenance quality** | **FIXED** | Replaced with **three maintenance signals**: (1) uptime ≥99.9%, (2) p99 latency <500ms, (3) CVE remediation time ≤7 days. Activity metrics are now optional context. |
| **Ignoring time-to-repair signals (e.g., 3-day SLA for critical bugs)** | **FIXED** | Added **SLA adherence** as a MEDIOCRE/DISQUALIFIER threshold: "Critical bug fixes must be addressed within 48 hours; otherwise DISQUALIFIED." |
| **Uncheckable signals like "respects user agency" or "just works"** | **FIXED** | Redefined as **observable behaviors**: (1) documented override options, (2) no silent failures (explicit error messages), (3) user testing pass rate ≥80%. |
| **Prioritizing technical rigor over user experience** | **FIXED** | Rebalanced the GOOD criteria to **50% technical (security, performance, interoperability) and 50% user-centric (usability, feedback, agency)**. |
| **Community trust (stars/reviews) being noisy** | **FIXED** | Removed as a primary signal. Replaced with **user-reported incidents** and **support response time** as observable metrics. |

---

### **FINAL GUIDELINE: Connector Quality Rubric**
*(The hub will use this to evaluate all connector elements.)*

#### **1. What GOOD Looks Like**
A connector is **GOOD** if it meets **all** of the following criteria:

**Technical Rigor (Non-Negotiable)**
- **Security:** No hardcoded secrets (API keys, tokens, passwords). Adheres to platform auth policies (OAuth 2.0, mTLS, or equivalent).
- **Interoperability:** Uses versioned endpoints (semantic version

## Sprocket (GLM-5.2 · mistral/mistral-small-latest)

### **Resolution of Weaknesses**

| **Weakness** | **Resolution** | **Reason** |
|--------------|---------------|------------|
| **Over-indexing on activity metrics (e.g., recent commits) as a proxy for reliability** | **FIXED** | Replaced with concrete maintenance artifacts (e.g., SLA adherence, CVE remediation time) and verifiable uptime/latency metrics. |
| **Treating "intuitive design" and "cognitive load reduction" as subjective claims** | **FIXED** | Defined measurable proxies (e.g., time-to-first-success in sandbox, absence of manual steps, clear error messages). |
| **Ignoring security trade-offs (e.g., "universal adapter" bypassing OAuth)** | **FIXED** | Explicitly listed "no hardcoded secrets" and "adherence to platform-wide auth standards" as disqualifiers. |
| **Conflating activity metrics with maintenance quality** | **FIXED** | Added explicit disqualifiers for connectors with unresolved critical issues or slow SLA responses. |
| **Uncheckable signals like "respects user agency" or "just works"** | **FIXED** | Redefined as observable outcomes (e.g., documented override options, absence of silent failures). |
| **Prioritizing technical rigor over user experience** | **FIXED** | Balanced the guideline to require *both* technical soundness *and* user-centric design, with equal weight. |
| **Missing explicit disqualifiers for security violations** | **FIXED** | Added "hardcoded secrets," "violation of platform auth standards," and "silent failures breaking downstream workflows" as disqualifiers. |
| **Ignoring time-to-repair signals (e.g., 3-day SLA for critical bugs)** | **FIXED** | Included "SLA adherence for critical issues" as a disqualifier if unmet. |
| **Subjective measures like "community trust" (stars/reviews) being noisy** | **FIXED** | Replaced with verifiable signals (e.g., uptime, test coverage, issue response time) and explicit disqualifiers for unresolved critical issues. |

---

### **FINAL GUIDELINE: Connector Quality Rubric**
*(The hub will use this to evaluate connectors. No further drafts or phases.)*

#### **1. What GOOD Looks Like**
A connector is **GOOD** if it meets **all** of the following:
- **Technical Soundness**
  - Adheres to platform-wide **authentication and authorization standards** (e.g., OAuth 2.0, no hardcoded secrets).
  - Provides **versioned API contracts** (e.g., OpenAPI/Swagger specs) and **measurable performance** (e.g., p99 latency <500ms, uptime ≥99.9%).
  - Includes **automated security checks** (e.g., dependency scans, no CVEs in critical paths).
- **Reliability**
  - Handles **edge cases gracefully** (e.g., retries, rate limit backoff, circuit breakers).
  - Provides **observable health signals** (e.g., uptime dashboards, test coverage ≥80%, recent activity

## Gauge (Kimi K2.7 · mistral/mistral-small-latest)

### **RESOLVED WEAKNESSES & FINAL RULING**

#### **1. Weakness: Over-indexing on activity metrics (e.g., Git commits) as a proxy for reliability**
- **Criticism raised by:** Ratchet, Sprocket, Gauge
- **Resolution:** **FIXED**
  - Activity metrics (e.g., recent commits, stars) are **not** standalone indicators of reliability.
  - **Added explicit thresholds:**
    - **GOOD:** Must demonstrate **recent, meaningful activity** (e.g., commits fixing critical issues, responsive issue triage) *and* **verifiable uptime/latency metrics** (≥99.9% uptime, p99 latency <500ms).
    - **MEDIOCRE:** Meets uptime/latency but lacks recent meaningful activity or has unresolved critical issues.
    - **DISQUALIFIED:** No activity for >6 months *or* activity consists solely of trivial changes (e.g., typo fixes) *without* addressing open issues.

---

#### **2. Weakness: Subjective claims (e.g., "intuitive design," "reduces cognitive load") with no audit trail**
- **Criticism raised by:** Ratchet, Gauge, Overhaul
- **Resolution:** **FIXED**
  - Replaced subjective terms with **observable proxies:**
    - **"Intuitive usability"** → **Time-to-first-success** (measured in sandbox testing; ≤5 minutes to complete a basic workflow).
    - **"Reduces cognitive load"** → **Clear error messages** (no silent failures; all errors include actionable guidance) *and* **no manual configuration steps** (defaults work out-of-the-box).
    - **"Respects user agency"** → **Override options documented in README** (e.g., environment variables for auth tokens) *and* **no forced defaults** (users can disable features).

---
#### **3. Weakness: Security trade-offs hand-waved (e.g., "universal adapter" vs. OAuth/no hardcoded secrets)**
- **Criticism raised by:** Ratchet, Gauge
- **Resolution:** **KEPT (strengthened)**
  - **DISQUALIFIED outright** if:
    - Hardcoded secrets (API keys, passwords) are present *or* required.
    - Violates platform-wide security policies (e.g., no OAuth 2.0 support).
  - **GOOD** must include:
    - **Security review artifacts** (e.g., dependency scans, CVE remediation time ≤7 days).
    - **Clear auth documentation** (e.g., "Uses OAuth 2.0; no secrets stored in config files").

---
#### **4. Weakness: "Two-way communication" assumed feasible for all connectors**
- **Criticism raised by:** Ratchet
- **Resolution:** **FIXED**
  - **GOOD** connectors must support **bidirectional sync** *only if the underlying tool supports it*.
  - **MEDIOCRE** if:
    - Read-only or fire-and-forget by design *but* lacks clear documentation of limitations.
  - **DISQUALIFIED** if:
    - Claims bidirectional sync but fails to deliver (e.g., syncs only in one direction).

---
#### **5.

## Overhaul (GPT-4o-mini · mistral/mistral-small-latest)

### **Resolution of Weaknesses**

| **Weakness Raised** | **Resolution** | **Reason** |
|---------------------|---------------|------------|
| **Activity metrics (e.g., commits) are unreliable proxies for reliability** | **FIXED** | Replaced with verifiable maintenance artifacts (e.g., SLA adherence, CVE remediation time, uptime ≥99.9%). |
| **"Intuitive design" and "cognitive load reduction" are uncheckable** | **FIXED** | Replaced with measurable proxies: time-to-first-success in sandbox, absence of manual steps, clear error messages, and documented override options. |
| **Security trade-offs are hand-waved (e.g., "universal adapters" bypassing OAuth)** | **FIXED** | Explicitly added "no hardcoded secrets" and "strict adherence to hub auth standards" as disqualifiers. |
| **Performance metrics (e.g., latency) are prioritized over usability** | **FIXED** | Balanced with reliability signals (uptime, retries, graceful failures) and user-centric checks (clear feedback, override options). |
| **Documentation depth is treated as a checklist rather than a usability signal** | **FIXED** | Documentation must include both technical specs (OpenAPI, changelogs) *and* user-facing signals (actionable error logs, setup time ≤10 minutes). |
| **"Two-way communication" is assumed feasible for all connectors** | **FIXED** | Clarified that connectors must align with their design (read-only, fire-and-forget, or bidirectional) and document limitations. |
| **Subjective claims like "respects user agency" lack audit trails** | **FIXED** | Defined "user agency" as *documented* override options and *measurable* absence of silent failures. |
| **Activity metrics conflated with maintenance quality** | **FIXED** | Replaced with concrete maintenance signals: recent critical bug fixes, SLA adherence, and responsive issue resolution. |
| **Time-to-repair signals (e.g., 3-day SLA for critical bugs) are ignored** | **FIXED** | Added explicit disqualifiers for connectors failing to meet repair SLAs. |
| **Community trust (stars/reviews) is noisy and uncheckable** | **FIXED** | Replaced with verifiable signals: uptime, test coverage, and documented issue resolution times. |

---

### **FINAL GUIDELINE: Connector Quality Rubric**
**Purpose:** This rubric determines whether a connector is **GOOD**, **MEDIOCRE**, or **DISQUALIFIED** for the hub. All evaluations must be based on **observable signals**—no subjective claims allowed.

---

#### **1. What GOOD Looks Like**
A connector is **GOOD** if it meets **all** of the following:
- **Security & Compliance:**
  - No hardcoded secrets (API keys, tokens, or credentials).
  - Strict adherence to hub-wide authentication (OAuth 2.0, API keys, or SSO) with no bypasses.
  - Passes dependency scans (no known CVEs in critical dependencies).
- **Reliability & Performance:**
  - Uptime ≥9
