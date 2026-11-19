# EXCAVATORTRON — current handoff
Updated 2026-11-19.

## Current owner direction
EXCAVATORTRON is a video knowledge library: retrieve from playlists and the web, analyze the real content, extract specific findings, categorize them and preserve source provenance. Keep the existing database and Heavy Machinery design.

EXCAVA is preserved as a disconnected candidate for a future optional plugin. Do not reactivate it, its workflows or its UI as part of routine core work. It is not the home screen or a prerequisite for any pipeline lane.

## Implementation
- Original OS modules moved unchanged to `plugins/excava/src/`; original workflows live outside the active workflow directory.
- Original frontend preserved in `plugins/excava/ui/`; core home is Overview + Video Library.
- Shared library data classes are now independent in `src/library.py`. Existing package stores remain readable.
- Stateless source-enrichment adapters are in `src/analysis_engines.py`.
- `src/video_catalog.py` derives stages and categories without modifying original data. Captions alone do not count as completed analysis.
- `src/source_inputs.py` adds validated direct video URLs and extra playlists, deduplicated before fetching.
- Existing skills, tools, models, prompts, commands, connectors, news, designs, packages, source discovery, quality reports and public API remain.
- Existing `data/` records and historical state were not rewritten by this source refactor.

## Verification
Run `python -m unittest discover -s tests -v`, `python -m compileall -q src`, and Node syntax checks on the dashboard, video-library script and service worker. The core-checks workflow runs these checks. The catalog workflow creates derived views from current branch data.

The previous local checkout was stale. This change is based on remote commit ee12b15a444b037ae42cb163b894468df4af7254; July data counts from the local preview are not current cloud counts.

## Scope limits
The preserved EXCAVA source is not yet an installable plugin. Reactivation requires its own adapter and tests. No new purchases, API keys, or local scheduling changes are part of this refactor. Do not invoke historical deployment/away-mode scripts.
