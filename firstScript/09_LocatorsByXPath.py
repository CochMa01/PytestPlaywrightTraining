from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://demoqa.com/text-box")

    header_elem = page.locator("xpath=//h1")
    header_elem.highlight()
    page.wait_for_timeout(3000)

    label_elem = page.locator("//label")
    label_elem.highlight()
    page.wait_for_timeout(3000)

    fullname_elem = page.locator("//label[@id='userName-label']")
    fullname_elem.highlight()
    page.wait_for_timeout(3000)

    email_field_elem = page.locator("//input[@placeholder='name@example.com']")
    email_field_elem.highlight()
    page.wait_for_timeout(3000)

    # Exercise Answer:
    submit_elem = page.locator("//button[@class='btn btn-primary']")
    submit_elem.highlight()
    page.wait_for_timeout(3000)

    # current_address_elem = page.locator("xpath=/html/body/div[2]/div/div/div/div[2]
    # /div[2]/form/div[3]/div[2]/textarea")
    # current_address_elem.highlight()
    # page.wait_for_timeout(3000)

    header_new_elem = page.locator("//h1[text()='Text Box']")
    header_new_elem.highlight()
    page.wait_for_timeout(3000)

    address_elem = page.locator("//label[contains(text(), 'Address')]")
    address_elem.highlight()
    page.wait_for_timeout(3000)

    address_field_elem = page.locator("//textarea[contains(@class, 'form-control')]")
    address_field_elem.highlight()
    page.wait_for_timeout(3000)

    address_field_1_elem = page.locator("(//textarea)[1]")
    address_field_1_elem.highlight()
    page.wait_for_timeout(3000)

    address_field_2_elem = page.locator("(//textarea[contains(@class, 'form-control')])[2]")
    address_field_2_elem.highlight()
    page.wait_for_timeout(3000)

    target_area_elem = page.locator("//div[@class='text-field-container']")
    target_area_elem.highlight()
    page.wait_for_timeout(3000)

    label_1_elem = page.locator("//div[@class='text-field-container']//label[@id='userName-label']")
    label_1_elem.highlight()
    page.wait_for_timeout(3000)

    label_2_elem = page.locator("//div[@class='text-field-container']//descendant::label[2]")
    label_2_elem.highlight()
    page.wait_for_timeout(3000)

    label_3_elem = page.locator("//label[@id='userName-label']//following::label[2]")
    label_3_elem.highlight()
    page.wait_for_timeout(3000)

    label_1_parent_elem = page.locator("//label[@id='userName-label']//parent::div")
    label_1_parent_elem.highlight()
    page.wait_for_timeout(3000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 08_LocatorsByCSS.py and rename it to 09_LocatorsByXPath.py.
    # On this script, we will focus on the locating elements by XPath selectors.
    # XPath supports locating elements by their tagname, classname, id, and attribute/value pair.
    # Two Types: Absolute and Relative
    # Absolute: Starts with the root node or the html tag. Demo on the DevTools by doing CTRL + F.
    # Relative: Starts with a double forward slash //.
    # In this topic, we will focus on the relative XPath.
    # Locate the Text Box header element using the XPath locator.
    # We will use the tagname for this example. Start by typing page.locator("//h1").
    # Store it in a variable named header_elem.
    # Highlight the element using header_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script using: python firstScript/09_LocatorsByXPath.py
    #
    # Now let's locate the label elements using the XPath and tagname locator.
    # Start by typing page.locator("//label").
    # Store it in a variable named label_elem.
    # Highlight the element using label_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Locate the label element with id attribute using the XPath locator.
    # Start by typing page.locator("//label[@id='userName-label']").
    # Store it in a variable named fullname_elem.
    # Highlight the element using fullname_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Locate the email field element with placeholder attribute using the XPath locator.
    # Start by typing page.locator("//input[@placeholder='name@example.com']").
    # Store it in a variable named email_field_elem.
    # Highlight the element using email_field_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Quick Exercise:
    # Locate the submit button element with any attribute available using the XPath locator.
    # Start by typing page.locator("//button[@id='submit']").
    # Store it in a variable named submit_elem.
    # Highlight the element using submit_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Let's locate the current address field element using the Absolute XPath.
    # Start by typing page.locator("/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/textarea").
    # Store it in a variable named current_address_elem.
    # Highlight the element using current_address_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.
    # Notice that the Absolute XPath is not recommended for locating elements due to its fragility.
    # It is prone to breaking when the structure of the HTML changes.
    # Always use the Relative XPath for locating elements.

    # Let's locate the header using the xpath's text function.
    # Start by typing page.locator("//h1[text()='Text Box']").
    # Store it in a variable named header_new_elem.
    # Highlight the element using header_new_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Let's locate the address label using the xpath's contains text function.
    # Start by typing page.locator("//label[contains(text(), 'Address')]").
    # Store it in a variable named address_elem.
    # Highlight the element using address_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Let's locate the address field using contains function on attributes.
    # Start by typing page.locator("//textarea[contains(@class, 'form-control')]").
    # Store it in a variable named address_field_elem.
    # Highlight the element using address_field_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Let's locate the first textarea element using tagname and its index.
    # Start by typing page.locator("(//textarea[1])").
    # Store it in a variable named address_field_1_elem.
    # Highlight the element using address_field_1_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).

    # Let's locate the 2nd address field using the xpath's index function.
    # Start by typing page.locator("(//textarea[contains(@class, 'form-control')])[2]").
    # Store it in a variable named address_field_2_elem.
    # Highlight the element using address_field_2_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Let's locate elements in combination with anchors.
    # Start by typing page.locator("//div[@class='text-field-container']").
    # Store it in a variable named target_area_elem.
    # Highlight the element using target_area_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Let's locate the first label element inside the target area.
    # Start by typing page.locator("//div[@class='text-field-container']//label[@id='userName-label']")
    # Store it in a variable named label_1_elem.
    # Highlight the element using label_1_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Let's discuss the common XPath Axes being used.
    # Starting of with descendant.
    # Let's locate the second label element using the descendant axis.
    # Descendant pertains to the child elements of the parent element.
    # Start by typing page.locator("//div[@class='text-field-container']//descendant::label[2]").
    # Store it in a variable named label_2_elem.
    # Highlight the element using label_2_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Next is the following axis.
    # Let's locate the 3rd label or the Current Address element using the following axis.
    # Following pertains to the sibling elements of the parent element.
    # Start by typing page.locator("//label[@id='userName-label']//following::label[2]").
    # Store it in a variable named label_3_elem.
    # Highlight the element using label_3_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.

    # Lastly, the parent axis.
    # Let's locate the parent element of the first label element.
    # Parent pertains to the parent element of the child element.
    # Start by typing page.locator("//label[@id='userName-label']//parent::div").
    # Store it in a variable named label_1_parent_elem.
    # Highlight the element using label_1_parent_elem.highlight().
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.
