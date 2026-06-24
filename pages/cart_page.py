from playwright.sync_api import Page, expect


class CartPage:
    """Page Object for the inventory/cart page after login."""

    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_item_to_cart(self, item_name: str):
        """Add a product by its data-test attribute name."""
        self.page.locator(f"[data-test='add-to-cart-{item_name}']").click()

    def remove_item_from_cart(self, item_name: str):
        """Remove a product by its data-test attribute name."""
        self.page.locator(f"[data-test='remove-{item_name}']").click()

    def go_to_cart(self):
        """Click the cart icon to open the cart page."""
        self.cart_icon.click()
