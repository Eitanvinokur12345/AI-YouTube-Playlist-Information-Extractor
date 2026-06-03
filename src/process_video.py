#!/usr/bin/env python3
"""
Helper script for processing a single pending video.
Reads analysis JSON from stdin and updates all data files.
Usage: python3 src/process_video.py <video_id> < analysis.json
"""
import json
import os
import sys
import glob
import shutil
from datetime import datetime, timezone

WORK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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

def process_video(video_id, analysis):
    """Process one video's analysis and update all data files."""
    now = datetime.now(timezone.utc).isoformat()

    # ── Load status ─────────────────────────────────────────────────────────
    status = load_json('data/status.json', {})
    run_report = status.setdefault('run_report', {})

    # ── If skipped ───────────────────────────────────────────────────────────
    if analysis.get('skipped'):
        run_report['skipped_not_relevant'] = run_report.get('skipped_not_relevant', 0) + 1
        pending_count = len(glob.glob(os.path.join(WORK_DIR, 'data/_pending/*.json'))) - 1
        run_report['pending_to_analyze'] = max(0, pending_count)
        status['last_analyze'] = now
        save_json('data/status.json', status)
        _move_pending(video_id)
        return {'updated': ['status.json'], 'moved': True}

    updated_files = []

    # ── Tab 1: Skills ────────────────────────────────────────────────────────
    skills_data = load_json('data/skills.json', {'videos_seen': [], 'skills': []})
    index_data = load_json('data/index.json', {})

    new_skills = analysis.get('skills', [])
    skills_added = 0
    skills_updated = 0

    for skill in new_skills:
        slug = skill['slug']
        existing_idx = index_data.get(slug)

        if existing_idx is None:
            # New skill
            skills_data['skills'].append(skill)
            index_data[slug] = {
                'score': skill.get('quality_score', 0),
                'video_quality_score': skill.get('video_quality_score', 0),
                'starred': skill.get('starred', False),
                'target_tool': skill.get('target_tool', 'claude')
            }
            skills_added += 1
            # Write SKILL.md
            if skill.get('quality_score', 0) >= 5:
                _write_skill_md(skill, analysis)
        else:
            # Existing slug — check if frozen
            existing_skill = next((s for s in skills_data['skills'] if s['slug'] == slug), None)
            if existing_skill and (existing_skill.get('starred') or existing_skill.get('locked')):
                continue  # Never touch frozen

            if existing_skill:
                # Keep best, merge
                new_score = skill.get('quality_score', 0)
                old_score = existing_skill.get('quality_score', 0)
                new_vqs = skill.get('video_quality_score', 0)
                old_vqs = existing_skill.get('video_quality_score', 0)

                if new_score > old_score or (new_score == old_score and new_vqs > old_vqs):
                    keeper = skill.copy()
                    keeper['tips'] = _dedup_list(skill.get('tips', []) + existing_skill.get('tips', []))
                    keeper['slash_commands'] = _dedup_list(skill.get('slash_commands', []) + existing_skill.get('slash_commands', []))
                    keeper['general_tips'] = _dedup_list(skill.get('general_tips', []) + existing_skill.get('general_tips', []))
                    keeper['endorsement_video_ids'] = list(set(skill.get('endorsement_video_ids', []) + existing_skill.get('endorsement_video_ids', [])))
                    keeper['popularity_signals'] = _dedup_list(skill.get('popularity_signals', []) + existing_skill.get('popularity_signals', []))
                    keeper['compatibility'] = _merge_compatibility(skill.get('compatibility', []), existing_skill.get('compatibility', []))
                    keeper['multi_tool'] = len({c['tool'].lower() for c in keeper['compatibility']}) >= 2

                    # Back up discarded
                    _backup_deleted_skill(existing_skill, f"superseded by higher quality record")

                    idx = skills_data['skills'].index(existing_skill)
                    skills_data['skills'][idx] = keeper
                    index_data[slug]['score'] = keeper['quality_score']
                    index_data[slug]['video_quality_score'] = keeper['video_quality_score']
                    skills_updated += 1
                else:
                    # Old is better — just merge endorsements/tips into old
                    existing_skill['tips'] = _dedup_list(existing_skill.get('tips', []) + skill.get('tips', []))
                    existing_skill['slash_commands'] = _dedup_list(existing_skill.get('slash_commands', []) + skill.get('slash_commands', []))
                    existing_skill['general_tips'] = _dedup_list(existing_skill.get('general_tips', []) + skill.get('general_tips', []))
                    existing_skill['endorsement_video_ids'] = list(set(existing_skill.get('endorsement_video_ids', []) + skill.get('endorsement_video_ids', [])))
                    existing_skill['popularity_signals'] = _dedup_list(existing_skill.get('popularity_signals', []) + skill.get('popularity_signals', []))
                    existing_skill['compatibility'] = _merge_compatibility(existing_skill.get('compatibility', []), skill.get('compatibility', []))
                    existing_skill['multi_tool'] = len({c['tool'].lower() for c in existing_skill['compatibility']}) >= 2

    save_json('data/skills.json', skills_data)
    save_json('data/index.json', index_data)
    updated_files += ['skills.json', 'index.json']

    # ── Tab 2: Models ────────────────────────────────────────────────────────
    models_data = load_json('data/models.json', {})
    for model in analysis.get('models', []):
        cat = model.get('category', 'other')
        if cat not in models_data:
            models_data[cat] = {'podium': [], 'full_ranking': []}

        cat_data = models_data[cat]
        key = f"{model['name']}|{model.get('version','')}"
        existing = next((m for m in cat_data['full_ranking'] if f"{m['name']}|{m.get('version','')}" == key), None)

        if existing is None:
            cat_data['full_ranking'].append({
                'rank': 0,
                'name': model['name'],
                'version': model.get('version', ''),
                'company': model.get('company', ''),
                'country': model.get('country', ''),
                'score': model.get('quality_score', 0),
                'open_source': model.get('open_source', False)
            })
        else:
            if model.get('quality_score', 0) > existing.get('score', 0):
                existing['score'] = model['quality_score']

        # Re-sort and re-rank
        cat_data['full_ranking'].sort(key=lambda x: x['score'], reverse=True)
        for i, m in enumerate(cat_data['full_ranking']):
            m['rank'] = i + 1
        cat_data['podium'] = [
            {'rank': m['rank'], 'name': m['name'], 'version': m.get('version',''),
             'company': m.get('company',''), 'score': m['score']}
            for m in cat_data['full_ranking'][:3]
        ]

    if analysis.get('models'):
        save_json('data/models.json', models_data)
        updated_files.append('models.json')

    # ── Tab 4: Tips & Commands ────────────────────────────────────────────────
    tips_data = load_json('data/tips.json', {
        'by_tool': {},
        'general': {
            'prompt engineering': [], 'automation': [], 'agents': [], 'code': [],
            'parallel tasks': [], 'self-improving systems': [], 'harness code': []
        }
    })

    tips_changed = False
    for tool_name, tool_tips in analysis.get('tips_by_tool', {}).items():
        existing_tool_tips = tips_data['by_tool'].setdefault(tool_name, [])
        for tip in tool_tips:
            if tip.lower() not in [t.lower() for t in existing_tool_tips]:
                existing_tool_tips.append(tip)
                tips_changed = True

    for topic, topic_tips in analysis.get('general_tips', {}).items():
        existing_topic = tips_data['general'].setdefault(topic, [])
        for tip in topic_tips:
            if tip.lower() not in [t.lower() for t in existing_topic]:
                existing_topic.append(tip)
                tips_changed = True

    if tips_changed:
        save_json('data/tips.json', tips_data)
        updated_files.append('tips.json')

    commands_data = load_json('data/commands.json', {'commands': []})
    cmds_changed = False
    for cmd in analysis.get('commands', []):
        existing_cmd = next((c for c in commands_data['commands'] if c['command'].lower() == cmd['command'].lower()), None)
        if existing_cmd is None:
            commands_data['commands'].append(cmd)
            cmds_changed = True

    if cmds_changed:
        save_json('data/commands.json', commands_data)
        updated_files.append('commands.json')

    # ── Tab 5: News summaries ────────────────────────────────────────────────
    news_summary = analysis.get('news_summary', '')
    vqs = analysis.get('video_quality_score', 5)
    lqs = analysis.get('low_quality_source', False)

    if news_summary:
        for news_file in ['data/daily_news.json', 'data/weekly_news.json', 'data/monthly_news.json']:
            news_data = load_json(news_file)
            if not news_data:
                continue
            entries = news_data.get('entries', [])
            changed = False
            for entry in entries:
                if entry.get('video_id') == video_id and not entry.get('summary'):
                    entry['summary'] = news_summary
                    entry['video_quality_score'] = vqs
                    entry['low_quality_source'] = lqs
                    changed = True
            if changed:
                save_json(news_file, news_data)
                updated_files.append(news_file)

    # ── Tab 6: Connectors ────────────────────────────────────────────────────
    connectors_data = load_json('data/connectors.json', {'connectors': []})
    conn_changed = False
    for conn in analysis.get('connectors', []):
        existing = next((c for c in connectors_data['connectors']
                        if c['name'].lower() == conn['name'].lower()), None)
        if existing is None:
            connectors_data['connectors'].append(conn)
            conn_changed = True
        else:
            if conn.get('quality_score', 0) > existing.get('quality_score', 0):
                existing.update(conn)
                conn_changed = True
            else:
                # Still merge what_it_does if empty
                if not existing.get('what_it_does') and conn.get('what_it_does'):
                    existing['what_it_does'] = conn['what_it_does']
                    conn_changed = True

    if conn_changed:
        save_json('data/connectors.json', connectors_data)
        updated_files.append('connectors.json')

    # ── Update status.json ───────────────────────────────────────────────────
    run_report['analyzed_this_run'] = run_report.get('analyzed_this_run', 0) + 1
    status['total_videos_analyzed'] = status.get('total_videos_analyzed', 0) + 1
    pending_count = len(glob.glob(os.path.join(WORK_DIR, 'data/_pending/*.json'))) - 1
    run_report['pending_to_analyze'] = max(0, pending_count)
    status['last_analyze'] = now
    save_json('data/status.json', status)
    updated_files.append('status.json')

    # ── Move pending → processed ──────────────────────────────────────────────
    _move_pending(video_id)

    return {
        'updated': updated_files,
        'skills_added': skills_added,
        'skills_updated': skills_updated,
        'moved': True
    }


def _move_pending(video_id):
    src = os.path.join(WORK_DIR, f'data/_pending/{video_id}.json')
    dst = os.path.join(WORK_DIR, f'data/processed/{video_id}.json')
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(src):
        shutil.move(src, dst)


def _write_skill_md(skill, analysis):
    slug = skill['slug']
    target_tool = skill.get('target_tool', 'claude')

    if target_tool == 'claude':
        folder = os.path.join(WORK_DIR, f'skills/{slug}')
    else:
        folder = os.path.join(WORK_DIR, f'other-skills/{target_tool}/{slug}')

    os.makedirs(folder, exist_ok=True)
    skill_md_path = os.path.join(folder, 'SKILL.md')

    # Don't overwrite existing SKILL.md if higher quality
    if os.path.exists(skill_md_path):
        return

    video_id = skill.get('source_video_id', '')
    title = analysis.get('title', '')
    channel = analysis.get('channel_name', '')

    tips = skill.get('tips', [])
    techniques = skill.get('key_techniques', tips[:3] if tips else ['See source video for techniques'])

    content = f"""---
name: {slug}
description: "{skill.get('skill_name', slug)} — {skill.get('use_case', 'AI productivity tool')}"
---

# {skill.get('skill_name', slug)}

## Overview
{skill.get('description', 'An AI tool or technique for productivity and automation.')}

## Key Techniques
{chr(10).join(f'- {t}' for t in (techniques[:3] if techniques else ['See source video']))}

## How to Apply
{skill.get('use_case', 'Apply this tool to your AI workflow as demonstrated in the source video.')}

## Examples
{skill.get('output', 'See the source video for concrete examples.')}

## Source
Extracted from: [{title}](https://www.youtube.com/watch?v={video_id})
Channel: {channel}
"""
    with open(skill_md_path, 'w') as f:
        f.write(content)


def _dedup_list(lst):
    seen = set()
    result = []
    for item in lst:
        key = item.lower() if isinstance(item, str) else str(item).lower()
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


def _merge_compatibility(compat1, compat2):
    merged = {c['tool'].lower(): c.copy() for c in compat1}
    for c in compat2:
        key = c['tool'].lower()
        if key not in merged:
            merged[key] = c.copy()
        else:
            # Keep higher version (simple string comparison — "any" is treated as low)
            v1 = merged[key].get('up_to_version', 'any')
            v2 = c.get('up_to_version', 'any')
            if v1 == 'any' and v2 != 'any':
                merged[key]['up_to_version'] = v2
            # Preserve capitalization from first occurrence
    return list(merged.values())


def _backup_deleted_skill(skill, reason):
    deleted = load_json('data/deleted_skills.json', [])
    deleted.append({**skill, 'reason': reason, 'deleted_at': datetime.now(timezone.utc).isoformat()})
    save_json('data/deleted_skills.json', deleted)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 src/process_video.py <video_id> < analysis.json")
        sys.exit(1)

    video_id = sys.argv[1]
    analysis = json.load(sys.stdin)
    result = process_video(video_id, analysis)
    print(json.dumps(result, indent=2))
