from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/python")

    docs_link = page.get_by_role("link", name="Docs")
    docs_link.highlight()
    docs_link.click()

    print("Current URL is:", page.url)
    expect(page).to_have_url("https://playwright.dev/python/docs/intro")
    page.wait_for_timeout(1000)

    print("Current Title is:", page.title())
    expect(page).to_have_title("Installation | Playwright Python")
    page.wait_for_timeout(1000)

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
    # Run the script using: python 02_ClickLink.py

    # Next goal is to validate the current URL and title of the page.
    # Add a line of code to print the current URL of the page.
    # Line 11: print("Current URL is:", page.url)
    # We can also validate the current URL of the page.
    # Add a line of code to validate the current URL of the page.
    # Line 12: expect(page).to_have_url("https://playwright.dev/python/docs/intro")
    # Add a line of code to wait for 1 second.
    # Run the script again and check the console output.

    # Add a line of code to print the current title of the page.
    # Line 13: print("Current Title is:", page.title)
    # Add a line of code to validate the current title of the page.
    # Line 14: expect(page).to_have_title("Installation | Playwright Python")
    # Add a line of code to wait for 1 second.
    # Run the script again and check the console output.
