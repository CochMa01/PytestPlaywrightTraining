from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    expect(page.get_by_text("The Free Encyclopedia")).to_be_visible()
    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("Cats")
    page.get_by_label("Search Wikipedia").click()
    expect(page.get_by_label("Search Wikipedia")).to_have_value("Cats")
    page.get_by_role("button", name="Search").click()
    page.locator("#toc-Senses").get_by_role("link", name="Senses").click()
    page.get_by_role("link", name="Whiskers", exact=True).click()
    expect(page.locator("#Behavior")).to_contain_text("Behavior")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

    # Run the command using python toolkit/19_Codegen.py.