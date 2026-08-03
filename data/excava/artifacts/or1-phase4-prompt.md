# OR-1 phase 4 — resolution — FINAL guideline — element type: prompt
> 2026-08-03T08:11:59.462689+00:00 · families used: DeepSeek V4, GLM-5.2, GPT-4o-mini, Kimi K2.7

## Ratchet (DeepSeek V4 · mistral/mistral-small-latest)

### **RESOLUTION OF WEAKNESSES INTO FINAL GUIDELINE**

#### **Resolved Weaknesses (with KEPT/FIXED/REJECTED decisions)**

1. **"Modularity/versioning are core to prompt quality"**
   - **Criticism:** Multiple reviewers (Ratchet, Sprocket, Overhaul) overemphasized modularity/versioning as *required* traits, conflating *process* (improvement tools) with *outcome* (prompt quality).
   - **Resolution:** **REJECTED as core requirement.**
     - Modularity/versioning are *optional enhancements* for iterative refinement, not guarantees of a GOOD prompt.
     - A prompt can be excellent without being reusable or versioned—it only needs to work *once*.

2. **"Tone constraints are universally necessary"**
   - **Criticism:** Proposals treated tone (e.g., "professional," "snarky") as a core constraint, but tone is subjective and often irrelevant unless *operationally defined* (e.g., "use contractions and em dashes").
   - **Resolution:** **FIXED.**
     - Tone constraints are *optional* and must be *anchored to concrete examples* (e.g., "rewrite this to sound like [example text]").
     - Vague tone directives (e.g., "sound better") are disqualifying.

3. **"Time sensitivity is ignored"**
   - **Criticism:** No proposal addressed how prompts degrade over time (e.g., outdated data, shifting norms).
   - **Resolution:** **KEPT as an implicit consideration.**
     - While not a disqualifier, prompts should avoid *time-sensitive references* unless explicitly noted (e.g., "as of [date]").
     - Reviewers should flag prompts relying on potentially outdated examples.

4. **"Observable signals like 'context-rich' or 'actionable' are unverifiable"**
   - **Criticism:** Terms like "context-rich" or "actionable" are subjective and lack measurable definitions.
   - **Resolution:** **FIXED.**
     - Replace vague terms with *specific, testable constraints*:
       - Instead of "add more detail," use: "Include at least 3 specific examples."
       - Instead of "be professional," use: "Use formal language (no contractions) and avoid first-person."
     - *Concrete examples* are now a *non-negotiable* requirement for GOOD prompts.

5. **"Ethical safeguards are mentioned but not verifiable"**
   - **Criticism:** Proposals disqualify harmful prompts but don’t define *how* to verify compliance.
   - **Resolution:** **FIXED.**
     - **Explicit disqualifiers:**
       - Requests for illegal, harmful, or unethical actions.
       - Prompts that *enable* harm (e.g., "help me bypass security").
     - **Verification method:**
       - If a prompt *could* plausibly lead to harm (even if unintended), it is disqualified unless *explicitly framed as safe* (e.g., "simulate a security test in a controlled environment").

6. **"'Testability' is circular (ambiguous prompts are disqualified by definition)"**
   - **Criticism:** "Testability" is tautological—if a prompt is

## Sprocket (GLM-5.2 · mistral/mistral-small-latest)

### **RESOLUTION OF WEAKNESSES INTO FINAL GUIDELINE**

#### **1. Modularity/Versioning as Core Traits (Raised by Ratchet, Sprocket, Gauge, Overhaul)**
- **WEAKNESS:** Multiple reviewers criticized the overemphasis on modularity and versioning as *core* requirements rather than *enhancements*.
- **RESOLUTION:** **REJECTED** as a disqualifying flaw. Modularity and versioning are valuable for iterative improvement but are not mandatory for a prompt to be "GOOD." They are now treated as *optional enhancements* in the final guideline.

#### **2. Tone Constraints as Universally Necessary (Raised by Ratchet, Sprocket, Gauge, Overhaul)**
- **WEAKNESS:** Tone constraints (e.g., "sound professional") are subjective and can introduce ambiguity unless anchored to concrete examples.
- **RESOLUTION:** **FIXED.** Tone constraints are now *optional* and must be *operationally defined* (e.g., "use contractions and em dashes") if included. Vague tone demands (e.g., "snarky millennial") are explicitly disqualifying unless clarified.

#### **3. Time Sensitivity (Raised by Ratchet, Sprocket)**
- **WEAKNESS:** Prompts may become ambiguous over time due to outdated references or shifting norms, but no mechanism addresses this.
- **RESOLUTION:** **REJECTED** as a disqualifying flaw. Time sensitivity is not a core requirement for prompt quality, but prompts should avoid *time-locked* constraints (e.g., "as of 2023") unless explicitly necessary. This is now a *best practice* note, not a rule.

#### **4. "Context-Richness" and "Actionability" as Unverifiable (Raised by Ratchet, Gauge, Overhaul)**
- **WEAKNESS:** Terms like "context-rich" and "actionable" are subjective and lack measurable signals.
- **RESOLUTION:** **FIXED.** "Context-richness" is replaced with *concrete examples* and *measurable constraints* (e.g., "include 3 bullet points summarizing X"). "Actionability" is defined as *a single, unambiguous task* with a clear call to action.

#### **5. Ethical Safeguards (Raised by Sprocket, Overhaul)**
- **WEAKNESS:** Ethical violations are mentioned but not clearly defined or verifiable.
- **RESOLUTION:** **FIXED.** Ethical safeguards are now *explicitly disqualifying* if the prompt:
  - Requests harmful, illegal, or unethical actions.
  - Enables bias, harassment, or misinformation *without safeguards*.
  - Lacks clarity in intent (e.g., "find a loophole" is ambiguous and risky).

#### **6. "Testability" as Uncheckable (Raised by Ratchet, Gauge, Overhaul)**
- **WEAKNESS:** "Testability" is mentioned but lacks a clear verification method.
- **RESOLUTION:** **FIXED.** Testability is now defined as:
  - Including *at least one concrete example* of desired output.

## Gauge (Kimi K2.7 · mistral/mistral-small-latest)

### **RESOLUTION OF WEAKNESSES INTO FINAL GUIDELINE**

#### **Resolved Weaknesses**

1. **"Modularity and versioning are overvalued as core traits."**
   - **FIXED:** Modularity and versioning are now treated as *optional enhancements* for iterative refinement, not mandatory qualities of a GOOD prompt. They are excluded from the core definition but mentioned as tools for improvement.

2. **"Tone constraints are subjective and can introduce ambiguity."**
   - **FIXED:** Tone constraints are now *optional* and must be *operationally defined* (e.g., "use contractions and em dashes" instead of "sound snarky"). If included, they must be paired with a concrete example to anchor expectations.

3. **"Time sensitivity is ignored."**
   - **REJECTED:** Time sensitivity is not included in the final guideline because it is not a universal requirement. A prompt’s relevance may decay, but this is a contextual factor, not a structural flaw in the prompt itself.

4. **"Observable signals like 'context-richness' and 'actionability' are unverifiable."**
   - **FIXED:** "Context-richness" and "actionability" are replaced with *concrete, measurable constraints* (e.g., "include at least three bullet points" or "rewrite this paragraph to sound more professional"). These are verifiable against the prompt’s output.

5. **"Ethical safeguards are mentioned but not defined."**
   - **FIXED:** Ethical violations (e.g., harmful, illegal, or unethical requests) are now an *outright disqualifier*. The guideline explicitly states that such prompts are rejected by default, with no ambiguity.

6. **"'Testability' is a circular requirement."**
   - **FIXED:** "Testability" is replaced with *predictable output*—a reviewer should be able to judge whether the AI’s response meets the prompt’s goals *without needing to guess intent*. This is anchored by concrete examples.

7. **"Over-constraint (e.g., 'use exactly 12 words') makes a prompt mediocre unless necessary."**
   - **KEPT:** Overly prescriptive constraints (e.g., rigid word counts) are explicitly labeled as *mediocre* unless the constraint is *demonstrably necessary* for the task. This balances precision with flexibility.

8. **"'Reusable structure' and 'versioning' are unverifiable without prior artifacts."**
   - **FIXED:** These are no longer core requirements. If included, they must be *optional metadata* (e.g., "v1" for tracking) rather than a rigid expectation.

9. **"'Context richness' is a buzzword with no measurable definition."**
   - **FIXED:** Replaced with *specific, task-relevant details* (e.g., "include the audience’s age range" or "cite at least two sources"). These are verifiable against the output.

10. **"Time sensitivity and decay of relevance are ignored."**
    - **REJECTED:** As above, this is not a universal flaw in prompt design. It is a contextual factor best handled by the prompt’s user, not a structural requirement.

---

### **FINAL GUIDELINE: WHAT MAKES A PROMPT GOOD

## Overhaul (GPT-4o-mini · mistral/mistral-small-latest)

### **RESOLUTION OF WEAKNESSES INTO FINAL GUIDELINE**

Below are the distinct weaknesses raised by reviewers, resolved as **KEPT**, **FIXED**, or **REJECTED**, with justification. Then follows the **FINAL GUIDELINE** as a ruling document.

---

#### **RESOLVED WEAKNESSES**

| **Weakness** | **Resolution** | **Rationale** |
|-------------|---------------|---------------|
| **Modularity/versioning as core requirements** | **REJECTED** | These are tools for iterative improvement, not inherent qualities of a prompt. They are now treated as *optional enhancements*, not disqualifiers or core traits. |
| **Tone constraints as universally necessary** | **FIXED** | Tone constraints are now *optional* and must be *operationally defined* (e.g., "use contractions and em dashes") to avoid subjectivity. Unanchored tone demands (e.g., "sound professional") are discouraged. |
| **Time sensitivity ignored** | **FIXED** | Added a clause requiring prompts to avoid reliance on *time-sensitive* references (e.g., "current events," "latest trends") unless explicitly anchored to verifiable sources. |
| **"Context-richness" as unverifiable** | **FIXED** | "Context-rich" is replaced with *measurable constraints* (e.g., "include 3 bullet points," "cite 2 sources"). Context must be tied to concrete, testable elements. |
| **"Reusable structure" as unverifiable** | **REJECTED** | Removed as a core requirement. Modularity is now framed as an *optional enhancement* for prompts intended for reuse, not a baseline trait. |
| **"Ethical safeguards" too vague** | **FIXED** | Explicitly disqualifies prompts that *request or enable* harmful/unethical actions. Includes a non-exhaustive list of red flags (e.g., hate speech, illegal requests, personal data exposure). |
| **"Testability" as uncheckable** | **FIXED** | Clarified that testability means the prompt must include *at least one concrete example of desired output* or *measurable constraints* (e.g., length, format) to enable verification. |
| **"Before/after" examples as non-essential** | **KEPT** | Examples are now *required* for GOOD prompts, but their form is flexible (e.g., side-by-side comparisons, input/output pairs). They anchor expectations and reduce ambiguity. |
| **Overly prescriptive constraints** | **FIXED** | Constraints must be *demonstrably necessary* (e.g., "limit to 50 words" only if the task requires it). Arbitrary limits (e.g., "exactly 12 words") are now MEDIOCRE unless justified. |
| **Subjective tone demands** | **REJECTED** | Tone constraints are now *optional* and must be *clearly defined* (e.g., "use active voice" vs. "sound snarky"). Unanchored tone requests are disqualified. |
| **"Jargon" as ambiguous** | **FIXED** | Jargon is defined as *domain-specific terms without explanation*. Prompts
