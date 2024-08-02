from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # 1 and 2
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    # 3
    page.goto("https://demo.nopcommerce.com/")

    # 4
    nopCommerce_logo_elem = page.get_by_alt_text("nopCommerce demo store")
    nopCommerce_logo_elem.highlight()
    expect(nopCommerce_logo_elem).to_be_visible()
    page.wait_for_timeout(1000)

    # 5
    register_link_elem = page.locator("//a[@class='ico-register']")
    register_link_elem.highlight()
    register_link_elem.click()
    page.wait_for_timeout(1000)

    # 6
    register_page_header_elem = page.get_by_role("heading", name="Register")
    register_page_header_elem.highlight()
    expect(register_page_header_elem).to_be_visible()
    page.wait_for_timeout(1000)

    # 7
    male_radiobutton_elem = page.locator("#gender-male")
    male_radiobutton_elem.highlight()
    male_radiobutton_elem.check()
    page.wait_for_timeout(1000)

    # 8
    first_name_field_elem = page.get_by_label("First name:")
    first_name_field_elem.highlight()
    first_name_field_elem.fill("Mark Anthony")
    page.wait_for_timeout(1000)

    # 9
    last_name_field_elem = page.get_by_label("Last name:")
    last_name_field_elem.highlight()
    last_name_field_elem.fill("Croissant")
    page.wait_for_timeout(1000)

    # 10
    birthdate_dropdown_elem = page.locator("select[name='DateOfBirthDay']")
    birthdate_dropdown_elem.highlight()
    birthdate_dropdown_elem.select_option("20")
    page.wait_for_timeout(1000)

    # 11
    birthmonth_dropdown_elem = page.locator("select[name='DateOfBirthMonth']")
    birthmonth_dropdown_elem.highlight()
    birthmonth_dropdown_elem.select_option("February")
    page.wait_for_timeout(1000)

    # 12
    birthyear_dropdown_elem = page.locator("select[name='DateOfBirthYear']")
    birthyear_dropdown_elem.highlight()
    birthyear_dropdown_elem.select_option("2020")
    page.wait_for_timeout(1000)

    # 13
    email_field_elem = page.get_by_label("Email:")
    email_field_elem.highlight()
    email_field_elem.fill("croissant_mark@testemail.com")
    page.wait_for_timeout(1000)
    # 14
    expect(email_field_elem).to_have_value("croissant_mark@testemail.com")

    # 15
    company_field_elem = page.get_by_label("Company name:")
    company_field_elem.highlight()
    company_field_elem.fill("Croissant Enterprises")
    page.wait_for_timeout(1000)

    # 16
    newsletter_checkbox_elem = page.locator("#Newsletter")
    newsletter_checkbox_elem.highlight()
    newsletter_checkbox_elem.uncheck()
    page.wait_for_timeout(1000)
    # 17
    expect(newsletter_checkbox_elem).not_to_be_checked()

    # 18
    password_field_elem = page.get_by_label("Password:", exact=True)
    password_field_elem.highlight()
    password_field_elem.type("testcroissant", delay=250)
    page.wait_for_timeout(1000)

    # 19
    confirm_password_field_elem = page.get_by_label("Confirm password:")
    confirm_password_field_elem.highlight()
    confirm_password_field_elem.type("testcroissant1", delay=250)
    page.wait_for_timeout(1000)

    # 20
    register_button_elem = page.get_by_role("button", name="Register")
    register_button_elem.highlight()
    register_button_elem.click()
    page.wait_for_timeout(1000)

    # 21
    error_message_elem = page.locator("#ConfirmPassword-error")
    error_message_elem.highlight()
    expect(error_message_elem).to_have_text("The password and confirmation password do not match.")
    page.wait_for_timeout(1000)

    # 22
    confirm_password_field_elem.clear()
    confirm_password_field_elem.type("testcroissant", delay=250)
    confirm_password_field_elem.highlight()
    page.wait_for_timeout(1000)

    # 23
    expect(error_message_elem).to_be_hidden()
    page.wait_for_timeout(1000)

    # 24
    register_button_elem.click()
    register_button_elem.highlight()
    page.wait_for_timeout(1000)

    # 25
    registration_message_elem = page.locator("//div[@id='main']//div[@class='result']")
    registration_message_elem.highlight()
    expect(registration_message_elem).to_have_text("Your registration completed")
    page.wait_for_timeout(1000)

    # 26
    continue_button_elem = page.get_by_role("link", name="Continue")
    continue_button_elem.highlight()
    continue_button_elem.click()
    page.wait_for_timeout(1000)

    # 27
    logout_link_elem = page.get_by_role("link", name="Log out")
    logout_link_elem.highlight()
    expect(logout_link_elem).to_be_visible()
    page.wait_for_timeout(1000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Copy the code from 14_SelectDropdownActions.py.py and rename it to 15_FileUploadActions.py.
    # On this script, we will focus on how we can automate Radio buttons and Checkbox actions.
    # Update first the URL to https://davidwalsh.name/demo/multiple-file-upload.php.
