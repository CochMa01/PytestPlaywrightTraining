from playwright.sync_api import sync_playwright, expect

with (sync_playwright() as playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://demoqa.com/dynamic-properties")

    # Happy Path
    button_disabled_elem = page.locator("#enableAfter")
    expect(button_disabled_elem).to_be_enabled()

    button_visible_elem = page.locator("#visibleAfter")
    expect(button_visible_elem).to_be_visible()

    # Negative Testing

    # button_disabled_elem = page.locator("#enableAfter")
    # page.wait_for_selector("#enableAfter", state="attached", timeout=1000, strict=True)
    # # expect(button_disabled_elem).to_be_enabled()
    # expect(button_disabled_elem).to_be_enabled(timeout=1000)

    # button_visible_elem = page.locator("#visibleAfter")
    # page.wait_for_selector("#visibleAfter", state="visible", timeout=1000, strict=True)
    # button_visible_elem.highlight()
    # expect(button_visible_elem).to_be_visible(timeout=1000)

    # Discuss ways to modify the default timeout values.
    # Wait up to 60 seconds for navigation to complete
    # page.goto("https://example.com", timeout=60000)

    # Wait up to 60 seconds for the element
    # page.wait_for_selector("selector", timeout=60000)

    # Set a default timeout of 60 seconds for all actions in this context
    # context.set_default_timeout(60000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 16_SwitchTabsWindowsActions.py and rename it to 17_Autowaits.py.
    # On this script, we will focus on how we can automate Radio buttons and Checkbox actions.
    # Update first the URL to https://davidwalsh.name/demo/multiple-file-upload.php.
