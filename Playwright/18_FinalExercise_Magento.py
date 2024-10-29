from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Required Strings
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
    order_total = "$144.00"
    thank_you_msg = "Thank you for your purchase!"

    # 1 and 2
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    # 3
    page.goto(url)

    # 4
    # Using CSS:
    # luma_logo_elem = page.locator(".logo")
    # Using get_by_label:
    luma_logo_elem = page.get_by_label("store logo")
    luma_logo_elem.highlight()
    expect(luma_logo_elem).to_be_visible()
    page.wait_for_timeout(1000)

    # 5
    # Using CSS:
    # gear_link = page.locator("#ui-id-6")
    # Using get_by_role:
    gear_link = page.get_by_role("menuitem", name="Gear", exact=False)
    gear_link.highlight()
    gear_link.hover()
    page.wait_for_timeout(1000)

    # 6
    # Using CSS:
    # watches_link = page.locator("#ui-id-27")
    # Using get_by_role:
    watches_link = page.get_by_role("menuitem", name="Watches")
    watches_link.highlight()
    watches_link.click()
    page.wait_for_timeout(1000)

    # 7
    print("Current URL is:", page.url)
    expect(page).to_have_url(watches_url)
    page.wait_for_timeout(1000)

    # 8
    # Using get_by_alt_text:
    luma_watch = page.get_by_alt_text("Luma Analog Watch")
    luma_watch.highlight()
    luma_watch.click()
    page.wait_for_timeout(1000)

    # 9
    # Using CSS:
    # luma_watch_count = page.locator("#qty")
    # Using get_by_label:
    luma_watch_count = page.get_by_label("Qty")
    luma_watch_count.highlight()
    luma_watch_count.fill("3")
    page.wait_for_timeout(1000)

    # 10
    # Using CSS:
    # add_to_cart = page.locator("#product-addtocart-button")
    # Using get_by_role:
    add_to_cart = page.get_by_role("button", name="Add to Cart")
    add_to_cart.highlight()
    add_to_cart.click()
    page.wait_for_timeout(1000)

    # 11
    # Using CSS:
    # cart_icon = page.locator(".action.showcart")
    # Using XPath:
    cart_icon = page.locator("//a[@class='action showcart']")
    cart_icon.highlight()
    cart_icon.click()
    page.wait_for_timeout(1000)

    # 12
    # Using CSS:
    # checkout_btn = page.locator("#top-cart-btn-checkout")
    # Using XPath:
    checkout_btn = page.locator("//button[@id='top-cart-btn-checkout']")
    checkout_btn.highlight()
    checkout_btn.click()
    page.wait_for_timeout(1000)

    # 13
    # Using XPath:
    # firstname_fld = page.locator("//input[@name='firstname']")
    # Using get_by_label:
    firstname_fld = page.get_by_label("First Name")
    firstname_fld.highlight()
    firstname_fld.type(firstname, delay=100)
    page.wait_for_timeout(1000)

    # 14
    # Using XPath:
    # lastname_fld = page.locator("//input[@name='lastname']")
    # Using get_by_label:
    lastname_fld = page.get_by_label("Last Name")
    lastname_fld.highlight()
    lastname_fld.type(lastname, delay=100)
    page.wait_for_timeout(1000)

    # 15
    # Using XPath:
    email_fld = page.locator("//fieldset[@id='customer-email-fieldset']//input[@name='username']")
    email_fld.highlight()
    email_fld.type(email, delay=100)
    page.wait_for_timeout(1000)

    # 16
    # Using XPath:
    # street_address_fld = page.locator("//input[@name='street[0]']")
    # Using get_by_label:
    street_address_fld = page.get_by_label("Street Address: Line 1")
    street_address_fld.highlight()
    street_address_fld.type(street_address, delay=100)
    page.wait_for_timeout(1000)

    # 17
    # Using XPath:
    # city_fld = page.locator("//input[@name='city']")
    # Using get_by_label:
    city_fld = page.get_by_label("City")
    city_fld.highlight()
    city_fld.type(city, delay=100)
    page.wait_for_timeout(1000)

    # 18
    # Using XPath:
    state_drp = page.locator("//select[@name='region_id']")
    state_drp.scroll_into_view_if_needed()
    state_drp.highlight()
    state_drp.select_option(state)
    page.wait_for_timeout(1000)

    # 19
    # Using XPath:
    # zip_fld = page.locator("//input[@name='postcode']")
    # Using get_by_label:
    zip_fld = page.get_by_label("Zip/Postal Code")
    zip_fld.highlight()
    zip_fld.type(zip_code, delay=100)
    page.wait_for_timeout(1000)

    # 20
    # Using XPath:
    # phone_fld = page.locator("//input[@name='telephone']")
    # Using get_by_label:
    phone_fld = page.get_by_label("Phone Number")
    phone_fld.highlight()
    phone_fld.type(phone_number, delay=100)
    page.wait_for_timeout(1000)

    # 21
    # Using XPath:
    # flat_rate = page.locator("//input[@value='flatrate_flatrate']")
    # Using get_by_label:
    flat_rate = page.get_by_label("Fixed")
    flat_rate.highlight()
    flat_rate.check()
    page.wait_for_timeout(1000)

    # 22
    # Using XPath:
    # next_btn = page.locator("//button[@data-role='opc-continue']")
    # Using get_by_role:
    next_btn = page.get_by_role("button", name="Next")
    next_btn.highlight()
    next_btn.click()
    page.wait_for_timeout(1000)

    # 23
    # Using XPath:
    order_total_fld = page.locator("//tr[@class='grand totals']//span")
    order_total_fld.highlight()
    expect(order_total_fld).to_have_text(order_total)
    page.wait_for_timeout(1000)

    # 24
    # Using XPath:
    # place_order = page.locator("//button[@class='action primary checkout']")
    # Using get_by_role:
    place_order = page.get_by_role("button", name="Place Order")
    place_order.highlight()
    place_order.click()
    page.wait_for_timeout(1000)

    # 25
    # Using XPath:
    # thank_you_hdr = page.locator("//span[@data-ui-id='page-title-wrapper']")
    # Using get_by_role:
    thank_you_hdr = page.get_by_role("heading", name="Thank you for your purchase!")
    thank_you_hdr.highlight()
    expect(thank_you_hdr).to_have_text(thank_you_msg)
    page.wait_for_timeout(1000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Run the script using the following command: python 18_FinalExercise_Magento.py
    