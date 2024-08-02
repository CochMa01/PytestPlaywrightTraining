from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://demoqa.com/checkbox")

    expand_elem = page.get_by_title("Expand all")
    expand_elem.highlight()
    page.wait_for_timeout(3000)

    collapse_elem = page.get_by_title("Collapse all")
    collapse_elem.highlight()
    page.wait_for_timeout(3000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 06_LocatorsByAltText.py and rename it to 07_LocatorsByTitle.py.
    # On this script, we will focus on locating elements by title.
    # We can use this to locate elements with the title attribute.
    # Examples with title attributes can be found on sources, links and sometimes images.
    # It will work as long there is a title attribute on the element, be it a checkbox, a button, a link, etc.
    # For the example, update the URL to https://demoqa.com/checkbox.
    # Locate the Expand All button using the title attribute.
    # Start by typing page.get_by_title("Expand all").
    # Store it in a variable named expand_elem.
    # Highlight the expand_elem by adding expand_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script using: python firstScript/07_LocatorsByTitle.py

    # Another example: Locate the Collapse All button using the title attribute.
    # Start by typing page.get_by_title("Collapse all").
    # Store it in a variable named collapse_elem.
    # Highlight the collapse_elem by adding collapse_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.

    # There is another method to locate elements by test-id.
    # This method works the same way as the get_by_title method.
    # This is only applicable to those element that has "data-testid" attribute.
    # Example: https://playwright.dev/docs/locators#locate-by-test-id
