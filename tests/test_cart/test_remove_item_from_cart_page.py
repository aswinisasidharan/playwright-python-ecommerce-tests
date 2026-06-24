import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_remove_item_from_inventory_page(page: Page):
    """Item can be removed from the cart directly on the inventory page."""
    login_page = LoginPage(page)
    cart_page = CartPage(page)

    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    cart_page.add_item_to_cart("sauce-labs-backpack")
    expect(cart_page.cart_badge).to_have_text("1")

    cart_page.remove_item_from_cart("sauce-labs-backpack")

    expect(cart_page.cart_badge).not_to_be_visible()
