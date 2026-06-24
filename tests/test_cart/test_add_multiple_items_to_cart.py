import re
import pytest
from playwright.sync_api import Page, expect


def test_add_multiple_items_to_cart(page: Page):
    """Adding two items updates the cart badge to 2."""
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
 
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()
 
    expect(page.locator(".shopping_cart_badge")).to_have_text("2")
