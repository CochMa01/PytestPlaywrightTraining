import os

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    file_upload_elem = page.locator("//input[@id='filesToUpload']")
    file_upload_elem.highlight()
    file_upload_elem.set_input_files("firstScript/file1.txt")
    page.wait_for_timeout(3000)

    file_upload_elem.set_input_files(["firstScript/file1.txt", "firstScript/file2.java", "firstScript/file3.gif"])
    page.wait_for_timeout(3000)

    page.goto("https://demoqa.com/upload-download")

    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download").click()

    download = download_info.value
    print(download.path())
    page.wait_for_timeout(3000)
    working_dir = os.getcwd()
    download.save_as(os.path.join(working_dir, "firstScript/downloaded_file.jpeg"))

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 14_SelectDropdownActions.py.py and rename it to 15_FileUploadActions.py.
    # On this script, we will focus on how we can automate Radio buttons and Checkbox actions.
    # Update first the URL to https://davidwalsh.name/demo/multiple-file-upload.php.
    # Let's automate an example of a File Upload element.
    # Start by typing page.locator("//input[@id='filesToUpload']").
    # Store it in a variable named file_upload_elem.
    # Highlight the element by calling file_upload_elem.highlight().
    # Now, let's upload a single file.
    # Call file_upload_elem.set_input_files("firstScript/file1.txt").
    # This will upload the file1.txt file.
    # Then explicitly wait for 3 seconds by calling page.wait_for_timeout(3000).
    # Run the script using: python firstScript/15_FileUploadActions.py

    # Next, let's upload multiple files.
    # Call file_upload_elem.set_input_files(["firstScript/file1.txt",
    # "firstScript/file2.java", "firstScript/file3.gif"]).
    # This will upload the file1.txt, file2.java, and file3.gif files.
    # Then explicitly wait for 3 seconds by calling page.wait_for_timeout(3000).
    # Run the script again.

    # Now, let's download a file.
    # Update the URL to https://demoqa.com/upload-download.
    # Click the Download link by calling page.get_by_role("link", name="Download").click().
    # Use the with statement to capture the download event.
    # with page.expect_download() as download_info:
    #     page.get_by_role("link", name="Download").click().
    # Store the download object in the download variable.
    # Print the path of the downloaded file by calling download.path().
    # Save the downloaded file to the current working directory by calling
    # download.save_as(os.path.join(working_dir, "firstScript/downloaded_file.jpeg")).
    # Explicitly wait for 3 seconds by calling page.wait_for_timeout(3000).
    # Run the script again.
