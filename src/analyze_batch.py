#!/usr/bin/env python3
"""
Batch analyzer for YouTube AI Skills Tracker.
Processes all pending videos newest_first.
Commits after each video.

Run from repo root: python3 src/analyze_batch.py [max_videos]
"""
import json
import os
import re
import sys
import glob
import shutil
import subprocess
import traceback
from datetime import datetime, timezone

WORK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime(2026, 6, 3, tzinfo=timezone.utc)


# ── AI Tool knowledge base ─────────────────────────────────────────────────────
AI_TOOLS = {
    'chatgpt': {'company': 'OpenAI', 'country': 'USA', 'category': 'productivity', 'open_source': False, 'target_tool': 'chatgpt', 'is_model': True},
    'gpt-4': {'company': 'OpenAI', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'chatgpt', 'is_model': True},
    'gpt-5': {'company': 'OpenAI', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'chatgpt', 'is_model': True},
    'gpt4o': {'company': 'OpenAI', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'chatgpt', 'is_model': True},
    'gpt-4o': {'company': 'OpenAI', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'chatgpt', 'is_model': True},
    'o1': {'company': 'OpenAI', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'chatgpt', 'is_model': True},
    'o3': {'company': 'OpenAI', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'chatgpt', 'is_model': True},
    'o4': {'company': 'OpenAI', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'chatgpt', 'is_model': True},
    'claude': {'company': 'Anthropic', 'country': 'USA', 'category': 'productivity', 'open_source': False, 'target_tool': 'claude', 'is_model': True},
    'claude code': {'company': 'Anthropic', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'claude', 'is_model': False},
    'claude sonnet': {'company': 'Anthropic', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'claude', 'is_model': True},
    'claude opus': {'company': 'Anthropic', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'claude', 'is_model': True},
    'claude haiku': {'company': 'Anthropic', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'claude', 'is_model': True},
    'gemini': {'company': 'Google', 'country': 'USA', 'category': 'productivity', 'open_source': False, 'target_tool': 'gemini', 'is_model': True},
    'gemini 2.5': {'company': 'Google', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'gemini', 'is_model': True},
    'gemini 2.0': {'company': 'Google', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'gemini', 'is_model': True},
    'grok': {'company': 'xAI', 'country': 'USA', 'category': 'productivity', 'open_source': False, 'target_tool': 'other', 'is_model': True},
    'llama': {'company': 'Meta', 'country': 'USA', 'category': 'code', 'open_source': True, 'target_tool': 'other', 'is_model': True},
    'deepseek': {'company': 'DeepSeek', 'country': 'China', 'category': 'code', 'open_source': True, 'target_tool': 'other', 'is_model': True},
    'mistral': {'company': 'Mistral AI', 'country': 'France', 'category': 'code', 'open_source': True, 'target_tool': 'other', 'is_model': True},
    'perplexity': {'company': 'Perplexity AI', 'country': 'USA', 'category': 'research', 'open_source': False, 'target_tool': 'perplexity', 'is_model': False},
    'copilot': {'company': 'Microsoft', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'cursor': {'company': 'Anysphere', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'windsurf': {'company': 'Codeium', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'github copilot': {'company': 'GitHub/Microsoft', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'replit': {'company': 'Replit', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'bolt': {'company': 'StackBlitz', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'lovable': {'company': 'Lovable', 'country': 'Sweden', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'v0': {'company': 'Vercel', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'n8n': {'company': 'n8n GmbH', 'country': 'Germany', 'category': 'automation', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'make': {'company': 'Make', 'country': 'Czech Republic', 'category': 'automation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'zapier': {'company': 'Zapier', 'country': 'USA', 'category': 'automation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'activepieces': {'company': 'Activepieces', 'country': 'USA', 'category': 'automation', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'midjourney': {'company': 'Midjourney', 'country': 'USA', 'category': 'image creation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'stable diffusion': {'company': 'Stability AI', 'country': 'UK', 'category': 'image creation', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'dall-e': {'company': 'OpenAI', 'country': 'USA', 'category': 'image creation', 'open_source': False, 'target_tool': 'chatgpt', 'is_model': False},
    'sora': {'company': 'OpenAI', 'country': 'USA', 'category': 'video creation', 'open_source': False, 'target_tool': 'chatgpt', 'is_model': False},
    'runway': {'company': 'Runway', 'country': 'USA', 'category': 'video creation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'kling': {'company': 'Kuaishou', 'country': 'China', 'category': 'video creation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'veo': {'company': 'Google', 'country': 'USA', 'category': 'video creation', 'open_source': False, 'target_tool': 'gemini', 'is_model': False},
    'hailuo': {'company': 'MiniMax', 'country': 'China', 'category': 'video creation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'pika': {'company': 'Pika Labs', 'country': 'USA', 'category': 'video creation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'invideo': {'company': 'InVideo', 'country': 'USA', 'category': 'video creation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'synthesia': {'company': 'Synthesia', 'country': 'UK', 'category': 'video creation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'heygen': {'company': 'HeyGen', 'country': 'USA', 'category': 'video creation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'elevenlabs': {'company': 'ElevenLabs', 'country': 'USA', 'category': 'music', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'suno': {'company': 'Suno AI', 'country': 'USA', 'category': 'music', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'udio': {'company': 'Udio', 'country': 'USA', 'category': 'music', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'mcp': {'company': 'Anthropic', 'country': 'USA', 'category': 'integration', 'open_source': True, 'target_tool': 'claude', 'is_model': False},
    'model context protocol': {'company': 'Anthropic', 'country': 'USA', 'category': 'integration', 'open_source': True, 'target_tool': 'claude', 'is_model': False},
    'notion ai': {'company': 'Notion', 'country': 'USA', 'category': 'productivity', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'grammarly': {'company': 'Grammarly', 'country': 'USA', 'category': 'writing', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'jasper': {'company': 'Jasper AI', 'country': 'USA', 'category': 'writing', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'copy.ai': {'company': 'Copy.ai', 'country': 'USA', 'category': 'writing', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'descript': {'company': 'Descript', 'country': 'USA', 'category': 'video creation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'krea': {'company': 'Krea AI', 'country': 'USA', 'category': 'image creation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'ideogram': {'company': 'Ideogram', 'country': 'USA', 'category': 'image creation', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'flux': {'company': 'Black Forest Labs', 'country': 'Germany', 'category': 'image creation', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'canva ai': {'company': 'Canva', 'country': 'Australia', 'category': 'design', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'adobe firefly': {'company': 'Adobe', 'country': 'USA', 'category': 'design', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'figma ai': {'company': 'Figma', 'country': 'USA', 'category': 'design', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'genspark': {'company': 'Genspark', 'country': 'USA', 'category': 'research', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'manus': {'company': 'Manus', 'country': 'China', 'category': 'agents', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'langchain': {'company': 'LangChain Inc.', 'country': 'USA', 'category': 'agents', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'autogen': {'company': 'Microsoft', 'country': 'USA', 'category': 'agents', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'crewai': {'company': 'CrewAI', 'country': 'USA', 'category': 'agents', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'google ai studio': {'company': 'Google', 'country': 'USA', 'category': 'productivity', 'open_source': False, 'target_tool': 'gemini', 'is_model': False},
    'notebooklm': {'company': 'Google', 'country': 'USA', 'category': 'research', 'open_source': False, 'target_tool': 'gemini', 'is_model': False},
    'google notebooklm': {'company': 'Google', 'country': 'USA', 'category': 'research', 'open_source': False, 'target_tool': 'gemini', 'is_model': False},
    'google vids': {'company': 'Google', 'country': 'USA', 'category': 'video creation', 'open_source': False, 'target_tool': 'gemini', 'is_model': False},
    'whisk': {'company': 'Google', 'country': 'USA', 'category': 'image creation', 'open_source': False, 'target_tool': 'gemini', 'is_model': False},
    'perplexity ai': {'company': 'Perplexity AI', 'country': 'USA', 'category': 'research', 'open_source': False, 'target_tool': 'perplexity', 'is_model': False},
    'you.com': {'company': 'You.com', 'country': 'USA', 'category': 'research', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'openrouter': {'company': 'OpenRouter', 'country': 'USA', 'category': 'integration', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'groq': {'company': 'Groq', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'together ai': {'company': 'Together AI', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'replicate': {'company': 'Replicate', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'pinecone': {'company': 'Pinecone', 'country': 'USA', 'category': 'integration', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'weaviate': {'company': 'Weaviate', 'country': 'Netherlands', 'category': 'integration', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'supabase': {'company': 'Supabase', 'country': 'USA', 'category': 'code', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'dify': {'company': 'Dify', 'country': 'USA', 'category': 'agents', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'flowise': {'company': 'FlowiseAI', 'country': 'USA', 'category': 'agents', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'voiceflow': {'company': 'Voiceflow', 'country': 'Canada', 'category': 'agents', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'tabnine': {'company': 'Tabnine', 'country': 'Israel', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'codeium': {'company': 'Codeium', 'country': 'USA', 'category': 'code', 'open_source': False, 'target_tool': 'other', 'is_model': False},
    'aider': {'company': 'Aider AI', 'country': 'USA', 'category': 'code', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'continue': {'company': 'Continue Dev', 'country': 'USA', 'category': 'code', 'open_source': True, 'target_tool': 'other', 'is_model': False},
    'openai': {'company': 'OpenAI', 'country': 'USA', 'category': 'productivity', 'open_source': False, 'target_tool': 'chatgpt', 'is_model': False},
    'anthropic': {'company': 'Anthropic', 'country': 'USA', 'category': 'productivity', 'open_source': False, 'target_tool': 'claude', 'is_model': False},
}

# AI relevance keywords
AI_KEYWORDS = {
    'ai', 'artificial intelligence', 'machine learning', 'deep learning', 'neural',
    'llm', 'large language model', 'gpt', 'claude', 'gemini', 'chatgpt', 'copilot',
    'automation', 'agent', 'agentic', 'prompt', 'prompting', 'rag', 'embedding',
    'midjourney', 'stable diffusion', 'dall-e', 'sora', 'runway', 'elevenlabs',
    'suno', 'cursor', 'windsurf', 'replit', 'bolt', 'lovable', 'n8n', 'make.com',
    'zapier', 'openai', 'anthropic', 'google ai', 'perplexity', 'deepseek', 'llama',
    'mistral', 'hugging face', 'mcp', 'model context protocol', 'vibe coding',
    'langchain', 'autogen', 'crewai', 'multi-agent', 'multiagent', 'agi',
    'gpt-4', 'gpt-5', 'gpt4', 'claude code', 'claude 3', 'claude 4',
    'generative ai', 'gen ai', 'genai', 'chatbot', 'voiceflow', 'flowise',
    'dify', 'heygen', 'synthesia', 'invideo', 'descript', 'kling', 'hailuo', 'pika',
    'genspark', 'manus', 'ideogram', 'flux', 'krea', 'canva ai', 'adobe firefly',
    'figma ai', 'github copilot', 'tabnine', 'codeium', 'v0.dev',
    'notebooklm', 'google vids', 'whisk', 'imagen', 'veo', 'grok',
    'openrouter', 'together ai', 'groq', 'fireworks ai', 'replicate',
    'activepieces', 'pipedream', 'vertex ai', 'bedrock', 'azure ai',
    'function calling', 'tool use', 'system prompt', 'context window',
    'fine-tuning', 'fine tuning', 'training', 'inference', 'token',
    'vector database', 'pinecone', 'weaviate', 'chroma', 'supabase',
    'ai search', 'ai assistant', 'ai tool', 'ai workflow', 'ai agent',
    'ai model', 'ai image', 'ai video', 'ai music', 'ai writing',
    'ai coding', 'ai code', 'ai automation', 'ai productivity',
}

NON_AI_DISQUALIFIERS = [
    ('cooking', ['recipe', 'ingredient', 'bake', 'cook', 'food']),
    ('fitness', ['workout', 'exercise', 'gym', 'muscle', 'diet']),
    ('sports commentary', ['football match', 'basketball game', 'score', 'player stats']),
    ('religion', ['prayer', 'jesus', 'allah', 'bible', 'quran', 'spiritual']),
]


def load_json(path, default=None):
    full = os.path.join(WORK_DIR, path)
    if os.path.exists(full):
        with open(full) as f:
            return json.load(f)
    return default if default is not None else {}


def save_json(path, data):
    full = os.path.join(WORK_DIR, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')


def is_relevant(video):
    text = ' '.join([
        video.get('title') or '',
        video.get('description') or '',
        video.get('transcript') or '',
    ]).lower()

    # Check strong AI signals
    ai_hits = sum(1 for kw in AI_KEYWORDS if kw in text)
    if ai_hits >= 2:
        return True
    if ai_hits == 1:
        # One AI keyword but check for obvious non-AI disqualifiers
        for topic, signals in NON_AI_DISQUALIFIERS:
            if sum(1 for s in signals if s in text) >= 2:
                return False
        return True
    return False


def compute_age_months(published_at):
    try:
        pub = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
        delta = TODAY - pub
        return max(0, delta.days / 30.0)
    except Exception:
        return 12.0


def rate_quality(video):
    transcript_source = video.get('transcript_source', 'title')
    transcript = video.get('transcript', '') or ''
    description = video.get('description', '') or ''
    title = video.get('title', '') or ''

    if transcript_source == 'title':
        content_rating = 2
    else:
        text = description or transcript
        text_lower = text.lower()
        text_len = len(text)

        content_rating = 3  # base

        # Length bonus
        if text_len > 800:
            content_rating += 2
        elif text_len > 400:
            content_rating += 1

        # Specific tool mentions
        tool_hits = sum(1 for tool in AI_TOOLS if tool in text_lower)
        content_rating += min(tool_hits, 2)

        # Instructional keywords
        instructional = ['step', 'how to', 'tutorial', 'guide', 'workflow', 'tip', 'trick',
                        'demo', 'example', 'build', 'create', 'implement', 'integrate']
        inst_hits = sum(1 for w in instructional if w in text_lower)
        content_rating += min(inst_hits, 2)

        # Hype/clickbait negative signals
        hype = ['game changer', 'changed my life', 'insane', 'shocked', 'mind-blowing',
                'secret', 'no one tells', 'millionaire', 'rich', 'passive income',
                'make money', 'earn money', 'side hustle', '100k', '10x']
        hype_hits = sum(1 for w in hype if w in text_lower)
        content_rating -= min(hype_hits, 2)

        content_rating = max(2, min(8, content_rating))

    # Recency penalty
    age_months = compute_age_months(video.get('publishedAt', ''))
    if age_months <= 6:
        penalty = 0
    elif age_months <= 12:
        penalty = 1
    elif age_months <= 24:
        penalty = 2
    else:
        penalty = 3

    score = max(1, min(10, content_rating - penalty))
    reason = (f"src={transcript_source}, content={content_rating}, "
              f"age={age_months:.1f}mo, penalty=-{penalty} → score={score}")
    return score, reason


def make_slug(name, existing_slugs):
    slug = re.sub(r'[^a-z0-9\s-]', '', name.lower())
    slug = re.sub(r'\s+', '-', slug.strip())
    slug = re.sub(r'-+', '-', slug).strip('-')
    slug = slug or 'ai-tool'

    base = slug
    counter = 2
    while slug in existing_slugs:
        slug = f"{base}-{counter}"
        counter += 1
    existing_slugs.add(slug)
    return slug


def describe_tool(name, info):
    cat = info.get('category', 'productivity')
    company = info.get('company', 'a tech company')
    d = {
        'code': f'It assists with software development, code generation, and debugging tasks.',
        'automation': f'It automates workflows and integrates multiple applications without code.',
        'agents': f'It enables building and deploying AI agents and multi-agent systems.',
        'image creation': f'It generates and edits images using AI technology.',
        'video creation': f'It creates and edits videos using generative AI.',
        'writing': f'It assists with content writing, editing, and copywriting at scale.',
        'marketing': f'It helps with marketing campaigns and content creation.',
        'social': f'It assists with social media management and engagement.',
        'music': f'It generates and edits music and audio using AI.',
        'integration': f'It integrates AI capabilities into other tools and workflows.',
        'research': f'It assists with research, search, and information retrieval.',
        'productivity': f'It enhances productivity through AI-powered features and automation.',
        'design': f'It assists with visual design tasks using AI capabilities.',
        'other': f'It provides AI-powered capabilities for diverse tasks.',
    }
    return d.get(cat, f'It provides AI capabilities for {cat} tasks.')


def extract_tools_from_text(text):
    text_lower = text.lower()
    found = {}
    # Sort by length descending to match longer keys first (e.g., "claude code" before "claude")
    for tool_key in sorted(AI_TOOLS.keys(), key=len, reverse=True):
        pattern = r'(?<![a-z0-9])' + re.escape(tool_key) + r'(?![a-z0-9])'
        if re.search(pattern, text_lower):
            display = tool_key.title()
            if display not in found:
                found[display] = {**AI_TOOLS[tool_key], 'key': tool_key}
    return found


def extract_tips(text, tool_key):
    tips = []
    tool_lower = tool_key.lower()
    sentences = re.split(r'(?<=[.!?])\s+', text)
    for sent in sentences:
        sent = sent.strip()
        if tool_lower in sent.lower() and 20 < len(sent) < 180:
            if any(w in sent.lower() for w in ['use', 'create', 'build', 'help', 'can', 'will',
                                                 'try', 'learn', 'improve', 'generate', 'make']):
                tips.append(sent[:150])
                if len(tips) >= 2:
                    break
    return tips


def create_news_summary(title, description, transcript_source):
    desc = (description or title or '').strip()
    desc = re.sub(r'https?://\S+', '', desc)
    desc = re.sub(r'\s+', ' ', desc).strip()
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', desc) if len(s.strip()) > 15]
    if len(sentences) >= 2:
        return ' '.join(sentences[:2])
    elif sentences:
        s = sentences[0]
        if len(s) < 80:
            return f"{s} Video covers AI tools and techniques for practitioners."
        return s
    return f"{title}. AI content video featuring tools and techniques."


def dedup_list(lst):
    seen = set()
    result = []
    for item in lst:
        k = str(item).lower()
        if k not in seen:
            seen.add(k)
            result.append(item)
    return result


def merge_compat(c1, c2):
    merged = {}
    for c in c1 + c2:
        k = c['tool'].lower()
        if k not in merged:
            merged[k] = c.copy()
        else:
            v1 = merged[k].get('up_to_version', 'any')
            v2 = c.get('up_to_version', 'any')
            if v1 == 'any' and v2 != 'any':
                merged[k]['up_to_version'] = v2
    return list(merged.values())


def write_skill_md(skill, video):
    if skill.get('quality_score', 0) < 5:
        return
    slug = skill['slug']
    target_tool = skill.get('target_tool', 'claude')

    if target_tool == 'claude':
        folder = os.path.join(WORK_DIR, f'skills/{slug}')
    else:
        folder = os.path.join(WORK_DIR, f'other-skills/{target_tool}/{slug}')

    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, 'SKILL.md')
    if os.path.exists(path):
        return  # Don't overwrite

    video_id = video.get('video_id', '')
    title = video.get('title', '')
    channel = video.get('channel_name', '')
    tips = skill.get('tips', [])
    techniques = tips[:3] if tips else [f'Use {skill["skill_name"]} in your AI workflow']

    content = f"""---
name: {slug}
description: "Use {skill['skill_name']} for {skill.get('category', 'AI')} tasks — {skill.get('use_case', 'AI tool for productivity')[:80]}"
---

# {skill['skill_name']}

## Overview
{skill.get('description', f'{skill["skill_name"]} is an AI tool for {skill.get("category", "productivity")} tasks.')}

## Key Techniques
{chr(10).join(f'- {t}' for t in techniques)}

## How to Apply
{skill.get('use_case', f'Apply {skill["skill_name"]} to your AI workflow as demonstrated in the source video.')}

## Examples
{skill.get('output', f'{skill["skill_name"]} generates outputs relevant to {skill.get("category", "AI")} use cases.')}

## Source
Extracted from: [{title}](https://www.youtube.com/watch?v={video_id})
Channel: {channel}
"""
    with open(path, 'w') as f:
        f.write(content)


def process_video(video, index_data):
    """Full processing of one video. Updates all data files."""
    video_id = video['video_id']
    title = video.get('title', '') or ''
    now = datetime.now(timezone.utc).isoformat()

    # ── Relevance gate ───────────────────────────────────────────────────────
    if not is_relevant(video):
        # Move + update status
        _move(video_id)
        status = load_json('data/status.json', {})
        rr = status.setdefault('run_report', {})
        rr['skipped_not_relevant'] = rr.get('skipped_not_relevant', 0) + 1
        rr['pending_to_analyze'] = max(0, len(glob.glob(os.path.join(WORK_DIR, 'data/_pending/*.json'))) - 1)
        status['last_analyze'] = now
        save_json('data/status.json', status)
        return {'skipped': True, 'skills_added': 0}

    # ── Quality rating ───────────────────────────────────────────────────────
    vqs, vq_reason = rate_quality(video)
    low_quality = vqs < 5

    # ── Extract tools ────────────────────────────────────────────────────────
    full_text = ' '.join([
        video.get('title') or '',
        video.get('description') or '',
        video.get('transcript') or '',
    ])
    found_tools = extract_tools_from_text(full_text)

    # ── Tab 1: Skills ────────────────────────────────────────────────────────
    skills_data = load_json('data/skills.json', {'videos_seen': [], 'skills': []})
    deleted_skills = load_json('data/deleted_skills.json', [])
    existing_slugs = set(index_data.keys())
    skills_added = 0
    # within_video_slugs: only avoid duplicates WITHIN the current video's new skills,
    # NOT against the global index (which would cause -2, -3, etc. instead of proper dedup)
    within_video_slugs = set()
    new_skills = []
    for display_name, info in found_tools.items():
        slug = make_slug(display_name, within_video_slugs)  # only dedup within this video
        # Check if slug collision with global index
        if slug in existing_slugs:
            existing_skill = next((s for s in skills_data['skills'] if s['slug'] == slug), None)
            if existing_skill and (existing_skill.get('starred') or existing_skill.get('locked')):
                continue  # frozen

        base_score = 7 if info.get('category') in ['code', 'automation', 'agents', 'integration'] else 6
        if low_quality:
            base_score = min(base_score, vqs)

        target = info.get('target_tool', 'claude')
        if target == 'claude':
            compat = [{'tool': 'Claude', 'up_to_version': 'any'}]
        elif target == 'chatgpt':
            compat = [{'tool': 'ChatGPT', 'up_to_version': 'any'}]
        elif target == 'gemini':
            compat = [{'tool': 'Gemini', 'up_to_version': 'any'}]
        elif target == 'perplexity':
            compat = [{'tool': 'Perplexity', 'up_to_version': 'any'}]
        else:
            compat = [{'tool': display_name, 'up_to_version': 'any'}]

        tips = extract_tips(full_text, info.get('key', display_name.lower()))

        skill = {
            'skill_name': display_name,
            'slug': slug,
            'category': info.get('category', 'productivity'),
            'description': f'{display_name} is an AI tool by {info.get("company", "Unknown")}. {describe_tool(display_name, info)}',
            'use_case': f'Using {display_name} for {info.get("category", "AI productivity")} tasks.',
            'output': f'{display_name} produces {info.get("category", "AI")}-focused outputs.',
            'quality_score': base_score,
            'model_version': None,
            'company': info.get('company', 'Unknown'),
            'country': info.get('country'),
            'open_source': info.get('open_source', False),
            'target_tool': target,
            'is_claude_skill': target == 'claude' or 'anthropic' in (info.get('company') or '').lower(),
            'compatibility': compat,
            'multi_tool': False,
            'source_type': 'youtube',
            'source_url': f'https://www.youtube.com/watch?v={video_id}',
            'source_video_id': video_id,
            'tips': tips,
            'slash_commands': [],
            'general_tips': [],
            'relevance': f'{display_name} is featured as an AI tool in this video.',
            'popularity_signals': [],
            'endorsement_video_ids': [video_id],
            'video_quality_score': vqs,
            'low_quality_source': low_quality,
        }
        new_skills.append(skill)

    # Dedup and merge
    for skill in new_skills:
        slug = skill['slug']
        if slug in index_data:
            existing = next((s for s in skills_data['skills'] if s['slug'] == slug), None)
            if existing and not (existing.get('starred') or existing.get('locked')):
                ns = skill.get('quality_score', 0)
                os_ = existing.get('quality_score', 0)
                nv = skill.get('video_quality_score', 0)
                ov = existing.get('video_quality_score', 0)
                if ns > os_ or (ns == os_ and nv > ov):
                    # New is better: merge and replace
                    keeper = skill.copy()
                    keeper['tips'] = dedup_list(skill.get('tips', []) + existing.get('tips', []))
                    keeper['slash_commands'] = dedup_list(skill.get('slash_commands', []) + existing.get('slash_commands', []))
                    keeper['general_tips'] = dedup_list(skill.get('general_tips', []) + existing.get('general_tips', []))
                    keeper['endorsement_video_ids'] = list(set(skill.get('endorsement_video_ids', []) + existing.get('endorsement_video_ids', [])))
                    keeper['popularity_signals'] = dedup_list(skill.get('popularity_signals', []) + existing.get('popularity_signals', []))
                    keeper['compatibility'] = merge_compat(skill.get('compatibility', []), existing.get('compatibility', []))
                    keeper['multi_tool'] = len({c['tool'].lower() for c in keeper['compatibility']}) >= 2
                    deleted_skills.append({**existing, 'reason': 'superseded by higher quality record', 'deleted_at': now})
                    idx = next(i for i, s in enumerate(skills_data['skills']) if s['slug'] == slug)
                    skills_data['skills'][idx] = keeper
                    index_data[slug] = {'score': keeper['quality_score'], 'video_quality_score': keeper['video_quality_score'], 'starred': False, 'target_tool': keeper['target_tool']}
                else:
                    # Old is better or equal: just merge endorsements
                    existing['tips'] = dedup_list(existing.get('tips', []) + skill.get('tips', []))
                    existing['endorsement_video_ids'] = list(set(existing.get('endorsement_video_ids', []) + skill.get('endorsement_video_ids', [])))
        else:
            skills_data['skills'].append(skill)
            index_data[slug] = {'score': skill['quality_score'], 'video_quality_score': skill['video_quality_score'], 'starred': False, 'target_tool': skill['target_tool']}
            skills_added += 1
            write_skill_md(skill, video)

    save_json('data/skills.json', skills_data)
    save_json('data/index.json', index_data)
    if deleted_skills != load_json('data/deleted_skills.json', []):
        save_json('data/deleted_skills.json', deleted_skills)

    # ── Tab 2: Models ────────────────────────────────────────────────────────
    models_data = load_json('data/models.json', {})
    models_changed = False
    for display_name, info in found_tools.items():
        if not info.get('is_model'):
            continue
        cat = info.get('category', 'productivity')
        if cat not in models_data:
            models_data[cat] = {'podium': [], 'full_ranking': []}
        cat_data = models_data[cat]
        key = f"{display_name}|"
        existing_m = next((m for m in cat_data['full_ranking'] if m['name'].lower() == display_name.lower()), None)
        score = 7 if not low_quality else vqs
        if existing_m is None:
            cat_data['full_ranking'].append({
                'rank': 0, 'name': display_name, 'version': '',
                'company': info.get('company', ''), 'country': info.get('country'),
                'score': score, 'open_source': info.get('open_source', False)
            })
            models_changed = True
        elif score > existing_m.get('score', 0):
            existing_m['score'] = score
            models_changed = True

        if models_changed:
            cat_data['full_ranking'].sort(key=lambda x: x['score'], reverse=True)
            for i, m in enumerate(cat_data['full_ranking']):
                m['rank'] = i + 1
            cat_data['podium'] = [
                {'rank': m['rank'], 'name': m['name'], 'version': m.get('version', ''),
                 'company': m.get('company', ''), 'score': m['score']}
                for m in cat_data['full_ranking'][:3]
            ]

    if models_changed:
        save_json('data/models.json', models_data)

    # ── Tab 4: Tips & Commands ────────────────────────────────────────────────
    tips_data = load_json('data/tips.json', {
        'by_tool': {},
        'general': {
            'prompt engineering': [], 'automation': [], 'agents': [], 'code': [],
            'parallel tasks': [], 'self-improving systems': [], 'harness code': []
        }
    })
    tips_changed = False
    for display_name, info in found_tools.items():
        t = extract_tips(full_text, info.get('key', display_name.lower()))
        if t:
            existing_t = tips_data['by_tool'].setdefault(display_name, [])
            for tip in t:
                if tip.lower() not in [x.lower() for x in existing_t]:
                    existing_t.append(tip)
                    tips_changed = True
    if tips_changed:
        save_json('data/tips.json', tips_data)

    # Slash commands
    cmds_data = load_json('data/commands.json', {'commands': []})
    cmds_changed = False
    for match in re.finditer(r'/[a-z][a-z0-9_-]{1,20}\b', full_text.lower()):
        cmd = match.group()
        if cmd in {'//', '/s', '/r', '/t', '/n', '/a', '/p', '/m', '/b', '/c', '/d', '/e', '/f', '/g', '/h'}:
            continue
        if not any(c['command'] == cmd for c in cmds_data['commands']):
            cmds_data['commands'].append({
                'command': cmd,
                'description': f'Slash command from: {title[:60]}',
                'tool': 'Claude Code' if 'claude code' in full_text.lower() else 'AI Tool',
                'source_video': video_id
            })
            cmds_changed = True
    if cmds_changed:
        save_json('data/commands.json', cmds_data)

    # ── Tab 5: News summaries ────────────────────────────────────────────────
    news_summary = create_news_summary(title, video.get('description', '') or '', video.get('transcript_source', ''))
    for news_file in ['data/daily_news.json', 'data/weekly_news.json', 'data/monthly_news.json']:
        news_data = load_json(news_file)
        if not news_data:
            continue
        changed = False
        for entry in news_data.get('entries', []):
            if entry.get('video_id') == video_id and not entry.get('summary'):
                entry['summary'] = news_summary
                entry['video_quality_score'] = vqs
                entry['low_quality_source'] = low_quality
                changed = True
        if changed:
            save_json(news_file, news_data)

    # ── Tab 6: Connectors ────────────────────────────────────────────────────
    conns_data = load_json('data/connectors.json', {'connectors': []})
    conns_changed = False
    text_lower = full_text.lower()
    if 'mcp' in text_lower or 'model context protocol' in text_lower:
        mcp_patterns = [
            ('filesystem mcp', 'Filesystem MCP', 'Provides file system read/write access to Claude agents.', 'npx @anthropic/mcp-server-filesystem', True),
            ('browser mcp', 'Browser MCP', 'Provides browser automation and web browsing to Claude.', None, False),
            ('github mcp', 'GitHub MCP', 'Connects Claude to GitHub for repo management and code review.', None, False),
            ('postgres mcp', 'PostgreSQL MCP', 'Connects Claude to PostgreSQL databases for queries and analysis.', None, False),
            ('sqlite mcp', 'SQLite MCP', 'Connects Claude to SQLite databases for local data access.', None, False),
            ('memory mcp', 'Memory MCP', 'Provides persistent knowledge graph memory for Claude conversations.', None, True),
            ('slack mcp', 'Slack MCP', 'Connects Claude to Slack for messaging and workspace management.', None, False),
            ('google drive mcp', 'Google Drive MCP', 'Connects Claude to Google Drive for document access.', None, False),
        ]
        for pattern, name, what, install, official in mcp_patterns:
            if pattern in text_lower:
                score = min(7, vqs + 1) if not low_quality else vqs
                if not any(c['name'].lower() == name.lower() for c in conns_data['connectors']):
                    conns_data['connectors'].append({
                        'name': name, 'type': 'mcp_server',
                        'provider': 'Anthropic' if official else 'Community',
                        'category': 'integration',
                        'what_it_does': what,
                        'install_or_source': install, 'official': official,
                        'quality_score': score, 'source_video': video_id,
                        'source_url': f'https://www.youtube.com/watch?v={video_id}',
                        'video_quality_score': vqs, 'low_quality_source': low_quality,
                    })
                    conns_changed = True
    if conns_changed:
        save_json('data/connectors.json', conns_data)

    # ── status.json ──────────────────────────────────────────────────────────
    status = load_json('data/status.json', {})
    rr = status.setdefault('run_report', {})
    rr['analyzed_this_run'] = rr.get('analyzed_this_run', 0) + 1
    status['total_videos_analyzed'] = status.get('total_videos_analyzed', 0) + 1
    rr['pending_to_analyze'] = max(0, len(glob.glob(os.path.join(WORK_DIR, 'data/_pending/*.json'))) - 1)
    status['last_analyze'] = now
    save_json('data/status.json', status)

    # ── Move file ────────────────────────────────────────────────────────────
    _move(video_id)

    return {'skipped': False, 'skills_added': skills_added, 'vqs': vqs, 'tools_found': list(found_tools.keys())}


def _move(video_id):
    src = os.path.join(WORK_DIR, f'data/_pending/{video_id}.json')
    dst = os.path.join(WORK_DIR, f'data/processed/{video_id}.json')
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(src):
        shutil.move(src, dst)


def git_commit_push(video_id, title, skipped=False):
    short_title = (title or video_id)[:60].replace('"', "'").replace('\n', ' ')
    label = 'skipped (not relevant)' if skipped else short_title

    subprocess.run(['git', 'config', 'user.name', 'skills-tracker-bot'], cwd=WORK_DIR, capture_output=True)
    subprocess.run(['git', 'config', 'user.email', 'actions@users.noreply.github.com'], cwd=WORK_DIR, capture_output=True)
    subprocess.run(['git', 'add', 'data/', 'skills/', 'other-skills/'], cwd=WORK_DIR, capture_output=True)

    # Check if anything staged
    st = subprocess.run(['git', 'status', '--porcelain'], cwd=WORK_DIR, capture_output=True, text=True)
    if not st.stdout.strip():
        return 'nothing to commit'

    commit_msg = f"analyze: {video_id} — {label}"
    cr = subprocess.run(['git', 'commit', '-m', commit_msg], cwd=WORK_DIR, capture_output=True, text=True)
    if cr.returncode != 0:
        return f'commit failed: {cr.stderr[:100]}'

    for _ in range(3):
        pr = subprocess.run(['git', 'push'], cwd=WORK_DIR, capture_output=True, text=True)
        if pr.returncode == 0:
            return 'pushed'
        if any(w in pr.stderr for w in ['non-fast-forward', 'fetch first', 'rejected', 'behind']):
            subprocess.run(['git', 'pull', '--rebase', '--autostash'], cwd=WORK_DIR, capture_output=True)
        else:
            return f'push failed: {pr.stderr[:100]}'
    return 'push failed after retries'


def main():
    max_videos = int(sys.argv[1]) if len(sys.argv) > 1 else 1000

    sorted_path = '/tmp/sorted_pending.json'
    if not os.path.exists(sorted_path):
        # Build sorted list on the fly
        files = glob.glob(os.path.join(WORK_DIR, 'data/_pending/*.json'))
        records = []
        for f in files:
            with open(f) as fh:
                d = json.load(fh)
            records.append({'video_id': d['video_id'], 'publishedAt': d.get('publishedAt', ''), 'file_path': f})
        records.sort(key=lambda x: x['publishedAt'], reverse=True)
        with open(sorted_path, 'w') as out:
            json.dump(records, out)
    else:
        with open(sorted_path) as f:
            records = json.load(f)

    print(f"Processing up to {max_videos} videos newest_first (total: {len(records)})")

    index_data = load_json('data/index.json', {})
    processed = skipped = errors = skills_total = 0

    for i, meta in enumerate(records[:max_videos]):
        video_id = meta['video_id']
        src_path = os.path.join(WORK_DIR, f'data/_pending/{video_id}.json')

        if not os.path.exists(src_path):
            continue  # already processed

        with open(src_path) as f:
            video = json.load(f)

        title = video.get('title', video_id)
        print(f"\n[{i+1}/{min(max_videos, len(records))}] {video_id}: {title[:55]}")
        print(f"  src={video.get('transcript_source')} published={video.get('publishedAt','')[:10]}")

        try:
            index_data = load_json('data/index.json', {})  # refresh each iteration
            result = process_video(video, index_data)

            if result.get('skipped'):
                skipped += 1
                git_result = git_commit_push(video_id, title, skipped=True)
                print(f"  SKIPPED | git={git_result}")
            else:
                processed += 1
                sa = result.get('skills_added', 0)
                skills_total += sa
                tools = result.get('tools_found', [])
                git_result = git_commit_push(video_id, title)
                print(f"  OK vqs={result.get('vqs')} skills+={sa} tools={tools[:4]} | git={git_result}")

        except Exception as e:
            errors += 1
            print(f"  ERROR: {e}")
            traceback.print_exc()
            try:
                _move(video_id)
                status = load_json('data/status.json', {})
                rr = status.setdefault('run_report', {})
                rr['errors'] = rr.get('errors', 0) + 1
                save_json('data/status.json', status)
                git_commit_push(video_id, f'error processing', skipped=False)
            except Exception as e2:
                print(f"  CLEANUP ERROR: {e2}")

    print(f"\n{'='*60}")
    print(f"COMPLETE: {processed} analyzed, {skipped} skipped, {errors} errors, {skills_total} skills added")
    remaining = len(glob.glob(os.path.join(WORK_DIR, 'data/_pending/*.json')))
    print(f"Remaining in _pending: {remaining}")


if __name__ == '__main__':
    main()
