import pytest
import re
from playwright.sync_api import Page, expect


def test_empty_credentials_shows_error(page: Page):
    """Submitting empty credentials shows a validation error."""
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("button", name="Login").click()
 
    expect(page.locator("[data-test='error']")).to_contain_text("Username is required")
