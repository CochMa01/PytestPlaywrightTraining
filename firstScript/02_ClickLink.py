from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/python")

    docs_link = page.get_by_role("link", name="Docs")
    docs_link.highlight()
    docs_link.click()
    print("Current URL is:", page.url)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 01_LaunchBrowser.py and rename it to 02_ClickLink.py.
    # Now our next task is to click the Documentation link.
    # Open an actual browser and navigate to the playwright.dev/python website.
    # Right-click on the Documentation link and select Inspect.
    # The Developer Tools window will open.
    # Check the highlighted node on the DevTools window.
    # The highlighted node is the <a> tag with the text Docs.
    # Update the code to locate the Documentation link first.
    # Add the following line of code after the page.goto method.
    # Line 8: page.locator("text=Docs") or page.get_by_role("link", name="Docs")
    # Next step is to create a variable to store the Documentation link locator.
    # Update the Line 8 to this: docs_link = page.locator("text=Docs") or
    # docs_link = page.get_by_role("link", name="Docs")
    # We can do another action to highlight the Documentation link.
    # Add Line 9: docs_link.highlight() to see the highlighted element.
    # Now click the docs_link variable by adding a new line and .click() method.
    # Line 10: docs_link.click()
    # Run the script using: python firstScript/02_ClickLink.py
    # To the participants, it should still be: python firstScript/myFirstCode.py
    # Add another line of code to print the current url of the page.
    # Line 11: print("Current URL is:", page.url)
    # Run the script again and check the console output.
