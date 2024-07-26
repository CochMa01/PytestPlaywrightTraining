from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://demoqa.com/radio-button")

    # yes_radio_elem = page.locator("//input[@id='yesRadio']")
    yes_radio_elem = page.locator("//label[@for='yesRadio']")
    yes_radio_elem.highlight()
    yes_radio_elem.check()
    page.wait_for_timeout(3000)
    assert yes_radio_elem.is_checked() is True

    no_radio_elem = page.locator("//label[@for='noRadio']")
    assert no_radio_elem.is_checked() is False

    text_success_elem = page.locator("//span[@class='text-success']")
    text_success_elem.highlight()
    print(f"Text Success value is: {text_success_elem.text_content()}")
    assert text_success_elem.text_content() == "Yes"
    page.wait_for_timeout(3000)

    # Exercise Answer:
    impressive_radio_elem = page.locator("//label[@for='impressiveRadio']")
    impressive_radio_elem.highlight()
    impressive_radio_elem.check()
    page.wait_for_timeout(3000)
    assert impressive_radio_elem.is_checked() is True
    print(f"Text Success value is: {text_success_elem.text_content()}")
    assert text_success_elem.text_content() == "Impressive"

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 11_InputFieldActions.py and rename it to 12_RadioButtonActions.py.
    # On this script, we will focus on how we can automate Radio buttons and Checkbox actions.
    # Update first the URL to https://demoqa.com/radio-button.
    # Start with locating the Yes Radio button element.
    # Start by typing page.locator("//input[@id='yesRadio']").
    # Store it in a variable named yes_radio_elem.
    # Highlight the element using yes_radio_elem.highlight().
    # Check the element using yes_radio_elem.check().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script using python firstScript/12_RadioButtonActions.py.
    # Notice that an error is showing. There is an element receiving the check event instead of the
    # one that we have declared. To fix this, we have to change the locator to the label element.
    # Update the locator to "//label[@for='yesRadio']".
    # Then run the script again.

    # This time, let's assert that the Yes Radio button is checked.
    # Assert by using yes_radio_elem.is_checked() is True.

    # Next, let's locate the No Radio button element.
    # Start by typing page.locator("//label[@for='noRadio']").
    # Store it in a variable named no_radio_elem.
    # Assert by using no_radio_elem.is_checked() is False.

    # Additional ways to do assertions.
    # Notice that if we click the Yes radio button, there's a text showing the one we selected.
    # Let's maximize this to do an assertion.
    # Locate the resulting element.
    # Start by typing page.locator("//span[@class='text-success']").
    # Store it in a variable named text_success_elem.
    # Highlight the element using text_success_elem.highlight().
    # Print the text value using print(f"Text Success value is: {text_success_elem.text_content()}").
    # Assert that value using assert text_success_elem.text_content() == "Yes".
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Now for the Quick Exercise:
    # Locate the Impressive Radio button element.
    # Start by typing page.locator("//label[@for='impressiveRadio']").
    # Store it in a variable named impressive_radio_elem.
    # Highlight the element using impressive_radio_elem.highlight().
    # Check the element using impressive_radio_elem.check().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Assert by using impressive_radio_elem.is_checked() is True.
    # Print the text value using print(f"Text Success value is: {text_success_elem.text_content()}").
    # Assert that value using assert text_success_elem.text_content() == "Impressive".
    # Run the script again.
