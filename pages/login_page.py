from playwright.sync_api import Page, expect


class LoginPage:
    """
    Page Object for the Sauce Demo login page.
    All locators and actions related to login live here.
    """

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        # Define locators once — if the site changes, fix it here only
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")

    def goto(self):
        self.page.goto(self.base_url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        return self.error_message.inner_text()
