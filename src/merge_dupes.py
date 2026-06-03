#!/usr/bin/env python3
"""Merge duplicate skill slugs caused by the make_slug bug."""
import json, os, re, shutil, glob
from datetime import datetime, timezone

WORK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.now(timezone.utc).isoformat()


def load_json(path, default=None):
    full = os.path.join(WORK_DIR, path)
    if os.path.exists(full):
        with open(full) as f:
            return json.load(f)
    return default if default is not None else {}


def save_json(path, data):
    full = os.path.join(WORK_DIR, path)
    with open(full, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')


def base_slug(slug):
    """Remove trailing -N suffix."""
    return re.sub(r'-\d+$', '', slug)


def dedup_list(lst):
    seen, result = set(), []
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


def skill_folder(skill):
    slug = skill['slug']
    target = skill.get('target_tool', 'claude')
    if target == 'claude':
        return os.path.join(WORK_DIR, f'skills/{slug}')
    else:
        return os.path.join(WORK_DIR, f'other-skills/{target}/{slug}')


def main():
    skills_data = load_json('data/skills.json', {'videos_seen': [], 'skills': []})
    deleted_skills = load_json('data/deleted_skills.json', [])
    merge_log = load_json('data/merge_log.json', [])

    skills = skills_data['skills']
    print(f"Starting with {len(skills)} skills")

    # Group by base slug
    from collections import defaultdict
    groups = defaultdict(list)
    for i, sk in enumerate(skills):
        b = base_slug(sk['slug'])
        groups[b].append((i, sk))

    # Find groups with duplicates
    dupe_groups = {b: items for b, items in groups.items() if len(items) > 1}
    print(f"Found {len(dupe_groups)} base slugs with duplicates")
    total_dupes = sum(len(v) - 1 for v in dupe_groups.values())
    print(f"Total duplicate records to merge: {total_dupes}")

    # Build new skills list
    kept_indices = set()
    discarded_indices = set()
    replacements = {}  # old_index -> replacement skill

    for base, items in dupe_groups.items():
        # Sort by quality: highest quality_score first, then video_quality_score
        items.sort(key=lambda x: (x[1].get('quality_score', 0), x[1].get('video_quality_score', 0)), reverse=True)

        # Check if any is frozen
        keeper_idx, keeper = items[0]
        if keeper.get('starred') or keeper.get('locked'):
            pass  # keep it

        # Merge all into keeper
        merged = keeper.copy()
        merged['slug'] = base  # normalize to base slug

        for i, (idx, sk) in enumerate(items):
            if i == 0:
                continue  # skip keeper
            # Merge fields
            merged['tips'] = dedup_list(merged.get('tips', []) + sk.get('tips', []))
            merged['slash_commands'] = dedup_list(merged.get('slash_commands', []) + sk.get('slash_commands', []))
            merged['general_tips'] = dedup_list(merged.get('general_tips', []) + sk.get('general_tips', []))
            merged['endorsement_video_ids'] = list(set(merged.get('endorsement_video_ids', []) + sk.get('endorsement_video_ids', [])))
            merged['popularity_signals'] = dedup_list(merged.get('popularity_signals', []) + sk.get('popularity_signals', []))
            merged['compatibility'] = merge_compat(merged.get('compatibility', []), sk.get('compatibility', []))
            merged['multi_tool'] = len({c['tool'].lower() for c in merged['compatibility']}) >= 2

            # Keep higher score
            if sk.get('quality_score', 0) > merged.get('quality_score', 0):
                merged['quality_score'] = sk['quality_score']
                merged['video_quality_score'] = sk['video_quality_score']
                merged['low_quality_source'] = sk['low_quality_source']

            discarded_indices.add(idx)
            deleted_skills.append({**sk, 'reason': f'merged into {base}', 'deleted_at': NOW})
            merge_log.append({'timestamp': NOW, 'merged_from': sk['slug'], 'merged_into': base, 'reason': 'duplicate slug (dedup fix)'})

            # Remove duplicate SKILL.md folder
            folder = skill_folder(sk)
            if os.path.exists(folder) and folder != skill_folder({'slug': base, 'target_tool': sk.get('target_tool', 'claude')}):
                try:
                    shutil.rmtree(folder)
                    print(f"  Removed folder: {folder}")
                except Exception as e:
                    print(f"  Could not remove {folder}: {e}")

        kept_indices.add(keeper_idx)
        replacements[keeper_idx] = merged

    # Build final skills list
    new_skills = []
    for i, sk in enumerate(skills):
        if i in discarded_indices:
            continue
        if i in replacements:
            new_skills.append(replacements[i])
        else:
            new_skills.append(sk)

    print(f"New skills count: {len(new_skills)}")

    # Rebuild index
    new_index = {}
    for sk in new_skills:
        slug = sk['slug']
        new_index[slug] = {
            'score': sk.get('quality_score', 0),
            'video_quality_score': sk.get('video_quality_score', 0),
            'starred': sk.get('starred', False),
            'target_tool': sk.get('target_tool', 'claude'),
        }

    # Also rename SKILL.md folders for kept skills if their slug changed
    for i, sk in enumerate(skills):
        if i in replacements:
            old_slug = sk['slug']
            new_slug = replacements[i]['slug']
            if old_slug != new_slug:
                target = sk.get('target_tool', 'claude')
                if target == 'claude':
                    old_folder = os.path.join(WORK_DIR, f'skills/{old_slug}')
                    new_folder = os.path.join(WORK_DIR, f'skills/{new_slug}')
                else:
                    old_folder = os.path.join(WORK_DIR, f'other-skills/{target}/{old_slug}')
                    new_folder = os.path.join(WORK_DIR, f'other-skills/{target}/{new_slug}')

                if os.path.exists(old_folder) and not os.path.exists(new_folder):
                    shutil.move(old_folder, new_folder)
                    print(f"  Renamed: {old_folder} → {new_folder}")
                elif os.path.exists(old_folder) and os.path.exists(new_folder):
                    shutil.rmtree(old_folder)

    # Save everything
    skills_data['skills'] = new_skills
    save_json('data/skills.json', skills_data)
    save_json('data/index.json', new_index)
    save_json('data/deleted_skills.json', deleted_skills)
    save_json('data/merge_log.json', merge_log)

    # Update status total_skills
    status = load_json('data/status.json', {})
    status['total_skills'] = len(new_skills)
    save_json('data/status.json', status)

    print(f"\nDone! Merged {total_dupes} duplicates into {len(dupe_groups)} base slugs")
    print(f"Final skills count: {len(new_skills)}")


if __name__ == '__main__':
    main()
