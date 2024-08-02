from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://demoqa.com/text-box")

    submit_elem = page.get_by_text("Submit")
    submit_elem.highlight()
    page.wait_for_timeout(3000)

    textbox_header_elem = page.get_by_text("Text Box")
    textbox_header_elem.highlight()
    page.wait_for_timeout(3000)

    address_elem = page.get_by_text("Address")
    address_elem.highlight()
    page.wait_for_timeout(3000)

    address_elem = page.get_by_text("Address", exact=False)
    address_elem.highlight()
    page.wait_for_timeout(3000)

    address_elem = page.get_by_text("Address", exact=False).first
    address_elem.highlight()
    page.wait_for_timeout(3000)

    address_elem = page.get_by_text("Address", exact=True)
    address_elem.highlight()
    page.wait_for_timeout(3000)

    # Exercise Answer:
    permanent_address_elem = page.get_by_text("Permanent Address", exact=True)
    permanent_address_elem.highlight()
    page.wait_for_timeout(3000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 04_LocatorsByLabel.py and rename it to 05_LocatorsByText.py.
    # On this script, we will focus on locating elements by their text.
    # Update the url to https://demoqa.com/text-box
    # This is useful when we cannot locate elements by role or label.
    # As an example let's try to locate the submit button on the Text Box page.
    # Start by typing page.get_by_text("Submit").
    # Store it in a variable named submit_elem.
    # Highlight the submit_elem by adding submit_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script using: python firstScript/05_LocatorsByText.py

    # Let's locate the Text Box header.
    # Start by typing page.get_by_text("Text Box").
    # Store it in a variable named textbox_header_elem.
    # Highlight the textbox_header_elem by adding textbox_header_elem.highlight().
    # Then explicitly add a delay of 10 seconds by typing page.wait_for_timeout(3000).
    # Run the script again. As you can see, there are two elements highlighted with the same text content.
    # Notice that there are also limitations when using the page.get_by_text method.
    # This limitation also applies to the page.get_by_label and page.get_by_role methods.
    # If there are more than one element with the same text content, it will only select the first element.

    # Locate the Address fields.
    # Start by typing page.get_by_text("Address").
    # Store it in a variable named address_elem.
    # Highlight the address_elem by adding address_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.
    # Notice that again, it returns two highlighted elements with the text content "Address".

    # By default, page.get_by_text satisfies the partial match of the text content.
    # If we want to use the exact match, we can add another parameter which is the exact=True.
    # Let's try to locate the Address texts on the same page.
    # Update the address_elem variable to this: address_elem = page.get_by_text("Address", exact=False).
    # Run the script again. It should return two elements since it follows the contains logic.

    # If we want to locate only the first element that contains "Address" on text, we can use the .first method.
    # Simply update the same code to this: address_elem = page.get_by_text("Address").first().
    # Run the script again. It should return only the first element that contains "Address" on text.

    # Update the address_elem variable to this: address_elem = page.get_by_text("Address", exact=True).
    # Run the script again. It will not return any element since it the text should be an exact match.

    # Quick Exercise: Locate the Permanent Address text on the same page.
    # Start by typing page.get_by_text("Permanent Address", exact=True).
    # Store it in a variable named permanent_address_elem.
    # Highlight the permanent_address_elem by adding permanent_address_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.
