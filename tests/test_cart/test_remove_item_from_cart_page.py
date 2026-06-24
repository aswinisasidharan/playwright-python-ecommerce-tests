import re
import pytest
from playwright.sync_api import Page, expect


def test_remove_item_from_cart_page(page: Page):
    """Item can be removed from the cart page."""
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
 
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator(".shopping_cart_link").click()
 
    assert "cart" in page.url
 
    page.locator("[data-test='remove-sauce-labs-backpack']").click()
 
    expect(page.locator(".cart_item")).not_to_be_visible()
