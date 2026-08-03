# OR-1 phase 4 — resolution — FINAL guideline — element type: package
> 2026-08-03T08:31:47.058291+00:00 · families used: DeepSeek V4, GLM-5.2, GPT-4o-mini, Kimi K2.7

## Ratchet (DeepSeek V4 · mistral/mistral-small-latest)

### **Resolution of Weaknesses into Final Guideline**

Below are the distinct weaknesses raised by reviewers, resolved into the final guideline. For each, I state whether the criticism was **KEPT**, **FIXED**, or **REJECTED**, with justification.

---

#### **1. Overemphasis on Procedural Signals (CI Badges, Lockfiles) Over Outcome-Based Proof (Working Demos, Benchmarks)**
- **Criticism:** Multiple reviewers (Ratchet, Gauge, Overhaul) noted that procedural signals (e.g., green CI badges, lockfiles) are prioritized over verifiable outputs (e.g., working demos, input/output examples, benchmarks).
- **Resolution:** **KEPT** as a core issue. The final guideline elevates **demonstrable outputs** (working demos, input/output examples, benchmarks) to the top tier of GOOD criteria, ensuring that "solves a real problem" is the primary measure, not just "passes CI."

---

#### **2. Lack of Clear "One Specific Problem" Test**
- **Criticism:** Sprocket and Gauge emphasized that packages must solve *one clear, specific problem* (e.g., "generate product descriptions in 3 tones"), but the proposals didn’t enforce this strictly. Ratchet noted that generic signals (e.g., CI badges) could allow vague or overbroad packages to pass.
- **Resolution:** **FIXED**. The final guideline explicitly requires that GOOD packages must:
  - State a **single, well-defined problem** in the README.
  - Provide **verifiable outputs** (e.g., a working demo, input/output examples, or benchmarks) that prove the problem is solved.
  - Avoid vague claims (e.g., "improves AI responses" without examples).

---

#### **3. Ethical Checks Treated as Uniformly Critical**
- **Criticism:** Gauge and Overhaul argued that ethical safeguards (e.g., no hidden telemetry, input validation) should be non-negotiable for all packages, while Ratchet and Sprocket noted that some ethical checks (e.g., telemetry opt-outs) may be overkill for trivial or local tools.
- **Resolution:** **FIXED**. The final guideline splits ethical checks into **two tiers**:
  - **Tier 1 (Non-Negotiable for All Packages):** Input validation, no discriminatory data, clear license, and no malicious code.
  - **Tier 2 (Context-Dependent):** Telemetry opt-outs, rate limits, and data transparency are **required only if the package handles sensitive data or operates in a high-risk domain** (e.g., AI models, APIs). Local CLI tools are held to Tier 1 only.

---

#### **4. "Green CI Badge" as a Meaningless Signal**
- **Criticism:** Ratchet, Gauge, and Overhaul all noted that a "green CI badge" is unverifiable if the badge isn’t linked to the actual repo’s CI or if the CI is flaky.
- **Resolution:** **FIXED**. The final guideline replaces "green CI badge" with **two verifiable signals**:
  - **A linked CI status** (e.g., GitHub Actions badge that links to the actual workflow).
  - **Reproducible lockfile** (e.g.,

## Sprocket (GLM-5.2 · mistral/mistral-small-latest)

### **RESOLUTION DISCUSSION: FINAL GUIDELINE**
*(Resolving all weaknesses into a single, actionable standard)*

---

### **RESOLVED WEAKNESSES**

| **Weakness Raised** | **Resolution** | **Reasoning** |
|---------------------|---------------|---------------|
| **Overemphasis on procedural signals (CI badges, lockfiles) over outcome-based proof (demos, benchmarks)** | **FIXED** | Outcome-based signals (working demos, verifiable outputs) are now **tier-1 requirements** for GOOD. Procedural signals (CI, lockfiles) are **supporting evidence** but not sufficient alone. |
| **Ethical checks treated as optional or layered too late** | **FIXED** | Ethical/legal safeguards (input validation, license clarity, no hidden telemetry) are now **tier-1 disqualifiers** for all packages. They cannot be deferred. |
| **"Green CI badge" as a standalone GOOD signal** | **REJECTED** | CI badges are **only meaningful if linked to a passing test suite** that covers the package’s core functionality. Stale or unverified badges are ignored. |
| **Lack of "one specific problem" test** | **KEPT** | The "single, clearly defined problem" requirement is now **explicit** in GOOD criteria. Vague claims (e.g., "improves AI responses") are disqualified. |
| **Discoverability (searchable tags, naming) ignored** | **FIXED** | Discoverability is now a **tier-2 MEDIOCRE signal** (not disqualifying, but critical for usability). Poor naming/tags can downgrade a GOOD package to MEDIOCRE. |
| **Benchmarks treated as optional** | **FIXED** | Benchmarks or **demonstrable outputs** (e.g., input/output examples) are **required for GOOD** if the package claims performance improvements. For non-performance-critical tools, clear examples suffice. |
| **Static analysis/modularity overemphasized for simple tools** | **FIXED** | Modularity and static analysis are **tier-3 signals** (only relevant for MEDIOCRE/GOOD packages). They are **not disqualifiers** for simple tools. |
| **Ethical checks (e.g., no hidden telemetry) treated as equally critical for all packages** | **FIXED** | Ethical checks are **tier-1 for AI tools** (e.g., models, APIs) but **tier-2 for local CLI tools** (e.g., input validation is required, but telemetry opt-outs are optional). |
| **"Working demo" as a GOOD signal** | **KEPT** | A **working demo link** is now **required for GOOD** if the package is interactive (e.g., web UI, API). For non-interactive tools, input/output examples suffice. |
| **Merge order prioritizing usability over ethics** | **REJECTED** | The final order is **ethics → usability → specificity → modularity**. Ethical/legal checks are **non-negotiable tier-1 disqualifiers**. |

---

### **FINAL GUIDELINE: "GOOD / MEDIOCRE /

## Gauge (Kimi K2.7 · mistral/mistral-small-latest)

### **RESOLUTION OF WEAKNESSES INTO FINAL GUIDELINE**

Below is the resolution of each distinct weakness raised by the reviewers. For each, I state whether the criticism was **KEPT** (incorporated into the final guideline), **FIXED** (addressed with a refined or new rule), or **REJECTED** (rejected with justification).

---

#### **1. Overlap on "minimal friction" and "CI badges" without distinguishing AI tools vs. general software**
- **Criticism:** The proposals treat procedural signals (CI badges, lockfiles) as universally critical, ignoring that AI tools may need benchmarks or verifiable outputs more than CI badges.
- **Resolution:** **KEPT** — The final guideline separates **core usability signals** (minimal friction, CI badges) from **AI-specific signals** (verifiable outputs, benchmarks). CI badges are retained as a usability signal, but AI tools must also meet **AI-specific deliverables** (e.g., working demo, input/output examples). The guideline now explicitly states that **AI tools require verifiable outputs**, while general software tools require **CI badges and lockfiles**.

---

#### **2. Missing explicit requirement for a working demo or verifiable outputs**
- **Criticism:** None of the proposals explicitly require a **working demo** or **verifiable outputs** as a GOOD signal, despite Sprocket and Gauge emphasizing it.
- **Resolution:** **FIXED** — The final guideline **explicitly requires verifiable outputs** for GOOD status:
  - For **AI tools**: A working demo or input/output examples.
  - For **general software**: A working installation or reproducible test case.
  This replaces vague "signals" with **concrete, observable deliverables**.

---

#### **3. "Green CI badge" is meaningless without linked CI or context**
- **Criticism:** A "green CI badge" is unverifiable if it doesn’t link to the actual CI or if the CI is flaky.
- **Resolution:** **FIXED** — The final guideline **requires the CI badge to link to the actual CI pipeline** (e.g., GitHub Actions, GitLab CI) and **requires the CI to test the package’s core functionality** (not just a dummy test). If the CI badge is stale or unlinked, it **does not count** as a GOOD signal.

---

#### **4. Ethical checks treated as universally critical, even for non-sensitive tools**
- **Criticism:** Ethical checks like "no hidden telemetry" or "no discriminatory data" are overkill for trivial tools (e.g., a local CLI script).
- **Resolution:** **FIXED** — The final guideline **tiers ethical checks by risk**:
  - **Tier 1 (Non-negotiable for all packages):** Input validation, opt-outs for telemetry, clear license.
  - **Tier 2 (AI tools only):** No discriminatory data, benchmarks with sources, stated limitations.
  - **Tier 3 (High-risk tools):** Rate limits, audited training data.
  Packages failing Tier 1 are **DISQUALIFIED**; Tier 2/3 failures are **MEDIOCRE** unless they are AI tools, in which case they are **DISQUALIFIED**.

---

####

## Overhaul (GPT-4o-mini · mistral/mistral-small-latest)

### **RESOLVED WEAKNESSES & FINAL RULING**

Below are the distinct weaknesses raised by reviewers, resolved into the final guideline. Each point is addressed as **KEPT**, **FIXED**, or **REJECTED**, with justification.

---

#### **1. Overemphasis on procedural signals (CI badges, lockfiles) over outcome-based proof (demos, benchmarks)**
- **Criticism:** Proposals prioritize "green CI badges" or "reproducible lockfiles" over verifiable outputs like working demos or benchmarks.
- **Resolution:** **FIXED**
  - Procedural signals (CI, lockfiles) remain important but are **demoted to MEDIOCRE-tier** unless tied to outcome-based proof.
  - **GOOD** now requires **demonstrable outputs** (demo, input/output examples) or **transparent benchmarks** as a **tier-1 requirement**.
  - CI badges are **only meaningful if linked to a passing test suite** that covers core functionality (not just a dummy test).

---

#### **2. Ignoring "one specific problem" as a core requirement**
- **Criticism:** Proposals treat "solves one clear problem" as optional, allowing vague packages to pass.
- **Resolution:** **KEPT**
  - **GOOD** now explicitly requires a **single, well-defined problem** with **verifiable outputs** (e.g., "generates product descriptions in 3 tones").
  - Packages with **vague claims** (e.g., "improves AI responses") are **DISQUALIFIED**.

---
#### **3. Ethical checks treated as universally critical (e.g., "no hidden telemetry" for all packages)**
- **Criticism:** Proposals demand ethical safeguards (input validation, no telemetry) for **all** packages, even trivial CLI tools where they’re irrelevant.
- **Resolution:** **FIXED**
  - **Ethical checks are tiered by risk:**
    - **Tier 1 (DISQUALIFIER):** Input validation, license clarity, no malicious code.
    - **Tier 2 (GOOD signal):** Rate limits, opt-out telemetry, data transparency (only required for packages handling user data or sensitive inputs).
  - **Hidden telemetry** is a **DISQUALIFIER** only for packages that **collect or transmit user data**.

---
#### **4. "Green CI badge" as a meaningless signal**
- **Criticism:** A green CI badge can hide flaky tests or irrelevant test suites.
- **Resolution:** **FIXED**
  - **GOOD** requires:
    - A **CI badge linked to a test suite** that covers **core functionality** (not just linting or formatting).
    - The test suite must be **reproducible** (e.g., pinned dependencies in the lockfile).
  - Stale or unlinked badges are **DISQUALIFIED**.

---
#### **5. Discoverability (searchable tags, typed interfaces) ignored**
- **Criticism:** Proposals don’t treat discoverability as a disqualifier, allowing technically sound but invisible packages.
- **Resolution:** **KEPT**
  - **GOOD** requires:
    - **Searchable tags** (e.g., `ai-tools`, `productivity`,
