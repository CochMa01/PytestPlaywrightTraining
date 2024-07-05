import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("Cats")
    page.get_by_label("Search Wikipedia").press("Enter")
    page.locator("#toc-Senses").get_by_role("link", name="Senses").click()
    page.get_by_role("link", name="Whiskers", exact=True).click()
    context.tracing.stop(path="toolkit/trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
