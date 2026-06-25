import pytest
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_remove_item_from_cart_page(page: Page, base_url: str):
    """Item can be removed from the cart page."""
    login_page = LoginPage(page, base_url)
    cart_page = CartPage(page)

    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    cart_page.add_item_to_cart("sauce-labs-backpack")
    cart_page.go_to_cart()

    expect(page).to_have_url(re.compile("cart"))

    cart_page.remove_item_from_cart("sauce-labs-backpack")

    expect(page.locator(".cart_item")).not_to_be_visible()
