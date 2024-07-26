import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://cert1-advance.lexis.com/")
    page.locator("#onetrust-banner-sdk").click()
    page.get_by_label("Privacy", exact=True).get_by_text("We use cookies which are").click()
    # page.get_by_label("ID Please enter a valid ID.").click()
    page.get_by_label("ID Please enter a valid ID.").fill("PRMAAutomation02")
    page.get_by_role("button", name="Next").click()
    # page.get_by_label("Password Please enter a valid").click()
    page.get_by_label("Password Please enter a valid").fill("H0gW@rtsFro5t")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(3000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)