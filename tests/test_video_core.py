"""Offline checks for the video core and preservation of EXCAVA."""
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch
from src.source_inputs import collect, configured_sources, parse_source
from src.video_catalog import build
from src import library

ROOT = Path(__file__).resolve().parents[1]
VID, SECOND = "abcdefghijk", "ZYXWVUTSRQP"


class CoreTest(unittest.TestCase):
    def test_urls_and_untrusted_hosts(self):
        for url in [f"https://youtu.be/{VID}", f"https://youtube.com/watch?v={VID}&t=30",
                    f"https://youtube.com/shorts/{VID}", f"https://youtube.com/live/{VID}"]:
            self.assertEqual(parse_source(url), ("video", VID))
        for bad in [f"https://youtube.com.evil.test/watch?v={VID}",
                    f"https://youtube.com@evil.test/watch?v={VID}", "file:///tmp/video", "../bad"]:
            with self.assertRaises(ValueError):
                parse_source(bad)

    def test_playlists_deduplicate_and_keep_membership(self):
        class NoNetwork:
            def videos(self):
                raise AssertionError("Direct video request was not needed")
        config = {"playlist_id": "PL1234567890", "playlist_ids": ["PL1234567890", "PL9876543210"]}
        with patch.dict(os.environ, {"SOURCE_URLS": ""}):
            rows = collect(NoNetwork(), config, lambda client, playlist: [{"video_id": VID, "title": "One"}])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["source_playlists"], ["PL1234567890", "PL9876543210"])

    def test_dispatch_validation(self):
        with patch.dict(os.environ, {"SOURCE_URLS": f"https://youtu.be/{VID}\nhttps://youtu.be/{VID}"}):
            self.assertEqual(configured_sources({}), ([], [VID]))
        with patch.dict(os.environ, {"SOURCE_URLS": "$(malicious)"}):
            with self.assertRaises(ValueError):
                configured_sources({})

    def test_captions_are_not_analysis_and_requeues_count_once(self):
        with tempfile.TemporaryDirectory() as folder:
            data = Path(folder)
            def put(path, value):
                p = data / path
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(json.dumps(value), encoding="utf-8")
            put(f"processed/{VID}.json", {"video_id": VID, "transcript_source": "transcript", "transcript": "Captions"})
            put(f"_pending/{VID}.json", {"video_id": VID, "title": "Requeued"})
            put(f"processed/{SECOND}.json", {"video_id": SECOND, "transcript_source": "description", "transcript": "Description"})
            put("gemini_analyzed.json", {"video_ids": [SECOND]})
            put("elements_index.json", {"elements": [{"id": "tool:one", "name": "One", "type": "tool", "category": "code", "source_videos": [VID]}]})
            before = {str(p): p.read_bytes() for p in data.rglob("*.json")}
            result = build(data)
            self.assertEqual(result["summary"]["total"], 2)
            self.assertEqual(result["summary"]["analyzed"], 1)
            self.assertEqual(result["summary"]["with_transcript"], 1)
            rows = {v["video_id"]: v for v in result["videos"]}
            self.assertEqual(rows[VID]["stage"], "queued")
            self.assertEqual(rows[VID]["categories"], ["code"])
            self.assertEqual(rows[SECOND]["stage"], "analyzed")
            self.assertEqual(before, {str(p): p.read_bytes() for p in data.rglob("*.json")})

    def test_corrupt_input_fails_visibly(self):
        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / "elements_index.json").write_text("{broken", encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                build(Path(folder))

    def test_library_without_os(self):
        with tempfile.TemporaryDirectory() as folder:
            index = Path(folder) / "index.json"
            index.write_text(json.dumps({"elements": [
                {"id": "tool:one", "name": "One", "type": "tool", "verified": {"status": "verified"}, "links": {"github": "https://github.com/example/one"}},
                {"id": "tool:dead", "name": "Dead", "type": "tool", "verified": {"status": "dead"}},
            ]}), encoding="utf-8")
            with patch.object(library, "INDEX", index), patch.object(library, "_INDEX_CACHE", None):
                self.assertTrue(library.load()["tool:one"].is_usable())
                self.assertEqual(library.find("one")[0].id, "tool:one")
                self.assertEqual(library.find("dead"), [])

    def test_both_historical_package_stores(self):
        with tempfile.TemporaryDirectory() as folder:
            a, b = Path(folder) / "a.json", Path(folder) / "b.json"
            a.write_text(json.dumps({"packages": [{"name": "Old", "elements": ["tool:one"]}]}), encoding="utf-8")
            b.write_text(json.dumps({"packages": [{"name": "New", "elements": ["tool:two"]}]}), encoding="utf-8")
            with patch.object(library, "PACKAGES", a), patch.object(library.Package, "LEGACY", b):
                self.assertEqual([p.name for p in library.Package.all()], ["Old", "New"])

    def test_os_source_blobs_preserved(self):
        records = json.loads((ROOT / "plugins/excava/preserved-files.json").read_text(encoding="utf-8"))
        for record in records:
            content = (ROOT / record["path"]).read_bytes()
            blob = b"blob " + str(len(content)).encode() + b"\0" + content
            self.assertEqual(hashlib.sha1(blob).hexdigest(), record["sha"], record["path"])

    def test_core_import_boundary(self):
        retired = {x["original"].split("/")[-1][:-3] for x in
                   json.loads((ROOT / "plugins/excava/preserved-files.json").read_text(encoding="utf-8"))
                   if x["original"].startswith("src/")}
        for path in (ROOT / "src").glob("*.py"):
            for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
                if isinstance(node, ast.ImportFrom):
                    names = [node.module or ""] + [x.name for x in node.names]
                elif isinstance(node, ast.Import):
                    names = [x.name for x in node.names]
                else:
                    continue
                self.assertFalse(any(name.split(".")[-1] in retired for name in names), path.name)

    def test_plugin_disabled_and_ui_disconnected(self):
        config = json.loads((ROOT / "plugins/excava/plugin.json").read_text(encoding="utf-8"))
        self.assertFalse(config["enabled"])
        html = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        js = (ROOT / "docs/dashboard.js").read_text(encoding="utf-8")
        self.assertNotIn('src="floor/floor.js"', html)
        for tab in ["excava", "rooms", "results", "proof"]:
            self.assertNotIn(f'data-tab="{tab}"', html)
        self.assertNotIn("function renderExcava", js)
        self.assertNotIn("function renderCrew", js)

    def test_active_workflows_no_os(self):
        for path in (ROOT / ".github/workflows").glob("*.yml"):
            self.assertIsNone(re.search(r"python\s+-m\s+src\.(?:excava\w*|horse)\b",
                                       path.read_text(encoding="utf-8")), path.name)


if __name__ == "__main__":
    unittest.main()
