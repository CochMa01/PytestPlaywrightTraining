
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/python")

    context.close()
    browser.close()

    # Run the script with the command: python 01_LaunchBrowser.py
    # The browser will open and navigate to the playwright.dev website but in headless mode.
    # This is the default setting when you have not specified the headless parameter.
    # Update the code to launch the browser in headed mode.
    # Line 8: browser = playwright.chromium.launch(headless=False)
    # Run the script again, and you will see the browser window open.
    # Notice that it is too fast and cannot clearly see the actions performed.
    # Update the code to slow down the actions.
    # Line 8: browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    # Run the script again, and you will see the actions performed slowly.
