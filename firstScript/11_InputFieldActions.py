from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://demoqa.com/text-box")

    full_name_elem = page.locator("//input[@placeholder='Full Name']")
    full_name_elem.highlight()
    full_name_elem.fill("John Doe")
    page.wait_for_timeout(3000)

    full_name_elem.clear()
    # full_name_elem.fill("")
    page.wait_for_timeout(3000)

    full_name_elem.type("John Smith", delay=250)
    page.wait_for_timeout(3000)

    print(f"Full Name value is: {full_name_elem.input_value()}")
    assert full_name_elem.input_value() == "John Smith"
    page.wait_for_timeout(3000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 10_MouseActions.py and rename it to 11_InputFieldActions.py.
    # On this script, we will focus on how we can automate Input Field actions.
    # Update first the URL to https://demoqa.com/text-box.
    # Starting off with the basic function to fill an input field.
    # Locate the Full Name input field element.
    # Start by typing page.locator("//input[@placeholder='Full Name']").
    # Store it in a variable named full_name_elem.
    # Highlight the element using full_name_elem.highlight().
    # Fill the element with a text using full_name_elem.fill("John Doe").
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script using python firstScript/11_InputFieldActions.py.

    # Next, let's clear the input field.
    # Using the same element, start by typing full_name_elem.clear().
    # Optional using full_name_elem.fill("") will also clear the input field.
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.
    # Note that the .fill() method simulates CTRL + C and CTRL + V functions.

    # Now if we want to simulate the actual typing, let's use the .type() method.
    # Using the same element, start by typing full_name_elem.type("John Smith").
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.
    # Notice that it is like the .fill() method in this case.
    # But by adding a delay, you can see the typing action.
    # Update the full_name_elem.type("John Smith") to full_name_elem.type("John Smith", delay=250).
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).

    # Another method we can use is to get the value of a specific field.
    # Get the value of the element using full_name_elem.input_value().
    # Print the value using print(full_name_elem.input_value()).
    # Add an assertion to check if the value is equal to "John Smith".
    # Use assert full_name_elem.input_value() == "John Smith".
    # Then explicitly wait for 3 seconds using page.wait_for_timeout(3000).
    # Run the script again.
