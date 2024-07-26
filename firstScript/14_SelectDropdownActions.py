from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://bootswatch.com/default/")

    select_elem = page.locator("//select[@id='exampleSelect1']")
    select_elem.scroll_into_view_if_needed()
    select_elem.highlight()
    select_elem.select_option("3")
    page.wait_for_timeout(3000)

    multi_select_elem = page.locator("//select[@id='exampleSelect2']")
    multi_select_elem.scroll_into_view_if_needed()
    multi_select_elem.highlight()
    multi_select_elem.select_option(["1", "3", "4"])
    page.wait_for_timeout(3000)

    dropdown_elem = page.locator("//button[@id='btnGroupDrop1']")
    dropdown_elem.scroll_into_view_if_needed()
    dropdown_elem.highlight()
    dropdown_elem.click()
    page.wait_for_timeout(3000)

    dropdown_option_elem = dropdown_elem.locator("//following-sibling::div[1]/a[2]")
    dropdown_option_elem.highlight()
    page.wait_for_timeout(3000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 13_CheckboxActions.py.py and rename it to 14_SelectDropdownActions.py.
    # On this script, we will focus on how we can automate Radio buttons and Checkbox actions.
    # Update first the URL to https://bootswatch.com/default/.
    # Let's automate an example of a Select element.
    # Start by typing page.locator("//select[@id='exampleSelect1']").
    # Store it in a variable named select_elem.
    # Sometimes the page is not that responsive, so we need to scroll it into view.
    # Scroll to the element by calling select_elem.scroll_into_view_if_needed().
    # Highlight the element by calling select_elem.highlight().
    # Now, let's select an option from the dropdown.
    # Call select_elem.select_option("3").
    # This will select the option with the value "3".
    # Then explicitly wait for 3 seconds by calling page.wait_for_timeout(3000).
    # Run the script using: python firstScript/14_SelectDropdownActions.py

    # Next, let's automate a Multi-Select element.
    # Start by typing page.locator("//select[@id='exampleSelect2']").
    # Store it in a variable named multi_select_elem.
    # Scroll to the element by calling multi_select_elem.scroll_into_view_if_needed().
    # Highlight the element by calling multi_select_elem.highlight().
    # Now, let's select multiple options from the dropdown.
    # Call multi_select_elem.select_option(["1", "3", "4"]).
    # This will select the options with the values "1", "3", and "4".
    # Then explicitly wait for 3 seconds by calling page.wait_for_timeout(3000).
    # Run the script again.

    # Lastly, let's automate a Dropdown element.
    # Start by typing page.locator("//button[@id='btnGroupDrop1']").
    # Store it in a variable named dropdown_elem.
    # Scroll to the element by calling dropdown_elem.scroll_into_view_if_needed().
    # Highlight the element by calling dropdown_elem.highlight().
    # Now, let's click the dropdown.
    # Call dropdown_elem.click().
    # Then explicitly wait for 3 seconds by calling page.wait_for_timeout(3000).
    # Run the script again.

    # Let's automate a Dropdown option element.
    # Start by typing dropdown_elem.locator("//following-sibling::div[1]/a[2]").
    # Store it in a variable named dropdown_option_elem.
    # Highlight the element by calling dropdown_option_elem.highlight().
    # Then explicitly wait for 3 seconds by calling page.wait_for_timeout(3000).
    # Run the script again.
