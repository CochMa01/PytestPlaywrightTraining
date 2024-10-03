from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Required Strings
    search_term = "Yoga Straps"
    firstname = "Mark"
    lastname = "Croissant"
    email = "croissant_mark@testemail.com"
    street_address = "4444 Croissant Street"
    city = "Yeast City"
    state = "Alaska"
    zip_code = "99631"
    phone_number = "1532394331"
    url = "https://magento.softwaretestingboard.com/"
    watches_url = "https://magento.softwaretestingboard.com/gear/watches.html"
    order_total = "$211.00"
    orange_warn_msg = "Please specify the quantity of product(s)."
    thank_you_msg = "Thank you for your purchase!"

    # 1 and 2
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    # 3
    page.goto(url)

    # 4
    luma_logo_elem = page.locator(".logo")
    # Using get_by_label: luma_logo_elem = page.get_by_label("store logo")
    luma_logo_elem.highlight()
    expect(luma_logo_elem).to_be_visible()
    page.wait_for_timeout(1000)

    # 5
    gear_link = page.locator("#ui-id-6")
    gear_link.highlight()
    gear_link.hover()
    page.wait_for_timeout(1000)

    # 6
    watches_link = page.locator("#ui-id-27")
    watches_link.highlight()
    watches_link.click()
    page.wait_for_timeout(1000)

    # 7
    print("Current URL is:", page.url)
    expect(page).to_have_url(watches_url)
    page.wait_for_timeout(1000)

    # 8
    luma_watch = page.get_by_alt_text("Luma Analog Watch")
    luma_watch.highlight()
    luma_watch.click()
    page.wait_for_timeout(1000)

    # 9
    luma_watch_count = page.locator("#qty")
    luma_watch_count.highlight()
    luma_watch_count.fill("3")
    page.wait_for_timeout(1000)

    # 10
    add_to_cart = page.locator("#product-addtocart-button")
    add_to_cart.highlight()
    add_to_cart.click()
    page.wait_for_timeout(1000)

    # 11
    search_bar = page.locator("#search")
    search_bar.highlight()
    search_bar.type(search_term, delay=100)
    page.wait_for_timeout(1000)

    search_icon = page.locator(".action.search")
    search_icon.highlight()
    search_icon.click()
    page.wait_for_timeout(1000)

    # You may also try pressing the Enter key.
    # search_icon.press("Enter")

    # 12
    yoga_straps = page.get_by_alt_text("Set of Sprite Yoga Straps")
    yoga_straps.highlight()
    yoga_straps.hover()
    page.wait_for_timeout(1000)

    add_to_cart = page.locator("//form[@data-product-sku='24-WG085_Group']/button")
    add_to_cart.highlight()
    add_to_cart.click()
    page.wait_for_timeout(1000)

    # 13
    orange_alert = page.locator("//div[@role='alert']")
    # Using get_by_role: orange_alert = page.get_by_role("alert")
    orange_alert.highlight()
    expect(orange_alert).to_have_text(orange_warn_msg)
    page.wait_for_timeout(1000)

    # 14
    yoga_strap_6ft = page.locator("//input[@name='super_group[33]']")
    yoga_strap_6ft.highlight()
    yoga_strap_6ft.fill("1")
    page.wait_for_timeout(1000)

    yoga_strap_8ft = page.locator("//input[@name='super_group[34]']")
    yoga_strap_8ft.highlight()
    yoga_strap_8ft.fill("1")
    page.wait_for_timeout(1000)

    yoga_strap_10ft = page.locator("//input[@name='super_group[35]']")
    yoga_strap_10ft.highlight()
    yoga_strap_10ft.fill("1")
    page.wait_for_timeout(1000)

    # 15
    add_to_cart = page.locator("#product-addtocart-button")
    add_to_cart.highlight()
    add_to_cart.click()
    page.wait_for_timeout(1000)

    # 16
    cart_icon = page.locator(".action.showcart")
    cart_icon.highlight()
    cart_icon.click()
    page.wait_for_timeout(1000)

    # 17
    checkout_btn = page.locator("#top-cart-btn-checkout")
    checkout_btn.highlight()
    checkout_btn.click()
    page.wait_for_timeout(1000)

    # 18
    firstname_fld = page.locator("//input[@name='firstname']")
    firstname_fld.highlight()
    firstname_fld.type(firstname, delay=100)
    page.wait_for_timeout(1000)

    # 19
    lastname_fld = page.locator("//input[@name='lastname']")
    lastname_fld.highlight()
    lastname_fld.type(lastname, delay=100)
    page.wait_for_timeout(1000)

    # 20
    email_fld = page.locator("//fieldset[@id='customer-email-fieldset']//input[@name='username']")
    email_fld.highlight()
    email_fld.type(email, delay=100)
    page.wait_for_timeout(1000)

    # 21
    street_address_fld = page.locator("//input[@name='street[0]']")
    street_address_fld.highlight()
    street_address_fld.type(street_address, delay=100)
    page.wait_for_timeout(1000)

    # 22
    city_fld = page.locator("//input[@name='city']")
    city_fld.highlight()
    city_fld.type(city, delay=100)
    page.wait_for_timeout(1000)

    # 23
    state_drp = page.locator("//select[@name='region_id']")
    state_drp.scroll_into_view_if_needed()
    state_drp.highlight()
    state_drp.select_option(state)
    page.wait_for_timeout(1000)

    # 24
    zip_fld = page.locator("//input[@name='postcode']")
    zip_fld.highlight()
    zip_fld.type(zip_code, delay=100)
    page.wait_for_timeout(1000)

    # 25
    phone_fld = page.locator("//input[@name='telephone']")
    phone_fld.highlight()
    phone_fld.type(phone_number, delay=100)
    page.wait_for_timeout(1000)

    # 26
    flat_rate = page.locator("//input[@value='flatrate_flatrate']")
    flat_rate.highlight()
    flat_rate.check()
    page.wait_for_timeout(1000)

    # 27
    next_btn = page.locator("//button[@data-role='opc-continue']")
    next_btn.highlight()
    next_btn.click()
    page.wait_for_timeout(1000)

    # 28
    order_total_fld = page.locator("//tr[@class='grand totals']//span")
    order_total_fld.highlight()
    expect(order_total_fld).to_have_text(order_total)
    page.wait_for_timeout(1000)

    # 29
    place_order = page.locator("//button[@class='action primary checkout']")
    place_order.highlight()
    place_order.click()
    page.wait_for_timeout(1000)

    # 30
    thank_you_hdr = page.locator("//span[@data-ui-id='page-title-wrapper']")
    thank_you_hdr.highlight()
    expect(thank_you_hdr).to_have_text(thank_you_msg)
    page.wait_for_timeout(1000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Run the script using the following command: python 18_FinalExercise.py
    