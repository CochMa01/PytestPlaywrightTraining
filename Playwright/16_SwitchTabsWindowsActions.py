from playwright.sync_api import sync_playwright

with (sync_playwright() as playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()
    context2 = browser.new_context()

    page = context.new_page()
    page2 = context2.new_page()

    page.goto("https://google.com/")
    page.wait_for_timeout(3000)

    page2.goto("https://bing.com/")
    page2.wait_for_timeout(3000)

    page3 = context.new_page()
    page3.goto("https://yahoo.com/")
    page3.wait_for_timeout(3000)

    page4 = context2.new_page()
    page4.wait_for_timeout(3000)

    all_pages_in_context = context.pages
    all_pages_in_context2 = context2.pages

    all_pages_in_context[0].bring_to_front()
    all_pages_in_context[0].goto("https://duckduckgo.com/")
    page.wait_for_timeout(3000)
    all_pages_in_context[1].close()
    page.wait_for_timeout(3000)

    all_pages_in_context2[0].bring_to_front()
    all_pages_in_context2[0].goto("https://ask.com/")
    page2.wait_for_timeout(3000)
    all_pages_in_context2[1].close()
    page2.wait_for_timeout(3000)
    # page4.wait_for_timeout(3000)

    # Practical Application #1
    # context = browser.new_context()
    # page = context.new_page()
    #
    # page.goto("https://demoqa.com/browser-windows")
    # new_tab_button = page.get_by_role("button", name="New Tab")
    # new_tab_button.click()
    # page.wait_for_timeout(3000)
    #
    # all_pages = context.pages
    # print(all_pages)
    # all_pages[1].goto("https://bing.com/")
    # all_pages[1].wait_for_timeout(3000)
    # all_pages[1].close()
    # all_pages[0].bring_to_front()
    # all_pages[0].goto("https://duckduckgo.com/")
    # page.wait_for_timeout(3000)

    # Practical Application #2
    # context = browser.new_context()
    # page = context.new_page()
    #
    # page.goto("https://demoqa.com/browser-windows")
    # new_window_button = page.get_by_role("button", name="New Window", exact=True)
    # new_window_button.click()
    # page.wait_for_timeout(3000)
    #
    # all_contexts = browser.contexts
    # print(all_contexts)
    # all_contexts[0].pages[1].goto("https://bing.com/")
    # all_contexts[0].pages[1].wait_for_timeout(3000)
    # all_contexts[0].pages[1].close()
    # all_contexts[0].pages[0].bring_to_front()
    # all_contexts[0].pages[0].goto("https://duckduckgo.com/")
    # page.wait_for_timeout(3000)

    # ----------------------------------------
    context.close()
    # context2.close()
    browser.close()

    # Copy the code from 14_SelectDropdownActions.py.py and rename it to 15_FileUploadActions.py.
    # On this script, we will focus on how we can automate Radio buttons and Checkbox actions.
    # Update first the URL to https://davidwalsh.name/demo/multiple-file-upload.php.

