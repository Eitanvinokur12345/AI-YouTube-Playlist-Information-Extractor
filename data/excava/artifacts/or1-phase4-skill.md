# OR-1 phase 4 — resolution — FINAL guideline — element type: skill
> 2026-08-03T08:03:09.303659+00:00 · families used: DeepSeek V4, GLM-5.2, GPT-4o-mini, Kimi K2.7

## Ratchet (DeepSeek V4 · mistral/mistral-small-latest)

### **FINAL GUIDELINE FOR WHAT MAKES A ‘SKILL’ ELEMENT GOOD**
*(Ratchet’s Resolution, Phase 4 – Final Ruling)*

---

### **1. WHAT GOOD LOOKS LIKE**
A **GOOD** skill element must:
- **Provide clear, immediate value** that is **measurable** (e.g., "reduces task time by 30%," "improves accuracy to 95%+") and **actionable** (one-click or minimal-setup usability).
- **Integrate seamlessly** with other tools/workflows without hidden dependencies or redundant effort (e.g., works with existing APIs, respects user’s toolchain).
- **Be reliable and efficient** (error rate <1%, response time <2s, no crashes under normal load) with **transparent logic** (users can inspect or audit how it works).
- **Adapt to user needs** through **customizable parameters** (e.g., adjustable thresholds, toggleable features) *without* compromising simplicity or integration.
- **Stay up-to-date** via **regular maintenance** (bug fixes, compatibility patches) and **clear versioning** (e.g., changelog, deprecation warnings).
- **Prioritize security and legality** (no malicious intent, no IP violations, no data leaks) and **document edge cases** (e.g., "fails gracefully if input is malformed").

**Example of a GOOD skill:**
*A "Text Summarizer" that:*
- Summarizes documents in one click with a configurable length (50–200 words).
- Integrates with Google Docs/Word via a plugin, syncing summaries automatically.
- Has <0.5% error rate, logs its processing steps, and updates monthly.
- Includes a quick-start guide *and* an advanced settings panel for power users.

---

### **2. WHAT MEDIOCRE LOOKS LIKE**
A **MEDIOCRE** skill element has **one or more** of these flaws:
- **Vague benefits** (e.g., "makes things better" without metrics).
- **High setup burden** (e.g., requires manual API keys, custom scripts, or niche dependencies).
- **Unreliable performance** (e.g., crashes 5% of the time, slow responses, inconsistent outputs).
- **Limited customization** (e.g., fixed settings that don’t adapt to user needs).
- **Poor documentation** (e.g., no changelog, missing edge-case warnings, or overly technical jargon).
- **Security/legal risks** (e.g., unclear data handling, no privacy policy).
- **Integration friction** (e.g., breaks existing workflows, requires workarounds).

**Example of a MEDIOCRE skill:**
*A "Data Cleaner" that:*
- Only works with a deprecated CSV format and requires Python scripting to use.
- Freezes when processing large files (>10MB) and lacks error handling.
- Has no updates in 2 years and no documentation beyond a 3-line README.

---

### **3. WHAT DISQUALIFIES AN ITEM OUTRIGHT**
A skill is **DISQUALIFIED** if it:
- **Causes harm** (e.g., spreads misinformation, enables bias, or

## Sprocket (GLM-5.2 · mistral/mistral-small-latest)

### **RESOLUTION DISCUSSION – FINAL GUIDELINE FOR ‘SKILL’ ELEMENTS**
*(Approved as the definitive standard for evaluation and integration)*

---

### **1. WHAT GOOD LOOKS LIKE**
A **GOOD** skill element is:
- **Actionable immediately**: It works out-of-the-box with minimal setup (e.g., one-click activation, clear prompts, or pre-configured defaults). Users can derive value within 30 seconds of encountering it.
- **Measurable in impact**: Its success is defined by quantifiable outcomes (e.g., "reduces task time by 20%," "achieves 95% accuracy on X dataset," "completes Y steps in under Z seconds"). Benchmarks or baseline comparisons must be provided.
- **Transparent in logic**: The skill’s decision-making is inspectable (e.g., audit trails, explainable prompts, or modular components that can be traced). Hidden dependencies or "black box" behavior are disqualifying.
- **Reliable and robust**: It handles edge cases gracefully (e.g., invalid inputs, partial data, or conflicting parameters) with error rates ≤5% and recovery paths (e.g., fallbacks, user prompts). Performance metrics (latency, throughput) are documented.
- **Seamlessly integrable**: It works within existing workflows without requiring users to adapt their tools or processes. APIs, hooks, or standard protocols (e.g., REST, CLI) are used for interoperability.
- **Customizable within bounds**: Users can adjust *non-critical* parameters (e.g., thresholds, output formats) without breaking core functionality or integration. Customization is gated to avoid complexity (e.g., "advanced mode" vs. default settings).
- **Secure and compliant**: It adheres to data protection standards (e.g., no logging of PII, encryption in transit), avoids IP infringement, and cannot be repurposed for malicious use (e.g., no jailbreaks, no bypassing safety filters).
- **Maintained and updated**: The skill has a clear update cadence (e.g., quarterly patches, changelog) and a mechanism for user feedback. Deprecation is announced 30 days in advance.
- **Provably beneficial**: Tangible value is demonstrated via user studies, A/B tests, or third-party validation (e.g., "reduces cognitive load by 30% in pilot tests"). Subjective claims (e.g., "users love it") are insufficient.

**Observable signals of GOOD:**
- A **README** with a 1-sentence value proposition, a 3-step quick-start guide, and a "how it works" section with diagrams or code snippets.
- **Metrics dashboard** (e.g., GitHub Actions, Prometheus) showing error rates, latency percentiles, and uptime.
- **Integration tests** demonstrating compatibility with at least 3 external tools (e.g., Slack, Notion, GitHub).
- **Changelog** with dated entries and version tags (e.g., SemVer).
- **User feedback loop** (e.g., a public issue tracker or survey link).

---

### **2. WHAT MEDIOCRE LOOKS LIKE**
A **MEDIOCRE** skill element is one that:
- **Works but is clunky**: Requ

## Gauge (Kimi K2.7 · mistral/mistral-small-latest)

### **FINAL GUIDELINE: What Makes a ‘Skill’ Element GOOD**

---

#### **1. What GOOD looks like**
A **GOOD** skill element must:

- **Deliver clear, immediate value** that is **actionable** (one-click usability or minimal setup) and **measurable** (success criteria are explicit and verifiable).
- **Work reliably** with minimal errors, high efficiency, and consistent performance across inputs.
- **Integrate seamlessly** with other tools or workflows without hidden dependencies or redundant work.
- **Be customizable** but not at the cost of simplicity—users should adjust core parameters without breaking functionality or integration.
- **Be transparent**—its logic, inputs, and outputs must be inspectable, and edge cases must be documented.
- **Stay relevant over time** through regular maintenance, updates, and adaptation to user needs.
- **Prioritize security and compliance**—it must not violate intellectual property, introduce malicious behavior, or cause ethical harm (e.g., bias, hallucinations).
- **Balance documentation** between quick-start guides (for actionability) and advanced tweaks (for customizability), with layered help to avoid overwhelming users.

---

#### **2. What MEDIOCRE looks like**
A **MEDIOCRE** skill element has **some** of the GOOD traits but falls short in key areas:

- **Partial value**—benefits exist but are vague, subjective, or hard to measure (e.g., "improves workflow" without specifics).
- **Inconsistent reliability**—errors occur under common conditions, or performance degrades with scale.
- **Weak integration**—works only in narrow contexts or requires manual workarounds to fit into broader workflows.
- **Limited customization**—offers rigid defaults with no way to adapt to user needs.
- **Poor transparency**—logic is opaque, or edge cases are undocumented, forcing users to guess.
- **Stagnant maintenance**—rarely updated, leaving gaps for bugs or outdated functionality.
- **Security risks**—relies on deprecated APIs, has unclear data handling, or lacks safeguards against misuse.
- **Over-documented or under-documented**—either a wall of text with no quick-start or a one-liner that omits critical details.

---

#### **3. What DISQUALIFIES an item outright**
A skill element is **DISQUALIFIED** if it:

- **Causes harm**—malicious, insecure, or violates intellectual property (e.g., scraping copyrighted data without permission).
- **Fails core functionality**—crashes frequently, produces incorrect results, or is unusable in basic scenarios.
- **Lacks transparency**—logic is intentionally obfuscated, or it hides dependencies that could disrupt workflows.
- **Requires excessive setup**—demands complex configuration, API keys, or tooling that most users won’t or can’t provide.
- **Introduces ethical risks**—reinforces bias, enables harassment, or generates harmful outputs (e.g., deepfakes, misinformation).
- **Breaks workflows**—updates or changes break existing integrations without backward compatibility.
- **Provides no measurable value**—claims of "tangible benefits" are unverifiable or purely aspirational.

---

#### **

## Overhaul (GPT-4o-mini · mistral/mistral-small-latest)

### **FINAL GUIDELINE: What Makes a "Skill" Element GOOD**
*(Resolved from Phase 2–4 discussions, incorporating all weaknesses and conflicts)*

---

### **1. WHAT GOOD LOOKS LIKE**
A **GOOD** skill element must meet **all** of the following criteria:

**A. Immediate Actionability & Measurable Value**
- The skill must deliver **clear, tangible benefits** that are **immediately usable** with minimal setup (e.g., one-click execution, no complex dependencies).
- Success must be **measurable** via predefined metrics (e.g., time saved, error reduction, output quality) that are **verifiable by the user or system**.
- **Example:** A skill that "summarizes long documents in 30 seconds with 95% accuracy" is good; one that "helps with writing" is not.

**B. Robustness & Reliability**
- The skill must **minimize errors** (e.g., crashes, incorrect outputs) and **handle edge cases** (e.g., unexpected inputs, API failures) gracefully.
- Performance must be **consistent and efficient** (e.g., response time <2s, no memory leaks).
- **Example:** A skill that "fails silently when given a 10MB file" is bad; one that "queues large files and notifies the user" is good.

**C. Seamless Integration & Modularity**
- The skill must **work independently** (modular) but also **combine smoothly** with other tools (e.g., APIs, workflows, plugins) without hidden dependencies.
- Integration must be **documented** (see *Transparency*).
- **Example:** A skill that "only works with Tool X" is bad; one that "exports data in JSON format for any tool" is good.

**D. Customizability (Without Sacrificing Simplicity)**
- Users must be able to **adjust key parameters** (e.g., output length, language, thresholds) **without breaking functionality**.
- Customization must be **intuitive** (e.g., dropdowns, sliders) and **non-destructive** (e.g., no manual config files).
- **Example:** A skill with "10+ advanced flags" is bad; one with "3 preset modes + one slider" is good.

**E. Transparency & Auditability**
- The skill’s **logic must be inspectable** (e.g., clear prompts, decision trees, or source code if applicable).
- **Documentation must be layered**:
  - **Quick-start guide** (1 paragraph: what it does, how to use it).
  - **Advanced tweaks** (optional, for power users).
  - **Error logs** (automatically generated, human-readable).
- **Example:** A skill with "no docs" is bad; one with "inline tooltips + a link to a 5-page manual" is good.

**F. Security, Legal Compliance & Ethical Safeguards**
- The skill must **not**:
  - Infringe on intellectual property (e.g., scraping copyrighted material).
  - Introduce security risks (e.g., exposing API keys).
  - Cause harm (e.g., bias, hallucinations, data leaks).
- **Example:**
