from playwright.sync_api import Page, expect


class CheckoutPage:
    """Page Object for the checkout flow."""

    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.error_message = page.locator("[data-test='error']")
        self.success_header = page.locator(".complete-header")

    def start_checkout(self):
        """Click the checkout button from the cart page."""
        self.checkout_button.click()

    def fill_details(self, first_name: str, last_name: str, postal_code: str):
        """Fill in the checkout form details."""
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):
        """Click continue to move to the overview page."""
        self.continue_button.click()

    def finish_checkout(self):
        """Click finish to complete the order."""
        self.finish_button.click()

    def is_on_step_one(self) -> bool:
        return "checkout-step-one" in self.page.url

    def is_on_step_two(self) -> bool:
        return "checkout-step-two" in self.page.url

    def is_complete(self) -> bool:
        return "checkout-complete" in self.page.url
