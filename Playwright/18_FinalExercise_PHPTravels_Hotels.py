from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Required Strings
    firstname = "Mark"
    lastname = "Croissant"
    email = "croissant_mark@testemail.com"
    url = "https://www.phptravels.net/"
    hotelsUrl = "https://www.phptravels.net/hotels"
    status = "unpaid"

    # 1 and 2
    browser = playwright.chromium.launch(headless=False, slow_mo=3000, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    # 3
    page.goto(url)

    # 4
    phptravels_logo_elem = page.locator("//img[@class='logo p-1 rounded']")
    phptravels_logo_elem.highlight()
    expect(phptravels_logo_elem).to_be_visible()
    page.wait_for_timeout(1000)

    # 5
    hotels_link_elem = page.get_by_role("link", name="Hotels", exact=True)
    # Using XPath: hotels_link_elem = page.locator("(//a[@class='nav-link fadeout  waves-effect'])[1]")
    hotels_link_elem.highlight()
    hotels_link_elem.click()
    page.wait_for_timeout(1000)

    # 6
    print("Current URL is:", page.url)
    expect(page).to_have_url(hotelsUrl)
    page.wait_for_timeout(1000)

    # 7
    # header_elem = page.get_by_text("Search for best hotels")
    # Using CSS:
    header_elem = page.locator("strong:text('Search for best hotels')")
    # Using XPath header_elem = page.locator("//strong[text()='Search for best hotels']")
    expect(header_elem).to_be_visible()
    page.wait_for_timeout(1000)

    # 8
    city_drop_elem = page.locator("css=b")
    # Using XPath: city_drop_elem = page.locator("xpath=//b")
    city_drop_elem.highlight()
    city_drop_elem.click()
    page.wait_for_timeout(1000)

    # 9
    dubai_option_elem = page.locator("//div[@class='most--popular-hotels']/div[1]")
    dubai_option_elem.highlight()
    dubai_option_elem.click()
    page.wait_for_timeout(1000)

    # 10
    checkin_elem = page.locator("#checkin")
    # Using XPath: checkin_elem = page.locator("//input[@id='checkin']")
    checkin_elem.highlight()
    checkin_elem.click()
    page.wait_for_timeout(1000)

    # 11
    # Using XPath: oct5_elem = page.locator("(//div[@class='datepicker-days'])[1]//tbody/tr[1]/td[7]")
    # Using get_by_role: 
    oct5_elem = page.get_by_role("cell", name="5").first
    oct5_elem.highlight()
    oct5_elem.click()
    page.wait_for_timeout(1000)

    # 12
    # Using XPath: oct6_elem = page.locator("(//div[@class='datepicker-days'])[2]//tbody/tr[2]/td[1]")
    # Using get_by_role:
    oct6_elem = page.get_by_role("cell", name="6").first
    oct6_elem.highlight()
    oct6_elem.click()
    page.wait_for_timeout(1000)

    # 13
    pax_count_elem = page.locator("//div[@class='dropdown dropdown-contain']/a")
    pax_count_elem.highlight()
    pax_count_elem.click()
    page.wait_for_timeout(1000)

    # 14
    dec_pax_count_elem = page.locator("(//div[@class='qtyDec'])[2]")
    dec_pax_count_elem.highlight()
    dec_pax_count_elem.click()
    page.wait_for_timeout(1000)

    # 15
    search_btn_elem = page.locator("//button[@type='submit']")
    search_btn_elem.highlight()
    search_btn_elem.click()
    page.wait_for_timeout(1000)

    # 16
    star5_elem = page.get_by_label("5")
    # Using CSS: star5_elem = page.locator("#starRating5")
    # Using Xpath: star5_elem = page.locator("//input[@id='starRating5']")
    star5_elem.highlight()
    star5_elem.check()
    page.wait_for_timeout(1000)

    # 17
    desc_elem = page.locator("#desc")
    # Using Xpath: desc_elem = page.locator("//input[@id='desc']")
    desc_elem.highlight()
    desc_elem.check()
    page.wait_for_timeout(1000)

    # 18
    apply_filters_elem = page.get_by_role("button", name="Apply Filters")
    # Using XPath: apply_filters_elem = page.locator("//button[text()='Apply Filters']")
    apply_filters_elem.highlight()
    apply_filters_elem.click()
    page.wait_for_timeout(1000)

    # 19
    view_more_btn_elem = page.locator("//a[@href='https://www.phptravels.net/hotel/2/movenpick-grand-al-bustan/05-10-2024/06-10-2024/1/1/0/PH/hotels']")
    view_more_btn_elem.highlight()
    view_more_btn_elem.click()
    page.wait_for_timeout(1000)

    # 20
    select_room_btn_elem = page.locator("//a[@href='#rooms']")
    select_room_btn_elem.highlight()
    select_room_btn_elem.click()
    page.wait_for_timeout(1000)

    # 21
    book_now_elem = page.locator("(//button[@type='submit'])[1]")
    book_now_elem.highlight()
    book_now_elem.click()
    page.wait_for_timeout(1000)

    # 22
    firstname_elem = page.locator("//input[@name='user[first_name]']")
    firstname_elem.highlight()
    firstname_elem.clear()
    firstname_elem.type(firstname, delay=100)
    page.wait_for_timeout(1000)

    # 23
    lastname_elem = page.locator("//input[@name='user[last_name]']")
    lastname_elem.highlight()
    lastname_elem.clear()
    lastname_elem.type(lastname, delay=100)
    page.wait_for_timeout(1000)

    # 24
    email_elem = page.locator("//input[@name='user[email]']")
    email_elem.highlight()
    email_elem.clear()
    email_elem.type(email, delay=100)
    page.wait_for_timeout(1000)

    # 25
    firstname_travInfo_elem = page.locator("//input[@name='firstname_1']")
    firstname_travInfo_elem.highlight()
    firstname_travInfo_elem.clear()
    firstname_travInfo_elem.type(firstname, delay=100)
    page.wait_for_timeout(1000)

    lastname_travInfo_elem = page.locator("//input[@name='lastname_1']")
    lastname_travInfo_elem.highlight()
    lastname_travInfo_elem.clear()
    lastname_travInfo_elem.type(lastname, delay=100)
    page.wait_for_timeout(1000)

    # 26
    pay_later_elem = page.locator("#gateway_pay_later")
    pay_later_elem.highlight()
    pay_later_elem.check()
    page.wait_for_timeout(1000)

    # 27
    agree_elem = page.locator("#agreechb")
    agree_elem.highlight()
    agree_elem.check()
    page.wait_for_timeout(1000)

    # 28
    booking_confirm_elem = page.locator("#booking")
    booking_confirm_elem.highlight()
    booking_confirm_elem.click()
    page.wait_for_timeout(1000)

    # 29
    payment_stat_elem = page.locator("//span[@class='text-danger']")
    payment_stat_elem.highlight()
    expect(payment_stat_elem).to_have_text(status)
    page.wait_for_timeout(1000)

    # 30
    qr_code_elem = page.locator("#InvoiceQR")
    expect(qr_code_elem).to_be_visible()
    page.wait_for_timeout(1000)

    # ----------------------------------------
    context.close()
    browser.close()

    # Run the script using the following command: python 18_FinalExercise.py
    