from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://demoqa.com/text-box")

    header_elem = page.locator("css=h1")
    header_elem.highlight()
    page.wait_for_timeout(3000)

    submit_elem = page.locator(".btn-primary")
    submit_elem.highlight()
    page.wait_for_timeout(3000)

    fullname_elem = page.locator("#userName")
    fullname_elem.highlight()
    page.wait_for_timeout(3000)

    email_elem = page.locator("[type=email]")
    email_elem.highlight()
    page.wait_for_timeout(3000)

    current_address_elem = page.locator("[placeholder='Current Address']")
    current_address_elem.highlight()
    page.wait_for_timeout(3000)

    # Exercise Answer:
    permanent_address_elem = page.locator("#permanentAddress")
    permanent_address_elem.highlight()
    page.wait_for_timeout(3000)

    label_elem = page.locator("label")
    label_elem.highlight()
    page.wait_for_timeout(3000)

    add_label_elem = page.locator("label:text('Address')")
    add_label_elem.highlight()
    page.wait_for_timeout(3000)

    perm_add_label_elem = page.locator("label:text-is('Permanent Address')")
    perm_add_label_elem.highlight()
    page.wait_for_timeout(3000)

    label3_elem = page.locator(":nth-match(label, 3)")
    label3_elem.highlight()
    page.wait_for_timeout(3000)

    address_label_2_elem = page.locator(":nth-match(label:text('Address'), 2)")
    address_label_2_elem.highlight()
    page.wait_for_timeout(3000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 07_LocatorsByTitle.py and rename it to 08_LocatorsByCSS.py.
    # On this script, we will focus on the locating elements by CSS selectors.
    # CSS supports locating elements by their tagname, classname, id, and attribute/value pair.
    # Cheat Sheet and Examples: https://www.w3schools.com/cssref/css_selectors.asp
    # Update the URL to https://demoqa.com/text-box.
    # Locate the header Text Box by its tagname.
    # Start by typing page.locator("h1").
    # Store the result in a variable called header_elem.
    # Highlight the element using header_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script using: python firstScript/08_LocatorsByCSS.py

    # Another example: Locate the submit button by its classname.
    # Start by typing page.locator(".btn-primary").
    # Store the result in a variable called submit_elem.
    # Highlight the element using submit_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.

    # Another example: Locate the Full name input field by its id.
    # Start by typing page.locator("#userName").
    # Store the result in a variable called fullname_elem.
    # Highlight the element using fullname_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.

    # Another example: Locate the Email input field by its attribute.
    # Start by typing page.locator("[type=email]").
    # Store the result in a variable called email_elem.
    # Highlight the element using email_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.

    # Another example: Locate the Current Address input field by its attribute.
    # Start by typing page.locator("[placeholder='Current Address']").
    # Store the result in a variable called current_address_elem.
    # Highlight the element using current_address_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.

    # Quick Exercise: For 3 mins, locate the Permanent Address input field using CSS Selector.
    # Start by typing page.locator("#permanentAddress").
    # Store the result in a variable called permanent_address_elem.
    # Highlight the element using permanent_address_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.

    # Pseudo Classes with CSS Selectors
    # Playwright supports additional ways to locate elements using Pseudo Classes
    # with CSS Selectors to make it so much easier. Here are some examples:
    # Locate those elements starting with the node label.
    # Start by typing page.locator("label").
    # Store the result in a variable called label_elem.
    # Highlight the element using label_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.
    #
    # As you can see, there are four visible elements with the label tag.
    # Using pseudo classes with CSS, we can pinpoint which element we want to target/highlight.
    # As an example, let us highlight the Address element/s. Note that this follows contain logic.
    # Start by typing page.locator("label:text('Address')").
    # Store the result in a variable called add_label_elem.
    # Highlight the element using add_label_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.
    #
    # Now to make it more exact, let us highlight the Permanent Address element.
    # Start by typing page.locator("label:text-is('Permanent Address')").
    # Store the result in a variable called perm_add_label_elem.
    # Highlight the element using perm_add_label_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.
    #
    # Nth Match Pseudo Class
    # Enable the example on multiple label elements.
    # Let's locate the 3rd label element which is the Current Address.
    # Start by typing page.locator(":nth-match(label, 3)").
    # Store the result in a variable called label3_elem.
    # Highlight the element using label3_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.
    #
    # Nth Match Pseudo Class with Text
    # Let's locate the 2nd Address label element.
    # Start by typing page.locator(":nth-match(label:text('Address'), 2)").
    # Store the result in a variable called address_label_2_elem.
    # Highlight the element using address_label_2_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.
    