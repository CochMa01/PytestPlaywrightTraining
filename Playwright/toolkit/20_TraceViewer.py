from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    expect(page.get_by_text("The Free Encyclopedia")).to_be_visible()
    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("Cats")
    page.get_by_label("Search Wikipedia").click()
    expect(page.get_by_label("Search Wikipedia")).to_have_value("Cats")
    page.get_by_role("button", name="Search").click()
    page.locator("#toc-Senses").get_by_role("link", name="Senses").click()
    page.get_by_role("link", name="Whiskers", exact=True).click()
    expect(page.locator("#Behavior")).to_contain_text("Behavior")

    context.tracing.stop(path="toolkit/trace/trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

    # Run the command using python toolkit/20_TraceViewer.py.
    # We are expecting to have a zip file in the toolkit/trace directory named trace.zip.
    # This zip file will contain the trace of the browser's activity.
    # To view the trace, run "playwright show-trace toolkit/trace/trace.zip" on the terminal.
