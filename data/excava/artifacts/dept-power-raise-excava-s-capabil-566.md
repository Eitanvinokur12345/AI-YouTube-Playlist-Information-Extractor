# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-566` (dept) · 2026-07-31T12:22:13.479566+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Run a 500-sample blind A/B test on EXCAVA comparing current model vs. Claude 3.7 Sonnet with frozen prompts and strict accuracy metric; if gain ≥0.4%, switch permanently.
**Plan:**
1. Prepare a 500-sample frozen prompt set from current EXCAVA task chains.
2. Configure Claude 3.7 Sonnet for integration with EXCAVA, ensuring compatibility and minimal disruption.
3. Execute a blind A/B test, splitting the 500 samples between the current model and Claude 3.7 Sonnet.
4. Evaluate test results using a strict accuracy metric to determine the gain from switching to Claude 3.7 Sonnet.
5. If the gain is ≥0.4%, permanently switch EXCAVA to utilize Claude 3.7 Sonnet.
**What changed:** The approach to upgrading EXCAVA's capability, now incorporating a rigorous testing process before committing to a new model.
