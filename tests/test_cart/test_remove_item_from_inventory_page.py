import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_remove_item_from_cart_page(page: Page):
    """Item can be removed from the cart page."""
    login_page = LoginPage(page)
    cart_page = CartPage(page)

    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    cart_page.add_item_to_cart("sauce-labs-backpack")
    cart_page.go_to_cart()

    assert "cart" in page.url

    cart_page.remove_item_from_cart("sauce-labs-backpack")

    expect(page.locator(".cart_item")).not_to_be_visible()