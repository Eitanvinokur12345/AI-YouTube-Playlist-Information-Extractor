import unittest
from src.original_sources import product_matches, skill_metadata
from src.reconcile_acquisition import combine

class PublisherSources(unittest.TestCase):
    def test_document_requires_frontmatter_name_and_body(self):
        self.assertIsNone(skill_metadata(b"# Notes on my prompt"))
        self.assertIsNone(skill_metadata(b"---\nname: x\n---\n"))
        self.assertEqual(skill_metadata(b"---\nname: pdf\n---\nOriginal instructions")[0], "pdf")

    def test_repository_identity(self):
        self.assertTrue(product_matches("playwright-mcp", "microsoft/playwright-mcp"))
        self.assertFalse(product_matches("unrelated", "microsoft/playwright-mcp"))

    def test_concurrent_additions_and_conflicts(self):
        old = {"tools": [{"name": "Existing"}]}
        latest = {"tools": old["tools"] + [{"name": "A"}]}
        new = {"tools": old["tools"] + [{"name": "B"}]}
        self.assertEqual([x["name"] for x in combine(old, latest, new)["tools"]], ["Existing", "A", "B"])
        with self.assertRaises(ValueError):
            combine({"v": 0}, {"v": 1}, {"v": 2})
