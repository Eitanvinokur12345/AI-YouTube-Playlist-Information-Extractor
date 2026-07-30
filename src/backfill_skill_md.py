#!/usr/bin/env python3
"""
Backfill SKILL.md packages for skills.json records that qualify (quality_score >= 5)
but never got a package folder written — e.g. records from an older pipeline run,
or a schema variant (mine_feeds/web_news) that predates source_video_id.

Reuses analyze_batch.write_skill_md() verbatim (Ponytail: no new writer logic,
same template/gate/no-overwrite behavior as the live analyze pipeline). This script
only adds the video-metadata lookup so the existing writer can run over records that
lack a direct source_video_id.

Run from repo root: python3 -m src.backfill_skill_md
"""
import json
import os
import re

from src.analyze_batch import WORK_DIR, write_skill_md


def load_json(path, default):
    full = os.path.join(WORK_DIR, path)
    if not os.path.exists(full):
        return default
    with open(full, 'r', encoding='utf-8') as f:
        return json.load(f)


def build_video_meta_index():
    """video_id -> {title, channel_name} from every source this repo already has."""
    meta = {}
    for f in ('data/daily_news.json', 'data/weekly_news.json', 'data/monthly_news.json'):
        d = load_json(f, {})
        for e in d.get('entries', []):
            vid = e.get('video_id')
            if vid and vid not in meta:
                meta[vid] = {'title': e.get('title', ''), 'channel_name': e.get('channel_name', '')}
    proc_dir = os.path.join(WORK_DIR, 'data/processed')
    if os.path.isdir(proc_dir):
        for fn in os.listdir(proc_dir):
            if not fn.endswith('.json'):
                continue
            vid = fn[:-5]
            if vid in meta:
                continue
            try:
                rec = json.load(open(os.path.join(proc_dir, fn), 'r', encoding='utf-8'))
            except Exception:
                continue
            meta[vid] = {'title': rec.get('title', ''), 'channel_name': rec.get('channel_name', '')}
    return meta


def resolve_video(skill, meta_index):
    """Best-effort {video_id, title, channel_name} for the Source line, across schema variants."""
    vid = skill.get('source_video_id')
    if vid:
        m = meta_index.get(vid, {})
        return {'video_id': vid, 'title': m.get('title', ''), 'channel_name': m.get('channel_name', '')}

    svs = skill.get('source_videos') or []
    if svs and isinstance(svs, list):
        sv = svs[0]
        vid = sv.get('id', '')
        m = meta_index.get(vid, {})
        return {
            'video_id': vid,
            'title': sv.get('title', '') or m.get('title', ''),
            'channel_name': m.get('channel_name', ''),
        }

    src_url = skill.get('source_url', '') or ''
    if 'watch?v=' in src_url:
        vid = src_url.split('watch?v=')[-1].split('&')[0]
        m = meta_index.get(vid, {})
        return {'video_id': vid, 'title': m.get('title', ''), 'channel_name': m.get('channel_name', '')}

    return None  # genuinely no usable source — write_skill_md still runs, Source line is bare


def path_for(skill):
    """Mirrors analyze_batch.write_skill_md()'s (now-fixed) folder resolution exactly,
    so a candidate already covered by an existing (differently-cased) tool folder is
    correctly seen as 'not missing' instead of triggering a duplicate write."""
    slug = skill['slug']
    tt = (skill.get('target_tool') or 'claude').strip().lower()
    if tt in ('', 'claude'):
        return os.path.join(WORK_DIR, f'skills/{slug}/SKILL.md')
    tool_slug = re.sub(r'[^a-z0-9]+', '-', tt).strip('-') or 'other'
    return os.path.join(WORK_DIR, f'other-skills/{tool_slug}/{slug}/SKILL.md')


def main():
    skills = load_json('data/skills.json', {'skills': []})['skills']
    meta_index = build_video_meta_index()

    candidates = [s for s in skills if s.get('quality_score', 0) >= 5 and not os.path.exists(path_for(s))]
    written = 0
    no_source = 0
    for skill in candidates:
        video = resolve_video(skill, meta_index) or {'video_id': skill.get('slug', ''), 'title': '', 'channel_name': ''}
        if not video.get('title') and not skill.get('source_video_id') and not (skill.get('source_videos')):
            no_source += 1
        before = os.path.exists(path_for(skill))
        write_skill_md(skill, video)
        if not before and os.path.exists(path_for(skill)):
            written += 1

    print(f"candidates={len(candidates)} written={written} no_source_meta={no_source}")


if __name__ == '__main__':
    main()
