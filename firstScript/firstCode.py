import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

siteUrl = "https://playwright.dev"


with sync_playwright() as p:
    browser = p.firefox.launch(headless=False, slow_mo=2000)
    print("Running SYNCHRONOUS in FIREFOX.")

    page = browser.new_page()

    page.goto(siteUrl)

    print(page.title(), "\n")
    browser.close()

async def main():
    async with async_playwright() as ap:
        browser = await ap.chromium.launch(headless=False, slow_mo=2000)
        print("Running ASYNCHRONOUS in CHROME.")

        page = await browser.new_page()

        await page.goto(siteUrl)

        print(await page.title())
        await browser.close()

asyncio.run(main())
