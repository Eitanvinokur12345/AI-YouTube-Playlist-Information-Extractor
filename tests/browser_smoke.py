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
        page.goto("http://127.0.0.1:8787/docs/", wait_until="domcontentloaded")
        page.get_by_role("heading", name="Your video knowledge, in one place.").wait_for()
        for tab in ["videos", "hub", "skills", "tools", "prompts", "tips", "connectors", "packages", "taste", "selfimprove", "effectiveness", "devbuild"]:
            page.locator(f'nav button[data-tab="{tab}"]').click()
            page.wait_for_function(
                """() => { const v=document.querySelector('#view');
                return v && v.textContent.trim() && !v.textContent.trim().startsWith('Loading'); }""")
            assert "This view could not load." not in page.locator("#view").inner_text(), tab
            assert not page.locator(".ex-strip, #crew, #approve-bell").count(), tab
        page.locator('nav button[data-tab="videos"]').click()
        page.locator("#video-stage").select_option("analyzed")
        page.get_by_role("heading", name="Video library", exact=True).wait_for()
        page.locator("#video-category").wait_for()
        page.locator('nav button[data-tab="overview"]').click()
        page.get_by_role("heading", name="Your video knowledge, in one place.").wait_for()
        page.set_viewport_size({"width": 390, "height": 844})
        assert page.locator("#view").is_visible()
        assert not errors, errors
        browser.close()
finally:
    server.terminate()
    server.wait(timeout=10)
