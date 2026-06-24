import pytest
import re
from playwright.sync_api import Page, expect


def test_locked_out_user_sees_error(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Assert the error message appears
    expect(page.locator("[data-test='error']")).to_contain_text("locked out")
