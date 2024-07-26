from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://demo.nopcommerce.com/login")

    email_elem = page.get_by_label("Email:")
    email_elem.highlight()
    page.wait_for_timeout(3000)

    password_elem = page.get_by_label("Password:")
    password_elem.highlight()
    page.wait_for_timeout(3000)

    page.goto("https://demoqa.com/text-box")

    fullname_elem = page.get_by_placeholder("Full Name")
    fullname_elem.highlight()
    page.wait_for_timeout(3000)

    email_elem = page.get_by_placeholder("name@example.com")
    email_elem.highlight()
    page.wait_for_timeout(3000)

    # Exercise Answer:
    current_address_elem = page.get_by_placeholder("Current Address")
    current_address_elem.highlight()
    page.wait_for_timeout(3000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 03_LocatorsByRole.py and rename it to 04_LocatorsByLabel.py.
    # On this script, we will focus on locating elements by label.
    # We just need to update few lines on the script.
    # Update the url to https://demo.nopcommerce.com/login.
    # Start by typing page.get_by_label("Email:").
    # Store it in a variable named email_elem.
    # Highlight the email_elem by adding email_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script using: python firstScript/04_LocatorsByLabel.py

    # Do the same for the password field.
    # Start by typing page.get_by_label("Password:").
    # Store it in a variable named password_elem.
    # Highlight the password_elem by adding password_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.

    # Please take note that depending on the website, page.get_by_label may not work.
    # This is mainly due to the nodes on HTML having a different structure.
    # We might need to try a different locator strategy which is by placeholder.
    # Navigate to the Text Box page that we have used in the previous script.
    # Update the URL to https://demoqa.com/text-box.
    # Start by typing page.get_by_placeholder("Full Name").
    # Store it in a variable named fullname_elem.
    # Highlight the fullname_elem by adding fullname_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.

    # Quick Exercise: For 3 mins, locate the Email and Current Address text fields using the placeholder locator.
    # Start by typing page.get_by_placeholder("Current Address").
    # Store it in a variable named current_address_elem.
    # Highlight the current_address_elem by adding current_address_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.
