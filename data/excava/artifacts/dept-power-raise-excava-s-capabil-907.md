# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-907` (dept) · 2026-07-15T21:18:06.453969+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Switch EXCAVA’s worst 10% of prompts to Cerebras Llama 3.3 70B if quality hits 85% without collapses.

**Plan:**
1. Torque selects the worst 10% of EXCAVA prompts (10K+ tokens) for testing.
2. Run 500 prompts through Cerebras Llama 3.3 70B.
3. Measure quality against the 85% benchmark and check for prompt collapses.
4. If successful, Torque confirms the switch.
5. EXCAVA integrates Cerebras Llama 3.3 70B for the worst 10% of prompts.
6. Monitor performance for 48 hours before full rollout.

**What changed:**
EXCAVA’s worst 10% of prompts now use Cerebras Llama 3.3 70B instead of Llama 4 Maverick 12B.
