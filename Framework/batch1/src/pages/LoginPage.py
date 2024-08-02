from batch1.src.pages.ProductsListPage import ProductsListPage


class LoginPage:

    def __init__(self, page, logger):
        self.page = page
        self.logger = logger
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.failure_elem = page.locator("//h3[@data-test='error']")


    def enter_username(self, username):
        self.username_field.clear()
        self.logger.info(f"Cleared username field.")
        self.username_field.fill(username)
        self.logger.info(f"Username field populated with: {username}.")


    def enter_password(self, password):
        self.password_field.clear()
        self.logger.info(f"Cleared password field.")
        self.password_field.fill(password)
        self.logger.info(f"Username field populated with: {'*' * len(password)}.")


    def click_login(self):
        self.login_button.click()
        self.logger.info(f"Clicked login button.")


    def do_login(self, credentials):
        self.enter_username(credentials["username"])
        self.enter_password(credentials["password"])
        self.click_login()
        return ProductsListPage(self.page, self.logger)


    @property
    def error_msg_locator(self):
        return self.failure_elem


    @property
    def login_button_locator(self):
        return self.login_button
