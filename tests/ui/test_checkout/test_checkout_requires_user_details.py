import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_requires_user_details(page: Page, base_url: str):
    """Checkout cannot proceed without filling in user details."""
    login_page = LoginPage(page, base_url)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Login
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    # Add item and go to checkout
    cart_page.add_item_to_cart("sauce-labs-backpack")
    cart_page.go_to_cart()
    checkout_page.start_checkout()

    assert checkout_page.is_on_step_one()

    # Try to continue without filling details
    checkout_page.continue_checkout()

    expect(checkout_page.error_message).to_contain_text("First Name is required")
