from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://demoqa.com/checkbox")

    expand_elem = page.locator("//button[@class='rct-collapse rct-collapse-btn']")
    expand_elem.highlight()
    expand_elem.click()
    page.wait_for_timeout(3000)

    desktop_checkbox_elem = page.locator("//label[@for='tree-node-desktop']/span[1]")
    desktop_checkbox_elem.highlight()
    desktop_checkbox_elem.dblclick(delay=1000)
    page.wait_for_timeout(3000)

    desktop_checkbox_elem.click(button="right")
    page.wait_for_timeout(3000)

    downloads_checkbox_elem = page.locator("//label[@for='tree-node-downloads']")
    downloads_checkbox_elem.highlight()
    downloads_checkbox_elem.hover()
    page.wait_for_timeout(3000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 09_LocatorsByXPath.py and rename it to 10_MouseActions.py.
    # On this script, we will focus on how we can automate mouse functions.
    # Update first the URL to https://demoqa.com/checkbox.
    # Starting off with the basic function which is the normal click or left-click.
    # Expand the caret button on the Home Folder page.
    # Locate the element of the Expand button.
    # Start by typing page.locator("//button[@class='rct-collapse rct-collapse-btn']")
    # Highlight the element using expand_elem.highlight().
    # Click the element using expand_elem.click().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script using python firstScript/10_MouseActions.py.

    # Next, let's do a double click on the Desktop Checkbox element.
    # Locate the Desktop checkbox element.
    # Start by typing page.locator("//label[@for='tree-node-desktop']/span[1]").
    # Store it in a variable named desktop_checkbox_elem.
    # Highlight the element using desktop_checkbox_elem.highlight().
    # Double click the element using desktop_checkbox_elem.dblclick(delay=1000).
    # Adding a delay helps us see the changes on the element.
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Let's do a right-click on the Desktop Checkbox element.
    # Using the same element, start by typing desktop_checkbox_elem.click(button="right").
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.
    # Notice the same context menu that appears when you right-click on a webpage.

    # Now let's do a hover action on the Downloads Checkbox element.
    # Start by typing page.locator("//label[@for='tree-node-downloads']").
    # Store it in a variable named downloads_checkbox_elem.
    # Highlight the element using downloads_checkbox_elem.highlight().
    # Hover the element using downloads_checkbox_elem.hover().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.
