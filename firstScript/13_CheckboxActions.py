from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://demoqa.com/checkbox")

    expand_all_button_elem = page.locator("//button[@title='Expand all']")
    expand_all_button_elem.highlight()
    expand_all_button_elem.click()
    page.wait_for_timeout(3000)

    desktop_checkbox_elem = page.locator("//label[@for='tree-node-desktop']/span[1]")
    desktop_checkbox_elem.highlight()
    desktop_checkbox_elem.check()
    page.wait_for_timeout(3000)

    desktop_checkbox_elem.check()
    # assert desktop_checkbox_elem.is_checked() is False
    assert desktop_checkbox_elem.is_checked() is True

    office_checkbox_elem = page.locator("//label[@for='tree-node-office']/span[1]")
    office_checkbox_elem.highlight()
    office_checkbox_elem.check()
    page.wait_for_timeout(3000)

    office_checkbox_elem.uncheck()
    page.wait_for_timeout(3000)
    assert office_checkbox_elem.is_checked() is False

    office_checkbox_elem.set_checked(True)
    page.wait_for_timeout(3000)
    assert office_checkbox_elem.is_checked() is True

    office_checkbox_elem.set_checked(False)
    page.wait_for_timeout(3000)
    assert office_checkbox_elem.is_checked() is False

    downloads_checkbox_elem = page.locator("//label[@for='tree-node-downloads']/span[1]")
    downloads_checkbox_elem.highlight()
    downloads_checkbox_elem.check()
    page.wait_for_timeout(3000)

    text_success_collection = []

    results_checked_elems = page.locator("//div[@id='result']//following-sibling::span[1]")
    for text_success_elem in results_checked_elems.element_handles():
        text_content = text_success_elem.text_content()
        print(f"Text Success value is: {text_content}")
        text_success_collection.append(text_content)

    print(text_success_collection)

    assert 'desktop' in text_success_collection
    assert 'notes' in text_success_collection
    assert 'commands' in text_success_collection
    assert 'downloads' in text_success_collection
    assert 'wordFile' in text_success_collection
    assert 'excelFile' in text_success_collection

    expected_texts = ['desktop', 'notes', 'commands', 'downloads1', 'wordFile1', 'excelFile1']
    for expected_text in expected_texts:
        try:
            assert expected_text in text_success_collection
            print(f"Assertion passed for: {expected_text}")
        except AssertionError:
            print(f"Assertion failed for: {expected_text}. Continuing...")
            continue

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 12_RadioButtonActions.py.py and rename it to 13_CheckboxActions.py.
    # On this script, we will focus on how we can automate Radio buttons and Checkbox actions.
    # Update first the URL to https://demoqa.com/checkbox.
    # First off, let's click the Expand All button located on the right side part of the page.
    # Start by typing page.locator("//button[@title='Expand all']").
    # Store it in a variable named expand_all_button_elem.
    # Highlight the element using expand_all_button_elem.highlight().
    # Click the element using expand_all_button_elem.click().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script using python firstScript/13_CheckboxActions.py.

    # Next, let's check the Desktop Checkbox element.
    # Start by typing page.locator("//label[@for='tree-node-desktop']/span[1]").
    # Store it in a variable named desktop_checkbox_elem.
    # Highlight the element using desktop_checkbox_elem.highlight().
    # Check the element using desktop_checkbox_elem.check().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Let's add another line of code to check again the Desktop Checkbox element.
    # By doing so, we are expecting that the element will be unchecked.
    # Let's also add an assertion to verify the element is unchecked.
    # Add: assert desktop_checkbox_elem.is_checked() is False.
    # This run will cause an error because the .click() is different from the .check() method.
    # The .click() method will always click the element regardless of its current state.
    # The .check() method will only check the element if it is not checked.
    # If it is checked, it will not do anything.

    # Next, let's update the assertion to True.
    # Update: assert desktop_checkbox_elem.is_checked() is True.
    # Run the script again.

    # Now, let's locate the Office Checkbox element.
    # Start by typing page.locator("//label[@for='tree-node-office']/span[1]").
    # Store it in a variable named office_checkbox_elem.
    # Highlight the element using office_checkbox_elem.highlight().
    # Check the element using office_checkbox_elem.check().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Now, uncheck the element using office_checkbox_elem.uncheck().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Assert that the element is unchecked using assert office_checkbox_elem.is_checked() is False.
    # Run the script again.

    # Another way to do check actions is by using the set_checked() method.
    # Let's check the Office Checkbox element again.
    # Start by typing office_checkbox_elem.set_checked(True).
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Assert that the element is checked using assert office_checkbox_elem.is_checked() is True.
    # Continue by typing office_checkbox_elem.set_checked(False).
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Assert that the element is unchecked using assert office_checkbox_elem.is_checked() is False.

    # Let's dig deeper into some assertions.
    # Locate the Downloads Checkbox element.
    # Start by typing page.locator("//label[@for='tree-node-downloads']/span[1]").
    # Store it in a variable named downloads_checkbox_elem.
    # Highlight the element using downloads_checkbox_elem.highlight().
    # Check the element using downloads_checkbox_elem.check().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.
    # Notice on the lower part of the page, there are texts showing the elements we checked.
    # Let's do an assertion to those texts displayed.
    # Locate the text results.
    # Start by typing page.locator("//div[@id='result']//following-sibling::span[1]").
    # Store it in a variable named results_checked_elems.
    # Loop through the elements and print the text content.
    # First let's create a for loop.
    # The results_checked_elems should be an XPath that will return multiple elements.
    # With the same XPath, we will use the element_handles() method.
    # This element_handles() method will return a list of elements.
    # For each element, we will need to get their corresponding text content.
    # ----------------------------------------
    # results_checked_elems = page.locator("//div[@id='result']//following-sibling::span[1]")
    # for text_success_elem in results_checked_elems.element_handles():
    #     text_content = text_success_elem.text_content()
    #     print(f"Text Success value is: {text_content}")
    # ----------------------------------------
    # Run the script. It will print the text content of the elements.

    # How about we store the text content in a list?
    # First, let's create an empty list named text_success_collection.
    # Then at the end of the for loop, append the text_content to the text_success_collection.
    # Also print the list created.
    # ----------------------------------------
    # text_success_collection = []
    #
    # results_checked_elems = page.locator("//div[@id='result']//following-sibling::span[1]")
    # for text_success_elem in results_checked_elems.element_handles():
    #     text_content = text_success_elem.text_content()
    #     print(f"Text Success value is: {text_content}")
    #     text_success_collection.append(text_content)
    #
    # print(text_success_collection)
    # ----------------------------------------
    # Run the script. It will print the list of text content of the elements.
    # It will also print the list created.

    # Now, do individual assertions for each text content found on the list.
    # ----------------------------------------
    # assert 'desktop' in text_success_collection
    # assert 'notes' in text_success_collection
    # assert 'commands' in text_success_collection
    # assert 'downloads' in text_success_collection
    # assert 'wordFile' in text_success_collection
    # assert 'excelFile' in text_success_collection
    # ----------------------------------------
    # Run the script. It will assert each text content found on the list.

    # For a geeker mode of assertion, how about we create a list of expected texts?
    # Then assert each of the texts against the collection of text content we have.
    # Declare the list of expected_texts.
    # Then create a for loop to assert each text content against the expected_texts.
    # On the expected_texts, intentionally append "1" for the last 3 texts.
    # This way we can see the assertion fail.
    # ----------------------------------------
    # expected_texts = ['desktop', 'notes', 'commands', 'downloads1', 'wordFile1', 'excelFile1']
    # for expected_text in expected_texts:
    #     assert expected_text in text_success_collection, f"{expected_text} not found in text_success_collection"
    # ----------------------------------------
    # Run the script. It will assert each text content found on the list.
    # Notice that at the text "downloads1", the run already stops.

    # What if I want the for loop to continue all the assertions until the end?
    # Also print those expected texts that passed.
    # For this case, we will add a try-except block to the for loop.
    # Add a try-except block to the for loop.
    # ----------------------------------------
    # for expected_text in expected_texts:
    #     try:
    #         assert expected_text in text_success_collection
    #         print(f"Assertion passed for: {expected_text}")
    #     except AssertionError:
    #         print(f"Assertion failed for: {expected_text}. Continuing...")
    #         continue
    # ----------------------------------------
    # Run the script. It will assert each text content found on the list.
    # It will even print the expected texts that passed and failed.
