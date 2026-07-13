import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage


@pytest.mark.regression
@pytest.mark.cart
def test_add_multiple_items_to_cart(page: Page, base_url: str):
    """Adding two items updates the cart badge to 2."""
    login_page = LoginPage(page, base_url)
    cart_page = CartPage(page)

    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    cart_page.add_item_to_cart("sauce-labs-backpack")
    cart_page.add_item_to_cart("sauce-labs-bike-light")

    expect(cart_page.cart_badge).to_have_text("2")
