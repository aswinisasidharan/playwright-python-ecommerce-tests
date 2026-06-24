
import re
import pytest
from playwright.sync_api import Page, expect


def test_complete_checkout_flow(page: Page):
    """User can complete the full checkout flow end to end."""
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
 
    # Add item to cart
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
 
    # Go to cart
    page.locator(".shopping_cart_link").click()
    assert "cart" in page.url
 
    # Start checkout
    page.locator("[data-test='checkout']").click()
    assert "checkout-step-one" in page.url
 
    # Fill in details
    page.locator("[data-test='firstName']").fill("Aswini")
    page.locator("[data-test='lastName']").fill("Sasidharan")
    page.locator("[data-test='postalCode']").fill("50667")
    page.locator("[data-test='continue']").click()
 
    # Confirm overview page
    assert "checkout-step-two" in page.url
    expect(page.locator(".title")).to_have_text("Checkout: Overview")
 
    # Finish the order
    page.locator("[data-test='finish']").click()
 
    # Confirm order success
    assert "checkout-complete" in page.url
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
