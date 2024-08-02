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
        browser2 = await ap.chromium.launch(headless=False, slow_mo=2000)
        print("Running ASYNCHRONOUS in CHROME.")

        page2 = await browser2.new_page()

        await page2.goto(siteUrl)

        print(await page2.title())
        await browser2.close()


asyncio.run(main())

    # Initiate discussion of the code with the sync_playwright.
    # Discuss the differences with sync and async codes.
    # Run the script using: python 00_FirstCode.py