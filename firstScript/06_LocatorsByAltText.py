from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://unsplash.com/")

    image_elem = page.get_by_alt_text("a woman in a pink dress covered in pink bows")
    image_elem.highlight()
    page.wait_for_timeout(3000)

    second_image_elem = page.get_by_alt_text("A red and blue object in the middle of the night sky")
    second_image_elem.highlight()
    page.wait_for_timeout(3000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 05_LocatorsByText.py and rename it to 06_LocatorsByAltText.py.
    # On this script, we will focus on locating elements by alt text.
    # Alt text are used to describe the content of an image.
    # We can use this to locate elements with images.
    # Update the url to https://unsplash.com/
    # Locate the first image on the page using inspect.
    # Start by typing page.get_by_alt_text("<insert desc from the first image").
    # Example: page.get_by_alt_text("a woman in a pink dress covered in pink bows").
    # Store it in a variable named image_elem.
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script using: python firstScript/06_LocatorsByAltText.py

    # Another example: Locate the second image on the page.
    # Start by typing page.get_by_alt_text("<insert desc from the second image").
    # Store it in a variable named second_image_elem.
    # Highlight the second_image_elem by adding second_image_elem.highlight().
    # Then explicitly add a delay of 3 seconds by typing page.wait_for_timeout(3000).
    # Run the script again.
