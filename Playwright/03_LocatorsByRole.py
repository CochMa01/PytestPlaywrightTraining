from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://demoqa.com/text-box")

    header_elem = page.get_by_role("heading", name="Text Box")
    header_elem.highlight()
    page.wait_for_timeout(3000)

    btn_elem = page.get_by_role("button", name="Submit")
    btn_elem.highlight()
    page.wait_for_timeout(3000)

    page.goto("https://demoqa.com/radio-button")

    radio_elem = page.get_by_role("radio", name="Impressive")
    radio_elem.highlight()
    page.wait_for_timeout(3000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 02_ClickLink.py and rename it to 03_LocatorsByRole.py.
    # On this script, we will focus on locating elements by role.
    # We just need to update few lines on the script.
    # Maximize the browser by adding this argument on the browser variable. For Chromium only.
    # Line 4: browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    # Line 5: context = browser.new_context(no_viewport=True)
    # If running on Firefox or WebKit, use this:
    # context = browser.new_context(viewport= {"width": 1920, "height": 1080})
    # and Remove args parameter on the browser variable.
    # Update the URL to https://demoqa.com/text-box.
    # Line 7: page.goto("https://demoqa.com/text-box").
    # Let's see how we can maximize the get_by_role method to locate elements.
    # Let us examine the elements on the page.
    # Once on the page, we need to locate the Text Box header.
    # Start by typing page.get_by_role("heading", name="Text Box").
    # Next is to store it in a variable named header_elem.
    # Highlight the header_elem by adding header_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script using: python firstScript/03_LocatorsByRole.py

    # Next, we will locate the Submit button on the same page.
    # Start by typing page.get_by_role("button", name="Submit").
    # Store it in a variable named btn_elem.
    # Highlight the btn_elem by adding btn_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.

    # For the next example, we need first to navigate to the Radio Button page.
    # Add the code: page.goto("https://demoqa.com/radio-button").
    # Locate the Impressive radio button by typing page.get_by_role("radio", name="Impressive").
    # Store it in a variable named radio_elem.
    # Highlight the radio_elem by adding radio_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.
