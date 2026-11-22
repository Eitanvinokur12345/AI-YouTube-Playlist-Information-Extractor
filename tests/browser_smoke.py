"""Smoke-test retained core tabs against real committed branch data."""
import subprocess
import sys
from playwright.sync_api import sync_playwright

server = subprocess.Popen([sys.executable, "-m", "http.server", "8787", "--bind", "127.0.0.1"])
try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" and any(t in m.text for t in ("ReferenceError", "TypeError", "SyntaxError")) else None)
        page.route("**/data/original_sources.json", lambda r: r.fulfill(json={
            "entries": [{"id": "fixture:publisher", "name": "Original document fixture", "type": "skill",
                         "publisher": "publisher", "raw_url": "https://example.org/pinned/SKILL.md",
                         "url": "https://example.org/pinned/SKILL.md", "package_url": "https://example.org/pinned/"}],
            "matches": {}}))
        page.goto("http://127.0.0.1:8787/docs/", wait_until="domcontentloaded")
        page.get_by_role("heading", name="Knowledge library").wait_for()
        assert page.locator('nav button[data-tab="videos"]').count() == 0
        page.locator('nav button[data-tab="skills"]').click()
        original = page.get_by_role("link", name="Use original SKILL.md").first
        original.wait_for()
        assert original.get_attribute("href") == "https://example.org/pinned/SKILL.md"
        assert not page.get_by_text("Copy ready-to-paste block").count()
        page.locator(".workspace-extras summary").click()
        for tab in ["hub", "skills", "tools", "prompts", "tips", "connectors", "packages", "taste", "selfimprove", "effectiveness", "devbuild"]:
            print("Testing tab:", tab, flush=True)
            page.locator(f'nav button[data-tab="{tab}"]').click()
            page.wait_for_function(
                """() => { const v=document.querySelector('#view');
                return v && v.textContent.trim() && !v.textContent.trim().startsWith('Loading'); }""")
            assert "This view could not load." not in page.locator("#view").inner_text(), (tab, errors)
            assert not page.locator(".ex-strip, #crew, #approve-bell").count(), tab
        page.locator('nav button[data-tab="overview"]').click()
        page.get_by_role("heading", name="Knowledge library").wait_for()
        page.set_viewport_size({"width": 390, "height": 844})
        assert page.locator("#view").is_visible()
        assert not errors, errors
        browser.close()
finally:
    server.terminate()
    server.wait(timeout=10)
