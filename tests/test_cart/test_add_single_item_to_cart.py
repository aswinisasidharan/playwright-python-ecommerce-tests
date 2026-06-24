import re
import pytest
from playwright.sync_api import Page, expect

def test_add_single_item_to_cart(page: Page):
    """Adding one item updates the cart badge to 1."""
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
 
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
 
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
