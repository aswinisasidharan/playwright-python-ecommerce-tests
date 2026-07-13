import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.regression
@pytest.mark.checkout
def test_complete_checkout_flow(page: Page, base_url: str):
    """User can complete the full checkout flow end to end."""
    login_page = LoginPage(page, base_url)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Login
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    # Add item and go to cart
    cart_page.add_item_to_cart("sauce-labs-backpack")
    cart_page.go_to_cart()

    # Start checkout
    checkout_page.start_checkout()
    assert checkout_page.is_on_step_one()

    # Fill in details and continue
    checkout_page.fill_details("Aswini", "Sasidharan", "50667")
    checkout_page.continue_checkout()

    # Confirm overview page
    assert checkout_page.is_on_step_two()
    expect(page.locator(".title")).to_have_text("Checkout: Overview")

    # Finish the order
    checkout_page.finish_checkout()

    # Confirm success
    assert checkout_page.is_complete()
    expect(checkout_page.success_header).to_have_text("Thank you for your order!")
