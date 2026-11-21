import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from src import gemini_video_analyze as watch, mine_feeds, element_model


class KnowledgePipeline(unittest.TestCase):
    def test_pending_only_video_survives_analysis_and_retry(self):
        with tempfile.TemporaryDirectory() as folder:
            data = Path(folder)
            pending = data / "_pending"
            pending.mkdir()
            vid = "abcdefghijk"
            original = {"video_id": vid, "title": "Queued", "description": "Keep me"}
            path = pending / (vid + ".json")
            path.write_text(json.dumps(original))
            with (patch.object(watch, "DATA", data),
                  patch.object(watch, "STATE", data / "state.json"),
                  patch.object(watch, "PROCESSED", data / "processed"),
                  patch.dict(watch.os.environ, {"GEMINI_API_KEY": "fixture"}, clear=True),
                  patch.object(sys, "argv", ["watch", "--limit", "1", "--sleep", "0"]),
                  patch.object(watch, "analyze_video") as analyze):
                analyze.side_effect = [{"_error": "429"}, {"_error": "429"}]
                self.assertEqual(watch.main(), 1)
                self.assertEqual(json.loads(path.read_text()), original)
                analyze.side_effect = [{"relevant": True, "tools": [{"name": "Example Product"}]}]
                self.assertEqual(watch.main(), 0)
                self.assertTrue(json.loads(path.read_text())["gemini_video_analyzed"])
                self.assertEqual(json.loads((data / "state.json").read_text())["video_ids"], [vid])
                self.assertTrue(json.loads((data / "tools.json").read_text())["tools"])
                self.assertEqual(watch.main(), 0)
                self.assertEqual(analyze.call_count, 3)

    def test_public_discovery_reaches_extractor_with_provenance(self):
        with tempfile.TemporaryDirectory() as folder:
            data = Path(folder)
            url = "https://huggingface.co/example/model"
            (data / "social_intake.json").write_text(json.dumps({"items": [
                {"url": url, "source": "huggingface-model", "title": "Example model"}]}))
            engine = dict(name="test", model="mock", provider="mock", base_url="", key="")
            with (patch.object(mine_feeds, "DATA", data), patch.object(mine_feeds, "STATE", data / "state.json"),
                  patch.object(mine_feeds, "build_pool", return_value=[engine]),
                  patch.object(sys, "argv", ["mine", "--limit", "1", "--sleep", "0"]),
                  patch.object(mine_feeds, "extract", return_value={"relevant": True, "tools": [{"name": "Example model"}]}) as extract):
                self.assertEqual(mine_feeds.main(), 0)
                self.assertEqual(json.loads((data / "tools.json").read_text())["tools"][0]["source_url"], url)
                self.assertEqual(mine_feeds.main(), 0)
                self.assertEqual(extract.call_count, 1)

    def test_one_live_link_does_not_verify_a_skill(self):
        element = {"type": "skill", "what": "A specific technique with a documented procedure." * 3,
                   "links": {"website": "https://example.org"}}
        self.assertEqual(element_model._status(element, {"status": "thin", "link_alive": True, "sources": 1})[0],
                         "unverified")
