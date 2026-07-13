# Indefinite tool/engine access — real options (owner demand 2026-07-13, non-negotiable)

## The hard truth about your 6 Gemini keys
Six Gemini keys created **under the same Google account/project do NOT multiply your quota** —
Google rate-limits per *project*, not per *key*. So a 7th Gemini key changes nothing. That's why
I kept seeing 429s no matter how many keys existed. To get more capacity you need EITHER different
*providers*, OR a *paid pay-as-you-go* path, OR *local* models. Here are the honest options.

## Option A — Spread across DIFFERENT free providers (free, ~15 min, biggest quick win)
Each of these has its own independent free tier with its own quota. Adding one key from each
multiplies real capacity (the canary already rotates whatever's healthy):
- **Groq** — 2 keys already; free, very fast. (console.groq.com)
- **Cerebras** — key is dead (regenerate; cloud.cerebras.ai). Free, very fast.
- **Together AI** — free tier, many open models. (api.together.xyz)
- **Fireworks AI** — free tier. (fireworks.ai)
- **Cloudflare Workers AI** — generous free tier, one token, many models. (dash.cloudflare.com)
- **OpenRouter** — already have a key; some models are free.
- **Cohere / Mistral / SambaNova / NVIDIA NIM** — each a free tier.
Six *different-provider* keys ≫ six Gemini keys. This alone likely ends the quota problem for text.

## Option B — One small PAID pay-as-you-go gateway (truly "indefinite", ~$5-10, your call)
- **OpenRouter with a $5-10 credit balance**: one key, hundreds of models, you pay only per token
  used and you SET a hard spend cap. For EXCAVA's text-sized calls, $10 lasts a very long time and
  never "exhausts" like a free tier — it just draws down slowly. This is the closest thing to
  "access all tools indefinitely" from a single key. (You control the cap; it can't overspend.)

## Option C — LOCAL models on the free VPS (free + truly unlimited, needs Oracle)
- Once the Oracle Always-Free VM exists (R1), it can run **Ollama** with small open models
  (llama-3.2, qwen2.5) — **no quota at all**, runs on the free ARM box, 24/7. Unlimited text for
  free forever. This is the real endgame; it's gated only on the parents' Oracle step.

## Option D — Video/vision specifically (the one genuinely quota-hard thing)
Video WATCH needs a multimodal model; free options are thin. Best paths: a **fresh Gemini key on a
NEW Google account** (separate project = separate quota), or a small OpenRouter balance (Option B)
which includes multimodal models. Text tasks don't need this.

## My recommendation, ranked
1. **Now, free:** add one key each from **Cerebras (regen), Together, Cloudflare** — 15 minutes,
   ends the text-quota problem. Tell me the secret names; I wire them.
2. **If you'll spend a little:** a **$10 OpenRouter balance** = indefinite single-key access.
3. **Endgame, free:** the **Oracle VPS + Ollama** = unlimited local models, when parents are home.
Nothing here is required to keep running today — but Option 1 is the highest-leverage 15 minutes
you could spend on the project right now.
