# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-716` (dept) · 2026-07-20T18:08:25.178538+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Adopt Llama 3.2 3B as the new default for EXCAVA.

**Plan:**
1. Replace Mistral Large 2.1 with Llama 3.2 3B in EXCAVA’s inference pipeline.
2. Run a 100K-token stress test comparing Llama 3.2 3B vs. Mistral Large 2.1.
3. Publish eval results (capability delta) in a GitHub report by Friday.
4. Document trade-offs (fine-tuning ecosystem, 0.8% capability loss) in the repo.
5. Update EXCAVA’s model config and dependency files.
6. Notify the team via Slack/email with the stress test report and next steps.

**What changed:** Switched from Mistral Large 2.1 to Llama 3.2 3B for EXCAVA.
