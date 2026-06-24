import re
import pytest
from playwright.sync_api import Page, expect


def test_checkout_requires_user_details(page: Page):
    """Checkout cannot proceed without filling in user details."""
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
 
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator(".shopping_cart_link").click()
    page.locator("[data-test='checkout']").click()
 
    assert "checkout-step-one" in page.url
 
    page.locator("[data-test='continue']").click()
 
    expect(page.locator("[data-test='error']")).to_contain_text("First Name is required")
