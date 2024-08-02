
class ProductsListPage:

    def __init__(self, page, logger):
        self.page = page
        self.logger = logger
        self.products_header = page.locator("//span[@class='title']")
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.add_to_cart = page.locator("//div[text()='Sauce Labs Bike Light']//ancestor::div["
                                        "@class='inventory_item_label']/following-sibling::div//button")


    @property
    def products_list_header(self):
        """Variable; Returns the locator of the Product Header after logging in."""
        return self.products_header


    def click_burger_menu(self):
        """Function; Clicks the burger menu."""
        self.burger_menu.click()
        self.logger.info("Clicked the burger menu.")


    def click_logout(self):
        """Function; Clicks the logout link."""
        self.logout_link.click()
        self.logger.info("Clicked the logout link.")


    def do_logout(self):
        """Function; Logs out the user by clicking the burger menu and then the logout link."""
        self.click_burger_menu()
        self.click_logout()


    def get_add_to_or_remove_from_cart_locator(self, product_name):
        """Function; Returns the locator of the 'Add to Cart' or 'Remove' button for the specified product_name."""
        return self.page.locator(f"//div[text()='{product_name}']//ancestor::div[@class='inventory_item_label']"
                                 f"/following-sibling::div//button")


    def click_add_to_or_remove_from_cart(self, product_name):
        """Function; Clicks the 'Add to Cart' or 'Remove' button."""
        self.get_add_to_or_remove_from_cart_locator(product_name).click()
        self.logger.info(f"Clicked Add to Cart or Remove button for {product_name}.")
