import pytest
import re
from playwright.sync_api import Page, expect


def test_valid_user_can_log_in(page: Page):
    # Navigate to the site
    page.goto("https://www.saucedemo.com/")

    # Fill in credentials
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    # Click login
    page.get_by_role("button", name="Login").click()

    # Assert we landed on the inventory page
    expect(page).to_have_url(re.compile("inventory"))
    expect(page.locator(".title")).to_have_text("Products")
