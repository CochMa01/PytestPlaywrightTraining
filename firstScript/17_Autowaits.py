from playwright.sync_api import sync_playwright

with (sync_playwright() as playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()



    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 14_SelectDropdownActions.py.py and rename it to 15_FileUploadActions.py.
    # On this script, we will focus on how we can automate Radio buttons and Checkbox actions.
    # Update first the URL to https://davidwalsh.name/demo/multiple-file-upload.php.

